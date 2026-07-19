#!/usr/bin/env python3
"""
Apple Calendar MCP Server -- Local EventKit access to every calendar
the Mac knows about.

Thin FastMCP layer over EventKit via PyObjC. Reads and writes the
calendars configured in macOS -- iCloud, Google, Exchange or local --
through the system calendar store, without driving Calendar.app.

EventKit was chosen over an AppleScript bridge deliberately: predicate
queries return in milliseconds where Calendar.app AppleScript
enumeration takes minutes on large calendars, EventKit exposes a full
structured CRUD surface, and it works without Calendar.app running.
The trade is a one-time macOS TCC grant: the first request_access call
raises a system dialog attributed to the hosting app, and Full Access
must be approved.

Write tools carry `WRITE.` in their description so the calling agent
follows Navigation Rule 3 and asks for confirmation before dispatch.
The server itself does not enforce the gate.
"""

import threading
from datetime import datetime, timezone
from typing import Optional, List, Dict, Any

import EventKit
import Foundation
from pydantic import BaseModel, Field
from mcp.server.fastmcp import FastMCP

# ---------------------------------------------------------------------------
# Configuration
# ---------------------------------------------------------------------------

# EventKit constants, resolved defensively with literal fallbacks.
EK_ENTITY_EVENT = int(getattr(EventKit, "EKEntityTypeEvent", 0))
EK_SPAN_THIS = int(getattr(EventKit, "EKSpanThisEvent", 0))
EK_SPAN_FUTURE = int(getattr(EventKit, "EKSpanFutureEvents", 1))

AUTH_STATUS_LABELS = {
    0: "not_determined",
    1: "restricted",
    2: "denied",
    3: "authorized_full",
    4: "write_only",
}

REQUEST_ACCESS_TIMEOUT_SECONDS = 180.0

_store_lock = threading.Lock()
_store: Optional[Any] = None


def _event_store(reset: bool = False):
    """Lazily build (or rebuild after an authorization change) the store."""
    global _store
    with _store_lock:
        if _store is None or reset:
            _store = EventKit.EKEventStore.alloc().init()
        return _store


def _auth_status() -> int:
    return int(EventKit.EKEventStore.authorizationStatusForEntityType_(EK_ENTITY_EVENT))


# ---------------------------------------------------------------------------
# Models
# ---------------------------------------------------------------------------


class LocalResponse(BaseModel):
    """Wrapper for responses that may fail before reaching EventKit."""

    ok: bool
    data: Optional[Any] = None
    error: Optional[str] = None
    fetched_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))


def _denied(read: bool = True) -> LocalResponse:
    status = AUTH_STATUS_LABELS.get(_auth_status(), "unknown")
    need = "Full Access" if read else "Full Access or write-only access"
    return LocalResponse(
        ok=False,
        error=(
            f"Calendar access not granted (status: {status}). {need} is required. "
            "Call request_access -- a macOS dialog appears for the hosting app; "
            "approve it, or grant Calendar access in System Settings > Privacy "
            "& Security > Calendars."
        ),
    )


def _guard_read() -> Optional[LocalResponse]:
    return None if _auth_status() == 3 else _denied(read=True)


def _guard_write() -> Optional[LocalResponse]:
    return None if _auth_status() in (3, 4) else _denied(read=False)


# ---------------------------------------------------------------------------
# Date helpers
# ---------------------------------------------------------------------------


def _parse_iso(value: str) -> datetime:
    """ISO 8601 in; naive values are taken as the Mac's local time."""
    dt = datetime.fromisoformat(value.replace("Z", "+00:00"))
    if dt.tzinfo is None:
        dt = dt.astimezone()
    return dt


def _to_nsdate(dt: datetime):
    return Foundation.NSDate.dateWithTimeIntervalSince1970_(dt.timestamp())


