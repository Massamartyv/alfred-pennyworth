# Five Points Calendar MCP

Venture-scoped Google Calendar access for Five Points Digital Studio. Exposes the calendars of the five `fivepoints.studio` Workspace users to Alfred via a unified MCP with `user` routing -- the calendar sibling of `fivepoints-mail`, sharing its service account.

The primary target is the `martavious` calendar, where Cal.com bookings land. Before this integration the studio calendar was invisible to Alfred; with it, bookings, availability and event management are agent-reachable.

## Users

| User key | Address | Calendar role |
|---|---|---|
| `hello` | `hello@fivepoints.studio` | Workspace admin calendar |
| `martavious` | `martavious@fivepoints.studio` | Owner-direct. Primary studio calendar; Cal.com bookings land here |
| `systems` | `systems@fivepoints.studio` | Technical infrastructure calendar |
| `opportunities` | `opportunities@fivepoints.studio` | Press, vendor and hiring calendar |
| `finance` | `finance@fivepoints.studio` | Financial platform calendar |

Every tool takes a `user` parameter. There is no implicit default, matching the `fivepoints-mail` doctrine: nothing is read or written without an explicit selection.

## Architecture

One Google Cloud service account with domain-wide delegation impersonates each user per request -- the same credential `fivepoints-mail` uses. The credential resolves through a fallback chain, so a single key drop provisions both servers:

1. `FIVEPOINTS_CALENDAR_SERVICE_ACCOUNT` (explicit override)
2. `FIVEPOINTS_MAIL_SERVICE_ACCOUNT` (the mail server's override)
3. `Integrations/fivepoints-mail/credentials/service-account.json` (the shared default drop location)

```
Alfred --> fivepoints-calendar MCP --> Calendar API v3 --> {user}@fivepoints.studio
                     |
        service-account.json (shared with fivepoints-mail)
```

## Status

**Scaffolded 2026-07-10.** Python 3.12 venv built, offline smoke test passing (registry, credential-missing envelope, 9 tools). Registered in `.mcp.json`. Blocked on two operator steps below -- note that as of 2026-07-10 the shared service-account key has never been dropped, so `fivepoints-mail` is blocked on the same step.

## Setup

### Google Cloud (operator step)

1. In the Five Points GCP project (the one from the `fivepoints-mail` setup), enable the **Google Calendar API** (APIs & Services > Library).
2. If no JSON key was ever downloaded for the service account, create one (IAM & Admin > Service Accounts > Keys) and download it.

### Workspace Admin (operator step)

1. Sign into https://admin.google.com as `hello@fivepoints.studio`.
2. Security > Access and data control > API controls > Manage Domain-wide Delegation.
3. On the service account's client ID, ensure the scope list includes the four Gmail scopes from the mail setup **plus**:

   ```
   https://www.googleapis.com/auth/calendar
   ```

### Local

1. Drop the JSON key at `Integrations/fivepoints-mail/credentials/service-account.json` (gitignored; one drop serves mail and calendar).
2. Dependencies are already installed in `.venv/`. To rebuild:

   ```bash
   cd "Integrations/fivepoints-calendar"
   /opt/homebrew/opt/python@3.12/bin/python3.12 -m venv .venv
   .venv/bin/pip install -r requirements.txt
   ```

3. Registration lives in `.mcp.json` at the project root (bash-source house pattern). Restart the MCP host after the key drop.

### Verify

Call `list_users`, then `health_check` for `martavious` -- a success proves the key file, the Calendar API enablement, the delegation scope and impersonation end to end. Then `list_events` with a two-week window should show Cal.com bookings.

## Tools

### Read (Tier 1)

| Tool | Endpoint | Purpose |
|---|---|---|
| `list_calendars` | `calendarList.list` | Calendars visible to a user, with access roles |
| `list_events` | `events.list` | Events in a window, recurring expanded, free-text query |
| `get_event` | `events.get` | One event's full record |
| `get_freebusy` | `freebusy.query` | Busy intervals for one or more calendars |

### Write (Tier 2, gated)

Every write tool must be confirmed in chat before dispatch, per Navigation Rule 3. `send_updates` defaults to `none` on all three -- attendee notification email is itself an outward send and needs explicit approval to switch on.

| Tool | Endpoint | Purpose |
|---|---|---|
| `create_event` | `events.insert` | Create a timed or all-day event, optionally with attendees |
| `update_event` | `events.patch` | Change only the provided fields |
| `delete_event` | `events.delete` | Remove an event |

### Helpers

| Tool | Purpose |
|---|---|
| `list_users` | Return the user registry |
| `health_check` | Fetch a user's primary calendar to verify the full auth chain |

## Response envelope

Every tool returns a normalized envelope: `{user, ok, status_code, data, error, fetched_at}`. On failure `ok` is `false` and `error` carries a short message. The server never raises.

## Scope boundary

Venture-scoped to Five Points. Personal and iCloud calendars route through the `apple-calendar` MCP, never through this server. The personal Gmail calendar has its own desktop connector. Never cross the boundary.

## Future scope

- **Push channels** -- `events.watch` webhooks so Cal.com bookings announce themselves instead of being polled.
- **Additional users** -- new Workspace users are one `USER_REGISTRY` entry away.

## References

- Google Calendar API v3: https://developers.google.com/calendar/api/v3/reference
- Sibling server: `Integrations/fivepoints-mail/`
- MCP registry: `Manual/mcp-registry.md`

---

*Last updated: 2026-07-10*
