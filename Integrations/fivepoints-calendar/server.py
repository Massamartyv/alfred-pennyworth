#!/usr/bin/env python3
"""
Five Points Calendar MCP Server -- Venture-scoped Google Calendar access.

Thin FastMCP layer over the Google Calendar API v3. Every tool takes a
`user` routing key which selects one of the Five Points Workspace users.
A single Google Cloud service account with domain-wide delegation
impersonates the target user per request -- the same credential the
fivepoints-mail server uses, resolved through a shared fallback chain,
so one key drop provisions both servers.

There is no implicit default user: nothing can be read or written
without an explicit selection, matching the fivepoints-mail doctrine.

Write tools carry `WRITE.` in their description so the calling agent
follows Navigation Rule 3 and asks for confirmation before dispatch.
The server itself does not enforce the gate.

Domain-wide delegation must include the Calendar scope below (admin
console: Security > API controls > Domain-wide delegation). Until that
grant exists, authenticated calls return 401/403 through the envelope.
"""

import os
from datetime import datetime, timezone
from enum import Enum
from functools import lru_cache
from typing import Optional, List, Dict, Any, Callable

from google.oauth2 import service_account
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from pydantic import BaseModel, Field
from mcp.server.fastmcp import FastMCP


# ---------------------------------------------------------------------------
# Configuration
# ---------------------------------------------------------------------------

_MAIL_DEFAULT_CREDENTIALS_PATH = os.path.abspath(
    os.path.join(
        os.path.dirname(os.path.abspath(__file__)),
        "..",
        "fivepoints-mail",
        "credentials",
        "service-account.json",
    )
)

# Resolution chain: calendar-specific override, then the mail override,
# then the mail server's default drop location. One credential, two servers.
SERVICE_ACCOUNT_PATH = (
    os.getenv("FIVEPOINTS_CALENDAR_SERVICE_ACCOUNT")
    or os.getenv("FIVEPOINTS_MAIL_SERVICE_ACCOUNT")
    or _MAIL_DEFAULT_CREDENTIALS_PATH
)

SCOPES = ["https://www.googleapis.com/auth/calendar"]


# ---------------------------------------------------------------------------
# User registry
# ---------------------------------------------------------------------------


class CalendarUser(str, Enum):
    """
    Routing key for a Five Points Calendar request. Each value maps to
    one user inside the fivepoints.studio Google Workspace.
    """

    HELLO = "hello"
    MARTAVIOUS = "martavious"
    SYSTEMS = "systems"
    OPPORTUNITIES = "opportunities"
    FINANCE = "finance"


USER_REGISTRY: Dict[CalendarUser, Dict[str, str]] = {
    CalendarUser.HELLO: {
        "email": "hello@fivepoints.studio",
        "label": "Hello",
        "role": "Workspace admin calendar.",
    },
    CalendarUser.MARTAVIOUS: {
        "email": "martavious@fivepoints.studio",
        "label": "Martavious",
        "role": "Owner-direct. Primary studio calendar; Cal.com bookings land here.",
    },
    CalendarUser.SYSTEMS: {
        "email": "systems@fivepoints.studio",
        "label": "Systems",
        "role": "Technical infrastructure calendar.",
    },
    CalendarUser.OPPORTUNITIES: {
        "email": "opportunities@fivepoints.studio",
        "label": "Opportunities",
        "role": "Press, vendor and hiring calendar.",
    },
    CalendarUser.FINANCE: {
        "email": "finance@fivepoints.studio",
        "label": "Finance",
        "role": "Financial platform calendar.",
    },
}


def _user_email(user: CalendarUser) -> str:
    return USER_REGISTRY[user]["email"]


# ---------------------------------------------------------------------------
# Models
# ---------------------------------------------------------------------------


class UserResponse(BaseModel):
    """Wrapper for responses that may fail before reaching Google."""

    user: str
    ok: bool
    data: Optional[Any] = None
    error: Optional[str] = None
    status_code: Optional[int] = None
    fetched_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))


# ---------------------------------------------------------------------------
# Calendar client factory -- one service per user, cached.
# ---------------------------------------------------------------------------


@lru_cache(maxsize=None)
def _calendar_service(user_email: str):
    """
    Build a Calendar service object impersonating `user_email` via the
    service account's domain-wide delegation. Cached so repeated calls
    do not re-read the key file.
    """
    if not os.path.exists(SERVICE_ACCOUNT_PATH):
        raise FileNotFoundError(
            f"Service account key not found at {SERVICE_ACCOUNT_PATH}. "
            "Drop the JSON key there (shared with fivepoints-mail) or set "
            "FIVEPOINTS_CALENDAR_SERVICE_ACCOUNT."
        )
    credentials = service_account.Credentials.from_service_account_file(
        SERVICE_ACCOUNT_PATH, scopes=SCOPES
    ).with_subject(user_email)
    return build("calendar", "v3", credentials=credentials, cache_discovery=False)