def _from_nsdate(nsdate) -> Optional[str]:
    if nsdate is None:
        return None
    return datetime.fromtimestamp(
        nsdate.timeIntervalSince1970(), tz=timezone.utc
    ).astimezone().isoformat()


# ---------------------------------------------------------------------------
# Serializers
# ---------------------------------------------------------------------------


def _calendar_dict(cal) -> Dict[str, Any]:
    source = cal.source()
    return {
        "id": str(cal.calendarIdentifier()),
        "title": str(cal.title()),
        "account": str(source.title()) if source is not None else None,
        "writable": bool(cal.allowsContentModifications()),
    }


def _event_dict(event, include_notes: bool = False) -> Dict[str, Any]:
    cal = event.calendar()
    data: Dict[str, Any] = {
        "id": str(event.eventIdentifier()),
        "title": str(event.title()) if event.title() else None,
        "start": _from_nsdate(event.startDate()),
        "end": _from_nsdate(event.endDate()),
        "all_day": bool(event.isAllDay()),
        "calendar": str(cal.title()) if cal is not None else None,
        "location": str(event.location()) if event.location() else None,
        "recurring": bool(event.hasRecurrenceRules()),
    }
    if include_notes and event.notes():
        data["notes"] = str(event.notes())
    return data


def _find_calendar(store, name: Optional[str]):
    """Resolve a calendar by title (case-insensitive); None means default."""
    if not name:
        return store.defaultCalendarForNewEvents()
    for cal in store.calendarsForEntityType_(EK_ENTITY_EVENT):
        if str(cal.title()).lower() == name.lower():
            return cal
    return None


# ---------------------------------------------------------------------------
# FastMCP server
# ---------------------------------------------------------------------------

mcp = FastMCP("apple-calendar")


# ---------------------------------------------------------------------------
# Access tools
# ---------------------------------------------------------------------------


@mcp.tool()
async def authorization_status() -> Dict[str, Any]:
    """
    Report the macOS Calendar permission status for this server's host
    process. Never triggers a permission dialog.
    """
    status = _auth_status()
    return LocalResponse(
        ok=True,
        data={
            "status": AUTH_STATUS_LABELS.get(status, f"unknown({status})"),
            "read_ready": status == 3,
            "write_ready": status in (3, 4),
        },
    ).model_dump(mode="json")


@mcp.tool()
async def request_access() -> Dict[str, Any]:
    """
    Request Full Access to the Mac's calendars. On first call macOS
    shows a permission dialog attributed to the hosting app -- the
    operator must approve it. Waits up to three minutes for the answer.
    Safe to call repeatedly; once granted it returns immediately.
    """
    if _auth_status() == 3:
        return LocalResponse(ok=True, data={"status": "authorized_full"}).model_dump(
            mode="json"
        )

    store = _event_store()
    done = threading.Event()
    outcome: Dict[str, Any] = {"granted": False, "error": None}

    def completion(granted, error):
        outcome["granted"] = bool(granted)
        outcome["error"] = str(error) if error else None
        done.set()

    if hasattr(store, "requestFullAccessToEventsWithCompletion_"):
        store.requestFullAccessToEventsWithCompletion_(completion)
    else:
        store.requestAccessToEntityType_completion_(EK_ENTITY_EVENT, completion)

    if not done.wait(REQUEST_ACCESS_TIMEOUT_SECONDS):
        return LocalResponse(
            ok=False,
            error="Timed out waiting for the macOS permission dialog.",
        ).model_dump(mode="json")

    _event_store(reset=True)
    status = _auth_status()
    return LocalResponse(
        ok=outcome["granted"],
        data={"status": AUTH_STATUS_LABELS.get(status, f"unknown({status})")},
        error=outcome["error"] if not outcome["granted"] else None,
    ).model_dump(mode="json")


# ---------------------------------------------------------------------------
# Tier 1 -- Read-only
# ---------------------------------------------------------------------------


