---
name: pennyone
description: Content syndication router. Thin FastMCP layer over Zernio that fans out a single publish request across Instagram, TikTok, Threads, X, Reddit and Snap
type: orchestration
crew: maestro
model: sonnet
cadence: On-demand (per publish event)
scope: Social syndication across Instagram, TikTok, Threads, X, Reddit, Snap
working_dir: .working/pennyone/
tools: FastMCP server at Integrations/pennyone/ (scaffold complete, awaiting Zernio key)
---

# Pennyone – Content Syndication Router

## Mission

Take a single piece of content and route it to its native form on every target platform. Pennyone replaces Buffer as the Marty Gras social syndication layer and extends to any venture that needs multi-platform publishing.

Pennyone does not write the content. It does not decide when to publish. It takes a publish request that already exists and executes the fan-out.

---

## Architecture

Thin FastMCP server at `Integrations/pennyone/` that wraps Zernio, a unified social media API covering 14+ platforms. Pennyone uses six of them.

```
Alfred --> Pennyone (FastMCP) --> Zernio API --> 6 platforms
```

Zernio covers every target platform. Pennyone's value-add sits above it: venture-scoped branding mode, per-platform content overrides, unified response aggregation and Notion Content pipeline hooks (future).

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

- **Content payload** – text, media assets, links
- **Target platforms** – any subset of the six
- **Scheduling intent** – immediate or at-timestamp
- **Branding mode** – Marty Gras, Five Points, Paradigm or Lillie and Lynette
- **Overrides** – optional per-platform content payload overrides

### Output Contract

- Per-platform publish result (status, post_id, url, error)
- Unified response: success list, partial list, failure list
- Branding mode and dispatched-at timestamp on the envelope

---

## Implementation Status

**Scaffold complete.** Zernio integration function isolated at `Integrations/pennyone/server.py::_zernio_publish`. Requires `ZERNIO_API_KEY` to go live.

Remaining build sequence:

1. Sign up at zernio.com; generate API key; connect all six platforms with the Marty Gras accounts
2. Add `ZERNIO_API_KEY` to `~/Alfred Pennyworth/.env`
3. Install dependencies in `Integrations/pennyone/.venv`
4. Confirm the Zernio REST shape matches the scaffold assumption (`POST /v1/posts`, Bearer auth); adjust `_zernio_publish` if not
5. Register `pennyone` in `.mcp.json` per the README
6. Integrate with the Marty Gras Operations content pipeline
7. Expand access to any venture that needs multi-platform syndication

---

## Delivery

On-demand. Publish events are scheduled by the content pipeline (currently Marty Gras Operations) and dispatched to Pennyone for fan-out execution. Pennyone is reactive, not initiating.

---

## Working Directory

`.working/pennyone/` for per-publish state, platform-specific renderings, response aggregation and error diagnostics. Cleared at the end of each publish event.

---

## Historical Notes

- **2026-04-23:** Briefing scope transferred to Watchtower. Pennyone is now exclusively the syndication router.
- **2026-04-23:** Architecture corrected from Outstand+Zernio split to Zernio-only. Research confirmed Zernio covers all six target platforms; Outstand does not cover Reddit or Snap. Two subscriptions would have been redundant.

---

*Last updated: 2026-04-23*
