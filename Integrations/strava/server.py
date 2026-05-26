#!/usr/bin/env python3
"""
Strava MCP server.

Thin FastMCP layer over the Strava v3 API with an optional bridge to the
personal Notion Fitness Journal. Read-only with respect to Strava; the
only writes happen against Notion when the sync tools are invoked.

Tools:
  - strava_auth_status: confirms tokens are valid and returns the athlete.
  - strava_list_activities: recent activities in a date range.
  - strava_get_activity: full detail with splits and HR zone distribution.
  - strava_sync_activity_to_notion: one activity -> one Cardiovascular
    Workout page in the Fitness Journal.
  - strava_sync_range_to_notion: batch sync across a date range.

Auth:
  - Strava tokens: ~/.config/alfred/strava-tokens.json (written by
    bootstrap.py). Refresh token flow handled internally.
  - Notion token: NOTION_PERSONAL_TOKEN env var. Must be an internal
    integration token with access to the Fitness Journal database.
"""

from __future__ import annotations

import json
import os
import time
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Optional

import httpx
from mcp.server.fastmcp import FastMCP
from pydantic import BaseModel, Field

# ---------------------------------------------------------------------------
# Configuration
# ---------------------------------------------------------------------------

STRAVA_API_BASE = "https://www.strava.com/api/v3"
STRAVA_TOKEN_URL = "https://www.strava.com/oauth/token"

TOKEN_PATH = Path.home() / ".config" / "alfred" / "strava-tokens.json"

NOTION_API_BASE = "https://api.notion.com/v1"
NOTION_VERSION = "2022-06-28"

FITNESS_JOURNAL_DATA_SOURCE_ID = "9084eeda-48b5-4793-80f2-03a97bfd4c63"
CARDIOVASCULAR_WORKOUT_TEMPLATE_NAME = "Cardiovascular Workout"

REQUEST_TIMEOUT_SECONDS = 30.0

# ---------------------------------------------------------------------------
# Strava client
# ---------------------------------------------------------------------------


class StravaTokenStore:
    """Loads, refreshes, and persists Strava OAuth tokens on disk."""

    def __init__(self, path: Path = TOKEN_PATH):
        self.path = path
        self._data: dict[str, Any] = {}
        self._load()

    def _load(self) -> None:
        if not self.path.exists():
            raise FileNotFoundError(
                f"Strava tokens not found at {self.path}. "
                "Run bootstrap.py first to authorize the personal Strava app."
            )
        self._data = json.loads(self.path.read_text())

    def _save(self) -> None:
        self.path.write_text(json.dumps(self._data, indent=2))
        self.path.chmod(0o600)

    @property
    def access_token(self) -> str:
        if time.time() >= self._data["expires_at"] - 60:
            self._refresh()
        return self._data["access_token"]

    @property
    def athlete_id(self) -> Optional[int]:
        return self._data.get("athlete_id")

    def _refresh(self) -> None:
        response = httpx.post(
            STRAVA_TOKEN_URL,
            data={
                "client_id": self._data["client_id"],
                "client_secret": self._data["client_secret"],
                "grant_type": "refresh_token",
                "refresh_token": self._data["refresh_token"],
            },
            timeout=REQUEST_TIMEOUT_SECONDS,
        )
        response.raise_for_status()
        payload = response.json()
        self._data["access_token"] = payload["access_token"]
        self._data["refresh_token"] = payload["refresh_token"]
        self._data["expires_at"] = payload["expires_at"]
        self._save()


class StravaClient:
    def __init__(self, tokens: StravaTokenStore):
        self.tokens = tokens

    def _headers(self) -> dict[str, str]:
        return {"Authorization": f"Bearer {self.tokens.access_token}"}

    def get(self, path: str, params: Optional[dict] = None) -> Any:
        response = httpx.get(
            f"{STRAVA_API_BASE}{path}",
            params=params or {},
            headers=self._headers(),
            timeout=REQUEST_TIMEOUT_SECONDS,
        )
        if response.status_code == 429:
            raise RuntimeError(
                "Strava rate limit exceeded (100 per 15 min, 1000 per day). "
                "Wait and retry."
            )
        response.raise_for_status()
        return response.json()


# ---------------------------------------------------------------------------
# Unit conversion helpers
# ---------------------------------------------------------------------------


