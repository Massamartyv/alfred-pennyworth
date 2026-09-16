---
file_type: integration_registry
department: Agents
venture: Five Points Digital Studio
status: active
last_updated: 2026-09-10
---

<!-- Added 2026-04-24: fivepoints-mail MCP (Gmail via domain-wide delegation). -->
<!-- Updated 2026-07-10: Instantly deprecated, replaced by Clay (tool-only, no MCP). Webflow removed; the site is Next.js on Vercel. -->
<!-- Updated 2026-07-10 (later): calcom MCP scaffolded and registered; Cal.com upgraded from dashboard-only to MCP-connected, awaiting key drop. -->
<!-- Updated 2026-07-10 (calendar lane): fivepoints-calendar MCP added, sharing the fivepoints-mail service account. -->
<!-- Updated 2026-08-08 (The Junction): every row live-verified. Vercel and Apify corrected from false "Live" claims to NOT CONNECTED. Mail, Calendar and Cal.com marked DARK against health-check evidence. -->


# Integrations

Plugin and tool connections scoped to Five Points Digital Studio. These are the external systems Alfred can operate within when working in Five Points context.

---

## Verification standard

Every status in this file was established by a live call on 2026-08-08, not by reading a config file. A row claiming "Live" without a verification date is not evidence and should be treated as unverified until a health check says otherwise.

This standard exists because the alternative failed. Two rows in this file – Vercel and Apify – read "Live – connected via `.mcp.json`" for an extended period while no such server existed at any scope. A registry that lies is more dangerous than one that is silent, because it stops you looking.

| Surface | Result, 2026-08-08 |
|---|---|
| Notion Five Points | Live – workspace and bot identity confirmed |
| Stripe Five Points | Live – account id and display name confirmed |
| Supabase Five Points | Live – three projects returned |
| Pennyone `five_points` | Live – one platform connected of six |
| Google Drive (desktop connector) | Registered, read-only, not independently exercised this pass |
| `fivepoints-mail` | **Dark** – no credentials, all five mailboxes |
| `fivepoints-calendar` | **Dark** – no credentials, shared key |
| `calcom` | **Dark** – pipeline not provisioned |
| `vercel-fivepoints` | **Does not exist** |
| `apify-fivepoints` | **Does not exist** – REST access only |

The three dark surfaces are the studio communications layer. Five Points can currently take money and cannot answer an email, hold a meeting or accept a booking. Two operator actions clear all three: the Google service-account JSON drop, and the Cal.com key.

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
| Status | **Live and verified 2026-08-08.** `API-get-self` returns workspace "Five Points Digital Studio", bot "Alfred Pennyworth", owner `systems@fivepoints.studio`. |
| Environment variable | `NOTION_FIVEPOINTS_TOKEN` (stored in `.env`) |
| Used by skills | offer-creator (cross-reference), discovery-architect, prospect-appraiser, switchboard, seo-audit |
| Routing rule | When operating in Five Points context, all Notion operations target this connection. Per the 2026-08-08 one-workspace-per-venture ruling this is one of several venture workspaces rather than one of two workspaces – Five Points state never enters a personal or other-venture workspace, and no other venture state enters this one. Atlas state currently misfiled here migrates out on Atlas provisioning. |

### Vercel – Five Points Account

| Field | Value |
|---|---|
| Account | Five Points Digital Studio – Vercel team `studio-fivepoints`, login `systems-9970` |
| Scope | Client deployments, preview URLs, production hosting |
| MCP server name | `vercel-fivepoints` – **does not exist** |
| MCP package | `@vercel/mcp@latest` |
| Status | **NOT CONNECTED. Corrected 2026-08-08 (The Junction).** This row previously read "Live – connected via `.mcp.json`". That was false and had been false for an unknown period. No `vercel-fivepoints` block exists in `.mcp.json`, no such server is registered at any scope and no tool from it has ever been reachable. |
| Verified | 2026-08-08. `list_teams` on the only reachable Vercel MCP returns a single team – `lavender-stingray`, "Headquarters" – which is the **personal** account. The Five Points team `studio-fivepoints` has no MCP surface at all. |
| Consequence | Every Five Points client deployment on the books – the studio site and Strong Tower – has been deployed outside the wiring or through the personal-scoped connector. The latter is a segmentation breach. |
| Environment variable | `VERCEL_FIVEPOINTS_TOKEN` – presence in `.env` unconfirmed; Alfred is denied reads of `.env` by design |
| Routing rule (target) | Once built, all Five Points Vercel operations target this connection and the desktop Vercel connector is treated as personal-only. Until then, no Vercel operation may be performed in Five Points context through the personal connector. |

