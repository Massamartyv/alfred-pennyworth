# Cal.com

Booking layer for the scheduling lane. Thin MCP layer over the Cal.com API v2. Surfaces bookings, event types and availability as tools Alfred can call from any session, plus a gated set of write operations for creating, rescheduling and cancelling bookings.

Cal.com is the client-facing booking engine for Five Points -- diagnostics, working calls, prospect conversations. Before this integration, bookings landed invisibly in the studio Google Workspace calendar and the dashboard was the only interface. This server gives Alfred eyes on the booking pipeline and, under explicit user confirmation, hands on it.

## Architecture

```
Alfred --> Cal.com MCP (FastMCP) --> Cal.com API v2 --> martavious-spicer account
```

Thin adapter. One helper function `_request` owns every API call. Tools are small wrappers that format parameters and return the raw response envelope. No client library; direct `httpx` against `https://api.cal.com/v2`.

## Pipelines

Every tool call declares a pipeline. The pipeline selects which Cal.com account the request executes against. Today only Five Points is provisioned; the registry is ready to extend to personal or other ventures without an API change.

| Pipeline | Label | Env var | Username | Status |
|---|---|---|---|---|
| `five_points` | Five Points Digital Studio | `CALCOM_FIVEPOINTS_API_KEY` | `martavious-spicer` | Awaiting key |

A pipeline without a configured key returns a clean "not provisioned" error with no network call.

## Live events

| Event | Slug | Length | Notes |
|---|---|---|---|
| The Working Call | `/the-working-call` | 45 min | Client commissioning calls; attendee-phone location, 15-min after-buffer |
| Operational Intelligence Diagnostic | `/30min` | 30 min | 30-minute hold for a 20-minute session; buffer by design |
| 15 min meeting | `/15min` | 15 min | General short call |

## API versioning

Cal.com versions v2 endpoints per resource via the `cal-api-version` header. Pinned values (verified against the docs 2026-07-10):

| Resource | Header value |
|---|---|
| List bookings | `2026-05-01` |
| Booking lifecycle (get, create, reschedule, cancel) | `2026-02-25` |
| Event types | `2024-06-14` |
| Slots | `2024-09-04` |

When Cal.com ships a new version, update the constant at the top of `server.py`, not the call sites.

## Status

**Scaffolded 2026-07-10.** Python 3.12 venv built, dependencies installed, offline smoke test passing (envelope, validation guards, tool registration). MCP registered in `.mcp.json`. Awaiting the API key drop; live verification against the Five Points account is the first action after the key lands.

## Setup

### 1. Cal.com API key (operator step)

Generate an API key in the Cal.com dashboard under Settings > Security (live keys carry the `cal_live_` prefix). The account is cal.com/martavious-spicer, primary email martavious@fivepoints.studio.

### 2. Environment variable (operator step)

Add the key to `~/Alfred Pennyworth/.env`:

```
CALCOM_FIVEPOINTS_API_KEY=cal_live_...
```

### 3. Install dependencies

```bash
cd ~/Alfred\ Pennyworth/Integrations/calcom
/opt/homebrew/opt/python@3.12/bin/python3.12 -m venv .venv
.venv/bin/pip install -r requirements.txt
```

### 4. Register with MCP

Add to `.mcp.json` at the project root, following the house pattern (bash sources `.env` and execs the venv Python):

```json
"calcom": {
  "type": "stdio",
  "command": "/bin/bash",
  "args": [
    "-c",
    "set -a; source '/Users/martyspicer/Alfred Pennyworth/.env'; set +a; exec '/Users/martyspicer/Alfred Pennyworth/Integrations/calcom/.venv/bin/python' '/Users/martyspicer/Alfred Pennyworth/Integrations/calcom/server.py'"
  ]
}
```

### 5. Verify

Restart the MCP-hosting client and call `pipeline_status` to confirm the key resolves, then `health_check` (GET /me) to confirm reachability, then `list_event_types` to confirm the three live events appear.

## Tools

### Read (Tier 1)

| Tool | Endpoint | Purpose |
|---|---|---|
| `list_event_types` | `GET /event-types` | List the account's event types, or one by slug |
| `list_bookings` | `GET /bookings` | List bookings with status, attendee, event-type and date filters |
| `get_booking` | `GET /bookings/{uid}` | Fetch a single booking's full record |
| `get_availability` | `GET /slots` | Available slots for an event type in a time range |

### Write (Tier 2, gated)

Every write tool must be confirmed in chat before dispatch, per Navigation Rule 3. All three trigger Cal.com notification emails to host and attendee.

| Tool | Endpoint | Purpose |
|---|---|---|
| `create_booking` | `POST /bookings` | Book an attendee into an event type |
| `reschedule_booking` | `POST /bookings/{uid}/reschedule` | Move a booking to a new start time |
| `cancel_booking` | `POST /bookings/{uid}/cancel` | Cancel a booking, optionally with subsequent recurrences |

### Helpers

| Tool | Purpose |
|---|---|
| `list_pipelines` | Return the pipeline registry |
| `pipeline_status` | Report, per pipeline, whether its key is set |
| `health_check` | Fetch the authenticated profile to verify reachability |

## Time handling

Booking `start` values are UTC ISO 8601 (`2026-07-15T14:00:00Z`). Cal.com interprets the start as UTC regardless of the attendee time zone -- a meeting at 11:00 in GMT+2 is submitted as 09:00Z. The attendee `timeZone` (IANA name, e.g. `America/New_York`) controls how times render in notifications.

## Response envelope

Every tool returns a normalized envelope:

```json
{
  "pipeline": "five_points",
  "ok": true,
  "status_code": 200,
  "data": { "status": "success", "data": { ... raw Cal.com response ... } },
  "error": null,
  "fetched_at": "2026-07-10T22:00:00+00:00"
}
```

On failure, `ok` is `false`, `error` carries a short message and `data` may carry Cal.com's error body when available. The server never raises -- every failure flows through this shape. Note that Cal.com wraps its own responses in `{status, data}`; the envelope preserves that wrapper verbatim.

## Future scope

Out of v1, easy to add later:

- **Webhooks** -- subscribe to BOOKING_CREATED / RESCHEDULED / CANCELLED and pipe them into the Five Points Notion CRM so Alfred stops polling. Closes the booking-to-CRM loop.
- **Event-type management** -- create and edit event types (lengths, buffers, locations) from chat.
- **Multi-pipeline** -- add `personal` or `marty_gras` to `PIPELINE_REGISTRY` when those Cal.com accounts exist.
- **Routing forms** -- if intake routing ever precedes booking.

## References

- Cal.com API v2 docs: https://cal.com/docs/api-reference/v2/introduction
- Five Points integrations: `Context/Spheres/System/Entrepreneurship/Five Points Digital Studio/Agents/integrations.md`
- MCP registry: `Manual/mcp-registry.md`

---

*Last updated: 2026-07-10*
