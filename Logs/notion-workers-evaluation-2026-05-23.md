# Notion Workers Evaluation – Pennyone and Other Custom Code

**Date:** 2026-05-23
**Trigger:** Notion 3.5 Developer Platform launch (2026-05-13). Workers introduced as a hosted runtime for custom code, sandboxed, deployed via the Notion CLI. Free during beta; runs on Notion credits from 2026-08-11.
**Author:** Alfred (session execution).
**Decision owner:** Martavious.

---

## Question

For each piece of custom code currently running in the Alfred ecosystem, should it migrate to a Notion Worker?

## Framework

A Worker is the right home when ALL three are true:

1. **The primary consumer is Notion** – the code is called by a Notion Custom Agent, an Automation, an AI Autofill, a database button, or a webhook-triggered workflow inside the workspace.
2. **The data primarily lives in Notion** – inputs and outputs are Notion pages/properties, or the code's purpose is to enrich Notion records.
3. **The code does not need long-running local resources** – no persistent OS-level state, no large local files, no machine-specific credentials that cannot be passed through.

If the primary consumer is Claude Code, the data lives outside Notion, or the code needs a long-running local process, FastMCP at `~/Alfred Pennyworth/Integrations/` remains the right home.

---

## Per-integration verdict

### 1. Pennyone – `Integrations/pennyone/`
- **What it does.** Social syndication across Instagram, TikTok, Threads, X, Reddit, Snap. Wraps the Zernio SDK. Multi-pipeline routing (personal vs. Five Points).
- **Primary consumer.** Claude Code, via MCP. Also called from the Notion Content Calendar publisher pattern.
- **Data location.** Zernio is the source of truth for posts; Notion Content Calendar holds the editorial plan.
- **Verdict.** **Stay on FastMCP.** Pennyone is a cross-venture syndication router whose Zernio dependency lives outside Notion. A Worker could expose a Notion-callable wrapper for the Content Calendar publisher, but that is a thin layer worth building only if Notion-native publishing becomes the preferred surface.

### 2. Instantly – `Integrations/instantly/`
- **What it does.** Five Points outbound lead pipeline reads + gated writes.
- **Primary consumer.** Claude Code, via MCP.
- **Data location.** Instantly platform. Five Points Notion CRM downstream.
- **Verdict.** **Stay on FastMCP.** No Notion-native consumer planned.

### 3. Strava – `Integrations/strava/`
- **What it does.** Activity reads and `sync_activity_to_notion` writes into Fitness Journal.
- **Primary consumer.** Claude Code today. Personal trainer skill.
- **Data location.** Strava and Notion Fitness Journal.
- **Verdict.** **Stay on FastMCP for now**, with a follow-up note: if a Notion Custom Agent ("Sensei") needs to pull or push from inside the workspace, the sync function is a clean Worker candidate. The Notion side is already the destination; only the trigger source differs.

### 4. Five Points Mail – `Integrations/fivepoints-mail/`
- **What it does.** Gmail surface across five Five Points inboxes via Google Workspace domain-wide delegation.
- **Primary consumer.** Claude Code, via MCP.
- **Data location.** Gmail. Five Points Notion downstream for CRM linkage.
- **Verdict.** **Stay on FastMCP.** Auth model relies on a Google service-account JSON loaded from the local `.env`; that does not move into a sandboxed Worker without re-architecting credentials.

### 5. Discord Setup – `Integrations/discord-setup-mcp/`
- **What it does.** Discord server scaffolding via Bot API.
- **Primary consumer.** Claude Code, via MCP, for one-off server builds.
- **Data location.** Discord platform.
- **Verdict.** **Stay on FastMCP.** No Notion involvement.

### 6. Fullscript – `Integrations/fullscript-mcp/`
- **What it does.** Supplement research and personal wellness protocols.
- **Primary consumer.** Claude Code, via MCP.
- **Data location.** Fullscript catalogue and personal protocols.
- **Verdict.** **Stay on FastMCP.** No Notion involvement.

---

## Workers candidates for future build

These do not exist as code yet. They are written here as a list of patterns a Worker would serve well, if and when the need surfaces:

- **Weekly Review data pull.** A Worker callable from the Custom Agent that fires on the Sunday 21:00 trigger. Reads Habits, Fitness Journal, Currently Reading, Contact reach-outs, Reflections-this-week. Pre-populates the new Weekly Review entry's Movement 3 numbers and Movement 4 reflection prompts. This is Notion-native work, Notion-triggered, with Notion as the only data surface.
- **Decision Log weekly digest.** A Worker that reads the past seven days of Decision Log entries and writes a digest page under the Alfred operating system Project. Triggered by the same Sunday 21:00 agent or on demand.
- **Sphere Manager rollup refresher.** A Worker that walks each sphere and tallies open Tasks, recent Reflections and Achievements per sphere, writing a "Sphere pulse" property back.
- **Strava-to-Fitness-Journal Notion-native sync.** If a Notion Custom Agent ("Sensei") needs to pull a Strava activity directly from inside the workspace rather than via Claude Code, a Worker is the right shape.

## Decision

**Defer Workers adoption ecosystem-wide.** No existing FastMCP integration meets all three criteria. Re-evaluate on either of two triggers:

1. **2026-08-11** – beta-to-paid transition, when Workers usage starts consuming Notion credits. Until then, free experimentation is the only cost of trying one.
2. **A specific Notion-internal automation need** that the current FastMCP + Claude Code path cannot serve. The most likely first such need is the Weekly Review trigger's pre-population work, which is also a V7/V8 deliverable.

## Sources

- [Notion 3.5: Notion Developer Platform – 2026-05-13](https://www.notion.com/releases/2026-05-13)
- [Notion Workers: Dev Day 2026 Complete Guide](https://matthiasfrank.de/en/notion-workers-dev-day-2026/)
- [Notion just turned its workspace into a hub for AI agents – TechCrunch](https://techcrunch.com/2026/05/13/notion-just-turned-its-workspace-into-a-hub-for-ai-agents/)