def meters_to_miles(m: float | None) -> float | None:
    return round(m / 1609.344, 2) if m is not None else None


def meters_to_feet(m: float | None) -> float | None:
    return round(m * 3.28084, 1) if m is not None else None


def seconds_to_hms(sec: int | None) -> str:
    if sec is None:
        return ""
    h, rem = divmod(int(sec), 3600)
    m, s = divmod(rem, 60)
    return f"{h}:{m:02d}:{s:02d}" if h else f"{m}:{s:02d}"


def mps_to_mile_pace(mps: float | None) -> str:
    """Convert m/s average speed to pace string MM:SS /mi."""
    if not mps or mps <= 0:
        return ""
    seconds_per_mile = 1609.344 / mps
    m, s = divmod(int(round(seconds_per_mile)), 60)
    return f"{m}:{s:02d} /mi"


def format_heart_rate(hr: float | None) -> str:
    return f"{int(round(hr))} bpm" if hr else ""


def infer_environment(activity: dict) -> str:
    """Best-effort derivation of outdoor vs indoor."""
    if activity.get("trainer"):
        return "Indoor"
    if activity.get("type") == "VirtualRun" or activity.get("type") == "VirtualRide":
        return "Virtual"
    if activity.get("manual"):
        return "Manual entry"
    return "Outdoor"


# ---------------------------------------------------------------------------
# Notion client (personal integration)
# ---------------------------------------------------------------------------


class NotionClient:
    def __init__(self, token: Optional[str]):
        self.token = token

    def require_token(self) -> str:
        if not self.token:
            raise RuntimeError(
                "NOTION_PERSONAL_TOKEN is not set. The Strava MCP cannot "
                "write to the Fitness Journal without a personal Notion "
                "integration token. See README.md section 'Notion setup'."
            )
        return self.token

    def _headers(self) -> dict[str, str]:
        return {
            "Authorization": f"Bearer {self.require_token()}",
            "Notion-Version": NOTION_VERSION,
            "Content-Type": "application/json",
        }

    def create_cardiovascular_workout(
        self,
        name: str,
        date_iso: str,
        difficulty: str,
        page_children: list[dict],
    ) -> dict:
        body = {
            "parent": {"database_id": FITNESS_JOURNAL_DATA_SOURCE_ID},
            "icon": {"type": "external", "external": {"url": "https://www.notion.so/icons/lungs_pink.svg"}},
            "properties": {
                "Name": {"title": [{"type": "text", "text": {"content": name}}]},
                "Date": {"date": {"start": date_iso}},
                "Difficulty": {"select": {"name": difficulty}},
            },
            "children": page_children,
        }
        response = httpx.post(
            f"{NOTION_API_BASE}/pages",
            headers=self._headers(),
            json=body,
            timeout=REQUEST_TIMEOUT_SECONDS,
        )
        if response.status_code >= 400:
            raise RuntimeError(
                f"Notion create page failed ({response.status_code}): {response.text}"
            )
        return response.json()


# ---------------------------------------------------------------------------
# Notion block builders
# ---------------------------------------------------------------------------


def _rt(text: str) -> list[dict]:
    return [{"type": "text", "text": {"content": text}}]


def _heading_3(text: str) -> dict:
    return {
        "object": "block",
        "type": "heading_3",
        "heading_3": {"rich_text": _rt(text)},
    }


def _divider() -> dict:
    return {"object": "block", "type": "divider", "divider": {}}


def _table_row(cells: list[str]) -> dict:
    return {
        "object": "block",
        "type": "table_row",
        "table_row": {"cells": [_rt(c) for c in cells]},
    }


def _table(rows: list[list[str]], column_count: int, has_header: bool = True) -> dict:
    return {
        "object": "block",
        "type": "table",
        "table": {
            "table_width": column_count,
            "has_column_header": has_header,
            "has_row_header": False,
            "children": [_table_row(r) for r in rows],
        },
    }


