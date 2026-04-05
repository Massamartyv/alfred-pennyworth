---
file_type: integration_registry
department: Operations/AI
venture: Five Points Digital Studio
status: active
last_updated: 2026-04-01
---

# Integrations

Plugin and tool connections scoped to Five Points Digital Studio. These are the external systems Alfred can operate within when working in Five Points context.

---

## Plugin Routing Principle

Five Points owns its plugins. When Alfred is operating in Five Points context -- clients, offers, business operations, venture strategy -- all plugin operations target the Five Points accounts. When no business context is active, Alfred defaults to the personal workspace and personal accounts.

Data never crosses between personal and business plugins. This is the same boundary established in the global CLAUDE.md Navigation Rules, extended to the plugin layer.

---

## Active Plugins

Plugins are MCP connections. Alfred can read, write and operate within these systems directly.

### Notion -- Five Points Workspace

| Field | Value |
|---|---|
| Workspace | Five Points Digital Studio (separate from personal) |
| Scope | CRM, project management, client workspaces, content calendar |
| Used by skills | offer-creator (cross-reference), future client skill |
| Routing rule | When operating in Five Points context, all Notion operations target this workspace |

### Stripe -- Five Points Account

| Field | Value |
|---|---|
| Account | Five Points Digital Studio |
| Scope | Payment processing, offer registration, invoicing, revenue tracking |
| MCP prefix | `mcp__claude_ai_Stripe__` |
| Used by skills | offer-creator |
| Routing rule | Stripe is exclusively a business asset. No personal Stripe exists in the ecosystem. All Stripe operations are Five Points-scoped. |

---

## Dormant Plugins

| Plugin | Status | Purpose | Reactivation Trigger |
|---|---|---|---|
| Instantly | Dormant since March 2026 | Outbound lead capture and pipeline automation | Phase 2 of 25K battle plan -- pipeline activation |

---

## Tool-Only -- No MCP Connection

These tools are used by Five Points but are not connected to Alfred via MCP. Alfred can reference them but cannot operate within them directly.

| Tool | Purpose | Notes |
|---|---|---|
| Google Workspace | Email, Drive, Docs, Calendar, Analytics, Search Console | Business operations. Managed manually. |
| Slack | Client communication channels | Per-client channels. Potential future MCP connection. |
| Adobe Creative Suite | Design production | $39.99/mo subscription |
| Icons8 | Icon and asset library | $15/mo subscription |
| Webflow | Website platform | Five Points site pending rebuild |

---

## Adding a New Plugin

When a new MCP connection is added for Five Points:

1. Register it in this file with: plugin name, account scope, MCP tool prefix, which skills use it, routing rules
2. Update any skills that should have access via their `allowed-tools` list
3. If the same service exists at the personal level -- e.g., a future personal Stripe account -- document the routing rule that distinguishes them
4. Update the project CLAUDE.md Plugin Routing section if the new connection introduces a routing pattern not yet documented
