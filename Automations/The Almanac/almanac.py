#!/usr/bin/env python3
"""
The Almanac -- render the personal Notion schedule onto Calendar.app.

Notion is the authority; the calendar is a one-way projection on the
state-cache pattern. Nothing is ever read back from the calendar into
Notion, and any edit made in Calendar.app is lost at the next render.

Design of record: .working/day-schedule/design-notes.md, and the mission
record at https://app.notion.com/p/The-Almanac-3ba1896165cf81ab80cac051406cc7b8

Two rules are load-bearing and must not be relaxed:

1. The signature rule. Every event this renderer writes carries
   SIGNATURE in its description. A render clears only events bearing
   that signature inside the target window, on the target calendar.
   The signature is checked, never inferred from title or position, so
   an operator-placed event is safe by construction and a partially
   failed render is recoverable by re-running.

2. No calendar fallback. If the named calendar does not exist the run
   aborts. The bridge's own resolver falls back to the first writable
   calendar when a name does not match, which would silently scatter a
   render across the wrong surface.

AppleScript plumbing is imported from the apple-calendar MCP server so
the escaping, date construction and bulk-read patterns live in exactly
one place.
"""

from __future__ import annotations

import argparse
import json
import os
import sys
import urllib.error
import urllib.request
from dataclasses import dataclass, field
from datetime import date, datetime, timedelta
from importlib import util as importlib_util
from pathlib import Path
from typing import Any, Dict, List, Optional, Tuple

# ---------------------------------------------------------------------------
# Bridge import
# ---------------------------------------------------------------------------

REPO_ROOT = Path(__file__).resolve().parents[2]
BRIDGE = REPO_ROOT / "Integrations" / "apple-calendar" / "server.py"


def _load_bridge():
    if not BRIDGE.exists():
        sys.exit(f"apple-calendar bridge not found at {BRIDGE}")
    spec = importlib_util.spec_from_file_location("_almanac_bridge", BRIDGE)
    module = importlib_util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


bridge = _load_bridge()

# ---------------------------------------------------------------------------
# Configuration
# ---------------------------------------------------------------------------

SIGNATURE = "⟡ almanac:v1"
SIGNATURE_NOTE = "Notion is the authority. Edits made here are lost at the next render."

DEFAULT_CALENDAR = "Almanac"

NOTION_VERSION = "2022-06-28"
TASKS_DATABASE_ID = "abbbb904-f0e2-4e4e-83c5-46fc3b950635"
NOTION_API = "https://api.notion.com/v1"

# Terminal statuses. A task in one of these never renders.
CLOSED_STATUSES = ("Done", "Archived")

TASK_MINUTES = 30
BLOCK_MINUTES = 240


@dataclass(frozen=True)
class Block:
    numeral: str
    name: str
    start_hour: int
    renders: bool
    character: str

    @property
    def title(self) -> str:
        return f"{self.numeral} · {self.name}"


# Six equal four-hour blocks tiling the full 24 hours from the 05:00
# wake. The two rest blocks are part of the model but are never drawn:
# rest is the absence of a block on the surface.
BLOCKS: Tuple[Block, ...] = (
    Block("I", "Morning Routine", 5, True,
          "Wake, prayer and manifestation, journal, plants and pets, training, supplements."),
    Block("II", "Administration", 9, True,
          "Language learning, email, administrative duties, team meetings, sales outreach, focus work."),
    Block("III", "Collaboration", 13, True,
          "External meetings, content, team building and recruitment, focus work. Next-day scheduling at the close."),
    Block("IV", "Social", 17, True,
          "Dinner, daily cleaning, instrument practice, social commitments."),
    Block("V", "Evening Routine", 21, False,
          "First rest block. Nightlife and going out eat into this one by design."),
    Block("VI", "Night Owl", 1, False,
          "Second rest block. Home before it begins."),
)

BY_NUMERAL = {b.numeral: b for b in BLOCKS}


