#!/usr/bin/env python3
"""
Cal.com MCP Server -- Booking layer for the scheduling lane.

Thin FastMCP layer over the Cal.com API v2. Exposes read access to
bookings, event types and availability, plus a gated set of write
operations for creating, rescheduling and cancelling bookings.

Each pipeline owns its own Cal.com account and its own API key.
Today only the `five_points` pipeline is provisioned; the pipeline
registry is ready to accept additional pipelines (personal, other
ventures) without an API break.

Write tools carry `WRITE.` in their description so the calling agent
follows Navigation Rule 3 and asks for confirmation before dispatch.
The server itself does not enforce the gate.

Cal.com versions its v2 endpoints per resource through the
`cal-api-version` header. The constants below are pinned to the
documented values as of 2026-07-10; when Cal.com ships a new version,
update the constant, not the call sites.
"""

import os
from datetime import datetime, timezone
from enum import Enum
from typing import Optional, List, Dict, Any

import httpx
from pydantic import BaseModel, Field
from mcp.server.fastmcp import FastMCP

# ---------------------------------------------------------------------------
# Configuration
# ---------------------------------------------------------------------------

CALCOM_API_BASE = os.getenv("CALCOM_API_BASE", "https://api.cal.com/v2")

REQUEST_TIMEOUT_SECONDS = 30.0
HEALTH_TIMEOUT_SECONDS = 10.0

# Per-resource API versions (cal-api-version header).
API_VERSION_BOOKINGS_LIST = "2026-05-01"
API_VERSION_BOOKINGS = "2026-02-25"
API_VERSION_EVENT_TYPES = "2024-06-14"
API_VERSION_SLOTS = "2024-09-04"


# ---------------------------------------------------------------------------
# Pipelines
# ---------------------------------------------------------------------------


class Pipeline(str, Enum):
    """
    Routing key for a Cal.com request. Each pipeline is isolated --
    its own Cal.com account, its own API key. Personal and venture
    pipelines never share credentials.
    """

    FIVE_POINTS = "five_points"
    # Future: PERSONAL = "personal", MARTY_GRAS = "marty_gras"


PIPELINE_REGISTRY: Dict[Pipeline, Dict[str, str]] = {
    Pipeline.FIVE_POINTS: {
        "label": "Five Points Digital Studio",
        "description": "Premium digital marketing agency -- client booking layer",
        "env_var": "CALCOM_FIVEPOINTS_API_KEY",
        "username": "martavious-spicer",
    },
}


def _get_pipeline_key(pipeline: Pipeline) -> Optional[str]:
    env_var = PIPELINE_REGISTRY[pipeline]["env_var"]
    value = os.getenv(env_var)
    return value or None


def _default_username(pipeline: Pipeline) -> str:
    return PIPELINE_REGISTRY[pipeline]["username"]


# ---------------------------------------------------------------------------
# Models
# ---------------------------------------------------------------------------


class PipelineResponse(BaseModel):
    """Wrapper for responses that may fail before reaching Cal.com."""

    pipeline: str
    ok: bool
    data: Optional[Any] = None
    error: Optional[str] = None
    status_code: Optional[int] = None
    fetched_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))


def _invalid(pipeline: Pipeline, message: str) -> PipelineResponse:
    """Tool-level validation failure. No network call is made."""
    return PipelineResponse(pipeline=pipeline.value, ok=False, error=message)


# ---------------------------------------------------------------------------
# Cal.com HTTP adapter -- the single swap point for API shape.
# ---------------------------------------------------------------------------