@mcp.tool()
async def list_calendars() -> Dict[str, Any]:
    """
    List every event calendar the Mac knows about -- iCloud, Google,
    Exchange, local -- with its account and writability.
    """
    guard = _guard_read()
    if guard:
        return guard.model_dump(mode="json")
    store = _event_store()
    cals = [_calendar_dict(c) for c in store.calendarsForEntityType_(EK_ENTITY_EVENT)]
    return LocalResponse(ok=True, data=cals).model_dump(mode="json")


@mcp.tool()
async def list_events(
    start: str,
    end: str,
    calendar_names: Optional[List[str]] = None,
    max_results: int = 200,
) -> Dict[str, Any]:
    """
    Events across the given window (ISO 8601; naive times read as Mac
    local time), sorted by start. Optionally restrict to calendars by
    title. Recurring events appear as expanded occurrences.
    """
    guard = _guard_read()
    if guard:
        return guard.model_dump(mode="json")
    store = _event_store()

    cals = None
    if calendar_names:
        wanted = {n.lower() for n in calendar_names}
        cals = [
            c
            for c in store.calendarsForEntityType_(EK_ENTITY_EVENT)
            if str(c.title()).lower() in wanted
        ]
        if not cals:
            return LocalResponse(
                ok=False, error=f"No calendars matched: {calendar_names}"
            ).model_dump(mode="json")

    predicate = store.predicateForEventsWithStartDate_endDate_calendars_(
        _to_nsdate(_parse_iso(start)), _to_nsdate(_parse_iso(end)), cals
    )
    events = store.eventsMatchingPredicate_(predicate) or []
    events = sorted(events, key=lambda e: e.startDate().timeIntervalSince1970())
    data = [_event_dict(e) for e in events[:max_results]]
    return LocalResponse(
        ok=True, data={"count": len(data), "events": data}
    ).model_dump(mode="json")


@mcp.tool()
async def search_events(
    query: str,
    start: str,
    end: str,
    max_results: int = 50,
) -> Dict[str, Any]:
    """
    Case-insensitive search over title, location and notes within a
    window (ISO 8601).
    """
    guard = _guard_read()
    if guard:
        return guard.model_dump(mode="json")
    store = _event_store()
    predicate = store.predicateForEventsWithStartDate_endDate_calendars_(
        _to_nsdate(_parse_iso(start)), _to_nsdate(_parse_iso(end)), None
    )
    needle = query.lower()
    hits = []
    for event in store.eventsMatchingPredicate_(predicate) or []:
        haystack = " ".join(
            str(part)
            for part in (event.title(), event.location(), event.notes())
            if part
        ).lower()
        if needle in haystack:
            hits.append(event)
    hits = sorted(hits, key=lambda e: e.startDate().timeIntervalSince1970())
    data = [_event_dict(e, include_notes=True) for e in hits[:max_results]]
    return LocalResponse(
        ok=True, data={"count": len(data), "events": data}
    ).model_dump(mode="json")


@mcp.tool()
async def get_event(event_id: str) -> Dict[str, Any]:
    """Fetch one event by its identifier, including notes."""
    guard = _guard_read()
    if guard:
        return guard.model_dump(mode="json")
    store = _event_store()
    event = store.eventWithIdentifier_(event_id)
    if event is None:
        return LocalResponse(
            ok=False, error=f"No event with identifier {event_id}."
        ).model_dump(mode="json")
    return LocalResponse(ok=True, data=_event_dict(event, include_notes=True)).model_dump(
        mode="json"
    )


# ---------------------------------------------------------------------------
# Tier 2 -- Writes (gated in chat per Navigation Rule 3)
# ---------------------------------------------------------------------------


