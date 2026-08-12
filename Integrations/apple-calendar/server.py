#!/usr/bin/env python3
"""
Apple Calendar MCP Server -- AppleScript access to every calendar
Calendar.app knows about.

Thin FastMCP layer driving Calendar.app over AppleScript. Reads and
writes the calendars configured in macOS -- iCloud, Google, Exchange or
local -- through the application rather than the system calendar store.

Rewritten 2026-08-12 (Domesday follow-through). The original build used
EventKit via PyObjC, chosen for predicate-query speed and structured
CRUD. That choice proved unreachable in practice: the server runs as a
bare Homebrew python3.12 with no application bundle, so it cannot raise
a TCC dialog itself, and the hosting Claude app declares no
NSCalendarsUsageDescription, so macOS refuses to raise one on its
behalf. Every request returned not_determined instantly and silently,
no Calendars entry was ever created in System Settings, and that pane
offers no manual add. The lane was dark from 2026-07-10 to 2026-08-12.

AppleScript reaches the same data through the Automation permission
(NSAppleEventsUsageDescription), which the Claude app does declare and
which the apple-mail server has used successfully throughout. The
trade-offs are accepted knowingly and documented at each site:

- Calendar.app must be installed; it is launched on demand.
- Per-occurrence editing of recurring events is not addressable through
  AppleScript. Writes reach the master event and therefore the whole
  series. The `span` parameter is retained for signature compatibility
  and reports this plainly rather than failing silently.
- Calendar accounts (iCloud, Google) are not exposed by Calendar.app,
  so the `account` field is always null.
- Enumeration is slower than EventKit predicates. Properties are read
  in bulk -- one Apple Event per property per calendar rather than one
  per event -- which keeps typical windows well inside a second.

Write tools carry `WRITE.` in their description so the calling agent
follows Navigation Rule 3 and asks for confirmation before dispatch.
The server itself does not enforce the gate.
"""

import subprocess
from datetime import datetime, timezone
from typing import Optional, List, Dict, Any

from pydantic import BaseModel, Field
from mcp.server.fastmcp import FastMCP

# ---------------------------------------------------------------------------
# Configuration
# ---------------------------------------------------------------------------

# Field and record separators. ASCII unit/record separators are used
# because they cannot occur in calendar text entered through any UI.
FS = "\x1f"
RS = "\x1e"

OSASCRIPT_TIMEOUT_SECONDS = 120.0

# Preferred calendar for new events when the caller names none.
DEFAULT_CALENDAR_PREFERENCE = "Calendar"


# ---------------------------------------------------------------------------
# Models
# ---------------------------------------------------------------------------


class LocalResponse(BaseModel):
    """Wrapper for responses that may fail before reaching Calendar.app."""

    ok: bool
    data: Optional[Any] = None
    error: Optional[str] = None
    fetched_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))


# ---------------------------------------------------------------------------
# AppleScript plumbing
# ---------------------------------------------------------------------------

# Date construction by component keeps the script locale-independent.
# Day is reset to 1 before year and month are set, so that assigning a
# month with fewer days than the current one cannot overflow.
DATE_HANDLER = """
on mkdate(y, m, d, hh, mm, ss)
    set dt to current date
    set day of dt to 1
    set year of dt to y
    set month of dt to m
    set day of dt to d
    set hours of dt to hh
    set minutes of dt to mm
    set seconds of dt to ss
    return dt
end mkdate

-- Plural property access returns a bare value when a whose clause
-- matches exactly one object. Normalise so the caller always indexes.
on aslist(v)
    if class of v is list then return v
    return {v}
end aslist
"""


class AppleScriptError(RuntimeError):
    pass


def _run(script: str, timeout: float = OSASCRIPT_TIMEOUT_SECONDS) -> str:
    """Execute AppleScript via osascript, returning trimmed stdout."""
    try:
        proc = subprocess.run(
            ["osascript", "-"],
            input=script,
            capture_output=True,
            text=True,
            encoding="utf-8",
            timeout=timeout,
        )
    except subprocess.TimeoutExpired:
        raise AppleScriptError(
            f"Calendar.app did not respond within {timeout:.0f}s. Large date "
            "windows enumerate slowly; narrow the range or name fewer calendars."
        )
    if proc.returncode != 0:
        raise AppleScriptError((proc.stderr or "osascript failed").strip())
    return proc.stdout.rstrip("\n")


