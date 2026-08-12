---
file_type: integration_registry
department: Agents
venture: Lillie and Lynette
status: active
last_updated: 2026-08-08
---

# Integrations

Plugin and tool connections scoped to Lillie and Lynette. These are the external systems Alfred can operate within when working in Lillie and Lynette context.

Created 2026-08-08 (The Junction). Lillie and Lynette had no integration registry for the whole of its life to that date.

---

## The standing contradiction

Stewardship is described in the venture index as the live revenue engine, with first doors in acquisition. Against that, the venture holds no property management system, no booking platform, no payment rail, no calendar and no state workspace of its own. This is the widest gap in the portfolio measured against stated stage: a venture in Validation, earning, with zero operational wiring.

Recording it here rather than resolving it quietly. Every row below is a consequence of that gap, and the sequencing question – which surface earns its provisioning first – belongs to the operator, not to this file.

---

## Plugin Routing Principle

Lillie and Lynette owns its plugins. When Alfred is operating in Lillie and Lynette context – guest care, managed doors, objects, estates – all plugin operations target the Lillie and Lynette accounts. Data never crosses to another venture or to personal.

Guest data carries a higher bar than the portfolio default. Names, stay dates, access codes and payment details for people staying in a managed home are personal data belonging to third parties, not to the operator. No guest record enters a personal workspace, a shared sheet or another venture surface under any circumstance.

---

## Provisioning Checklist

| Surface | Status | Blocking step |
|---|---|---|
| Notion workspace | **Not provisioned** – state currently routes to the personal workspace, itself unreachable since 12 July 2026 | Operator creates the Lillie and Lynette workspace and mints the token, per the 2026-08-08 one-workspace-per-venture ruling. This venture graduates first: it is the only one of the four with live revenue. |
| Pennyone pipeline | **Not provisioned** – the `lillie_and_lynette` pipeline exists in `Integrations/pennyone/` and returns `no_key` on health check, verified 2026-08-08 | Operator provisions the Zernio account and drops `ZERNIO_LILLIEANDLYNETTE_API_KEY` |
| Payment rail | **Not provisioned** – no Stripe account exists | Stewardship is taking money now. This is the most urgent unprovisioned surface in the portfolio. |

---

## Active Plugins

No connection is live and verified for Lillie and Lynette as of 2026-08-08.

| Service | Account scope | MCP server | Status | Last verified |
|---|---|---|---|---|
| _none_ | | | | |

---

## Target-State Plugins

### Notion – Lillie and Lynette workspace

| Field | Value |
|---|---|
| Workspace | Lillie and Lynette – to be created |
| Scope | Projects, Tasks, the managed-door portfolio, the written operating standard, guest and vendor records, supplier registries for the Objects line |
| MCP server name | `notion-lillieandlynette` |
| MCP package | `@notionhq/notion-mcp-server` |
| Status | **Not provisioned.** |
| Environment variable | `NOTION_LILLIEANDLYNETTE_TOKEN` |
| Migration note | State currently sits in the personal workspace under "Lillie and Lynette – Venture Operations" and moves on provisioning. Guest records must never be created in the personal workspace in the interim – hold them at the property management system until the workspace exists. |

### Stripe – Lillie and Lynette

| Field | Value |
|---|---|
| Account | Lillie and Lynette – to be created |
| Scope | Stewardship management fees, direct stay payments, damage deposits, Objects retail when Phase 4 opens |
| MCP server name | `stripe-lillieandlynette` |
| MCP package | `@stripe/mcp@latest` |
| Status | **Not provisioned. Highest-priority gap.** |
| Environment variable | `STRIPE_LILLIEANDLYNETTE_SECRET_KEY` |
| Routing rule | Venture-scoped. Never the Five Points account. |

### Property management system – the Stewardship spine

The single largest decision on this page, and it is a selection question before it is a wiring question. Stewardship manages short lets and estates across property the company does not own; the PMS is where doors, calendars, cleaning schedules, guest messaging and channel sync all live.

| Field | Value |
|---|---|
| Candidates | Hospitable, Guesty, Lodgify, Hostaway – all carry public APIs; none has an official MCP server |
| Selection criteria | Multi-calendar sync across Airbnb and direct booking, an API good enough to build a thin FastMCP adapter against, and a boutique-portfolio price band rather than enterprise |
| Status | **Not selected.** No candidate evaluated as of this pass. |
| Build shape | Once selected, the connection follows the Pennyone pattern – a thin FastMCP service at `Integrations/lillieandlynette-pms/` routing one intent through the vendor API, with writes gated on the ask list |
| Routing rule | The PMS becomes the source of truth for door state and guest stays. Notion holds the operating standard and the portfolio; it does not duplicate live booking data. |

### Booking channels

| Channel | Purpose | Status |
|---|---|---|
| Airbnb | Primary short-let distribution for managed doors | No API access without host-partner status; realistically reached through the PMS channel manager rather than directly |
| Direct booking | Owned demand, no platform commission | Depends on the PMS and a web property; neither exists |

### Pennyone – social syndication

| Field | Value |
|---|---|
| Account | Zernio (Lillie and Lynette) – to be provisioned |
| Pipeline value | `lillie_and_lynette` |
| Status | **Pipeline registered in code, no key.** Verified 2026-08-08. |
| Environment variable | `ZERNIO_LILLIEANDLYNETTE_API_KEY` |

### Calendar

| Field | Value |
|---|---|
| Scope | Turnovers, cleaning windows, owner visits, viewings |
| Status | **Not provisioned.** No venture calendar surface exists. |
| Note | Do not route Lillie and Lynette scheduling through `apple-calendar` or `fivepoints-calendar`. The first is personal, the second is another venture. A dedicated Google Workspace tenant is the likely answer, on the Five Points pattern – one service account, domain-wide delegation, per-user routing. |

---

## Tool-Only – No MCP Connection

| Tool | Purpose | Notes |
|---|---|---|
| Cleaning and turnover vendors | Service delivery on managed doors | Coordinated manually |
| Bath and body manufacturer | The Objects line | Not selected; Objects are an amenity before they are retail |

---

## Secrets

| Environment variable | Service | Status |
|---|---|---|
| `NOTION_LILLIEANDLYNETTE_TOKEN` | Notion (venture workspace) | Not provisioned |
| `ZERNIO_LILLIEANDLYNETTE_API_KEY` | Zernio (venture pipeline) | Not provisioned – pipeline exists in code |
| `STRIPE_LILLIEANDLYNETTE_SECRET_KEY` | Stripe (venture) | Not provisioned |
| PMS API credential | Property management system | Vendor not selected; variable name follows on selection |

Every row above must also appear in `Manual/secrets-inventory.md`.

---

## Adding a New Plugin

Follow the eight-step sequence in `New Venture/Agents/integrations.md`. A row moves to Active only after a live health check returns successfully, with the verification date recorded.

---

*Last updated: 2026-08-08 – The Junction. Registry created; the revenue-without-wiring contradiction recorded, PMS selection named as the gating decision.*