def build_session_overview(activity: dict) -> list[dict]:
    distance_mi = meters_to_miles(activity.get("distance"))
    elevation_ft = meters_to_feet(activity.get("total_elevation_gain"))
    moving_time = seconds_to_hms(activity.get("moving_time"))
    avg_pace = mps_to_mile_pace(activity.get("average_speed"))
    avg_hr = format_heart_rate(activity.get("average_heartrate"))
    max_hr = format_heart_rate(activity.get("max_heartrate"))
    calories = activity.get("calories")
    cadence = activity.get("average_cadence")

    rows = [
        ["Field", "Value"],
        ["Discipline", activity.get("sport_type", activity.get("type", ""))],
        ["Environment", infer_environment(activity)],
        ["Total Distance", f"{distance_mi} mi" if distance_mi else ""],
        ["Total Time", moving_time],
        ["Average Pace", avg_pace],
        ["Average Heart Rate", avg_hr],
        ["Max Heart Rate", max_hr],
        ["Calories", str(int(calories)) if calories else ""],
        ["Elevation Gain", f"{elevation_ft} ft" if elevation_ft else ""],
        ["Cadence", str(round(cadence, 1)) if cadence else ""],
        ["RPE", ""],
    ]
    return [
        _heading_3("Session Overview"),
        _divider(),
        _table(rows, column_count=2, has_header=True),
    ]


def build_splits_section(activity: dict) -> list[dict]:
    splits = activity.get("splits_standard") or []
    rows: list[list[str]] = [["Split", "Distance", "Time", "Pace", "Heart Rate", "Notes"]]
    for s in splits:
        distance_mi = meters_to_miles(s.get("distance"))
        pace = mps_to_mile_pace(s.get("average_speed"))
        hr = format_heart_rate(s.get("average_heartrate"))
        rows.append(
            [
                str(s.get("split", "")),
                f"{distance_mi} mi" if distance_mi else "",
                seconds_to_hms(s.get("moving_time")),
                pace,
                hr,
                "",
            ]
        )
    if len(rows) == 1:
        rows.append(["1", "", "", "", "", ""])
    return [
        _heading_3("Splits"),
        _divider(),
        _table(rows, column_count=6, has_header=True),
    ]


def build_hr_zones_section(zones_payload: Any) -> list[dict]:
    """zones_payload is a list from /activities/{id}/zones."""
    descriptions = ["Recovery", "Endurance", "Tempo", "Threshold", "VO2 Max"]
    times: list[int] = [0, 0, 0, 0, 0]

    if isinstance(zones_payload, list):
        for entry in zones_payload:
            if entry.get("type") == "heartrate":
                buckets = entry.get("distribution_buckets") or []
                for idx, bucket in enumerate(buckets[:5]):
                    times[idx] = bucket.get("time", 0)
                break

    rows: list[list[str]] = [["Zone", "Description", "Time"]]
    for idx, desc in enumerate(descriptions):
        rows.append([f"Zone {idx + 1}", desc, seconds_to_hms(times[idx])])
    return [
        _heading_3("Heart Rate Zones"),
        _divider(),
        _table(rows, column_count=3, has_header=True),
    ]


def build_session_notes_section(activity: dict) -> list[dict]:
    description = activity.get("description") or ""
    conditions = ""
    gear = activity.get("gear", {})
    if gear and isinstance(gear, dict):
        gear_name = gear.get("name")
        if gear_name:
            conditions = f"Gear: {gear_name}"
    rows = [
        ["Field", "Value"],
        ["Conditions", conditions],
        ["Body Feel", description[:200] if description else ""],
        ["Forward Look", ""],
    ]
    return [
        _heading_3("Session Notes"),
        _divider(),
        _table(rows, column_count=2, has_header=True),
    ]


def build_page_children(activity: dict, zones_payload: Any) -> list[dict]:
    return [
        *build_session_overview(activity),
        *build_splits_section(activity),
        *build_hr_zones_section(zones_payload),
        *build_session_notes_section(activity),
    ]


def infer_difficulty(activity: dict) -> str:
    """Map Strava perceived exertion / suffer score to the Difficulty select."""
    suffer = activity.get("suffer_score") or 0
    if suffer >= 100:
        return "High Intensity"
    if suffer >= 40:
        return "Medium Intensity"
    return "Low Intensity"


def derive_activity_date(activity: dict) -> str:
    start = activity.get("start_date_local") or activity.get("start_date")
    if not start:
        return datetime.now(timezone.utc).date().isoformat()
    return start.split("T", 1)[0]


