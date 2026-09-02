---
file_type: integration_registry
department: Agents
venture: Marty Gras
status: active
last_updated: 2026-08-11
---

<!-- Updated 2026-08-11 (Domesday walk): the marty_gras pipeline contradiction resolved by operator ruling - pipeline retired from the router; Notion row corrected to the live notion-personal server. Prior pass 2026-08-08 (The Junction). -->

# Integrations

Plugin and tool connections scoped to Marty Gras. These are the external systems Alfred can operate within when working in Marty Gras context.

---

## Plugin Routing Principle

Marty Gras runs on personal credentials by design, not by default. It is the personal media identity – the venture and the person are the same audience – and the 2026-08-08 one-workspace-per-venture ruling names it the single standing exception. Where every other sovereign venture provisions its own Notion workspace, Marty Gras state routes to the personal workspace, permanently and by ruling rather than by deferral.

The exception covers state and syndication. It does not cover money: if Marty Gras ever takes payment directly, that rail is venture-scoped like any other, since no personal Stripe exists in the ecosystem.

---

## The contradiction, resolved

Ruled 2026-08-11 during the Domesday walk: the `marty_gras` pipeline was retired from the Pennyone router, executing the 2026-07-23 decision. The `Pipeline` enum, registry, publisher maps and README no longer carry it; `ZERNIO_MARTYGRAS_API_KEY` is marked retired in the secrets inventory and will never exist. Marty Gras publishes through `pipeline: "personal"`, permanently. The false red is gone from `health_check`.

---

## Active Plugins

Marty Gras does not yet own dedicated venture-scoped MCP connections. The table below captures the routing that applies while operations fall through to personal defaults.

| Service | Routing | MCP package | Status, verified 2026-08-08 | Environment variable | Notes |
|---|---|---|---|---|---|
| Notion | Personal workspace | `@notionhq/notion-mcp-server` (npx, server name `notion-personal`) | **Live, verified 2026-08-11** – the project-scoped token server is the working route; the retired OAuth enhanced connector stays dark and superseded | `NOTION_PERSONAL_TOKEN` | Content calendar, media database, Sphere Manager. The writable state surface is back. |
| ElevenLabs | Personal | `elevenlabs-mcp` (uvx, server name `elevenlabs`) | **DARK** – registered in `.mcp.json` but not one tool surfaces, meaning the server halts on the missing key at launch | `ELEVENLABS_API_KEY` | Voice production for the Conversation and audio work. Registered at project scope 2026-07-10; connects automatically once the operator mints a key at elevenlabs.io/app/settings/api-keys and adds the line to `.env`. Generated audio routes to `.working/elevenlabs/`. The podcast voice lane has been dark since the registration. |
| Vercel | Personal account | `@vercel/mcp@latest` | **Live** – `list_teams` returns team `lavender-stingray`, "Headquarters" | n/a – desktop connector, no local env var | Hosting for any Marty Gras web properties. This is the personal Vercel account and it is the correct one for Marty Gras under the personal-identity exception. |
| Supabase | Personal management token | `@supabase/mcp-server-supabase@latest` | Registered – desktop connector present, not exercised this pass | `SUPABASE_PERSONAL_TOKEN` | Backend for any Marty Gras web properties |
| Pennyone | Personal pipeline per the 2026-07-23 ruling | Custom FastMCP at `Integrations/pennyone/` | **Live via `personal`** – `health_check` returns `ok`, seven connected accounts across Discord, Instagram, LinkedIn, Reddit, Threads, TikTok and YouTube | `ZERNIO_PERSONAL_API_KEY` | The working and permanent syndication path for Marty Gras; the orphaned `marty_gras` pipeline was retired 2026-08-11. |

---

## Target-State Plugins

Plugins Marty Gras needs once each lane goes live. The dedicated Pennyone pipeline is no longer among them – retired 2026-08-11; syndication is permanently the personal pipeline.

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