@mcp.tool()
async def create_event(
    title: str,
    start: str,
    end: str,
    calendar_name: Optional[str] = None,
    all_day: bool = False,
    location: Optional[str] = None,
    notes: Optional[str] = None,
) -> Dict[str, Any]:
    """
    WRITE. Create an event on a calendar (by title; default is the
    system default calendar for new events). Times are ISO 8601; naive
    values read as Mac local time.

    Alfred must confirm with the user before calling. Events on shared
    or subscribed-account calendars sync outward to those services.
    """
    guard = _guard_write()
    if guard:
        return guard.model_dump(mode="json")
    store = _event_store()
    calendar = _find_calendar(store, calendar_name)
    if calendar is None:
        return LocalResponse(
            ok=False, error=f"No calendar titled '{calendar_name}'."
        ).model_dump(mode="json")

    event = EventKit.EKEvent.eventWithEventStore_(store)
    event.setTitle_(title)
    event.setStartDate_(_to_nsdate(_parse_iso(start)))
    event.setEndDate_(_to_nsdate(_parse_iso(end)))
    event.setAllDay_(all_day)
    if location:
        event.setLocation_(location)
    if notes:
        event.setNotes_(notes)
    event.setCalendar_(calendar)

    ok, error = store.saveEvent_span_error_(event, EK_SPAN_THIS, None)
    if not ok:
        return LocalResponse(
            ok=False, error=f"Save failed: {error}"
        ).model_dump(mode="json")
    return LocalResponse(ok=True, data=_event_dict(event)).model_dump(mode="json")


@mcp.tool()
async def update_event(
    event_id: str,
    title: Optional[str] = None,
    start: Optional[str] = None,
    end: Optional[str] = None,
    location: Optional[str] = None,
    notes: Optional[str] = None,
    span: str = "this",
) -> Dict[str, Any]:
    """
    WRITE. Update an event -- only the provided fields change. `span`
    is 'this' for a single occurrence or 'future' to change this and
    all later occurrences of a recurring event.

    Alfred must confirm with the user before calling.
    """
    guard = _guard_write()
    if guard:
        return guard.model_dump(mode="json")
    store = _event_store()
    event = store.eventWithIdentifier_(event_id)
    if event is None:
        return LocalResponse(
            ok=False, error=f"No event with identifier {event_id}."
        ).model_dump(mode="json")

    if title is not None:
        event.setTitle_(title)
    if start is not None:
        event.setStartDate_(_to_nsdate(_parse_iso(start)))
    if end is not None:
        event.setEndDate_(_to_nsdate(_parse_iso(end)))
    if location is not None:
        event.setLocation_(location)
    if notes is not None:
        event.setNotes_(notes)

    ek_span = EK_SPAN_FUTURE if span == "future" else EK_SPAN_THIS
    ok, error = store.saveEvent_span_error_(event, ek_span, None)
    if not ok:
        return LocalResponse(
            ok=False, error=f"Save failed: {error}"
        ).model_dump(mode="json")
    return LocalResponse(ok=True, data=_event_dict(event)).model_dump(mode="json")


@mcp.tool()
async def delete_event(event_id: str, span: str = "this") -> Dict[str, Any]:
    """
    WRITE. Delete an event. `span` is 'this' for a single occurrence
    or 'future' to remove this and all later occurrences.

    Alfred must confirm with the user before calling. Deletions on
    shared calendars propagate to other participants.
    """
    guard = _guard_write()
    if guard:
        return guard.model_dump(mode="json")
    store = _event_store()
    event = store.eventWithIdentifier_(event_id)
    if event is None:
        return LocalResponse(
            ok=False, error=f"No event with identifier {event_id}."
        ).model_dump(mode="json")

    ek_span = EK_SPAN_FUTURE if span == "future" else EK_SPAN_THIS
    ok, error = store.removeEvent_span_error_(event, ek_span, None)
    if not ok:
        return LocalResponse(
            ok=False, error=f"Delete failed: {error}"
        ).model_dump(mode="json")
    return LocalResponse(ok=True, data={"deleted": event_id}).model_dump(mode="json")


# ---------------------------------------------------------------------------
# Entrypoint
# ---------------------------------------------------------------------------


if __name__ == "__main__":
    mcp.run(transport="stdio")
