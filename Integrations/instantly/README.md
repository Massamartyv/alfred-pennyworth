# Instantly

Outbound lead pipeline router. Thin MCP layer over the Instantly v2 API. Surfaces campaigns, leads, unibox and analytics as tools Alfred can call from any session.

Instantly is the top of the Five Points lead funnel. Pennyone handles syndication; Instantly handles outbound email. This integration gives Alfred eyes on the pipeline and a gated set of actions for qualifying responses, pausing campaigns and replying under explicit user confirmation.

## Architecture

```
Alfred --> Instantly MCP (FastMCP) --> Instantly v2 API --> Five Points workspace
```

Thin adapter. One helper function `_request` owns every API call. Tools are small wrappers that format parameters and return the raw response envelope. No client library; direct `httpx` against `https://api.instantly.ai/api/v2`.

## Pipelines

Every tool call declares a pipeline. The pipeline selects which Instantly workspace the request executes against. Today only Five Points is provisioned; the registry is ready to extend to personal or other ventures without an API change.

| Pipeline | Label | Env var | Status |
|---|---|---|---|
| `five_points` | Five Points Digital Studio | `INSTANTLY_FIVEPOINTS_API_KEY` | Active |

A pipeline without a configured key returns a clean "not provisioned" error with no network call.

## Status

**Live** (2026-04-24). Dependencies installed (Python 3.12 venv), MCP registered in `.mcp.json`, smoke-tested against the Five Points workspace. Two campaigns visible; every Tier 1 tool returns 200.

## Setup

### 1. Instantly v2 API key

Generate a v2 key in the Instantly workspace settings. v1 keys do not work -- the API is a clean break.

### 2. Environment variables

Add the key to `~/Alfred Pennyworth/.env`:

```
INSTANTLY_FIVEPOINTS_API_KEY=your_v2_key
```

### 3. Install dependencies

```bash
cd ~/Alfred\ Pennyworth/Integrations/instantly
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

### 4. Register with MCP

Add to `.mcp.json` at the project root:

```json
"instantly": {
  "type": "stdio",
  "command": "/Users/martyspicer/Alfred Pennyworth/Integrations/instantly/.venv/bin/python",
  "args": ["/Users/martyspicer/Alfred Pennyworth/Integrations/instantly/server.py"],
  "env": {
    "INSTANTLY_FIVEPOINTS_API_KEY": "${INSTANTLY_FIVEPOINTS_API_KEY}"
  }
}
```

### 5. Verify

Restart the MCP-hosting client and call `pipeline_status` to confirm the key resolves, then `health_check` to confirm reachability of the Five Points workspace.

## Tools

### Read (Tier 1)

| Tool | Endpoint | Purpose |
|---|---|---|
| `list_campaigns` | `GET /campaigns` | List campaigns with optional search and pagination |
| `get_campaign_analytics` | `GET /campaigns/{id}/analytics` | Per-campaign performance metrics |
| `get_analytics_overview` | `GET /campaigns/analytics/overview` | Portfolio aggregate |
| `get_daily_analytics` | `GET /campaigns/analytics/daily` | Daily trend time series |
| `list_leads` | `POST /leads/list` | List leads with filters (campaign, list, email, interest status) |
| `get_lead` | `GET /leads/{id}` | Fetch a single lead record |
| `list_inbox_emails` | `GET /emails` | Unibox listing with unread and campaign filters |
| `count_unread` | `GET /emails/unread/count` | Unread count, Watchtower signal |
| `search_campaign_by_lead` | `POST /campaigns/search-by-lead-email` | Attribution and de-dup check |

### Write (Tier 2, gated)

Every write tool must be confirmed in chat before dispatch, per Navigation Rule 3.

| Tool | Endpoint | Purpose |
|---|---|---|
| `update_lead_interest` | `PATCH /leads/{id}/interest-status` | Qualify a response (interested, booked, closed, etc.) |
| `add_leads_bulk` | `POST /leads/bulk-add` | Push a lead list into a campaign |
| `pause_campaign` | `POST /campaigns/{id}/pause` | Emergency stop on an active campaign |
| `reply_to_email` | `POST /emails/{id}/reply` | Send a reply from the unibox |

### Helpers

| Tool | Purpose |
|---|---|
| `list_pipelines` | Return the pipeline registry |
| `pipeline_status` | Report, per pipeline, whether its key is set |
| `health_check` | Fetch the current workspace to verify reachability |

## Interest status codes

For `update_lead_interest`, Instantly uses the following codes:

| Code | Meaning |
|---|---|
| `1` | Interested |
| `2` | Meeting booked |
| `3` | Meeting completed |
| `4` | Closed |
| `-1` | Not interested |
| `-2` | Wrong person |
| `-3` | Lost |

## Response envelope

Every tool returns a normalised envelope:

```json
{
  "pipeline": "five_points",
  "ok": true,
  "status_code": 200,
  "data": { ... raw Instantly response ... },
  "error": null,
  "fetched_at": "2026-04-24T18:23:00+00:00"
}
```

On failure, `ok` is `false`, `error` carries a short message and `data` may carry Instantly's error body when available. The server never raises -- every failure flows through this shape.

## Future scope

Out of v1, easy to add later:

- **Webhooks** -- subscribe to Instantly event types and pipe them into a Supabase edge function that writes to the Five Points Notion CRM. Closes the loop so Alfred stops polling.
- **Campaign creation and editing** -- full `POST /campaigns` and `PATCH /campaigns/{id}` with step configuration.
- **Subsequences** -- follow-up automation.
- **SuperSearch enrichment** -- run enrichment jobs from a Notion prospect list.
- **Multi-pipeline** -- add `personal` or other ventures to `PIPELINE_REGISTRY` when an Instantly workspace is provisioned for them.

## References

- Instantly v2 API docs: https://developer.instantly.ai/
- Five Points integrations: `Context/Spheres/System/Entrepreneurship/Five Points Digital Studio/Agents/integrations.md`

---

*Last updated: 2026-04-24*