async def _request(
    pipeline: Pipeline,
    method: str,
    path: str,
    *,
    api_version: Optional[str] = None,
    params: Optional[Dict[str, Any]] = None,
    json_body: Optional[Dict[str, Any]] = None,
    timeout: float = REQUEST_TIMEOUT_SECONDS,
) -> PipelineResponse:
    """
    Execute a single Cal.com v2 API call scoped to a pipeline.

    Returns a PipelineResponse envelope. Never raises -- every error
    (missing key, network, non-2xx) is surfaced through `ok` and `error`.
    """
    api_key = _get_pipeline_key(pipeline)
    if not api_key:
        env_var = PIPELINE_REGISTRY[pipeline]["env_var"]
        return PipelineResponse(
            pipeline=pipeline.value,
            ok=False,
            error=f"Pipeline '{pipeline.value}' not provisioned. Set {env_var}.",
        )

    url = f"{CALCOM_API_BASE}{path}"
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Accept": "application/json",
    }
    if api_version:
        headers["cal-api-version"] = api_version
    if json_body is not None:
        headers["Content-Type"] = "application/json"

    try:
        async with httpx.AsyncClient(timeout=timeout) as client:
            resp = await client.request(
                method,
                url,
                headers=headers,
                params=params,
                json=json_body,
            )
    except httpx.HTTPError as exc:
        return PipelineResponse(
            pipeline=pipeline.value,
            ok=False,
            error=f"HTTP request failed: {exc}",
        )

    body: Any
    if resp.headers.get("content-type", "").startswith("application/json"):
        try:
            body = resp.json()
        except ValueError:
            body = resp.text
    else:
        body = resp.text

    if resp.status_code >= 400:
        return PipelineResponse(
            pipeline=pipeline.value,
            ok=False,
            status_code=resp.status_code,
            error=f"Cal.com {resp.status_code}: {str(body)[:500]}",
            data=body if isinstance(body, dict) else None,
        )

    return PipelineResponse(
        pipeline=pipeline.value,
        ok=True,
        status_code=resp.status_code,
        data=body,
    )


# ---------------------------------------------------------------------------
# FastMCP server
# ---------------------------------------------------------------------------

mcp = FastMCP("calcom")


# ---------------------------------------------------------------------------
# Helper tools
# ---------------------------------------------------------------------------


@mcp.tool()
async def list_pipelines() -> List[Dict[str, str]]:
    """Return the pipeline registry -- label, description, env var, username."""
    return [
        {"pipeline": pipeline.value, **info}
        for pipeline, info in PIPELINE_REGISTRY.items()
    ]


@mcp.tool()
async def pipeline_status() -> Dict[str, Dict[str, Any]]:
    """
    Per-pipeline: is the API key set? Does not make a network call.
    Use health_check to test reachability.
    """
    status: Dict[str, Dict[str, Any]] = {}
    for pipeline in Pipeline:
        info = PIPELINE_REGISTRY[pipeline]
        key = _get_pipeline_key(pipeline)
        status[pipeline.value] = {
            "provisioned": key is not None,
            "env_var": info["env_var"],
            "label": info["label"],
            "username": info["username"],
        }
    return status


@mcp.tool()
async def health_check(pipeline: Pipeline = Pipeline.FIVE_POINTS) -> Dict[str, Any]:
    """
    Verify Cal.com reachability by fetching the authenticated profile
    (GET /me). Returns the account id, username, email and time zone
    on success.
    """
    result = await _request(
        pipeline, "GET", "/me", timeout=HEALTH_TIMEOUT_SECONDS
    )
    return result.model_dump(mode="json")


# ---------------------------------------------------------------------------
# Tier 1 -- Read-only
# ---------------------------------------------------------------------------


@mcp.tool()
async def list_event_types(
    pipeline: Pipeline = Pipeline.FIVE_POINTS,
    username: Optional[str] = None,
    event_slug: Optional[str] = None,
) -> Dict[str, Any]:
    """
    List event types for a Cal.com user. Defaults to the pipeline's
    own username. Pass event_slug to fetch a single event type by its
    slug (e.g. 'the-working-call').
    """
    params: Dict[str, Any] = {"username": username or _default_username(pipeline)}
    if event_slug:
        params["eventSlug"] = event_slug
    result = await _request(
        pipeline,
        "GET",
        "/event-types",
        api_version=API_VERSION_EVENT_TYPES,
        params=params,
    )
    return result.model_dump(mode="json")


