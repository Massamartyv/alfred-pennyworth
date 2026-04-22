---
file_type: integration_registry
department: Agents
venture: Marty Gras
status: active
last_updated: 2026-04-22
---

# Integrations

Plugin and tool connections scoped to Marty Gras. These are the external systems Alfred can operate within when working in Marty Gras context.

---

## Plugin Routing Principle

Marty Gras currently operates mostly on personal MCP defaults. Venture-scoped connections will be added as the content pipeline stands up. Until then, personal credentials handle audience-adjacent work. Data never crosses between personal and business plugins.

---

## Active Plugins

Marty Gras does not yet own dedicated venture-scoped MCP connections. The table below captures the routing that applies while operations fall through to personal defaults.

| Service | Routing | MCP package | Status | Environment variable | Notes |
|---|---|---|---|---|---|
| Notion | Personal workspace | Managed (enhanced) | Live | n/a (managed) | Content calendar, media database, Sphere Manager |
| ElevenLabs | Personal | n/a – MCP broken | Needs fix | n/a | Voice production for podcast and audio content. MCP key currently broken – manual fix required. |
| Vercel | Personal account | `@vercel/mcp@latest` | Live | `VERCEL_PERSONAL` (personal slot) | Hosting for any Marty Gras web properties |
| Supabase | Personal management token | `@supabase/mcp-server-supabase@latest` | Live | `SUPABASE_PERSONAL_TOKEN` | Backend for any Marty Gras web properties |

---

## Target-State Plugins

Plugins Marty Gras needs once the pipeline is live.

### Pennyone – Social syndication

| Field | Value |
|---|---|
| Account | Marty Gras (future) |
| Scope | Social syndication across Instagram, TikTok, Threads, X (via Outstand) and Reddit, Snap (via Zernio) |
| MCP server name | `pennyone` (target) |
| MCP package | Custom Python/FastMCP server |
| Status | **Target state.** Replaces Buffer ecosystem-wide per April 2026 decision. To be stood up as part of the Pennyone build. |
| Environment variable | To be defined |
| Routing rule | Pennyone is the content syndication layer for the Marty Gras platform. Buffer is deprecated. |

### Substack, Podcast host

| Service | Status | Notes |
|---|---|---|
| Substack | No MCP exists | Newsletter publishing handled manually until an official integration appears |
| Podcast host | Not selected | Audio distribution host to be chosen during the launch sequence |

---

## Deprecated Plugins

| Plugin | Status | Replacement | Reason |
|---|---|---|---|
| Buffer | **Deprecated ecosystem-wide (April 2026)** | Pennyone | Per Marty OS final document – Pennyone routes to Outstand and Zernio. Buffer subscription to be cancelled. |

---

## Tool-Only – No MCP Connection

These tools are used by Marty Gras but are not connected to Alfred via MCP.

| Tool | Purpose | Notes |
|---|---|---|
| Substack | Newsletter publishing (Epiphany) | Manual publishing. |
| Podcast platforms | Distribution for Marty Gras podcast | Managed manually. |
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