def _quote(value: str) -> str:
    """Escape a Python string for embedding as an AppleScript literal."""
    escaped = value.replace("\\", "\\\\").replace('"', '\\"')
    return f'"{escaped}"'


def _parse_iso(value: str) -> datetime:
    """ISO 8601 in; naive values are taken as the Mac's local time."""
    dt = datetime.fromisoformat(value.replace("Z", "+00:00"))
    if dt.tzinfo is None:
        return dt
    return dt.astimezone()


def _date_expr(value: str) -> str:
    """Render an ISO timestamp as a call to the mkdate handler."""
    dt = _parse_iso(value)
    return (
        f"(my mkdate({dt.year}, {dt.month}, {dt.day}, "
        f"{dt.hour}, {dt.minute}, {dt.second}))"
    )


def _iso_out(raw: str) -> Optional[str]:
    """Attach the Mac's local offset to an AppleScript isot string."""
    if not raw or raw == "missing value":
        return None
    try:
        return datetime.fromisoformat(raw).astimezone().isoformat()
    except ValueError:
        return raw


def _clean(raw: str) -> Optional[str]:
    return None if raw in ("", "missing value") else raw


# ---------------------------------------------------------------------------
# Calendar helpers
# ---------------------------------------------------------------------------


def _calendar_names() -> List[Dict[str, Any]]:
    script = f"""
set FS to (character id 31)
set RS to (character id 30)
set out to ""
tell application "Calendar"
    set cals to every calendar
    repeat with c in cals
        set out to out & (name of c) & FS & (writable of c) & RS
    end repeat
end tell
return out
"""
    raw = _run(script)
    entries = []
    for record in raw.split(RS):
        if not record.strip():
            continue
        parts = record.split(FS)
        if len(parts) < 2:
            continue
        entries.append(
            {
                "id": parts[0],
                "title": parts[0],
                # Calendar.app exposes no account or source property.
                "account": None,
                "writable": parts[1].strip().lower() == "true",
            }
        )
    return entries


def _resolve_calendar(name: Optional[str]) -> Optional[str]:
    """Resolve a calendar by title, case-insensitively. None picks a default."""
    calendars = _calendar_names()
    if name:
        for cal in calendars:
            if cal["title"].lower() == name.lower():
                return cal["title"]
        return None
    for cal in calendars:
        if cal["title"] == DEFAULT_CALENDAR_PREFERENCE and cal["writable"]:
            return cal["title"]
    for cal in calendars:
        if cal["writable"]:
            return cal["title"]
    return None