def block_for_hour(hour: int) -> Block:
    """
    Derive the block from the hour. The block is never stored -- there is
    no second copy of the truth to drift, and moving a task between
    blocks means changing one value rather than two.
    """
    if 5 <= hour < 9:
        return BY_NUMERAL["I"]
    if 9 <= hour < 13:
        return BY_NUMERAL["II"]
    if 13 <= hour < 17:
        return BY_NUMERAL["III"]
    if 17 <= hour < 21:
        return BY_NUMERAL["IV"]
    if 21 <= hour < 24:
        return BY_NUMERAL["V"]
    return BY_NUMERAL["VI"]


# ---------------------------------------------------------------------------
# Notion
# ---------------------------------------------------------------------------


class NotionError(RuntimeError):
    pass


def _notion_token() -> str:
    token = os.environ.get("NOTION_PERSONAL_TOKEN") or os.environ.get("NOTION_TOKEN")
    if token:
        return token
    # Fall back to the repo dotenv so the script runs without direnv.
    dotenv = REPO_ROOT / ".env"
    if dotenv.exists():
        for line in dotenv.read_text().splitlines():
            line = line.strip()
            if line.startswith("NOTION_PERSONAL_TOKEN="):
                return line.split("=", 1)[1].strip().strip('"').strip("'")
    raise NotionError(
        "NOTION_PERSONAL_TOKEN is not set and was not found in the repo .env. "
        "Run through almanac.sh, which sources it."
    )


