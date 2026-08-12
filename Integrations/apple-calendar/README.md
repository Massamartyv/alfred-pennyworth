# Apple Calendar MCP

Local access to every calendar Calendar.app knows about -- iCloud first and foremost, plus any Google, Exchange or local calendars configured in macOS. Personal-scope counterpart to `fivepoints-calendar`.

Driven over AppleScript since the rewrite of 2026-08-12. No third-party dependencies beyond `mcp` and `pydantic`.

## Why AppleScript, after all

The original build chose EventKit over an AppleScript bridge on four arguments: predicate-query speed, structured CRUD, no dependency on Calendar.app running, and account breadth. Every one of those arguments was correct on its merits. The build still failed, because the evaluation never tested the premise underneath them -- that the permission could be obtained at all.

It could not:

- The server runs as a bare Homebrew `python3.12` with no application bundle, so it cannot raise a TCC dialog on its own behalf.
- The design assumed macOS would attribute the request to the hosting app instead. The Claude app's `Info.plist` declares neither `NSCalendarsUsageDescription` nor `NSCalendarsFullAccessUsageDescription`, so the system refuses to raise one.
- `requestFullAccessToEvents` therefore returned `not_determined` instantly and silently, every time.
- Because no request ever succeeded, macOS never created an entry under System Settings > Privacy & Security > Calendars, and that pane has no manual add button. There was nothing for the operator to approve.

The lane was dark from 2026-07-10 to 2026-08-12 and reported no error while it was.

AppleScript reaches the same calendars through the Automation permission (`NSAppleEventsUsageDescription`), which the Claude app does declare and which the `apple-mail` server had been using successfully throughout. The lesson is worth more than the fix: an integration's hardest constraint is often the permission model, not the API surface, and it should be proven first.

## Trade-offs accepted

| Area | Consequence |
|---|---|
| Recurring events | Calendar.app exposes only the master event, carrying its original start date. Occurrences are not expanded, and a single occurrence cannot be edited or deleted. The `span` parameter is retained for signature compatibility and reports plainly that writes reach the whole series. |
| Accounts | Calendar.app exposes no source or account property, so `account` is always `null`. |
| App dependency | Calendar.app must be installed; it is launched on demand. |
| Speed | Slower than EventKit predicates. Properties are read in bulk -- one Apple Event per property per calendar rather than one per event -- which keeps typical windows well inside a second. |

## Implementation notes

Two AppleScript behaviours are load-bearing and easy to regress:

1. **Bulk reads need a live reference.** `set evs to (every event whose ...)` collapses the specifier to a plain list, and plural property access then fails with `Can't get id of {...}`. The query keeps `a reference to (every event whose ...)` unmaterialised so `uid of evRefs` works.
2. **Plural access returns a bare value on a single match.** The `aslist` handler normalises so the caller always indexes safely.

Dates are constructed component by component through the `mkdate` handler, which keeps the script locale-independent. Day is reset to 1 before year and month are assigned so that a shorter month cannot overflow the value.

Field and record separators are ASCII 31 and 30 -- characters no calendar UI can produce -- so parsing never collides with event text.

## Status

**Live, verified 2026-08-12.** All nine tools exercised against real calendars, including a full create, read, search, update and delete round trip on a disposable event that was removed at the end of the run. Eight calendars visible.

## Tools

Read: `list_calendars`, `list_events`, `search_events`, `get_event`
Write: `create_event`, `update_event`, `delete_event`
Access: `authorization_status`, `request_access`

Write tools carry `WRITE.` in their description so the calling agent follows Navigation Rule 3 and confirms before dispatch. The server does not enforce the gate; `create_event`, `update_event` and `delete_event` also sit on the ask list in `~/.claude/settings.json`.

## Setup

The venv at `.venv/` needs only `pip install -r requirements.txt`. Registration lives in the repo-root `.mcp.json`.

On first use macOS raises an Automation prompt for Calendar.app, attributed to the hosting app. Approve it. If it is declined, re-enable at System Settings > Privacy & Security > Automation. Unlike the Calendars pane, this one lists the app and can be toggled by hand.