@mcp.tool()
async def list_bookings(
    pipeline: Pipeline = Pipeline.FIVE_POINTS,
    status: Optional[str] = None,
    attendee_email: Optional[str] = None,
    attendee_name: Optional[str] = None,
    event_type_id: Optional[int] = None,
    after_start: Optional[str] = None,
    before_end: Optional[str] = None,
    sort_start: Optional[str] = None,
    limit: int = 50,
    cursor: Optional[str] = None,
) -> Dict[str, Any]:
    """
    List bookings on the pipeline's Cal.com account. `status` accepts
    upcoming, recurring, past, cancelled or unconfirmed. Date filters
    (`after_start`, `before_end`) take ISO 8601 date-times. Cursor
    pagination via the response's `pagination.nextCursor`.
    """
    if status and status not in {"upcoming", "recurring", "past", "cancelled", "unconfirmed"}:
        return _invalid(
            pipeline,
            "status must be one of: upcoming, recurring, past, cancelled, unconfirmed",
        ).model_dump(mode="json")
    params: Dict[str, Any] = {"limit": limit}
    if status:
        params["status"] = status
    if attendee_email:
        params["attendeeEmail"] = attendee_email
    if attendee_name:
        params["attendeeName"] = attendee_name
    if event_type_id is not None:
        params["eventTypeId"] = event_type_id
    if after_start:
        params["afterStart"] = after_start
    if before_end:
        params["beforeEnd"] = before_end
    if sort_start:
        params["sortStart"] = sort_start
    if cursor:
        params["cursor"] = cursor
    result = await _request(
        pipeline,
        "GET",
        "/bookings",
        api_version=API_VERSION_BOOKINGS_LIST,
        params=params,
    )
    return result.model_dump(mode="json")


@mcp.tool()
async def get_booking(
    booking_uid: str,
    pipeline: Pipeline = Pipeline.FIVE_POINTS,
) -> Dict[str, Any]:
    """
    Fetch a single booking by its uid, including hosts, attendees,
    status, times and booking-field responses. A recurring booking
    uid returns all recurrences.
    """
    result = await _request(
        pipeline,
        "GET",
        f"/bookings/{booking_uid}",
        api_version=API_VERSION_BOOKINGS,
    )
    return result.model_dump(mode="json")


@mcp.tool()
async def get_availability(
    start: str,
    end: str,
    pipeline: Pipeline = Pipeline.FIVE_POINTS,
    event_type_id: Optional[int] = None,
    event_type_slug: Optional[str] = None,
    username: Optional[str] = None,
    time_zone: Optional[str] = None,
    duration: Optional[int] = None,
    slot_format: Optional[str] = None,
) -> Dict[str, Any]:
    """
    Available slots for an event type within a UTC ISO 8601 time range.
    Reference the event type by id, or by slug (the pipeline's own
    username is filled in automatically when only a slug is given).
    `slot_format` accepts 'range' or 'time'.
    """
    if event_type_id is None and not event_type_slug:
        return _invalid(
            pipeline, "Provide event_type_id or event_type_slug."
        ).model_dump(mode="json")
    params: Dict[str, Any] = {"start": start, "end": end}
    if event_type_id is not None:
        params["eventTypeId"] = event_type_id
    else:
        params["eventTypeSlug"] = event_type_slug
        params["username"] = username or _default_username(pipeline)
    if time_zone:
        params["timeZone"] = time_zone
    if duration is not None:
        params["duration"] = duration
    if slot_format:
        params["format"] = slot_format
    result = await _request(
        pipeline,
        "GET",
        "/slots",
        api_version=API_VERSION_SLOTS,
        params=params,
    )
    return result.model_dump(mode="json")


# ---------------------------------------------------------------------------
# Tier 2 -- Writes (gated in chat per Navigation Rule 3)
# ---------------------------------------------------------------------------