### Apify – Five Points Account

| Field | Value |
|---|---|
| Account | Five Points Digital Studio (Apify user: yYCnD6Fz8Y65f9u7e) |
| Scope | Web scraping, data retrieval, competitor research for client projects |
| MCP server name | `apify-fivepoints` – **does not exist** |
| MCP package | `@apify/actors-mcp-server` |
| Status | **NOT CONNECTED VIA MCP. Corrected 2026-08-08 (The Junction).** This row previously read "Live – connected via `.mcp.json`". No such block exists and no such server is registered at any scope. |
| How Apify is actually used | Directly over the REST API using the scoped token, in the async pattern recorded in the "Apify integration" reference memory – validated actors are `reddit-scraper-lite`, `automation-lab/trustpilot`, `kaitoeasyapi` X and `compass` google-maps. The capability is real; the MCP surface is not. |
| Environment variable | `APIFY_FIVEPOINTS_TOKEN` (stored in `.env`) |
| Routing rule | **Dual-scope service.** Apify exists at both personal and Five Points levels. Five Points context – client research, competitor analysis, business development scrapes – uses `APIFY_FIVEPOINTS_TOKEN`. Personal context uses `APIFY_PERSONAL_TOKEN`. Data never crosses. The routing rule holds whether the access path is MCP or REST. |

### Supabase – Five Points Account

| Field | Value |
|---|---|
| Account | Five Points Digital Studio (systems@fivepoints.studio login) |
| Scope | Client project databases, backend infrastructure, edge functions |
| MCP server name | `supabase-fivepoints` |
| MCP package | `@supabase/mcp-server-supabase@latest` |
| Status | **Live and verified 2026-08-08.** `list_projects` returns three under org `auenrodwupfdfrfdhbrf` – `fivepoints-site` (ACTIVE_HEALTHY), `strong-tower-christian-ministry` (INACTIVE), `Nomad Express` (INACTIVE). |
| Environment variable | `SUPABASE_FIVEPOINTS_TOKEN` (stored in `.env`) |
| Routing rule | When operating in Five Points context, all Supabase operations target this connection. The personal Supabase management token is separate (`SUPABASE_PERSONAL_TOKEN`). |

### Stripe – Five Points Account

| Field | Value |
|---|---|
| Account | Five Points Digital Studio |
| Scope | Payment processing, offer registration, invoicing, revenue tracking |
| MCP server name | `stripe-fivepoints` |
| MCP package | `@stripe/mcp@latest` |
| Status | **Live and verified 2026-08-08.** `get_stripe_account_info` returns `acct_1PfTxpDH3f10EsHc`, display name "Five Points Digital Studio". |
| Environment variable | `STRIPE_FIVEPOINTS_SECRET_KEY` (stored in `.env`) |
| Used by skills | offer-creator |
| Routing rule | Stripe is exclusively a business asset. No personal Stripe exists in the ecosystem. All Stripe operations are Five Points-scoped. |
| Env var naming | The `_SECRET_KEY` suffix is retained (not aligned to `_TOKEN`) because Stripe uses "secret key" as its canonical terminology. Domain-specific naming is preferred over forced uniformity. |

### Pennyone – Social syndication

| Field | Value |
|---|---|
| Account | Zernio (Five Points, live 2026-04-23) |
| Scope | Social syndication across Instagram, TikTok, Threads, X, Reddit and Snap for Five Points handles |
| Pipeline value | `five_points` |
| MCP server name | `pennyone` (cross-venture router) |
| MCP package | Custom Python/FastMCP server at `Integrations/pennyone/` |
| Status | **Live and verified 2026-08-08.** `health_check` returns `ok` – one connected account, one active: Instagram (`studio.fivepoints`). Five of six intended platforms remain unconnected. For contrast the personal pipeline carries seven active accounts across Discord, Instagram, LinkedIn, Reddit, Threads, TikTok and YouTube; the studio publishes to a single channel. |
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
| Routing rule | When Gemini is needed in Five Points context, reference this key. Scope relocated from the retired Alfred operating system Backend. |

### Five Points Mail – Gmail (five inboxes)

