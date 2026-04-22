---
file_type: integration_registry
department: Agents
venture: Marty Gras
status: active
last_updated: 2026-04-08
---

# Integrations

Plugin and tool connections scoped to Marty Gras. These are the external systems Alfred can operate within when working in Marty Gras context.

---

## Plugin Routing Principle

Marty Gras currently operates on personal MCP defaults. It does not own venture-scoped plugin connections. All plugin operations in Marty Gras context target the personal workspace and personal accounts unless a dedicated connection is added below.

Data never crosses between personal and business plugins. This is the same boundary established in the global CLAUDE.md Navigation Rules, extended to the plugin layer.

---

## Active Plugins

No dedicated venture-scoped MCP connections. All operations fall through to personal defaults:

| Service | Routing | Notes |
|---|---|---|
| Notion | Personal workspace | Content calendar, media database, sphere manager |
| Buffer | Personal account | Social scheduling across Instagram, LinkedIn, TikTok, YouTube, Substack, Threads |
| ElevenLabs | Personal account | Voice production for podcast and audio content. MCP key currently broken – manual fix required. |
| Vercel | Personal account | Hosting for any Marty Gras web properties |
| Supabase | Personal account | Backend for any Marty Gras web properties |

---

## Dormant Plugins

None.

---

## Tool-Only – No MCP Connection

These tools are used by Marty Gras but are not connected to Alfred via MCP. Alfred can reference them but cannot operate within them directly.

| Tool | Purpose | Notes |
|---|---|---|
| Substack | Newsletter publishing (Epiphany) | Manual publishing. Potential future MCP connection. |
| Podcast platforms | Distribution for Marty Gras podcast | Managed manually. |
| Adobe Creative Suite | Design and video production | Shared with Five Points subscription |

---

## Adding a New Plugin

When a new MCP connection is added for Marty Gras:

1. Register it in this file with: plugin name, account scope, MCP tool prefix, which skills use it, routing rules
2. Update any skills that should have access via their `allowed-tools` list
3. If the same service exists at the personal level, document the routing rule that distinguishes them
4. Update the project CLAUDE.md Plugin Routing section if the new connection introduces a routing pattern not yet documented
