# Pennyone

Content syndication router. Thin MCP layer over Zernio. Fans out a single publish request to Instagram, TikTok, Threads, X, Reddit, Snap, LinkedIn, YouTube and Discord under the pipeline's own Zernio account.

Pennyone does not write the content. It does not decide when to publish. It takes an existing publish request and executes the fan-out.

## Architecture

Pennyone is a thin FastMCP server that wraps Zernio, a unified social media API covering 14+ platforms. Pennyone uses nine of them.

```
Alfred --> Pennyone (FastMCP) --> Zernio (per-pipeline account) --> 9 platforms
```

Pennyone adds:

- **Pipeline routing.** The routing key. Each pipeline is isolated -- it has its own Zernio account, its own connected social handles and its own API key. Personal and venture pipelines never share credentials.
- **Per-platform content overrides.** Swap the caption, media or links for a specific platform while keeping one dispatch.
- **Unified response aggregation.** Per-platform success, partial and failure lists in a single envelope.
- **Notion Content pipeline hooks** (future).

## Pipelines

Every publish request must declare a pipeline. The pipeline selects which Zernio account executes the post.

| Pipeline | Label | Env var | Status |
|---|---|---|---|
| `personal` | Personal | `ZERNIO_PERSONAL_API_KEY` | Provisioning |
| `five_points` | Five Points Digital Studio | `ZERNIO_FIVEPOINTS_API_KEY` | Provisioning |
| `paradigm` | Paradigm | `ZERNIO_PARADIGM_API_KEY` | Future |
| `lillie_and_lynette` | Lillie and Lynette | `ZERNIO_LILLIEANDLYNETTE_API_KEY` | Future |

A pipeline without a configured key returns a clean "pipeline not provisioned" error for every platform in the request. No Zernio call is made.

## Status

**Live** for the personal and Five Points pipelines. Keys provisioned 2026-04-23; adapter verified against Zernio's real API shape. MCP registration in local `.mcp.json`.

Connected and active accounts (verified 2026-06-23):

| Pipeline | Connected and active |
|---|---|
| personal | Instagram, TikTok, Threads, Reddit, LinkedIn, YouTube, Discord |
| five_points | Instagram (`studio.fivepoints`) |

X and Snap are in the router but no account is connected on either pipeline; they connect through Zernio's dashboard and Pennyone picks them up automatically. Five Points currently runs Instagram only.

## Setup

### 1. Zernio accounts