def _notion(path: str, payload: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
    request = urllib.request.Request(
        f"{NOTION_API}{path}",
        data=json.dumps(payload).encode() if payload is not None else None,
        method="POST" if payload is not None else "GET",
        headers={
            "Authorization": f"Bearer {_notion_token()}",
            "Notion-Version": NOTION_VERSION,
            "Content-Type": "application/json",
        },
    )
    try:
        with urllib.request.urlopen(request, timeout=45) as response:
            return json.loads(response.read())
    except urllib.error.HTTPError as exc:
        detail = exc.read().decode(errors="replace")[:400]
        raise NotionError(f"Notion {exc.code} on {path}: {detail}") from exc
    except urllib.error.URLError as exc:
        raise NotionError(f"Notion unreachable: {exc.reason}") from exc


_TITLE_CACHE: Dict[str, str] = {}


def _relation_title(page_id: str) -> str:
    if page_id in _TITLE_CACHE:
        return _TITLE_CACHE[page_id]
    try:
        page = _notion(f"/pages/{page_id}")
    except NotionError:
        _TITLE_CACHE[page_id] = ""
        return ""
    title = ""
    for prop in page.get("properties", {}).values():
        if prop.get("type") == "title":
            title = "".join(part.get("plain_text", "") for part in prop.get("title", []))
            break
    _TITLE_CACHE[page_id] = title
    return title


def _first_relation_title(prop: Dict[str, Any]) -> str:
    relations = prop.get("relation") or []
    if not relations:
        return ""
    return _relation_title(relations[0]["id"])


@dataclass
class Task:
    page_id: str
    name: str
    scheduled_raw: str
    url: str
    status: str = ""
    priority: str = ""
    energy: str = ""
    due: str = ""
    sphere: str = ""
    project: str = ""
    start: Optional[datetime] = None

    @property
    def dateless(self) -> bool:
        return self.start is None


def _row_to_task(row: Dict[str, Any]) -> Optional[Task]:
    props = row.get("properties", {})
    name = "".join(
        part.get("plain_text", "") for part in (props.get("Name") or {}).get("title", [])
    ).strip() or "(untitled task)"
    scheduled = (props.get("Scheduled") or {}).get("date") or {}
    raw = scheduled.get("start") or ""

    start: Optional[datetime] = None
    if "T" in raw:
        parsed = datetime.fromisoformat(raw.replace("Z", "+00:00"))
        if parsed.tzinfo is not None:
            parsed = parsed.astimezone().replace(tzinfo=None)
        start = parsed

    return Task(
        page_id=row["id"],
        name=name,
        scheduled_raw=raw,
        url=row.get("url", ""),
        status=((props.get("Status") or {}).get("status") or {}).get("name", ""),
        priority=((props.get("Priority") or {}).get("select") or {}).get("name", ""),
        energy=((props.get("Energy") or {}).get("select") or {}).get("name", ""),
        due=((props.get("Due Date") or {}).get("date") or {}).get("start", "") or "",
        sphere=_first_relation_title(props.get("Sphere") or {}),
        project=_first_relation_title(props.get("Project") or {}),
        start=start,
    )


def _query_tasks(filters: List[Dict[str, Any]], sort_property: str) -> List[Dict[str, Any]]:
    payload: Dict[str, Any] = {
        "filter": {"and": filters},
        "sorts": [{"property": sort_property, "direction": "ascending"}],
        "page_size": 100,
    }
    results: List[Dict[str, Any]] = []
    cursor: Optional[str] = None
    while True:
        if cursor:
            payload["start_cursor"] = cursor
        page = _notion(f"/databases/{TASKS_DATABASE_ID}/query", payload)
        results.extend(page.get("results", []))
        if not page.get("has_more"):
            break
        cursor = page.get("next_cursor")
    return results


OPEN_ONLY = [
    {"property": "Status", "status": {"does_not_equal": status}}
    for status in CLOSED_STATUSES
]


def fetch_pool() -> List[Task]:
    """Open tasks with no Scheduled value -- everything wanting time."""
    rows = _query_tasks(
        [*OPEN_ONLY, {"property": "Scheduled", "date": {"is_empty": True}}],
        "Due Date",
    )
    is_next_action = []
    for row in rows:
        task = _row_to_task(row)
        parent = (row.get("properties", {}).get("Parent Task") or {}).get("relation") or []
        children = (row.get("properties", {}).get("Next Actions") or {}).get("relation") or []
        # A task with children is a parent and stays at goal level; only
        # pomodoro-sized next actions and standalone tasks want a slot.
        if children:
            continue
        task.status = task.status or ""
        is_next_action.append((task, bool(parent)))
    return [t for t, _ in is_next_action]


def fetch_stale(before: datetime) -> List[Task]:
    """
    Open tasks whose Scheduled has already passed. Unworked time does not
    roll forward on its own -- the session returns these to the pool so
    the operator decides afresh whether each still earns a slot.
    """
    rows = _query_tasks(
        [*OPEN_ONLY, {"property": "Scheduled", "date": {"before": before.date().isoformat()}}],
        "Scheduled",
    )
    tasks = []
    for row in rows:
        task = _row_to_task(row)
        if task.start is not None and task.start >= before:
            continue
        tasks.append(task)
    return tasks


def clear_scheduled(tasks: List[Task]) -> int:
    for task in tasks:
        _notion_patch(task.page_id, {"Scheduled": {"date": None}})
    return len(tasks)


def _notion_patch(page_id: str, properties: Dict[str, Any]) -> Dict[str, Any]:
    request = urllib.request.Request(
        f"{NOTION_API}/pages/{page_id}",
        data=json.dumps({"properties": properties}).encode(),
        method="PATCH",
        headers={
            "Authorization": f"Bearer {_notion_token()}",
            "Notion-Version": NOTION_VERSION,
            "Content-Type": "application/json",
        },
    )
    try:
        with urllib.request.urlopen(request, timeout=45) as response:
            return json.loads(response.read())
    except urllib.error.HTTPError as exc:
        detail = exc.read().decode(errors="replace")[:400]
        raise NotionError(f"Notion {exc.code} patching {page_id}: {detail}") from exc


def fetch_tasks(window_start: datetime, window_end: datetime) -> List[Task]:
    """Every personal task scheduled inside the window and not yet closed."""
    payload: Dict[str, Any] = {
        "filter": {
            "and": [
                {"property": "Scheduled", "date": {"on_or_after": window_start.date().isoformat()}},
                {"property": "Scheduled", "date": {"before": window_end.date().isoformat()}},
                *[
                    {"property": "Status", "status": {"does_not_equal": status}}
                    for status in CLOSED_STATUSES
                ],
            ]
        },
        "sorts": [{"property": "Scheduled", "direction": "ascending"}],
        "page_size": 100,
    }

    results: List[Dict[str, Any]] = []
    cursor: Optional[str] = None
    while True:
        if cursor:
            payload["start_cursor"] = cursor
        page = _notion(f"/databases/{TASKS_DATABASE_ID}/query", payload)
        results.extend(page.get("results", []))
        if not page.get("has_more"):
            break
        cursor = page.get("next_cursor")

    tasks: List[Task] = []
    for row in results:
        props = row.get("properties", {})
        scheduled = (props.get("Scheduled") or {}).get("date") or {}
        raw = scheduled.get("start") or ""
        if not raw:
            continue

        name = "".join(
            part.get("plain_text", "") for part in (props.get("Name") or {}).get("title", [])
        ).strip() or "(untitled task)"

        start: Optional[datetime] = None
        if "T" in raw:
            parsed = datetime.fromisoformat(raw.replace("Z", "+00:00"))
            if parsed.tzinfo is not None:
                parsed = parsed.astimezone().replace(tzinfo=None)
            start = parsed

        # The date filter is day-granular, so a same-day task outside the
        # window's hours can slip through. Drop it here.
        if start is not None and not (window_start <= start < window_end):
            continue

        tasks.append(
            Task(
                page_id=row["id"],
                name=name,
                scheduled_raw=raw,
                url=row.get("url", ""),
                status=((props.get("Status") or {}).get("status") or {}).get("name", ""),
                priority=((props.get("Priority") or {}).get("select") or {}).get("name", ""),
                energy=((props.get("Energy") or {}).get("select") or {}).get("name", ""),
                due=((props.get("Due Date") or {}).get("date") or {}).get("start", "") or "",
                sphere=_first_relation_title(props.get("Sphere") or {}),
                project=_first_relation_title(props.get("Project") or {}),
                start=start,
            )
        )

    tasks.sort(key=lambda t: (t.start is None, t.start or datetime.max, t.name))
    return tasks


# ---------------------------------------------------------------------------
# Calendar
# ---------------------------------------------------------------------------


def calendar_exists(title: str) -> bool:
    return any(c["title"].lower() == title.lower() for c in bridge._calendar_names())


def resolve_calendar(title: str) -> str:
    """
    Exact resolution with no fallback. The bridge's resolver silently
    picks the first writable calendar when a name does not match, which
    would scatter a render across the wrong surface.
    """
    for cal in bridge._calendar_names():
        if cal["title"].lower() == title.lower():
            if not cal["writable"]:
                sys.exit(f"Calendar '{cal['title']}' is not writable.")
            return cal["title"]
    sys.exit(
        f"No calendar titled '{title}'. Create it in Calendar.app under the "
        "iCloud account (File > New Calendar > iCloud) so it syncs to your "
        "devices, then run again."
    )


def signed(body: str, stamped: datetime) -> str:
    return f"{body}\n\n{SIGNATURE} · rendered {stamped.strftime('%Y-%m-%d %H:%M')}\n{SIGNATURE_NOTE}"


def is_signed(event: Dict[str, Any]) -> bool:
    return SIGNATURE in (event.get("notes") or "")


def _parse_event_end(event: Dict[str, Any]) -> datetime:
    """Naive local end time for an event returned by the bridge."""
    raw = event.get("end") or event.get("start") or ""
    try:
        parsed = datetime.fromisoformat(raw.replace("Z", "+00:00"))
    except ValueError:
        return datetime.max
    if parsed.tzinfo is not None:
        parsed = parsed.astimezone().replace(tzinfo=None)
    return parsed


def _mkdate(dt: datetime) -> str:
    return f"(my mkdate({dt.year}, {dt.month}, {dt.day}, {dt.hour}, {dt.minute}, 0))"


@dataclass
class Draft:
    title: str
    start: datetime
    end: datetime
    notes: str
    kind: str  # "block" or "task"
    block: str = ""
    task: Optional[Task] = None


def create_many(calendar: str, drafts: List[Draft]) -> int:
    """Write every event in one osascript call rather than one call each."""
    if not drafts:
        return 0
    lines = []
    for draft in drafts:
        props = ", ".join(
            [
                f"summary:{bridge._quote(draft.title)}",
                f"start date:{_mkdate(draft.start)}",
                f"end date:{_mkdate(draft.end)}",
                "allday event:false",
                f"description:{bridge._quote(draft.notes)}",
            ]
        )
        lines.append(f"        make new event at end of events with properties {{{props}}}")

    script = f"""
{bridge.DATE_HANDLER}
tell application "Calendar"
    tell calendar {bridge._quote(calendar)}
{chr(10).join(lines)}
    end tell
end tell
return "ok"
"""
    bridge._run(script)
    return len(drafts)


def delete_many(calendar: str, uids: List[str]) -> int:
    if not uids:
        return 0
    listing = "{" + ", ".join(bridge._quote(u) for u in uids) + "}"
    script = f"""
set targets to {listing}
tell application "Calendar"
    tell calendar {bridge._quote(calendar)}
        repeat with t in targets
            set hits to (every event whose uid is (t as string))
            repeat with h in hits
                delete h
            end repeat
        end repeat
    end tell
end tell
return "ok"
"""
    bridge._run(script)
    return len(uids)


# ---------------------------------------------------------------------------
# Planning
# ---------------------------------------------------------------------------


@dataclass
class Plan:
    window_start: datetime
    window_end: datetime
    calendar: str
    drafts: List[Draft] = field(default_factory=list)
    clearing: List[Dict[str, Any]] = field(default_factory=list)
    dateless: List[Task] = field(default_factory=list)
    collisions: List[Tuple[Draft, Draft]] = field(default_factory=list)
    load: Dict[str, int] = field(default_factory=dict)
    foreign: List[Dict[str, Any]] = field(default_factory=list)


def build_plan(
    window_start: datetime,
    window_end: datetime,
    calendar: str,
    tasks: List[Task],
    existing: List[Dict[str, Any]],
    stamped: datetime,
    blocks_only: bool = False,
) -> Plan:
    plan = Plan(window_start=window_start, window_end=window_end, calendar=calendar)

    # Clear on overlap, not on start. A block container reaches back to
    # its own 05:00/09:00/13:00/17:00 start, so a window opened mid-block
    # by --from-now draws a block that began before the window. Matching
    # only on start date leaves the previous render's copy in place and
    # the day acquires a duplicate every time it is re-rendered.
    overlapping = [
        e for e in existing if _parse_event_end(e) > window_start
    ]
    plan.clearing = [e for e in overlapping if is_signed(e)]
    plan.foreign = [e for e in overlapping if not is_signed(e)]

    # Container blocks -- the four waking blocks, every day in the window.
    day = window_start.date()
    while day < window_end.date():
        for block in BLOCKS:
            if not block.renders:
                continue
            start = datetime.combine(day, datetime.min.time()).replace(hour=block.start_hour)
            end = start + timedelta(minutes=BLOCK_MINUTES)
            if end <= window_start or start >= window_end:
                continue
            plan.drafts.append(
                Draft(
                    title=block.title,
                    start=start,
                    end=end,
                    notes=signed(
                        f"Block {block.numeral} of VI · "
                        f"{start.strftime('%H:%M')}–{end.strftime('%H:%M')}\n"
                        f"{block.character}",
                        stamped,
                    ),
                    kind="block",
                    block=block.numeral,
                )
            )
        day += timedelta(days=1)

    if blocks_only:
        plan.dateless = [t for t in tasks if t.dateless]
        return plan

    for task in tasks:
        if task.dateless:
            # Find, do not silently resolve. A Scheduled value without a
            # time has no hour, and the block is derived from the hour.
            plan.dateless.append(task)
            continue
        block = block_for_hour(task.start.hour)
        end = task.start + timedelta(minutes=TASK_MINUTES)
        detail = [f"Block {block.numeral} · {block.name}"]
        if not block.renders:
            detail.append("Rest block – the container is not drawn.")
        if task.sphere:
            detail.append(f"Sphere: {task.sphere}")
        if task.project:
            detail.append(f"Project: {task.project}")
        meta = " · ".join(x for x in (task.priority, task.energy, task.status) if x)
        if meta:
            detail.append(meta)
        if task.due:
            detail.append(f"Due {task.due}")
        if task.url:
            detail.append(task.url)
        plan.drafts.append(
            Draft(
                title=task.name,
                start=task.start,
                end=end,
                notes=signed("\n".join(detail), stamped),
                kind="task",
                block=block.numeral,
                task=task,
            )
        )

    placed = sorted(
        [d for d in plan.drafts if d.kind == "task"], key=lambda d: d.start
    )
    for i, current in enumerate(placed):
        for later in placed[i + 1 :]:
            if later.start >= current.end:
                break
            plan.collisions.append((current, later))

    for draft in placed:
        key = f"{draft.start.date().isoformat()}|{draft.block}"
        plan.load[key] = plan.load.get(key, 0) + TASK_MINUTES

    plan.drafts.sort(key=lambda d: (d.start, 0 if d.kind == "block" else 1))
    return plan


# ---------------------------------------------------------------------------
# Reporting
# ---------------------------------------------------------------------------


def report(plan: Plan, executed: bool) -> str:
    out: List[str] = []
    verb = "Rendered" if executed else "Would render"
    # An Almanac day runs 05:00 to 05:00, so the window's final minute
    # belongs to the previous calendar date. Shift back past the wake
    # before naming the last day, or every report reads a day long.
    last_day = plan.window_end - timedelta(hours=5, minutes=1)
    span = (
        f"{plan.window_start.strftime('%a %d %b')} "
        f"→ {last_day.strftime('%a %d %b')}"
    )
    out.append(f"The Almanac · {span} · calendar '{plan.calendar}'")
    out.append("")

    blocks = [d for d in plan.drafts if d.kind == "block"]
    tasks = [d for d in plan.drafts if d.kind == "task"]
    cleared = "Cleared" if executed else "Would clear"
    out.append(
        f"{cleared} {len(plan.clearing)} signed event(s). "
        f"{len(plan.foreign)} unsigned event(s) in the window left untouched."
    )
    out.append(f"{verb} {len(blocks)} block container(s) and {len(tasks)} task(s).")
    out.append("")

    current_day: Optional[date] = None
    for draft in plan.drafts:
        if draft.start.date() != current_day:
            current_day = draft.start.date()
            out.append(f"  {current_day.strftime('%A %d %B')}")
        if draft.kind == "block":
            key = f"{draft.start.date().isoformat()}|{draft.block}"
            used = plan.load.get(key, 0)
            gauge = f"  [{used}/{BLOCK_MINUTES} min]" if used else "  [empty]"
            out.append(
                f"    {draft.start.strftime('%H:%M')}  {draft.title}{gauge}"
            )
        else:
            out.append(
                f"      {draft.start.strftime('%H:%M')}  {draft.title}"
            )
    out.append("")

    if plan.collisions:
        out.append("Collisions – two tasks claim the same minutes:")
        for a, b in plan.collisions:
            out.append(
                f"  {a.start.strftime('%a %H:%M')} {a.title}  ✕  "
                f"{b.start.strftime('%H:%M')} {b.title}"
            )
        out.append("")

    over = {k: v for k, v in plan.load.items() if v > BLOCK_MINUTES}
    if over:
        out.append("Oversubscribed blocks – more scheduled than the block holds:")
        for key, minutes in sorted(over.items()):
            day_iso, numeral = key.split("|")
            out.append(
                f"  {date.fromisoformat(day_iso).strftime('%a %d %b')} "
                f"block {numeral}: {minutes} min of {BLOCK_MINUTES}"
            )
        out.append("")

    if plan.dateless:
        out.append("Unplaceable – Scheduled carries a date but no time:")
        for task in plan.dateless:
            out.append(f"  {task.scheduled_raw}  {task.name}")
        out.append("")

    if not executed:
        out.append("Dry run. Nothing was written. Re-run with --execute to render.")
    return "\n".join(out)


def as_json(plan: Plan, executed: bool) -> str:
    return json.dumps(
        {
            "executed": executed,
            "calendar": plan.calendar,
            "window": {
                "start": plan.window_start.isoformat(),
                "end": plan.window_end.isoformat(),
            },
            "cleared": [
                {"id": e["id"], "title": e["title"], "start": e["start"]}
                for e in plan.clearing
            ],
            "untouched": len(plan.foreign),
            "events": [
                {
                    "kind": d.kind,
                    "block": d.block,
                    "title": d.title,
                    "start": d.start.isoformat(),
                    "end": d.end.isoformat(),
                    "task_url": d.task.url if d.task else None,
                }
                for d in plan.drafts
            ],
            "collisions": [
                {
                    "a": {"title": a.title, "start": a.start.isoformat()},
                    "b": {"title": b.title, "start": b.start.isoformat()},
                }
                for a, b in plan.collisions
            ],
            "load": plan.load,
            "unplaceable": [
                {"name": t.name, "scheduled": t.scheduled_raw, "url": t.url}
                for t in plan.dateless
            ],
        },
        indent=2,
    )


# ---------------------------------------------------------------------------
# Window resolution
# ---------------------------------------------------------------------------


def resolve_window(args: argparse.Namespace, now: datetime) -> Tuple[datetime, datetime]:
    """
    Windows begin at the 05:00 wake, not at midnight -- a day in this
    system runs 05:00 to 05:00. `--from-now` starts at the current hour
    instead, so a mid-day render does not draw blocks already spent.
    """
    if args.start:
        start_day = date.fromisoformat(args.start)
    elif args.week == "next":
        start_day = now.date() + timedelta(days=(7 - now.weekday()) % 7 or 7)
    else:
        start_day = now.date()

    if args.days:
        days = args.days
    elif args.week:
        days = 7
    else:
        # Through the coming Sunday inclusive; Monday is the week start.
        days = 7 - start_day.weekday()

    start = datetime.combine(start_day, datetime.min.time()).replace(hour=5)
    end = start + timedelta(days=days)

    if args.from_now and now > start:
        start = now.replace(minute=0, second=0, microsecond=0)
    return start, end


# ---------------------------------------------------------------------------
# Entry point
# ---------------------------------------------------------------------------


def cmd_check(args: argparse.Namespace) -> int:
    print(f"Bridge:    {BRIDGE}")
    try:
        calendars = bridge._calendar_names()
    except Exception as exc:  # noqa: BLE001 -- report, never raise, at the boundary
        print(f"Calendar:  UNREACHABLE – {exc}")
        return 1
    names = [c["title"] for c in calendars]
    print(f"Calendars: {len(names)} visible – {', '.join(names)}")
    present = calendar_exists(args.calendar)
    print(f"Target:    '{args.calendar}' {'present' if present else 'MISSING'}")
    try:
        now = datetime.now()
        tasks = fetch_tasks(now, now + timedelta(days=14))
        timed = sum(1 for t in tasks if not t.dateless)
        print(f"Notion:    reachable – {len(tasks)} scheduled task(s) in the next 14 days "
              f"({timed} with a time, {len(tasks) - timed} without)")
    except NotionError as exc:
        print(f"Notion:    UNREACHABLE – {exc}")
        return 1
    return 0 if present else 1


def cmd_render(args: argparse.Namespace) -> int:
    now = datetime.now()
    window_start, window_end = resolve_window(args, now)
    calendar = resolve_calendar(args.calendar)

    try:
        tasks = [] if args.blocks_only else fetch_tasks(window_start, window_end)
    except NotionError as exc:
        print(f"Notion is unreachable, so the render is not attempted: {exc}", file=sys.stderr)
        return 1

    # Reach back one block so an event overlapping the window's opening
    # minute is visible to the clear. Nothing this renderer writes can
    # begin earlier than one block before the window starts.
    lookback = window_start - timedelta(minutes=BLOCK_MINUTES)
    existing = bridge._fetch_events(
        lookback.isoformat(), window_end.isoformat(), [calendar]
    )

    plan = build_plan(
        window_start, window_end, calendar, tasks, existing, now, args.blocks_only
    )

    if args.clear_only:
        plan.drafts = []

    if args.execute:
        delete_many(calendar, [e["id"] for e in plan.clearing])
        create_many(calendar, plan.drafts)

    print(as_json(plan, args.execute) if args.json else report(plan, args.execute))
    return 0


def _task_line(task: Task) -> str:
    bits = [x for x in (task.project, task.sphere, task.priority, task.energy) if x]
    tail = f"  ({' · '.join(bits)})" if bits else ""
    due = f"  due {task.due}" if task.due else ""
    return f"  {task.name}{due}{tail}"


def cmd_pool(args: argparse.Namespace) -> int:
    tasks = fetch_pool()
    if args.json:
        print(json.dumps(
            [
                {
                    "page_id": t.page_id, "name": t.name, "status": t.status,
                    "priority": t.priority, "energy": t.energy, "due": t.due,
                    "sphere": t.sphere, "project": t.project, "url": t.url,
                }
                for t in tasks
            ],
            indent=2,
        ))
        return 0
    print(f"{len(tasks)} open task(s) wanting a slot:\n")
    for task in tasks:
        print(_task_line(task))
    return 0


def cmd_sweep(args: argparse.Namespace) -> int:
    now = datetime.now()
    stale = fetch_stale(now)
    if args.json:
        print(json.dumps(
            [
                {"page_id": t.page_id, "name": t.name, "scheduled": t.scheduled_raw,
                 "status": t.status, "url": t.url}
                for t in stale
            ],
            indent=2,
        ))
    else:
        verb = "Returned" if args.execute else "Would return"
        print(f"{verb} {len(stale)} unworked task(s) to the pool:\n")
        for task in stale:
            print(f"  {task.scheduled_raw}  {task.name}  [{task.status}]")
        if not args.execute:
            print("\nDry run. Nothing was cleared. Re-run with --execute.")
    if args.execute:
        clear_scheduled(stale)
    return 0


def main() -> int:
    parser = argparse.ArgumentParser(
        prog="almanac",
        description="Render the personal Notion schedule onto Calendar.app.",
    )
    parser.add_argument("--calendar", default=DEFAULT_CALENDAR,
                        help=f"Target calendar title (default: {DEFAULT_CALENDAR}). No fallback.")
    sub = parser.add_subparsers(dest="command", required=True)

    check = sub.add_parser("check", help="Verify the bridge, the calendar and Notion.")
    check.set_defaults(func=cmd_check)

    render = sub.add_parser("render", help="Render a window. Dry run unless --execute.")
    render.add_argument("--start", help="First day, YYYY-MM-DD (default: today).")
    render.add_argument("--days", type=int, help="Window length in days.")
    render.add_argument("--week", choices=["this", "next"],
                        help="Seven days from this or next Monday.")
    render.add_argument("--from-now", action="store_true",
                        help="Begin at the current hour rather than the 05:00 wake.")
    render.add_argument("--blocks-only", action="store_true",
                        help="Draw the block containers and place no tasks.")
    render.add_argument("--clear-only", action="store_true",
                        help="Remove signed events in the window and write nothing back.")
    render.add_argument("--execute", action="store_true",
                        help="Actually write. Without it the run is a dry run.")
    render.add_argument("--json", action="store_true", help="Machine-readable output.")
    render.set_defaults(func=cmd_render)

    pool = sub.add_parser("pool", help="Open tasks with no Scheduled value.")
    pool.add_argument("--json", action="store_true", help="Machine-readable output.")
    pool.set_defaults(func=cmd_pool)

    sweep = sub.add_parser(
        "sweep",
        help="Return unworked past-scheduled tasks to the pool. Dry run unless --execute.",
    )
    sweep.add_argument("--execute", action="store_true", help="Actually clear Scheduled.")
    sweep.add_argument("--json", action="store_true", help="Machine-readable output.")
    sweep.set_defaults(func=cmd_sweep)

    args = parser.parse_args()
    try:
        return args.func(args)
    except bridge.AppleScriptError as exc:
        print(f"Calendar.app refused the script: {exc}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