def derive_activity_name(activity: dict) -> str:
    custom = activity.get("name")
    if custom and not custom.startswith(("Morning", "Afternoon", "Evening", "Lunch", "Night")):
        return custom
    sport = activity.get("sport_type", activity.get("type", "Workout"))
    sport_label = {
        "Run": "Endurance Run",
        "VirtualRun": "Endurance Run",
        "TrailRun": "Trail Run",
        "Ride": "Ride",
        "VirtualRide": "Indoor Ride",
        "Swim": "Swim",
        "Walk": "Walk",
        "Hike": "Hike",
    }.get(sport, f"{sport} Session")
    return sport_label


# ---------------------------------------------------------------------------
# Pydantic response models
# ---------------------------------------------------------------------------


class ActivitySummary(BaseModel):
    id: int
    name: str
    sport_type: str
    start_date_local: str
    distance_mi: Optional[float] = None
    moving_time: str
    average_pace: str
    average_heart_rate: Optional[int] = None
    max_heart_rate: Optional[int] = None
    elevation_gain_ft: Optional[float] = None
    calories: Optional[int] = None
    suffer_score: Optional[int] = None


def summarize_activity(a: dict) -> ActivitySummary:
    return ActivitySummary(
        id=a["id"],
        name=a.get("name", ""),
        sport_type=a.get("sport_type", a.get("type", "")),
        start_date_local=a.get("start_date_local", a.get("start_date", "")),
        distance_mi=meters_to_miles(a.get("distance")),
        moving_time=seconds_to_hms(a.get("moving_time")),
        average_pace=mps_to_mile_pace(a.get("average_speed")),
        average_heart_rate=int(a["average_heartrate"]) if a.get("average_heartrate") else None,
        max_heart_rate=int(a["max_heartrate"]) if a.get("max_heartrate") else None,
        elevation_gain_ft=meters_to_feet(a.get("total_elevation_gain")),
        calories=int(a["calories"]) if a.get("calories") else None,
        suffer_score=int(a["suffer_score"]) if a.get("suffer_score") else None,
    )


# ---------------------------------------------------------------------------
# FastMCP server
# ---------------------------------------------------------------------------


mcp = FastMCP("strava")


def _client() -> StravaClient:
    return StravaClient(StravaTokenStore())


def _notion() -> NotionClient:
    return NotionClient(os.environ.get("NOTION_PERSONAL_TOKEN"))


def _parse_date(value: Optional[str]) -> Optional[int]:
    if not value:
        return None
    dt = datetime.fromisoformat(value)
    if dt.tzinfo is None:
        dt = dt.replace(tzinfo=timezone.utc)
    return int(dt.timestamp())


@mcp.tool()
def strava_auth_status() -> dict:
    """
    Confirm that Strava tokens are present and valid.

    Returns the authorized athlete profile and the current scope.
    """
    client = _client()
    athlete = client.get("/athlete")
    return {
        "authorized": True,
        "athlete_id": athlete.get("id"),
        "firstname": athlete.get("firstname"),
        "lastname": athlete.get("lastname"),
        "username": athlete.get("username"),
        "city": athlete.get("city"),
        "state": athlete.get("state"),
        "country": athlete.get("country"),
        "premium": athlete.get("premium"),
    }


@mcp.tool()
def strava_list_activities(
    after: Optional[str] = Field(
        default=None,
        description="ISO date or datetime. Only activities on or after this moment are returned.",
    ),
    before: Optional[str] = Field(
        default=None,
        description="ISO date or datetime. Only activities on or before this moment are returned.",
    ),
    limit: int = Field(
        default=30,
        description="Maximum activities to return (Strava caps page size at 200).",
        ge=1,
        le=200,
    ),
) -> list[dict]:
    """
    List recent Strava activities with imperial-unit summaries.

    All distance and pace values are converted from Strava's metric
    defaults to miles and minutes per mile.
    """
    client = _client()
    params: dict[str, Any] = {"per_page": limit}
    after_ts = _parse_date(after)
    before_ts = _parse_date(before)
    if after_ts:
        params["after"] = after_ts
    if before_ts:
        params["before"] = before_ts

    raw = client.get("/athlete/activities", params=params)
    return [summarize_activity(a).model_dump() for a in raw]


