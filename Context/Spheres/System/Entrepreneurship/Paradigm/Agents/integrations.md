---
file_type: integration_registry
department: Agents
venture: Paradigm
status: active
last_updated: 2026-08-08
---

# Integrations

Plugin and tool connections scoped to Paradigm, including the Paradigm Farms sub-brand. These are the external systems Alfred can operate within when working in Paradigm context.

Created 2026-08-08 (The Junction). Paradigm had no integration registry for the whole of its life to that date; every row below is either newly verified or newly named as absent.

---

## Plugin Routing Principle

Paradigm owns its plugins. When Alfred is operating in Paradigm context – formulation, packaging, DTC and wholesale channels, the Farms app – all plugin operations target the Paradigm accounts. Data never crosses to another venture or to personal.

Paradigm Farms is a sub-brand, not a sovereign venture. It shares the Paradigm workspace, the Paradigm payment rail and the Paradigm Pennyone pipeline. It does not get its own. Sub-brands inherit; only ventures provision.

---

## Provisioning Checklist

| Surface | Status | Blocking step |
|---|---|---|
| Notion workspace | **Not provisioned** – state currently routes to the personal workspace, which has itself been unreachable since 12 July 2026 | Operator creates the Paradigm workspace and mints the token, per the 2026-08-08 one-workspace-per-venture ruling |
| Pennyone pipeline | **Not provisioned** – the `paradigm` pipeline exists in `Integrations/pennyone/` and returns `no_key` on health check, verified 2026-08-08 | Operator provisions the Paradigm Zernio account and drops `ZERNIO_PARADIGM_API_KEY` |
| Payment rail | **Not provisioned** – no Stripe account exists for Paradigm | Required before any product sells. A wellness brand with a product line and no payment rail cannot transact. |

---

## Active Plugins

No connection is live and verified for Paradigm as of 2026-08-08. The venture is currently operated entirely on file-level context.

| Service | Account scope | MCP server | Status | Last verified |
|---|---|---|---|---|
| _none_ | | | | |

---

## Target-State Plugins

### Notion – Paradigm workspace

| Field | Value |
|---|---|
| Workspace | Paradigm – to be created |
| Scope | Projects, Tasks, formulation records, supplier and ingredient registries, The Orangery mission record |
| MCP server name | `notion-paradigm` |
| MCP package | `@notionhq/notion-mcp-server` |
| Status | **Not provisioned.** |
| Environment variable | `NOTION_PARADIGM_TOKEN` |
| Migration note | Paradigm state currently sits in the personal workspace under "Paradigm – Venture Operations" and "The Orangery". Both move on provisioning. The Botany sphere data layer that Paradigm Farms reads is sphere knowledge, not venture state – it stays in the personal workspace under Sphere Manager and Paradigm reads it rather than owning it. |
| Routing rule | All Paradigm and Paradigm Farms state targets this connection once live. |

### Pennyone – social syndication

| Field | Value |
|---|---|
| Account | Zernio (Paradigm) – to be provisioned |
| Pipeline value | `paradigm` |
| MCP server name | `pennyone` (cross-venture router) |
| Status | **Pipeline registered in code, no key.** `health_check` returns `no_key`, verified 2026-08-08. |
| Environment variable | `ZERNIO_PARADIGM_API_KEY` |
| Routing rule | Dispatches pass `pipeline: "paradigm"`. Paradigm Farms publishes under the same pipeline – the sub-brand carries its own voice register, not its own account. |

### Stripe – Paradigm

| Field | Value |
|---|---|
| Account | Paradigm – to be created |
| Scope | DTC checkout, wholesale invoicing, subscription rituals if the line extends that way |
| MCP server name | `stripe-paradigm` |
| MCP package | `@stripe/mcp@latest` |
| Status | **Not provisioned.** |
| Environment variable | `STRIPE_PARADIGM_SECRET_KEY` |
| Routing rule | Stripe is always venture-scoped. The Five Points Stripe account is not the Paradigm Stripe account and the two never share a key. |
| Confirmation | All write tools gate on the ask list per Navigation Rule 3. |

### Paradigm Farms – iOS build and AI lane

The Farms application has infrastructure needs no other venture in the portfolio carries.

| Surface | Purpose | Status |
|---|---|---|
| Anthropic API | The plant identification and horticultural AI layer. Paradigm Farms needs its own key rather than borrowing the Claude Code session credentials, on the Oracle precedent – an app manages its own key independently of the session. | Not provisioned. `ANTHROPIC_PARADIGM_API_KEY`. |
| Apple Developer Program | TestFlight distribution and App Store release for the iOS and visionOS builds | Not confirmed. Enrolment status unverified as of this pass. |
| iOS Simulator | Build, run and visually verify the app. The Simulator control surface is available at session level and is not venture-scoped. | Available, ungoverned. Governed here by declaration: Simulator use in Paradigm context targets Paradigm Farms builds only. |
| Core ML model hosting | Where the trained vision models live and how they ship with the binary | Undecided. A build-plan question, not a wiring gap. |

---

## Tool-Only – No MCP Connection

| Tool | Purpose | Notes |
|---|---|---|
| Manufacturing and fulfilment | Contract manufacturer, co-packer, 3PL | None selected. Sequenced with the first product run. |
| Adobe Creative Suite | Packaging and brand production | Shared subscription across the portfolio |

---

## Secrets

| Environment variable | Service | Status |
|---|---|---|
| `NOTION_PARADIGM_TOKEN` | Notion (Paradigm workspace) | Not provisioned |
| `ZERNIO_PARADIGM_API_KEY` | Zernio (Paradigm pipeline) | Not provisioned – pipeline exists in code |
| `STRIPE_PARADIGM_SECRET_KEY` | Stripe (Paradigm) | Not provisioned |
| `ANTHROPIC_PARADIGM_API_KEY` | Anthropic (Paradigm Farms AI layer) | Not provisioned |

Every row above must also appear in `Manual/secrets-inventory.md`.

---

## Adding a New Plugin

Follow the eight-step sequence in `New Venture/Agents/integrations.md`. A row moves from Target-State to Active only after a live health check returns successfully, and it carries the verification date.

---

*Last updated: 2026-08-08 – The Junction. Registry created; three universal surfaces and the Farms build lane named as unprovisioned.*