| Field | Value |
|---|---|
| Workspace | fivepoints.studio Google Workspace (hello@ admin, four user seats beneath) |
| Scope | Read, search, draft, reply, send, label and trash operations across all five inboxes |
| Mailbox keys | `hello`, `martavious`, `systems`, `opportunities`, `finance` |
| MCP server name | `fivepoints-mail` |
| MCP package | Custom Python/FastMCP server at `Integrations/fivepoints-mail/` |
| Status | **DARK. Verified 2026-08-08.** `health_check` returns `no_credentials` on all five mailboxes: "Service account key not found at `Integrations/fivepoints-mail/credentials/service-account.json`". Scaffolded 2026-04-24; the key has never been dropped. The studio has been unable to read or send business email through Alfred for roughly three and a half months. |
| Auth | One Google Cloud service account with domain-wide delegation. Impersonates each mailbox per request. Single credential, five inboxes. |
| Credential path | `Integrations/fivepoints-mail/credentials/service-account.json` (gitignored). Optional override via `FIVEPOINTS_MAIL_SERVICE_ACCOUNT`. |
| Scopes | `gmail.modify`, `gmail.send`, `gmail.readonly`, `gmail.compose` |
| Routing rule | Venture-scoped. All Five Points inbox operations go through this MCP. Personal email routes through Apple Mail (`mcp-apple-mail`). Never cross the boundary. |
| Access pattern | Department heads access their inbox via `mailbox:` parameter. Suggested mapping: Operations → `hello`, Owner → `martavious`, builds and dev tooling → `systems`, Business Development → `opportunities`, Finances → `finance`. Enforced through skill `allowed-tools` scoping rather than at the server. |
| Confirmation | Write tools (`send_draft`, `send_message`, `create_draft`, `trash_message`, `modify_labels`, etc.) declare `writes: True`. Per Navigation Rule 3, any send must be confirmed in chat before dispatch. |

### Five Points Calendar – Workspace calendars

| Field | Value |
|---|---|
| Workspace | fivepoints.studio Google Workspace – the five user calendars; `martavious` is where Cal.com bookings land |
| Scope | Read events, calendars and free-busy; create, update and delete events as gated writes |
| User keys | `hello`, `martavious`, `systems`, `opportunities`, `finance` – explicit on every call, no implicit default |
| MCP server name | `fivepoints-calendar` |
| MCP package | Custom Python/FastMCP server at `Integrations/fivepoints-calendar/` |
| Status | **DARK. Verified 2026-08-08.** `health_check` on user `martavious` returns the same `no_credentials` error as fivepoints-mail, naming the shared key path. Registered in `.mcp.json`, offline smoke test passing (9 tools). Blocked on the shared service-account key drop plus the Calendar scope addition to the domain-wide delegation grant – the same key fivepoints-mail has awaited since April. One key drop lights both servers. |
| Auth | The fivepoints-mail service account via a shared fallback chain; optional `FIVEPOINTS_CALENDAR_SERVICE_ACCOUNT` override |
| Routing rule | Venture-scoped. Studio calendar operations go through this MCP. Personal and iCloud calendars route through `apple-calendar`; the personal Gmail calendar has its own desktop connector. Never cross the boundary. |
| Confirmation | Write tools (`create_event`, `update_event`, `delete_event`) sit on the settings ask list per Navigation Rule 3. `send_updates` defaults to `none`, so attendee notification email requires separate, explicit approval. |

### Cal.com – Booking layer

| Field | Value |
|---|---|
| Account | martavious-spicer (cal.com/martavious-spicer), primary email martavious@fivepoints.studio, gmail as interim backup |
| Scope | Client-facing booking links for Five Points calls – diagnostics, working calls, prospect conversations |
| MCP server name | `calcom` |
| MCP package | Custom Python/FastMCP server at `Integrations/calcom/` |
| Status | **DARK. Verified 2026-08-08.** `health_check` returns `Pipeline 'five_points' not provisioned. Set CALCOM_FIVEPOINTS_API_KEY`. Registered in `.mcp.json`, offline smoke test passing (10 tools). Awaiting the key drop into `.env`; live verification is the first action after the key lands. Account live and consolidated to the studio email 2026-07-10 – an accidental gmail-created duplicate account was deleted by the operator. |
| Environment variable | `CALCOM_FIVEPOINTS_API_KEY` (stored in `.env`) |
| Confirmation | Write tools (`create_booking`, `reschedule_booking`, `cancel_booking`) sit on the settings ask list and must be confirmed in chat before dispatch per Navigation Rule 3. All three trigger Cal.com notification emails. |
| Public events | The Working Call (45 min, `/the-working-call`, attendee-phone location, 15-min after-buffer – client commissioning calls); Operational Intelligence Diagnostic (30 min, `/30min` – a 30-minute hold for a 20-minute session, buffer by design); 15 min meeting (15 min, `/15min`) |
| Routing rule | Business booking only. Prospecting instruments reference `/30min` (see Business Development/Prospecting/). Client proposals reference the event matched to the promised call length – create a named event per call type rather than reusing a mismatched slug. |