@mcp.tool()
async def create_booking(
    start: str,
    attendee_name: str,
    attendee_time_zone: str,
    pipeline: Pipeline = Pipeline.FIVE_POINTS,
    event_type_id: Optional[int] = None,
    event_type_slug: Optional[str] = None,
    username: Optional[str] = None,
    attendee_email: Optional[str] = None,
    attendee_phone: Optional[str] = None,
    attendee_language: Optional[str] = None,
    guests: Optional[List[str]] = None,
    location: Optional[Dict[str, Any]] = None,
    metadata: Optional[Dict[str, Any]] = None,
    length_in_minutes: Optional[int] = None,
) -> Dict[str, Any]:
    """
    WRITE. Create a booking on the pipeline's Cal.com account.

    `start` must be UTC ISO 8601 (e.g. 2026-07-15T14:00:00Z) -- Cal.com
    interprets it as UTC regardless of the attendee time zone. Reference
    the event type by id, or by slug (the pipeline's own username is
    filled in automatically). At least one of attendee_email or
    attendee_phone is required so the attendee receives confirmations.

    Alfred must confirm with the user before calling. The booking
    triggers Cal.com confirmation emails to host and attendee.
    """
    if event_type_id is None and not event_type_slug:
        return _invalid(
            pipeline, "Provide event_type_id or event_type_slug."
        ).model_dump(mode="json")
    if not attendee_email and not attendee_phone:
        return _invalid(
            pipeline, "Provide attendee_email or attendee_phone."
        ).model_dump(mode="json")

    attendee: Dict[str, Any] = {
        "name": attendee_name,
        "timeZone": attendee_time_zone,
    }
    if attendee_email:
        attendee["email"] = attendee_email
    if attendee_phone:
        attendee["phoneNumber"] = attendee_phone
    if attendee_language:
        attendee["language"] = attendee_language

    body: Dict[str, Any] = {"start": start, "attendee": attendee}
    if event_type_id is not None:
        body["eventTypeId"] = event_type_id
    else:
        body["eventTypeSlug"] = event_type_slug
        body["username"] = username or _default_username(pipeline)
    if guests:
        body["guests"] = guests
    if location:
        body["location"] = location
    if metadata:
        body["metadata"] = metadata
    if length_in_minutes is not None:
        body["lengthInMinutes"] = length_in_minutes

    result = await _request(
        pipeline,
        "POST",
        "/bookings",
        api_version=API_VERSION_BOOKINGS,
        json_body=body,
    )
    return result.model_dump(mode="json")


@mcp.tool()
async def reschedule_booking(
    booking_uid: str,
    start: str,
    pipeline: Pipeline = Pipeline.FIVE_POINTS,
    rescheduling_reason: Optional[str] = None,
    rescheduled_by: Optional[str] = None,
) -> Dict[str, Any]:
    """
    WRITE. Reschedule a booking to a new UTC ISO 8601 start time.
    If `rescheduled_by` is the event-type owner's email the new time
    is auto-confirmed; otherwise the host must confirm.

    Alfred must confirm with the user before calling. The reschedule
    triggers Cal.com notification emails to host and attendee.
    """
    body: Dict[str, Any] = {"start": start}
    if rescheduling_reason:
        body["reschedulingReason"] = rescheduling_reason
    if rescheduled_by:
        body["rescheduledBy"] = rescheduled_by
    result = await _request(
        pipeline,
        "POST",
        f"/bookings/{booking_uid}/reschedule",
        api_version=API_VERSION_BOOKINGS,
        json_body=body,
    )
    return result.model_dump(mode="json")


@mcp.tool()
async def cancel_booking(
    booking_uid: str,
    pipeline: Pipeline = Pipeline.FIVE_POINTS,
    cancellation_reason: Optional[str] = None,
    cancel_subsequent_bookings: bool = False,
) -> Dict[str, Any]:
    """
    WRITE. Cancel a booking. For a recurring booking uid, set
    cancel_subsequent_bookings to also cancel every recurrence after
    the given one.

    Alfred must confirm with the user before calling. The cancellation
    triggers Cal.com notification emails to host and attendee.
    """
    body: Dict[str, Any] = {}
    if cancellation_reason:
        body["cancellationReason"] = cancellation_reason
    if cancel_subsequent_bookings:
        body["cancelSubsequentBookings"] = True
    result = await _request(
        pipeline,
        "POST",
        f"/bookings/{booking_uid}/cancel",
        api_version=API_VERSION_BOOKINGS,
        json_body=body,
    )
    return result.model_dump(mode="json")


# ---------------------------------------------------------------------------
# Entrypoint
# ---------------------------------------------------------------------------


if __name__ == "__main__":
    mcp.run(transport="stdio")
