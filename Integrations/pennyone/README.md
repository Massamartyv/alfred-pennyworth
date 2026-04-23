# Pennyone

Content syndication router. Thin MCP layer over Zernio. Fans out a single publish request to Instagram, TikTok, Threads, X, Reddit and Snap under the pipeline's own Zernio account.

Pennyone does not write the content. It does not decide when to publish. It takes an existing publish request and executes the fan-out.

## Architecture

Pennyone is a thin FastMCP server that wraps Zernio, a unified social media API covering 14+ platforms. Pennyone uses six of them.

```
Alfred --> Pennyone (FastMCP) --> Zernio (per-pipeline account) --> 6 platforms
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
| `marty_gras` | Marty Gras | `ZERNIO_MARTYGRAS_API_KEY` | Future |
| `five_points` | Five Points Digital Studio | `ZERNIO_FIVEPOINTS_API_KEY` | Provisioning |
| `paradigm` | Paradigm | `ZERNIO_PARADIGM_API_KEY` | Future |
| `lillie_and_lynette` | Lillie and Lynette | `ZERNIO_LILLIEANDLYNETTE_API_KEY` | Future |

A pipeline without a configured key returns a clean "pipeline not provisioned" error for every platform in the request. No Zernio call is made.

## Status

**Live** for the personal and Five Points pipelines. Keys provisioned 2026-04-23; adapter verified against Zernio's real API shape. MCP registration in local `.mcp.json`.

Connected accounts as of go-live:

| Pipeline | Connected |
|---|---|
| personal | Instagram, Threads, TikTok (`massamartyv`) |
| five_points | Instagram (`studio.fivepoints`) |

Remaining platforms per pipeline (X, Reddit, Snap on both; TikTok and Threads on Five Points) connect through Zernio's dashboard; Pennyone picks them up automatically.

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
    "ZERNIO_MARTYGRAS_API_KEY": "${ZERNIO_MARTYGRAS_API_KEY}",
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

All six platforms route through Zernio regardless of pipeline.

| Platform | Via |
|---|---|
| Instagram | Zernio |
| TikTok | Zernio |
| Threads | Zernio |
| X | Zernio |
| Reddit | Zernio |
| Snap | Zernio |

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

## References

- Zernio docs: https://docs.zernio.com
- Zernio Python SDK: https://pypi.org/project/zernio-sdk/
- Pennyone agent definition: `Agents/Orchestration/pennyone.md`
- Five Points integrations: `Context/Spheres/System/Entrepreneurship/Five Points Digital Studio/Agents/integrations.md`
- Marty Gras integrations: `Context/Spheres/System/Entrepreneurship/Marty Gras/Agents/integrations.md`

---

*Last updated: 2026-04-23*
