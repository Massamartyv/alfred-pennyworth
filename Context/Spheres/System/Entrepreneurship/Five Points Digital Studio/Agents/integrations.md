---
file_type: integration_registry
department: Operations/AI
venture: Five Points Digital Studio
status: active
last_updated: 2026-04-09
---

# Integrations

Plugin and tool connections scoped to Five Points Digital Studio. These are the external systems Alfred can operate within when working in Five Points context.

---

## Plugin Routing Principle

Five Points owns its plugins. When Alfred is operating in Five Points context – clients, offers, business operations, venture strategy – all plugin operations target the Five Points accounts. When no business context is active, Alfred defaults to the personal workspace and personal accounts.

Data never crosses between personal and business plugins. This is the same boundary established in the global CLAUDE.md Navigation Rules, extended to the plugin layer.

---

## Active Plugins

Plugins are MCP connections. Alfred can read, write and operate within these systems directly.

### Notion – Five Points Workspace

| Field | Value |
|---|---|
| Workspace | Five Points Digital Studio (separate from personal) |
| Scope | CRM, project management, client workspaces, content calendar |
| MCP server name | `notion-fivepoints` |
| MCP package | `@notionhq/notion-mcp-server` |
| Status | Live – connected via `.mcp.json` |
| Environment variable | `NOTION_FIVEPOINTS_TOKEN` (stored in `.env`) |
| Used by skills | offer-creator (cross-reference), future client skill |
| Routing rule | When operating in Five Points context, all Notion operations target this connection. The managed/enhanced Notion MCP targets the personal workspace. |

### Vercel – Five Points Account

| Field | Value |
|---|---|
| Account | Five Points Digital Studio |
| Scope | Client deployments, preview URLs, production hosting |
| MCP server name | `vercel-fivepoints` |
| MCP package | `@vercel/mcp@latest` |
| Status | Live – connected via `.mcp.json` |
| Environment variable | `VERCEL_FIVEPOINTS_TOKEN` (stored in `.env`) |
| Routing rule | When operating in Five Points context, all Vercel operations target this connection. The managed Vercel MCP targets the personal account. |

### Apify – Five Points Account

| Field | Value |
|---|---|
| Account | Five Points Digital Studio (Apify user: yYCnD6Fz8Y65f9u7e) |
| Scope | Web scraping, data retrieval, competitor research for client projects |
| MCP server name | `apify-fivepoints` |
| Routing rule | When operating in Five Points context, all Apify operations target this connection. The managed Apify MCP targets the personal account. |

### Supabase – Five Points Account

| Field | Value |
|---|---|
| Account | Five Points Digital Studio (systems@fivepoints.studio login) |
| Scope | Client project databases, backend infrastructure, edge functions |
| MCP server name | `supabase-fivepoints` |
| MCP package | `@supabase/mcp-server-supabase@latest` |
| Status | Live – connected via `.mcp.json` |
| Environment variable | `SUPABASE_FIVEPOINTS_TOKEN` (stored in `.env`) |
| Routing rule | When operating in Five Points context, all Supabase operations target this connection. The managed Supabase MCP targets the personal account. |

### Stripe – Five Points Account

| Field | Value |
|---|---|
| Account | Five Points Digital Studio |
| Scope | Payment processing, offer registration, invoicing, revenue tracking |
| MCP server name | `stripe-fivepoints` |
| MCP package | `@stripe/mcp@latest` |
| Status | Live – connected via `.mcp.json` |
| Environment variable | `STRIPE_FIVEPOINTS_SECRET_KEY` (stored in `.env`) |
| Used by skills | offer-creator |
| Routing rule | Stripe is exclusively a business asset. No personal Stripe exists in the ecosystem. All Stripe operations are Five Points-scoped. |

---

## Dormant Plugins

| Plugin | Status | Purpose | Reactivation Trigger |
|---|---|---|---|
| Instantly | Dormant since March 2026 | Outbound lead capture and pipeline automation | Phase 2 of 25K battle plan – pipeline activation |

---

## Tool-Only – No MCP Connection

These tools are used by Five Points but are not connected to Alfred via MCP. Alfred can reference them but cannot operate within them directly.

| Tool | Purpose | Notes |
|---|---|---|
| Google Workspace | Email, Drive, Docs, Calendar, Analytics, Search Console | Business operations. Managed manually. |
| Slack | Client communication channels | Per-client channels. Potential future MCP connection. |
| Adobe Creative Suite | Design production | $39.99/mo subscription |
| Icons8 | Icon and asset library | $15/mo subscription |
| Webflow | Website platform | Five Points site pending rebuild |

---

## Secrets Management

All API keys are stored in `~/Alfred Pennyworth/.env` (gitignored). The `.mcp.json` config references these via `${VARIABLE_NAME}` syntax. No raw keys live in the config file.

| Environment Variable | Service | Stored In |
|---|---|---|
| `NOTION_FIVEPOINTS_TOKEN` | Notion (Five Points workspace) | `.env` |
| `VERCEL_FIVEPOINTS_TOKEN` | Vercel (Five Points account) | `.env` |
| `SUPABASE_FIVEPOINTS_TOKEN` | Supabase (Five Points account) | `.env` |
| `STRIPE_FIVEPOINTS_SECRET_KEY` | Stripe (Five Points account) | `.env` |

To activate in a new shell session: `source ~/Alfred\ Pennyworth/.env`

---

## Adding a New Plugin

When a new MCP connection is added for Five Points:

1. Add the API key to `~/Alfred Pennyworth/.env` with a descriptive variable name following the pattern `SERVICE_FIVEPOINTS_VARIABLE`
2. Add the server config to `.mcp.json` referencing the env var via `${VARIABLE_NAME}`
3. Register it in this file with: plugin name, account scope, MCP server name, MCP package, environment variable, which skills use it, routing rules
4. Update any skills that should have access via their `allowed-tools` list
5. If the same service exists at the personal level, document the routing rule that distinguishes them
6. Update the project CLAUDE.md Plugin Routing section if the new connection introduces a routing pattern not yet documented