def _fetch_events(
    start: str,
    end: str,
    calendar_names: Optional[List[str]] = None,
) -> List[Dict[str, Any]]:
    """
    Read events in a window across the named calendars, or all of them.

    Properties are pulled as whole lists -- one Apple Event per property
    per calendar -- rather than per event, which is the difference
    between a fast query and a slow one on a populated calendar.
    """
    if calendar_names:
        available = {c["title"].lower(): c["title"] for c in _calendar_names()}
        resolved = [available[n.lower()] for n in calendar_names if n.lower() in available]
        if not resolved:
            raise AppleScriptError(f"No calendars matched: {calendar_names}")
        target = "{" + ", ".join(f"calendar {_quote(n)}" for n in resolved) + "}"
    else:
        target = "(every calendar)"

    script = f"""
{DATE_HANDLER}
set FS to (character id 31)
set RS to (character id 30)
set d1 to {_date_expr(start)}
set d2 to {_date_expr(end)}
set out to ""
tell application "Calendar"
    repeat with c in {target}
        set calName to name of c
        tell c
            -- The reference must be kept unmaterialised: assigning the
            -- whose clause to a plain variable collapses it to a list
            -- and plural property access then fails.
            set evRefs to (a reference to (every event whose start date is greater than or equal to d1 and start date is less than d2))
            set theUIDs to my aslist(uid of evRefs)
            set n to (count of theUIDs)
            if n is greater than 0 then
                set theSummaries to my aslist(summary of evRefs)
                set theStarts to my aslist(start date of evRefs)
                set theEnds to my aslist(end date of evRefs)
                set theAllDay to my aslist(allday event of evRefs)
                set theLocations to my aslist(location of evRefs)
                set theNotes to my aslist(description of evRefs)
            end if
        end tell
        if n is greater than 0 then
            repeat with i from 1 to n
                set s to (item i of theStarts)
                set e to (item i of theEnds)
                set sTxt to ((s as «class isot») as string)
                set eTxt to ((e as «class isot») as string)
                set sumTxt to (item i of theSummaries)
                if sumTxt is missing value then set sumTxt to ""
                set locTxt to (item i of theLocations)
                if locTxt is missing value then set locTxt to ""
                set noteTxt to (item i of theNotes)
                if noteTxt is missing value then set noteTxt to ""
                set out to out & (item i of theUIDs) & FS & sumTxt & FS & sTxt & FS & eTxt & FS & (item i of theAllDay) & FS & locTxt & FS & noteTxt & FS & calName & RS
            end repeat
        end if
    end repeat
end tell
return out
"""
    raw = _run(script)
    events: List[Dict[str, Any]] = []
    for record in raw.split(RS):
        if not record.strip():
            continue
        parts = record.split(FS)
        if len(parts) < 8:
            continue
        events.append(
            {
                "id": parts[0],
                "title": _clean(parts[1]),
                "start": _iso_out(parts[2]),
                "end": _iso_out(parts[3]),
                "all_day": parts[4].strip().lower() == "true",
                "calendar": parts[7],
                "location": _clean(parts[5]),
                "notes": _clean(parts[6]),
                # Calendar.app exposes recurrence only as a rule string on
                # the master event; occurrences are not addressable.
                "recurring": None,
            }
        )
    events.sort(key=lambda e: e["start"] or "")
    return events


def _strip_notes(event: Dict[str, Any]) -> Dict[str, Any]:
    trimmed = dict(event)
    trimmed.pop("notes", None)
    return trimmed


def _locate_event(event_id: str) -> Optional[Dict[str, str]]:
    """Find which calendar holds a uid. Returns the calendar title."""
    script = f"""
tell application "Calendar"
    repeat with c in (every calendar)
        tell c
            set hits to (every event whose uid is {_quote(event_id)})
        end tell
        if (count of hits) is greater than 0 then return (name of c)
    end repeat
end tell
return ""
"""
    name = _run(script).strip()
    return {"calendar": name} if name else None


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
    Report whether Calendar.app is reachable over AppleScript. Since the
    2026-08-12 rewrite this reflects the macOS Automation permission
    rather than the Calendars privacy pane, which this server no longer
    uses. Does not trigger a permission dialog on its own.
    """
    try:
        _run('tell application "Calendar" to return name of first calendar', timeout=20)
    except AppleScriptError as exc:
        return LocalResponse(
            ok=True,
            data={
                "status": "denied",
                "read_ready": False,
                "write_ready": False,
                "detail": str(exc),
            },
        ).model_dump(mode="json")
    return LocalResponse(
        ok=True,
        data={"status": "authorized_full", "read_ready": True, "write_ready": True},
    ).model_dump(mode="json")


@mcp.tool()
async def request_access() -> Dict[str, Any]:
    """
    Trigger the macOS Automation prompt for Calendar.app if it has not
    yet been granted. The dialog is attributed to the hosting app and
    the operator must approve it. Safe to call repeatedly; once granted
    it returns immediately.
    """
    try:
        count = _run('tell application "Calendar" to return count of every calendar')
    except AppleScriptError as exc:
        return LocalResponse(
            ok=False,
            error=(
                f"Calendar.app is not reachable: {exc} Approve the Automation "
                "prompt if one appeared, or enable it at System Settings > "
                "Privacy & Security > Automation."
            ),
        ).model_dump(mode="json")
    return LocalResponse(
        ok=True,
        data={"status": "authorized_full", "calendars_visible": int(count or 0)},
    ).model_dump(mode="json")


# ---------------------------------------------------------------------------
# Tier 1 -- Read-only
# ---------------------------------------------------------------------------


@mcp.tool()
async def list_calendars() -> Dict[str, Any]:
    """
    List every calendar Calendar.app knows about -- iCloud, Google,
    Exchange, local -- with its writability. The owning account is not
    exposed by Calendar.app and is always null.
    """
    try:
        return LocalResponse(ok=True, data=_calendar_names()).model_dump(mode="json")
    except AppleScriptError as exc:
        return LocalResponse(ok=False, error=str(exc)).model_dump(mode="json")


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
    title.

    Recurring events are NOT expanded. Calendar.app exposes only the
    master event over AppleScript, carrying its original start date, so
    an annually recurring birthday first set in 1990 matches a window
    around 1990 and not around this year. Widen the window when hunting
    a recurring series. This is a real difference from the EventKit
    build replaced on 2026-08-12 and cannot be worked around from here.
    """
    try:
        events = _fetch_events(start, end, calendar_names)
    except AppleScriptError as exc:
        return LocalResponse(ok=False, error=str(exc)).model_dump(mode="json")
    data = [_strip_notes(e) for e in events[:max_results]]
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
    try:
        events = _fetch_events(start, end)
    except AppleScriptError as exc:
        return LocalResponse(ok=False, error=str(exc)).model_dump(mode="json")
    needle = query.lower()
    hits = [
        e
        for e in events
        if needle
        in " ".join(
            part for part in (e["title"], e["location"], e["notes"]) if part
        ).lower()
    ]
    data = hits[:max_results]
    return LocalResponse(
        ok=True, data={"count": len(data), "events": data}
    ).model_dump(mode="json")