def _execute(user: CalendarUser, call: Callable[[Any], Any]) -> UserResponse:
    """
    Run one Calendar API call for a user and normalize every failure
    into the envelope. Never raises.
    """
    try:
        service = _calendar_service(_user_email(user))
        data = call(service)
        return UserResponse(user=user.value, ok=True, status_code=200, data=data)
    except FileNotFoundError as exc:
        return UserResponse(user=user.value, ok=False, error=str(exc))
    except HttpError as exc:
        status = exc.resp.status if exc.resp is not None else None
        return UserResponse(
            user=user.value,
            ok=False,
            status_code=status,
            error=f"Google Calendar {status}: {str(exc)[:500]}",
        )
    except Exception as exc:
        return UserResponse(
            user=user.value, ok=False, error=f"Request failed: {exc}"
        )


# ---------------------------------------------------------------------------
# FastMCP server
# ---------------------------------------------------------------------------

mcp = FastMCP("fivepoints-calendar")


# ---------------------------------------------------------------------------
# Helper tools
# ---------------------------------------------------------------------------


@mcp.tool()
async def list_users() -> List[Dict[str, str]]:
    """Return the user registry -- routing key, email, label, role."""
    return [
        {"user": user.value, **info}
        for user, info in USER_REGISTRY.items()
    ]


@mcp.tool()
async def health_check(user: CalendarUser) -> Dict[str, Any]:
    """
    Verify Calendar API access for a user by fetching their primary
    calendar. Proves the key file exists, delegation covers the
    Calendar scope and impersonation works end to end.
    """
    result = _execute(user, lambda s: s.calendars().get(calendarId="primary").execute())
    return result.model_dump(mode="json")


# ---------------------------------------------------------------------------
# Tier 1 -- Read-only
# ---------------------------------------------------------------------------


@mcp.tool()
async def list_calendars(user: CalendarUser) -> Dict[str, Any]:
    """
    List the calendars visible to a user -- their own plus anything
    shared with them, with access roles.
    """
    def call(s):
        items = s.calendarList().list(maxResults=100).execute().get("items", [])
        return [
            {
                "id": c.get("id"),
                "summary": c.get("summary"),
                "primary": c.get("primary", False),
                "access_role": c.get("accessRole"),
                "time_zone": c.get("timeZone"),
            }
            for c in items
        ]

    return _execute(user, call).model_dump(mode="json")


@mcp.tool()
async def list_events(
    user: CalendarUser,
    calendar_id: str = "primary",
    time_min: Optional[str] = None,
    time_max: Optional[str] = None,
    query: Optional[str] = None,
    max_results: int = 50,
) -> Dict[str, Any]:
    """
    List events on a calendar, recurring events expanded to single
    instances, ordered by start time. `time_min` and `time_max` are
    RFC 3339 date-times with an offset (e.g. 2026-07-15T00:00:00Z).
    `query` free-text matches summary, description, location and
    attendees.
    """
    def call(s):
        params: Dict[str, Any] = {
            "calendarId": calendar_id,
            "maxResults": max_results,
            "singleEvents": True,
            "orderBy": "startTime",
        }
        if time_min:
            params["timeMin"] = time_min
        if time_max:
            params["timeMax"] = time_max
        if query:
            params["q"] = query
        items = s.events().list(**params).execute().get("items", [])
        return [
            {
                "id": e.get("id"),
                "summary": e.get("summary"),
                "start": e.get("start"),
                "end": e.get("end"),
                "status": e.get("status"),
                "location": e.get("location"),
                "attendees": [
                    {"email": a.get("email"), "response": a.get("responseStatus")}
                    for a in e.get("attendees", [])
                ],
                "organizer": (e.get("organizer") or {}).get("email"),
                "hangout_link": e.get("hangoutLink"),
                "html_link": e.get("htmlLink"),
            }
            for e in items
        ]

    return _execute(user, call).model_dump(mode="json")


@mcp.tool()
async def get_event(
    user: CalendarUser,
    event_id: str,
    calendar_id: str = "primary",
) -> Dict[str, Any]:
    """Fetch one event's full record, including description and attendees."""
    return _execute(
        user,
        lambda s: s.events().get(calendarId=calendar_id, eventId=event_id).execute(),
    ).model_dump(mode="json")


