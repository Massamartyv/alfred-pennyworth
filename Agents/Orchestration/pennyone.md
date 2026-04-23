---
name: pennyone
description: Content syndication router. Publishes a single piece of content to multiple social platforms via Outstand and Zernio
type: orchestration
crew: maestro
model: sonnet
cadence: On-demand (per publish event)
scope: Social syndication across Instagram, TikTok, Threads, X, Reddit, Snap
working_dir: .working/pennyone/
tools: TBD – FastMCP server with platform integrations
---

# Pennyone – Content Syndication Router

## Mission

Take a single piece of content and route it to its native form on every target platform. Instagram, TikTok, Threads and X via Outstand. Reddit and Snap via Zernio. Pennyone replaces Buffer as the Marty Gras social syndication layer and extends to any venture that needs multi-platform publishing.

Pennyone does not write the content. It does not decide when to publish. It takes a publish request that already exists and executes the fan-out.

---

## Architecture

Python/FastMCP server running locally. Registers with the MCP ecosystem so Alfred can dispatch publish requests through it. Each platform has a dedicated adapter; Pennyone coordinates routing, per-platform formatting and error aggregation.

### Platform Routing

| Platform | Via | Format Focus |
|---|---|---|
| Instagram | Outstand | Visual-first (reels, carousels, stories) |
| TikTok | Outstand | Short-form video with captions |
| Threads | Outstand | Text-first, compressed |
| X | Outstand | Text-first. Threads handled as multi-post sequences |
| Reddit | Zernio | Community-targeted, markdown-native |
| Snap | Zernio | Visual-first, ephemeral |

### Input Contract

A publish request contains:

- **Content payload** – text, media assets, links
- **Target platforms** – any subset of the six
- **Scheduling intent** – immediate, at timestamp, or per-platform best-time
- **Branding mode** – Marty Gras, Five Points, or other active venture voice

### Output Contract

- Per-platform publish confirmation or error
- Unified response to the caller: success map, partial-success map, failure map
- Links to the published content on each platform where available

---

## Implementation Status

**Target state. Not yet built.** Replaces Buffer which is deprecated ecosystem-wide as of April 2026.

Build sequence:

1. Scaffold FastMCP server skeleton at `Integrations/pennyone/` (or similar)
2. Implement Outstand integration covering Instagram, TikTok, Threads and X
3. Implement Zernio integration covering Reddit and Snap
4. Register as an MCP server in `.mcp.json`
5. Integrate with the Marty Gras Operations content pipeline
6. Expand access to any venture that needs multi-platform syndication

---

## Delivery

On-demand. Publish events are scheduled by the content pipeline (currently Marty Gras Operations) and dispatched to Pennyone for fan-out execution. Pennyone is reactive, not initiating.

---

## Working Directory

`.working/pennyone/` for per-publish state, platform-specific renderings, response aggregation and error diagnostics. Cleared at the end of each publish event.

---

## Historical Note

Pennyone briefly claimed a second scope as a portfolio briefing agent (weekly briefing generated every Monday, aggregating intelligence across ventures). That briefing responsibility has been transferred to Watchtower as part of the 2026-04-23 architectural reconciliation. Pennyone is now exclusively the syndication router per the Marty OS final document.

---

*Last updated: 2026-04-23*