@mcp.tool()
async def get_event(event_id: str) -> Dict[str, Any]:
    """Fetch one event by its identifier, including notes."""
    script = f"""
set FS to (character id 31)
tell application "Calendar"
    repeat with c in (every calendar)
        set calName to name of c
        tell c
            set hits to (every event whose uid is {_quote(event_id)})
        end tell
        if (count of hits) is greater than 0 then
            set e to item 1 of hits
            set sumTxt to summary of e
            if sumTxt is missing value then set sumTxt to ""
            set locTxt to location of e
            if locTxt is missing value then set locTxt to ""
            set noteTxt to description of e
            if noteTxt is missing value then set noteTxt to ""
            return (uid of e) & FS & sumTxt & FS & (((start date of e) as «class isot») as string) & FS & (((end date of e) as «class isot») as string) & FS & (allday event of e) & FS & locTxt & FS & noteTxt & FS & calName
        end if
    end repeat
end tell
return ""
"""
    try:
        raw = _run(script)
    except AppleScriptError as exc:
        return LocalResponse(ok=False, error=str(exc)).model_dump(mode="json")
    if not raw.strip():
        return LocalResponse(
            ok=False, error=f"No event with identifier {event_id}."
        ).model_dump(mode="json")
    parts = raw.split(FS)
    data = {
        "id": parts[0],
        "title": _clean(parts[1]),
        "start": _iso_out(parts[2]),
        "end": _iso_out(parts[3]),
        "all_day": parts[4].strip().lower() == "true",
        "calendar": parts[7],
        "location": _clean(parts[5]),
        "notes": _clean(parts[6]),
        "recurring": None,
    }
    return LocalResponse(ok=True, data=data).model_dump(mode="json")


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
    calendar named "Calendar", else the first writable one). Times are
    ISO 8601; naive values read as Mac local time.

    Alfred must confirm with the user before calling. Events on shared
    or subscribed-account calendars sync outward to those services.
    """
    try:
        resolved = _resolve_calendar(calendar_name)
    except AppleScriptError as exc:
        return LocalResponse(ok=False, error=str(exc)).model_dump(mode="json")
    if resolved is None:
        return LocalResponse(
            ok=False,
            error=(
                f"No calendar titled '{calendar_name}'."
                if calendar_name
                else "No writable calendar available."
            ),
        ).model_dump(mode="json")

    props = [
        f"summary:{_quote(title)}",
        f"start date:{_date_expr(start)}",
        f"end date:{_date_expr(end)}",
        f"allday event:{'true' if all_day else 'false'}",
    ]
    if location:
        props.append(f"location:{_quote(location)}")
    if notes:
        props.append(f"description:{_quote(notes)}")

    script = f"""
{DATE_HANDLER}
tell application "Calendar"
    tell calendar {_quote(resolved)}
        set newEvent to make new event at end of events with properties {{{", ".join(props)}}}
        return uid of newEvent
    end tell
