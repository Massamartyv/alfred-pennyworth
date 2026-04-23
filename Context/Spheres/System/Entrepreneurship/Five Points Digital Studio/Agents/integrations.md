---
file_type: integration_registry
department: Agents
venture: Five Points Digital Studio
status: active
last_updated: 2026-04-22
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
| MCP package | `@apify/actors-mcp-server` |
| Status | Live – connected via `.mcp.json` |
| Environment variable | `APIFY_FIVEPOINTS_TOKEN` (stored in `.env`) |
| Routing rule | **Dual-scope service.** Apify exists at both personal and Five Points levels. When operating in Five Points context (client research, competitor analysis, business development scrapes), use this connection. When operating in personal context (research, curiosity scrapes, cross-venture exploration), use the personal Apify connection (`APIFY_PERSONAL_TOKEN`). Data never crosses. |

### Supabase – Five Points Account

| Field | Value |
|---|---|
| Account | Five Points Digital Studio (systems@fivepoints.studio login) |
| Scope | Client project databases, backend infrastructure, edge functions |
| MCP server name | `supabase-fivepoints` |
| MCP package | `@supabase/mcp-server-supabase@latest` |
| Status | Live – connected via `.mcp.json` |
| Environment variable | `SUPABASE_FIVEPOINTS_TOKEN` (stored in `.env`) |
| Routing rule | When operating in Five Points context, all Supabase operations target this connection. The personal Supabase management token is separate (`SUPABASE_PERSONAL_TOKEN`). |

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
| Env var naming | The `_SECRET_KEY` suffix is retained (not aligned to `_TOKEN`) because Stripe uses "secret key" as its canonical terminology. Domain-specific naming is preferred over forced uniformity. |

### Pennyone – Social syndication

| Field | Value |
|---|---|
| Account | Zernio (Five Points, provisioning) |
| Scope | Social syndication across Instagram, TikTok, Threads, X, Reddit and Snap for Five Points handles |
| Pipeline value | `five_points` |
| MCP server name | `pennyone` (cross-venture router) |
| MCP package | Custom Python/FastMCP server at `Integrations/pennyone/` |
| Status | Scaffold complete, multi-pipeline routing wired. Provisioning Five Points Zernio account now. |
| Environment variable | `ZERNIO_FIVEPOINTS_API_KEY` |
| Routing rule | When the Five Points content pipeline dispatches through Pennyone, it passes `pipeline: "five_points"` and Pennyone routes under the Five Points Zernio account. Pennyone itself is cross-venture; only the Zernio account is venture-scoped. |

### Gemini – Five Points

| Field | Value |
|---|---|
| Account | Five Points (Google AI) |
| Scope | Image generation, model evaluation, Five Points creative work that requires Gemini |
| MCP server name | n/a – used by design skill directly |
| Status | Live – credential rotated 2026-04-22 |
| Environment variable | `GEMINI_FIVEPOINTS_API_KEY` (stored in `.env`) |
| Routing rule | When Gemini is needed in Five Points context, reference this key. Scope relocated from the retired Alfred OS Backend. |

---

## Dormant Plugins

| Plugin | Status | Purpose | Reactivation Trigger |
|---|---|---|---|
| Instantly | Dormant since March 2026 | Outbound lead capture and pipeline automation | Phase 2 of 25K battle plan. Credential rotated 2026-04-22 as `INSTANTLY_FIVEPOINTS_API_KEY`; slot in `.mcp.json` returns on reactivation. |

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
| `APIFY_FIVEPOINTS_TOKEN` | Apify (Five Points account) | `.env` |
| `INSTANTLY_FIVEPOINTS_API_KEY` | Instantly (Five Points account, dormant) | `.env` |
| `GEMINI_FIVEPOINTS_API_KEY` | Gemini (Five Points) | `.env` |
| `ZERNIO_FIVEPOINTS_API_KEY` | Zernio (Five Points account, provisioning) | `.env` |

To activate in a new shell session: `source ~/Alfred\ Pennyworth/.env`

---

## Adding a New Plugin

When a new MCP connection is added for Five Points:

1. Add the API key to `~/Alfred Pennyworth/.env` with a descriptive variable name following the pattern `SERVICE_FIVEPOINTS_TOKEN` (or a domain-specific suffix where the service has its own canonical terminology)
2. Add the server config to `.mcp.json` referencing the env var via `${VARIABLE_NAME}`
3. Register it in this file with: plugin name, account scope, MCP server name, MCP package, status, environment variable, which skills use it, routing rules
4. Update any skills that should have access via their `allowed-tools` list
5. If the same service exists at the personal level, document the routing rule that distinguishes them (see Apify for the dual-scope pattern)
6. Update the project CLAUDE.md Plugin Routing section if the new connection introduces a routing pattern not yet documented
