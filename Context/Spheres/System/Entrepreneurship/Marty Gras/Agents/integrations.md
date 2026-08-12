---
file_type: integration_registry
department: Agents
venture: Marty Gras
status: active
last_updated: 2026-08-08
---

<!-- Updated 2026-08-08 (The Junction): every row live-verified. ElevenLabs confirmed halting, the marty_gras Pennyone pipeline recorded as an unresolved contradiction, the personal-workspace exception restated against the one-workspace-per-venture ruling. -->

# Integrations

Plugin and tool connections scoped to Marty Gras. These are the external systems Alfred can operate within when working in Marty Gras context.

---

## Plugin Routing Principle

Marty Gras runs on personal credentials by design, not by default. It is the personal media identity – the venture and the person are the same audience – and the 2026-08-08 one-workspace-per-venture ruling names it the single standing exception. Where every other sovereign venture provisions its own Notion workspace, Marty Gras state routes to the personal workspace, permanently and by ruling rather than by deferral.

The exception covers state and syndication. It does not cover money: if Marty Gras ever takes payment directly, that rail is venture-scoped like any other, since no personal Stripe exists in the ecosystem.

---

## The unresolved contradiction

Two records disagree and neither has been retired.

- **The 2026-07-23 operator ruling**, recorded in `Manual/secrets-inventory.md`, states that Marty Gras routes through the personal Zernio pipeline and that no separate account is planned. `ZERNIO_MARTYGRAS_API_KEY` is marked "not needed".
- **`Integrations/pennyone/`** still registers a `marty_gras` pipeline in the `Pipeline` enum, advertises it through `list_pipelines` with the voice "architect of vibe", and demands `ZERNIO_MARTYGRAS_API_KEY`. `health_check` returns `no_key`, verified 2026-08-08.

Either the pipeline is retired from the router or the ruling is reversed. Left as it stands, `health_check` reports a permanent failure for a pipeline that is not meant to exist, which trains the eye to ignore a red status – the most expensive kind of small mess.

This file does not pick a side. The ruling is the operator's to make.

---

---

## Active Plugins

Marty Gras does not yet own dedicated venture-scoped MCP connections. The table below captures the routing that applies while operations fall through to personal defaults.

| Service | Routing | MCP package | Status, verified 2026-08-08 | Environment variable | Notes |
|---|---|---|---|---|---|
| Notion | Personal workspace | Managed (enhanced) | **DARK** – the enhanced connector does not appear in the session tool surface at all. Consistent with the personal Notion token being down since 12 July 2026. | n/a (managed) | Content calendar, media database, Sphere Manager. Marty Gras has no writable state surface while this is down. |
| ElevenLabs | Personal | `elevenlabs-mcp` (uvx, server name `elevenlabs`) | **DARK** – registered in `.mcp.json` but not one tool surfaces, meaning the server halts on the missing key at launch | `ELEVENLABS_API_KEY` | Voice production for the Conversation and audio work. Registered at project scope 2026-07-10; connects automatically once the operator mints a key at elevenlabs.io/app/settings/api-keys and adds the line to `.env`. Generated audio routes to `.working/elevenlabs/`. The podcast voice lane has been dark since the registration. |
| Vercel | Personal account | `@vercel/mcp@latest` | **Live** – `list_teams` returns team `lavender-stingray`, "Headquarters" | n/a – desktop connector, no local env var | Hosting for any Marty Gras web properties. This is the personal Vercel account and it is the correct one for Marty Gras under the personal-identity exception. |
| Supabase | Personal management token | `@supabase/mcp-server-supabase@latest` | Registered – desktop connector present, not exercised this pass | `SUPABASE_PERSONAL_TOKEN` | Backend for any Marty Gras web properties |
| Pennyone | Personal pipeline per the 2026-07-23 ruling | Custom FastMCP at `Integrations/pennyone/` | **Live via `personal`** – `health_check` returns `ok`, seven connected accounts across Discord, Instagram, LinkedIn, Reddit, Threads, TikTok and YouTube | `ZERNIO_PERSONAL_API_KEY` | This is the working syndication path for Marty Gras today. See the contradiction section above regarding the orphaned `marty_gras` pipeline. |

---

## Target-State Plugins

Plugins Marty Gras needs once the pipeline is live.

### Pennyone – Social syndication

| Field | Value |
|---|---|
| Account | Zernio (Marty Gras, to be provisioned) |
| Scope | Social syndication across Instagram, TikTok, Threads, X, Reddit and Snap for Marty Gras handles |
| Pipeline value | `marty_gras` |
| MCP server name | `pennyone` (cross-venture router) |
| MCP package | Custom Python/FastMCP server at `Integrations/pennyone/` |
| Status | **Orphaned. Verified 2026-08-08 – `health_check` returns `no_key`.** Superseded by the 2026-07-23 ruling that Marty Gras routes through the personal pipeline. The pipeline remains in the router code and should be retired or reinstated by ruling; see the contradiction section above. |
| Environment variable | `ZERNIO_MARTYGRAS_API_KEY` – marked "not needed" in the secrets inventory |
| Routing rule | **Superseded.** Marty Gras dispatches pass `pipeline: "personal"` under the current ruling. Were the ruling reversed, dispatches would pass `pipeline: "marty_gras"` and route under a dedicated Marty Gras Zernio account. Pennyone itself is cross-venture; only the Zernio account is venture-scoped. Buffer is deprecated. |

### Substack, audio host

| Service | Status | Notes |
|---|---|---|
| Substack | No MCP exists | Epiphany publishing handled manually until an official integration appears |
| Audio host | Not selected | Audio distribution host for the Conversation, to be chosen during the launch sequence |

---

## Deprecated Plugins

| Plugin | Status | Replacement | Reason |
|---|---|---|---|
| Buffer | **Deprecated ecosystem-wide (April 2026)** | Pennyone | Pennyone routes to Zernio. Buffer subscription to be cancelled. |

---

## Tool-Only – No MCP Connection

These tools are used by Marty Gras but are not connected to Alfred via MCP.

| Tool | Purpose | Notes |
|---|---|---|
| Substack | Epiphany publishing | Manual publishing. |
| Audio platforms | Distribution for the Conversation | Managed manually. |
| Adobe Creative Suite | Design and video production | Shared with Five Points subscription |

---

## Adding a New Plugin

When a new MCP connection is added for Marty Gras:

1. Add the API key to `~/Alfred Pennyworth/.env` using a descriptive variable name following the pattern `SERVICE_MARTYGRAS_TOKEN` (or a domain-specific suffix where the service has its own canonical terminology)
2. Add the server config to `.mcp.json` referencing the env var via `${VARIABLE_NAME}`
3. Register it in this file with: plugin name, account scope, MCP server name, MCP package, status, environment variable, which skills use it, routing rules
4. Update any skills that should have access via their `allowed-tools` list
5. If the same service exists at the personal level, document the routing rule that distinguishes them
6. Update the project CLAUDE.md Plugin Routing section if the new connection introduces a routing pattern not yet documented