end tell
"""
    try:
        uid = _run(script).strip()
    except AppleScriptError as exc:
        return LocalResponse(ok=False, error=f"Create failed: {exc}").model_dump(
            mode="json"
        )
    return LocalResponse(
        ok=True,
        data={
            "id": uid,
            "title": title,
            "start": _parse_iso(start).astimezone().isoformat(),
            "end": _parse_iso(end).astimezone().isoformat(),
            "all_day": all_day,
            "calendar": resolved,
            "location": location,
        },
    ).model_dump(mode="json")


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
    WRITE. Update an event -- only the provided fields change.

    `span` is retained for signature compatibility but Calendar.app
    cannot address a single occurrence of a recurring event over
    AppleScript: edits reach the master event and therefore the whole
    series. The response reports when that has happened.

    Alfred must confirm with the user before calling.
    """
    try:
        located = _locate_event(event_id)
    except AppleScriptError as exc:
        return LocalResponse(ok=False, error=str(exc)).model_dump(mode="json")
    if located is None:
        return LocalResponse(
            ok=False, error=f"No event with identifier {event_id}."
        ).model_dump(mode="json")

    assignments = []
    if title is not None:
        assignments.append(f"set summary of e to {_quote(title)}")
    if start is not None:
        assignments.append(f"set start date of e to {_date_expr(start)}")
    if end is not None:
        assignments.append(f"set end date of e to {_date_expr(end)}")
    if location is not None:
        assignments.append(f"set location of e to {_quote(location)}")
    if notes is not None:
        assignments.append(f"set description of e to {_quote(notes)}")
    if not assignments:
        return LocalResponse(ok=False, error="No fields supplied to update.").model_dump(
            mode="json"
        )

    script = f"""
{DATE_HANDLER}
tell application "Calendar"
    tell calendar {_quote(located["calendar"])}
        set hits to (every event whose uid is {_quote(event_id)})
        set e to item 1 of hits
        {chr(10).join("        " + line for line in assignments).strip()}
        return uid of e
    end tell
end tell
"""
    try:
        _run(script)
    except AppleScriptError as exc:
        return LocalResponse(ok=False, error=f"Update failed: {exc}").model_dump(
            mode="json"
        )
    return LocalResponse(
        ok=True,
        data={
            "id": event_id,
            "calendar": located["calendar"],
            "updated": [a.split()[1] for a in assignments],
            "span_note": (
                "Applied to the master event. If this event recurs, the change "
                "reaches the whole series -- AppleScript cannot address a single "
                "occurrence."
            ),
        },
    ).model_dump(mode="json")


@mcp.tool()
async def delete_event(event_id: str, span: str = "this") -> Dict[str, Any]:
    """
    WRITE. Delete an event.

    `span` is retained for signature compatibility but Calendar.app
    cannot address a single occurrence of a recurring event over
    AppleScript: a deletion removes the master event and therefore the
    whole series. The response reports this.

    Alfred must confirm with the user before calling. Deletions on
    shared calendars propagate to other participants.
    """
    try:
        located = _locate_event(event_id)
    except AppleScriptError as exc:
        return LocalResponse(ok=False, error=str(exc)).model_dump(mode="json")
    if located is None:
        return LocalResponse(
            ok=False, error=f"No event with identifier {event_id}."
        ).model_dump(mode="json")

    script = f"""
tell application "Calendar"
    tell calendar {_quote(located["calendar"])}
        set hits to (every event whose uid is {_quote(event_id)})
        delete (item 1 of hits)
    end tell
end tell
return "ok"
"""
    try:
        _run(script)
    except AppleScriptError as exc:
        return LocalResponse(ok=False, error=f"Delete failed: {exc}").model_dump(
            mode="json"
        )
    return LocalResponse(
        ok=True,
        data={
            "deleted": event_id,
            "calendar": located["calendar"],
            "span_note": (
                "Removed the master event. If this event recurred, the whole "
                "series is gone -- AppleScript cannot delete a single occurrence."
            ),
        },
    ).model_dump(mode="json")


# ---------------------------------------------------------------------------
# Entrypoint
# ---------------------------------------------------------------------------


if __name__ == "__main__":
    mcp.run(transport="stdio")