@mcp.tool()
async def get_freebusy(
    user: CalendarUser,
    time_min: str,
    time_max: str,
    calendar_ids: Optional[List[str]] = None,
) -> Dict[str, Any]:
    """
    Busy intervals for one or more calendars in a window. Defaults to
    the user's primary calendar. Times are RFC 3339 with an offset.
    """
    ids = calendar_ids or ["primary"]

    def call(s):
        body = {
            "timeMin": time_min,
            "timeMax": time_max,
            "items": [{"id": cid} for cid in ids],
        }
        return s.freebusy().query(body=body).execute().get("calendars", {})

    return _execute(user, call).model_dump(mode="json")


# ---------------------------------------------------------------------------
# Tier 2 -- Writes (gated in chat per Navigation Rule 3)
# ---------------------------------------------------------------------------


@mcp.tool()
async def create_event(
    user: CalendarUser,
    summary: str,
    start: str,
    end: str,
    calendar_id: str = "primary",
    description: Optional[str] = None,
    location: Optional[str] = None,
    attendees: Optional[List[str]] = None,
    time_zone: Optional[str] = None,
    all_day: bool = False,
    send_updates: str = "none",
) -> Dict[str, Any]:
    """
    WRITE. Create an event. For timed events `start` and `end` are
    RFC 3339 date-times; for all-day events pass dates (YYYY-MM-DD)
    and all_day=true. `send_updates` controls invitation email --
    none, externalOnly or all; leave at none unless the user has
    explicitly approved notifying attendees.

    Alfred must confirm with the user before calling.
    """
    time_key = "date" if all_day else "dateTime"
    start_obj: Dict[str, Any] = {time_key: start}
    end_obj: Dict[str, Any] = {time_key: end}
    if time_zone and not all_day:
        start_obj["timeZone"] = time_zone
        end_obj["timeZone"] = time_zone

    body: Dict[str, Any] = {"summary": summary, "start": start_obj, "end": end_obj}
    if description:
        body["description"] = description
    if location:
        body["location"] = location
    if attendees:
        body["attendees"] = [{"email": a} for a in attendees]

    return _execute(
        user,
        lambda s: s.events()
        .insert(calendarId=calendar_id, body=body, sendUpdates=send_updates)
        .execute(),
    ).model_dump(mode="json")


@mcp.tool()
async def update_event(
    user: CalendarUser,
    event_id: str,
    calendar_id: str = "primary",
    summary: Optional[str] = None,
    description: Optional[str] = None,
    location: Optional[str] = None,
    start: Optional[str] = None,
    end: Optional[str] = None,
    time_zone: Optional[str] = None,
    attendees: Optional[List[str]] = None,
    all_day: bool = False,
    send_updates: str = "none",
) -> Dict[str, Any]:
    """
    WRITE. Patch an event -- only the provided fields change. Time
    fields follow the same rules as create_event. `send_updates`
    stays at none unless attendee notification is explicitly approved.

    Alfred must confirm with the user before calling.
    """
    body: Dict[str, Any] = {}
    if summary is not None:
        body["summary"] = summary
    if description is not None:
        body["description"] = description
    if location is not None:
        body["location"] = location
    time_key = "date" if all_day else "dateTime"
    if start is not None:
        start_obj: Dict[str, Any] = {time_key: start}
        if time_zone and not all_day:
            start_obj["timeZone"] = time_zone
        body["start"] = start_obj
    if end is not None:
        end_obj: Dict[str, Any] = {time_key: end}
        if time_zone and not all_day:
            end_obj["timeZone"] = time_zone
        body["end"] = end_obj
    if attendees is not None:
        body["attendees"] = [{"email": a} for a in attendees]
    if not body:
        return UserResponse(
            user=user.value, ok=False, error="No fields to update."
        ).model_dump(mode="json")

    return _execute(
        user,
        lambda s: s.events()
        .patch(
            calendarId=calendar_id,
            eventId=event_id,
            body=body,
            sendUpdates=send_updates,
        )
        .execute(),
    ).model_dump(mode="json")


@mcp.tool()
async def delete_event(
    user: CalendarUser,
    event_id: str,
    calendar_id: str = "primary",
    send_updates: str = "none",
) -> Dict[str, Any]:
    """
    WRITE. Delete an event. `send_updates` controls cancellation email
    to attendees -- none, externalOnly or all.

    Alfred must confirm with the user before calling.
    """
    def call(s):
        s.events().delete(
            calendarId=calendar_id, eventId=event_id, sendUpdates=send_updates
        ).execute()
        return {"deleted": event_id}

    return _execute(user, call).model_dump(mode="json")


# ---------------------------------------------------------------------------
# Entrypoint
# ---------------------------------------------------------------------------


if __name__ == "__main__":
    mcp.run(transport="stdio")