### SAM.gov – Federal contract opportunities and entity data

| Field | Value |
|---|---|
| Account | Personal SAM.gov user account (interim). Rotate to a Five Points account once `systems@fivepoints.studio` is reachable. |
| Scope | Federal contract opportunity search, entity registration lookup, contract award data |
| MCP server name | `samgov` – not yet built |
| Status | **Key live, key rate-limited.** Verified working against both `entity-information/v4` and `opportunities/v2` on 2026-07-14. |
| Environment variable | `SAM_FIVEPOINTS_API_KEY` (stored in `.env`) |
| Key expiry | 90 days. `SAM_FIVEPOINTS_API_KEY_EXPIRES` in `.env`; monthly credential expiry sweep in `Agents/heartbeat.md` flags at 21 days. No key transfer path exists between SAM.gov accounts – the replacement account generates a fresh key and the value is swapped in place. |
| **Rate limit** | **10 requests/day.** Non-federal user with no SAM.gov role. Rises to **1,000/day** once the user holds a role on a registered entity. This is an account-level limit across all api.sam.gov endpoints, not per-endpoint. |
| Architecture consequence | The API cannot carry a search workload at 10 calls/day. Bulk opportunity data comes from the SAM.gov Contract Opportunities extract (no key, no limit); historical award intelligence comes from USASpending.gov (no key, no limit). The SAM API is reserved for surgical single-record lookups. |
| Dead upstream | The FPDS ATOM feed was retired in February 2026 and now returns valid but empty XML rather than an error. Do not build against it. Its replacement is the SAM.gov Contract Awards API, which shares the same rate-limit tiers. |
| Routing rule | Venture-scoped to Five Points. No personal SAM.gov usage exists. |

---

## Dormant Plugins

_No dormant plugins._

---

## Deprecated Plugins

| Plugin | Status | Replacement | Reason |
|---|---|---|---|
| Instantly | **Deprecated 2026-07-10** | Clay | Clay owns the outbound lane end to end (enrichment, sequencing, sending). The `instantly` MCP server is pending unregistration from `.mcp.json`; account cancellation pending operator action. |

---

## Tool-Only – No MCP Connection

These tools are used by Five Points but are not connected to Alfred via MCP. Alfred can reference them but cannot operate within them directly.

| Tool | Purpose | Notes |
|---|---|---|
| Google Workspace | Email, Drive, Docs, Calendar, Analytics, Search Console | Business operations. Managed manually. |
| Slack | Client communication channels | Per-client channels. Potential future MCP connection. |
| Adobe Creative Suite | Design production | $39.99/mo subscription |
| Icons8 | Icon and asset library | $15/mo subscription |
| Clay | Outbound lead engine: enrichment, sequencing, sending | Replaced Instantly 2026-07-10. No MCP connection yet; API wiring is a candidate build. |

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
| `INSTANTLY_FIVEPOINTS_API_KEY` | Instantly (deprecated 2026-07-10; remove after account cancellation) | `.env` |
| `GEMINI_FIVEPOINTS_API_KEY` | Gemini (Five Points) | `.env` |
| `ZERNIO_FIVEPOINTS_API_KEY` | Zernio (Five Points account, provisioning) | `.env` |
| `CALCOM_FIVEPOINTS_API_KEY` | Cal.com (Five Points booking layer; pending operator drop) | `.env` |
| `FIVEPOINTS_MAIL_SERVICE_ACCOUNT` (optional) | Override path for the Gmail service account key. Default is `Integrations/fivepoints-mail/credentials/service-account.json` | `.env` if overridden |

Note: the Five Points Mail MCP authenticates via a service account JSON file, not an API key in `.env`. The default path is inside the integration folder and gitignored. Only set `FIVEPOINTS_MAIL_SERVICE_ACCOUNT` if storing the key elsewhere.

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
