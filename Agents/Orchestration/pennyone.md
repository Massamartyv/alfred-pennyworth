---
name: pennyone
description: Content syndication router. Thin FastMCP layer over Zernio. Fans out a single publish request across Instagram, TikTok, Threads, X, Reddit and Snap under the requesting pipeline's own Zernio account
type: orchestration
crew: maestro
model: sonnet
cadence: On-demand (per publish event)
scope: Cross-portfolio social syndication. Pipelines today: personal, marty_gras, five_points, paradigm, lillie_and_lynette
working_dir: .working/pennyone/
tools: FastMCP server at Integrations/pennyone/ (scaffold complete, multi-pipeline routing wired)
---

# Pennyone – Content Syndication Router

## Mission

Take a single piece of content and route it to its native form on every target platform, under the Zernio account that belongs to the requesting pipeline. Pennyone replaces Buffer as the syndication layer for every venture that ships content and extends to any venture that comes online later.

Pennyone does not write the content. It does not decide when to publish. It takes a publish request that already exists and executes the fan-out under the right account.

---

## Architecture

Thin FastMCP server at `Integrations/pennyone/` that wraps Zernio, a unified social media API covering 14+ platforms. Pennyone uses six of them.

```
Alfred --> Pennyone (FastMCP) --> Zernio (per-pipeline account) --> 6 platforms
```

The pipeline field on every publish request is the **routing key**. Each pipeline is isolated – it has its own Zernio account, its own connected social handles and its own API key. Personal content cannot accidentally publish on venture accounts. Venture A content cannot cross into Venture B.

### Pipelines

| Pipeline | Label | Env var | Status |
|---|---|---|---|
| `personal` | Personal | `ZERNIO_PERSONAL_API_KEY` | Live |
| `marty_gras` | Marty Gras | `ZERNIO_MARTYGRAS_API_KEY` | Future |
| `five_points` | Five Points Digital Studio | `ZERNIO_FIVEPOINTS_API_KEY` | Live |
| `paradigm` | Paradigm | `ZERNIO_PARADIGM_API_KEY` | Future |
| `lillie_and_lynette` | Lillie and Lynette | `ZERNIO_LILLIEANDLYNETTE_API_KEY` | Future |

A pipeline without a configured key returns a clean "pipeline not provisioned" error for every platform in the request. No Zernio call is made.

### Platform Routing

| Platform | Via | Format Focus |
|---|---|---|
| Instagram | Zernio | Visual-first (reels, carousels, stories) |
| TikTok | Zernio | Short-form video with captions |
| Threads | Zernio | Text-first, compressed |
| X | Zernio | Text-first. Threads handled as multi-post sequences |
| Reddit | Zernio | Community-targeted, markdown-native |
| Snap | Zernio | Visual-first, ephemeral |

### Input Contract

A publish request contains:

- **Pipeline** – the routing key. Required.
- **Content payload** – text, media assets, links
- **Target platforms** – any subset of the six
- **Scheduling intent** – immediate or at-timestamp
- **Overrides** – optional per-platform content payload overrides

### Output Contract

- Per-platform publish result (status, post_id, url, error)
- Unified response: success list, partial list, failure list
- Pipeline echo and dispatched-at timestamp on the envelope

---

## Implementation Status

**Live** for the personal and Five Points pipelines (2026-04-23). Zernio accounts provisioned; adapter verified against Zernio's real API shape (`https://zernio.com/api/v1`, Bearer auth, single multi-platform `POST /posts`). MCP registration in local `.mcp.json`.

**Connected accounts at go-live:**

| Pipeline | Connected |
|---|---|
| personal | Instagram, Threads, TikTok (`massamartyv`) |
| five_points | Instagram (`studio.fivepoints`) |

**Remaining work:**

1. Connect remaining platforms (X, Reddit, Snap on both pipelines; TikTok and Threads on Five Points) through the Zernio dashboard. Pennyone picks them up automatically on the next `publish` call.
2. Provision Marty Gras, Paradigm and Lillie and Lynette Zernio accounts as each venture's content pipeline comes online.
3. Wire each venture's content pipeline to dispatch through Pennyone with its pipeline value.
4. Wire any bespoke per-platform fields (TikTok privacy levels, YouTube tags, LinkedIn carousel ordering) as use cases surface. The core media path covers image/video/gif/document, multi-media and Meta/Instagram Reels thumbnails.

---

## Delivery

On-demand. Publish events are scheduled by each venture's content pipeline and dispatched to Pennyone with the correct pipeline value for fan-out under that venture's Zernio account. Pennyone is reactive, not initiating.

---

## Working Directory

`.working/pennyone/` for per-publish state, platform-specific renderings, response aggregation and error diagnostics. Cleared at the end of each publish event.

---

## Historical Notes

- **2026-04-23:** Briefing scope transferred to Watchtower. Pennyone is now exclusively the syndication router.
- **2026-04-23:** Architecture corrected from Outstand+Zernio split to Zernio-only. Research confirmed Zernio covers all six target platforms; Outstand does not cover Reddit or Snap.
- **2026-04-23:** Multi-pipeline routing wired. The branding-mode label became a hard routing key. Each pipeline owns its own Zernio account and API key.
- **2026-04-23:** Personal and Five Points pipelines live. Adapter rewritten against Zernio's verified API shape. MCP registered locally. Four accounts connected total (Instagram + Threads + TikTok on personal; Instagram on Five Points).
- **2026-04-23:** Media upload wired. `MediaAsset` with a `path` reads the file and uploads via the Zernio SDK; `MediaAsset` with a `url` passes through. Initial wiring attached a single URL as `imageUrl`.
- **2026-04-23:** Media corrected and extended. Posts endpoint actually uses `mediaItems[]` (not `imageUrl`), which natively supports multi-media plus typed assets plus per-item `thumbnail` and `instagramThumbnail`. `MediaAsset` now carries `kind`, `title`, `thumbnail_url`/`thumbnail_path`, `instagram_thumbnail_url`/`instagram_thumbnail_path`. Every entry uploads and emits correctly.

---

*Last updated: 2026-04-23*