Sign up at [zernio.com](https://zernio.com) once per pipeline that needs its own Zernio account. For each account, connect Instagram, TikTok, Threads, X, Reddit and Snap with the handles that belong to that pipeline. Generate an API key per account.

### 2. Environment variables

Add the keys you have to `~/Alfred Pennyworth/.env`:

```
ZERNIO_PERSONAL_API_KEY=your_personal_key
ZERNIO_FIVEPOINTS_API_KEY=your_fivepoints_key
# Add other pipelines as they come online
```

Any pipeline without a key simply returns "not provisioned" when called. Missing keys are not an error at startup.

### 3. Install dependencies

```bash
cd ~/Alfred\ Pennyworth/Integrations/pennyone
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

### 4. Register with MCP

Add to `.mcp.json`:

```json
"pennyone": {
  "type": "stdio",
  "command": "/Users/martyspicer/Alfred Pennyworth/Integrations/pennyone/.venv/bin/python",
  "args": ["/Users/martyspicer/Alfred Pennyworth/Integrations/pennyone/server.py"],
  "env": {
    "ZERNIO_PERSONAL_API_KEY": "${ZERNIO_PERSONAL_API_KEY}",
    "ZERNIO_FIVEPOINTS_API_KEY": "${ZERNIO_FIVEPOINTS_API_KEY}",
    "ZERNIO_PARADIGM_API_KEY": "${ZERNIO_PARADIGM_API_KEY}",
    "ZERNIO_LILLIEANDLYNETTE_API_KEY": "${ZERNIO_LILLIEANDLYNETTE_API_KEY}"
  }
}
```

Unset env vars resolve to empty strings and are treated as "no key." You can keep every pipeline listed even before all accounts are provisioned.

### 5. Verify

Restart the MCP-hosting client and call `pipeline_status` to see which pipelines are provisioned, then `health_check` to confirm Zernio connectivity for each.

## Tools

| Tool | Purpose |
|---|---|
| `publish` | Fan out a publish request to multiple platforms under a given pipeline |
| `list_platforms` | Return every platform Pennyone can publish to |
| `list_pipelines` | Return the full pipeline registry with labels, voices and env vars |
| `pipeline_status` | Report, for each pipeline, whether its key is set (no network call) |
| `health_check` | Verify Zernio reachability for one pipeline or all provisioned pipelines |

## Platform coverage

All nine platforms route through Zernio regardless of pipeline.

| Platform | Via |
|---|---|
| Instagram | Zernio |
| TikTok | Zernio |
| Threads | Zernio |
| X | Zernio |
| Reddit | Zernio |
| Snap | Zernio |
| LinkedIn | Zernio |
| YouTube | Zernio |
| Discord | Zernio |

## Zernio adapter

Three functions in `server.py` hold every Zernio API dependency:

- `_zernio_list_accounts(api_key)` -- `GET /accounts`. Returns the full account list for a pipeline.
- `_zernio_upload_media(api_key, media)` -- resolves each `MediaAsset` into a Zernio `mediaItems[]` entry. Uploads local paths via the Zernio SDK's `media.aupload_bytes`; passes URLs through unchanged. Handles primary media and thumbnails uniformly.
- `_zernio_publish_batch(api_key, content, platform_accounts, schedule_at, media_items)` -- `POST /posts` carrying the multi-platform array and the `mediaItems[]` array.

Base URL: `https://zernio.com/api/v1`. Auth: `Authorization: Bearer <key>`. Platform names map Pennyone canonical (`x`, `snap`) to Zernio's strings (`twitter`, `snapchat`) via `PLATFORM_TO_ZERNIO`.

Account resolution is automatic: `publish()` calls `_zernio_list_accounts` and picks the first active account per requested platform, unless the caller passes explicit `account_ids`.

## Media support

A publish request's `content.media` is a list of `MediaAsset` objects. Each asset carries:

| Field | Purpose |
|---|---|
| `url` | Public URL. Passed through unchanged; Zernio pulls it at post time. |
| `path` | Local file path. Read, uploaded via the Zernio SDK, converted to a public URL. |
| `kind` | `image`, `video`, `gif` or `document`. Defaults to `image`. |
| `title` | Optional title (used by LinkedIn PDF/carousel, YouTube, Pinterest). |
| `thumbnail_url` / `thumbnail_path` | Custom cover for Facebook video / Facebook Reels / regular video uploads. Max 10MB, JPG or PNG recommended. |
| `instagram_thumbnail_url` / `instagram_thumbnail_path` | Custom cover for Instagram Reels. |

Multi-media is supported -- pass multiple `MediaAsset` entries and every one appears as an entry in Zernio's `mediaItems[]`. Video thumbnails are resolved the same way as primary media (URL pass-through or path upload), then attached as `thumbnail` / `instagramThumbnail` on the corresponding item.

Instagram, TikTok, YouTube and Snap require media at Zernio's end -- text-only publishes to these platforms fail with a Zernio validation error. Threads, X and Reddit accept text-only content.

## Notion Content Calendar publisher

`publisher.py` is the mapping layer between a Notion Content Calendar and Pennyone. Pennyone stays pure; the publisher owns the Notion schema assumptions.

### Content Calendar contract

Each pipeline runs its own Notion workspace with its own Content Calendar. The calendar schema must include (at minimum):

| Property | Type | Purpose |
|---|---|---|
| `Name` | title | Editorial title for the entry |
| `Caption` | rich_text | Post text; becomes `content.text` |
| `Platform` | relation | Platforms to publish to (relation to a Platforms database) |
| `Publish Date` | date | If future, used as `schedule_at`; otherwise `publishNow` |
| `Type` | select | Informs default `MediaAsset.kind` (Short/Long Form Videography -> `video`) |
| `Status` | status | Editorial workflow. `Scheduled` = eligible. On success -> `Published` |
| `Media` | files | Images or videos. Publisher downloads Notion-hosted files to temp paths before dispatch |
| `Pennyone Log` | rich_text | Per-platform outcomes + any mapper warnings; Zernio post IDs appear inline in the `[success]` lines |

The Platforms database stores one row per platform with `Name` as the title. Row names map to Pennyone platforms via `PLATFORM_NAME_MAP` in `publisher.py` (`Instagram`, `TikTok`, `Threads`, `X`, `Reddit`, `Snapchat`).

### Pipeline -> Content Calendar registry

`PIPELINE_TO_CONTENT_CALENDAR` in `publisher.py` maps each pipeline to its Content Calendar data source ID. Add entries as each venture's workspace is provisioned.

### Two modes

**Library mode.** Import the pure mapping helpers:

```python
from publisher import build_request_from_notion, format_pennyone_log

request, warnings = build_request_from_notion(page_properties, platform_names, pipeline)
response = await server._publish_core(request)
log = format_pennyone_log(response, warnings)
```

Useful from Claude sessions that already have Notion access via the managed MCP. The Claude session queries Notion, feeds properties into the mapper, calls Pennyone, writes back.

**CLI mode.** Runs standalone (suitable for cron):

```bash
# Dispatch every eligible entry for the personal pipeline
python publisher.py --pipeline personal

# Dispatch a single page by ID
python publisher.py --pipeline personal --page-id <id>

# Map and preview without calling Zernio or writing back
python publisher.py --pipeline personal --dry-run
```

Requires a Notion integration token for the pipeline's workspace. Env var naming: `NOTION_PERSONAL_TOKEN`, `NOTION_FIVEPOINTS_TOKEN`, etc. The marty_gras pipeline was retired 2026-08-11 by operator ruling; Marty Gras publishes through the personal pipeline.

### Per-pipeline Notion integration setup

For each pipeline that runs the CLI:

1. Go to https://www.notion.so/profile/integrations (or the workspace-equivalent) and create an internal integration scoped to that workspace.
2. In the Content Calendar database's "Connections" menu, grant the integration read and update access. Do the same for the Platforms database.
3. Copy the integration's secret token.
4. Add to `~/Alfred Pennyworth/.env` with the env var naming from `PIPELINE_TO_NOTION_TOKEN_ENV` in `publisher.py`.

Note: the managed Notion MCP used inside Claude sessions is separate from the CLI's integration token. Library mode can use either -- the CLI must have the dedicated integration.

### Eligibility filter

An entry is eligible when `Status == "Scheduled"` and `Publish Date <= now`. After a successful dispatch (no partials or failures), the status moves to `Published` and the per-platform outcomes, including Zernio post IDs, land in `Pennyone Log`. Partial or failed dispatches leave the status at `Scheduled` and log the detail in `Pennyone Log` so the next run retries.

---

## References

- Zernio docs: https://docs.zernio.com
- Zernio Python SDK: https://pypi.org/project/zernio-sdk/
- Pennyone agent definition: `Agents/Orchestration/pennyone.md`
- Five Points integrations: `Context/Spheres/System/Entrepreneurship/Five Points Digital Studio/Agents/integrations.md`
- Marty Gras integrations: `Context/Spheres/System/Entrepreneurship/Marty Gras/Agents/integrations.md`

---

*Last updated: 2026-06-23 -- LinkedIn, YouTube and Discord added to the router; personal pipeline connected-account list refreshed.*
