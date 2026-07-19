# Apple Calendar MCP

Local EventKit access to every calendar the Mac knows about -- iCloud first and foremost, plus any Google, Exchange or local calendars configured in macOS. Personal-scope counterpart to `fivepoints-calendar`.

## Why EventKit and not AppleScript

The build brief asked for an evaluation of an EventKit-based MCP versus an AppleScript bridge in the spirit of `mcp-apple-mail`. Verdict: **EventKit**, for four reasons.

1. **Speed.** EventKit predicate queries return a date window in milliseconds. Calendar.app's AppleScript dictionary enumerates events linearly and is notorious for multi-minute stalls on large or long-lived calendars -- the mail bridge works because Mail's AppleScript surface is tolerable; Calendar's is the weak one.
2. **Structured CRUD.** EventKit exposes identifiers, recurrence spans, calendars and sources as objects. AppleScript round-trips everything through fragile string and date coercions.
3. **No app dependency.** EventKit talks to the system calendar store directly; Calendar.app need not be running.
4. **Account breadth.** The store surfaces every account macOS syncs, so iCloud coverage comes with the rest for free.

The trade: a one-time macOS TCC grant (Full Access to Calendars) attributed to the hosting app, and a PyObjC dependency. Both acceptable.

## Status

**Scaffolded 2026-07-10.** Python 3.12 venv built, offline smoke test passing (authorization status reads `not_determined` without prompting, guards return instructive errors, 9 tools). Registered in `.mcp.json`. Blocked on the one-time TCC grant below.

## Setup

### TCC grant (operator step, one time)

Call the `request_access` tool from a live session. macOS shows a permission dialog attributed to the hosting app (Claude); approve **Full Access**. Alternatively pre-grant under System Settings > Privacy & Security > Calendars. The `authorization_status` tool reports the current state without ever triggering the dialog.

### Local

Dependencies are already installed in `.venv/`. To rebuild:

```bash
cd "Integrations/apple-calendar"
/opt/homebrew/opt/python@3.12/bin/python3.12 -m venv .venv
.venv/bin/pip install -r requirements.txt
```

Registration lives in `.mcp.json` at the project root. No environment variables and no credentials -- authorization is entirely TCC.

### Verify

`authorization_status` should read `authorized_full` after the grant; then `list_calendars` should show the iCloud calendars and `list_events` a populated week.

## Tools

### Access

| Tool | Purpose |
|---|---|
| `authorization_status` | Report the TCC state. Never prompts. |
| `request_access` | Trigger the one-time macOS permission dialog and wait for the answer |

### Read (Tier 1)

| Tool | Purpose |
|---|---|
| `list_calendars` | Every event calendar with its account and writability |
| `list_events` | Events in a window, optionally restricted to named calendars |
| `search_events` | Case-insensitive search over title, location and notes in a window |
| `get_event` | One event by identifier, including notes |

### Write (Tier 2, gated)

Every write tool must be confirmed in chat before dispatch, per Navigation Rule 3. Writes to shared or account-synced calendars propagate outward to those services.

| Tool | Purpose |
|---|---|
| `create_event` | Create an event on a named calendar (default: the system default) |
| `update_event` | Change only the provided fields; `span` handles recurring events |
| `delete_event` | Remove an event or a recurring tail |

## Time handling

Inputs are ISO 8601. Values without an offset are read as the Mac's local time. Outputs carry the local offset explicitly.

## Response envelope

Every tool returns `{ok, data, error, fetched_at}`. On failure `ok` is `false` and `error` carries a short, instructive message. The server never raises.

## Scope boundary

Personal scope. The store shows whatever macOS syncs -- if a studio account were ever added to macOS Calendar it would surface here too; venture calendar work still routes through `fivepoints-calendar` regardless. Never cross the boundary.

## Future scope

- **Reminders** -- the same store serves `EKEntityTypeReminder`; a sibling surface if Apple Reminders ever joins the system.
- **Alarms and travel time** -- settable on events if the need appears.
- **Invitations** -- EventKit does not reliably send invites for non-iCloud accounts; attendee workflows belong to `fivepoints-calendar`.

## References

- EventKit documentation: https://developer.apple.com/documentation/eventkit
- Sibling servers: `Integrations/fivepoints-calendar/`, `mcp-apple-mail` (user scope)
- MCP registry: `Manual/mcp-registry.md`

---

*Last updated: 2026-07-10*