@mcp.tool()
def strava_get_activity(
    activity_id: int = Field(description="Strava activity ID."),
    include_zones: bool = Field(
        default=True,
        description="Also fetch HR zone distribution for the activity.",
    ),
) -> dict:
    """
    Fetch full activity detail including per-mile splits and HR zones.
    """
    client = _client()
    activity = client.get(f"/activities/{activity_id}")

    zones = None
    if include_zones:
        try:
            zones = client.get(f"/activities/{activity_id}/zones")
        except httpx.HTTPStatusError:
            zones = None

    return {
        "summary": summarize_activity(activity).model_dump(),
        "splits": activity.get("splits_standard", []),
        "zones": zones,
        "description": activity.get("description"),
        "gear": activity.get("gear"),
        "start_date_local": activity.get("start_date_local"),
        "timezone": activity.get("timezone"),
        "trainer": activity.get("trainer"),
        "commute": activity.get("commute"),
    }


@mcp.tool()
def strava_sync_activity_to_notion(
    activity_id: int = Field(description="Strava activity ID to sync."),
) -> dict:
    """
    Create a Cardiovascular Workout page in the Fitness Journal for a
    single Strava activity. Fills Session Overview, Splits, Heart Rate
    Zones and Session Notes using Strava data.
    """
    client = _client()
    notion = _notion()

    activity = client.get(f"/activities/{activity_id}")
    try:
        zones = client.get(f"/activities/{activity_id}/zones")
    except httpx.HTTPStatusError:
        zones = None

    page_children = build_page_children(activity, zones)
    created = notion.create_cardiovascular_workout(
        name=derive_activity_name(activity),
        date_iso=derive_activity_date(activity),
        difficulty=infer_difficulty(activity),
        page_children=page_children,
    )
    return {
        "notion_page_id": created.get("id"),
        "notion_page_url": created.get("url"),
        "activity_id": activity_id,
        "activity_name": activity.get("name"),
        "date": derive_activity_date(activity),
    }


@mcp.tool()
def strava_sync_range_to_notion(
    after: str = Field(
        description="ISO date (inclusive). Activities on or after this date are synced.",
    ),
    before: Optional[str] = Field(
        default=None,
        description="ISO date (inclusive). Activities on or before this date are synced.",
    ),
    sport_types: Optional[list[str]] = Field(
        default=None,
        description=(
            "Optional filter by Strava sport_type (e.g. 'Run', 'Ride', 'Swim'). "
            "When omitted all types are synced."
        ),
    ),
    limit: int = Field(
        default=50,
        description="Maximum activities to sync in one batch.",
        ge=1,
        le=200,
    ),
) -> dict:
    """
    Batch sync every activity in a date range into the Fitness Journal.
    Returns a list of created Notion page URLs and any skipped activities.
    """
    client = _client()
    notion = _notion()

    params: dict[str, Any] = {"per_page": limit}
    after_ts = _parse_date(after)
    before_ts = _parse_date(before)
    if after_ts:
        params["after"] = after_ts
    if before_ts:
        params["before"] = before_ts

    activities = client.get("/athlete/activities", params=params)
    created: list[dict] = []
    skipped: list[dict] = []

    for a in activities:
        if sport_types and a.get("sport_type") not in sport_types:
            skipped.append({"id": a["id"], "reason": "sport_type filter"})
            continue
        try:
            detail = client.get(f"/activities/{a['id']}")
            try:
                zones = client.get(f"/activities/{a['id']}/zones")
            except httpx.HTTPStatusError:
                zones = None
            children = build_page_children(detail, zones)
            page = notion.create_cardiovascular_workout(
                name=derive_activity_name(detail),
                date_iso=derive_activity_date(detail),
                difficulty=infer_difficulty(detail),
                page_children=children,
            )
            created.append(
                {
                    "activity_id": a["id"],
                    "name": detail.get("name"),
                    "date": derive_activity_date(detail),
                    "notion_page_url": page.get("url"),
                }
            )
        except Exception as exc:  # pragma: no cover - surface failure per activity
            skipped.append({"id": a["id"], "reason": str(exc)})

    return {
        "synced_count": len(created),
        "skipped_count": len(skipped),
        "created": created,
        "skipped": skipped,
    }


if __name__ == "__main__":
    mcp.run()
