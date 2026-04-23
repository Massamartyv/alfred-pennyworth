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
| `personal` | Personal | `ZERNIO_PERSONAL_API_KEY` | Provisioning |
| `marty_gras` | Marty Gras | `ZERNIO_MARTYGRAS_API_KEY` | Future |
| `five_points` | Five Points Digital Studio | `ZERNIO_FIVEPOINTS_API_KEY` | Provisioning |
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

**Scaffold complete. Multi-pipeline routing wired.** Zernio integration function isolated at `Integrations/pennyone/server.py::_zernio_publish`. Requires at least one pipeline's API key to go live.

Remaining build sequence:

1. Sign up at zernio.com per pipeline that needs its own account (personal and Five Points first)
2. Connect Instagram, TikTok, Threads, X, Reddit and Snap within each Zernio account with that pipeline's handles
3. Add each pipeline's API key to `~/Alfred Pennyworth/.env`
4. Install dependencies in `Integrations/pennyone/.venv`
5. Confirm the Zernio REST shape matches the scaffold assumption (`POST /v1/posts`, Bearer auth); adjust `_zernio_publish` if not
6. Register `pennyone` in `.mcp.json` per the README with every pipeline's env var listed
7. Wire each venture's content pipeline to dispatch through Pennyone with its pipeline value

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
- **2026-04-23:** Multi-pipeline routing wired. The branding-mode label became a hard routing key. Each pipeline owns its own Zernio account and API key. Starting pipelines: personal and Five Points.

---

*Last updated: 2026-04-23*
