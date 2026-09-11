# The Almanac

Renders the personal Notion schedule onto the `Almanac` calendar in Calendar.app.

Notion is the authority; the calendar is a one-way projection on the state-cache pattern. Nothing is ever read back, and an edit made in Calendar.app is lost at the next render.

- Design of record: `design-notes.md`, beside this file
- Mission record: https://app.notion.com/p/The-Almanac-3ba1896165cf81ab80cac051406cc7b8
- Interactive ritual: the `almanac` skill at `~/.claude/skills/almanac/`

## Usage

Every write is a dry run unless `--execute` is passed.

```bash
./almanac.sh check                          # bridge, calendar and Notion reachable?
./almanac.sh pool [--json]                  # open tasks with no Scheduled value
./almanac.sh sweep [--execute] [--json]     # return unworked past-scheduled tasks to the pool
./almanac.sh render [options]
```

`render` options:

| Flag | Effect |
|---|---|
| `--start YYYY-MM-DD` | First day of the window. Defaults to today. |
| `--days N` | Window length. Defaults to today through the coming Sunday. |
| `--week this\|next` | Seven days from this or next Monday. |
| `--from-now` | Begin at the current hour rather than the 05:00 wake. |
| `--blocks-only` | Draw the containers, place no tasks. |
| `--clear-only` | Remove signed events in the window, write nothing back. |
| `--calendar TITLE` | Target calendar. Defaults to `Almanac`. No fallback. |
| `--execute` | Actually write. |
| `--json` | Machine-readable output for the skill. |

## The six blocks

Six equal four-hour blocks tile the full 24 hours from the 05:00 wake.

| # | Name | Hours | Renders |
|---|---|---|---|
| I | Morning Routine | 05:00 – 09:00 | yes |
| II | Administration | 09:00 – 13:00 | yes |
| III | Collaboration | 13:00 – 17:00 | yes |
| IV | Social | 17:00 – 21:00 | yes |
| V | Evening Routine | 21:00 – 01:00 | no |
| VI | Night Owl | 01:00 – 05:00 | no |

The block is derived from the hour and never stored, so there is no second copy of the truth to drift out of step. The rest blocks are part of the model and are never drawn; a task scheduled into one still renders, only its container is missing.

## The signature rule

Every event this renderer writes carries `⟡ almanac:v1` in its description. A render clears only events bearing that signature inside the window, on the target calendar. The signature is checked, never inferred from title or position.

Operator-placed events are therefore safe by construction rather than by care, and a partially failed render is recoverable – re-running clears exactly its own output and nothing else.

An event written by any other route carries no signature and the renderer can never clear it. Place events through this script, not through the calendar MCP tools.

## Two invariants

**Clear on overlap, not on start.** A block container reaches back to its own 05:00, 09:00, 13:00 or 17:00 start, so a window opened mid-block by `--from-now` draws a block that began before the window. The clear therefore fetches one block earlier than the window opens and matches on end time. Matching only on start date leaves the previous render's copy in place, and the day acquires a duplicate on every re-render. This was a live defect on 2026-09-09; the regression test is to run `render --from-now --execute` three times and confirm the cleared count equals the written count from the second run onward.

**No calendar fallback.** `resolve_calendar` aborts when the named calendar does not exist. The apple-calendar bridge's own resolver falls back to the first writable calendar on a name miss, which would scatter a render across the wrong surface.

## Dependencies

Runs on the `apple-calendar` venv, which already carries the bridge's dependencies. The AppleScript plumbing – escaping, date construction, bulk reads – is imported from `Integrations/apple-calendar/server.py` so it lives in exactly one place. Notion is reached over `urllib` from the standard library; no third-party HTTP client is added.

`almanac.sh` sources the repo `.env` for `NOTION_PERSONAL_TOKEN`. The Python falls back to reading the same file directly when the variable is absent from the environment.

## Provisioning the calendar

The `Almanac` calendar must exist in Calendar.app under the iCloud account so it syncs to the phone.

Creating it over AppleScript works, but only while Calendar.app is running – `make new calendar` reports success against a quiescent app and silently fails to commit. Either create it by hand (File > New Calendar > iCloud) or run:

```bash
osascript -e 'tell application "Calendar" to activate' \
          -e 'tell application "Calendar" to make new calendar with properties {name:"Almanac"}' \
          -e 'delay 2'
```

Then confirm with `./almanac.sh check`. A calendar that appears in `~/Library/Calendars/` is local to this Mac and will not sync; that directory should stay empty.

## Known behaviour

- **No recurrence.** Calendar.app exposes only the master event of a recurring series over AppleScript and cannot address a single occurrence, so every event is written discrete. Never create a recurring event on this calendar.
- **A `Scheduled` value with no time is unplaceable.** The block derives from the hour. The renderer reports these rather than guessing an hour.
- **Rest-block tasks group by calendar date.** An Almanac day runs 05:00 to 05:00, so a task at 02:00 Tuesday belongs to Monday's block VI in the model but is reported under Tuesday.
- **Parents are excluded from the pool.** A task with next actions stays at goal level; only pomodoro-sized next actions and standalone tasks want a slot.
- **Personal scope only.** Five Points tasks do not flow in until the Navigation Rule 2 boundary is ruled.
