---
file_type: integration_registry
department: Agents
venture: Atlas
status: active
last_updated: 2026-08-08
---

# Integrations

Plugin and tool connections scoped to Atlas. These are the external systems Alfred can operate within when working in Atlas context.

Created 2026-08-08 (The Junction). Atlas is at Reconnaissance, so thin wiring is appropriate. Two findings are not appropriate and are recorded below.

---

## Finding 1 – Atlas state is misfiled in the Five Points workspace

The venture index records live state as "Notion Projects and Tasks, Five Points workspace". Atlas is a sovereign venture and a peer brand. It is not a Five Points asset, not a Five Points client and not a Five Points product line. Filing its state inside the Five Points workspace breaches venture sovereignty in the same way a shared Stripe account would.

Corrected by the 2026-08-08 one-workspace-per-venture ruling. Atlas provisions its own workspace and the existing records migrate out. Until the workspace exists, the Arlando Parker Jr. pilot terms remain where they are rather than being moved twice.

## Finding 2 – Atlas is absent from the Pennyone router entirely

Every other active venture has a pipeline registered in `Integrations/pennyone/`, provisioned or not. Atlas has none – it is not in the `Pipeline` enum. The absence is defensible while the venture is pre-brand, since the final identity awaits an art-direction pass and there is nothing to publish under. It is recorded so that it is a decision rather than an oversight, and so that the pipeline is added at the same moment the identity lands.

---

## Plugin Routing Principle

Atlas owns its plugins. Data never crosses to another venture or to personal.

**Atlas carries a constraint no other venture in the portfolio carries: protected health information.** The moment the pilot handles a real patient encounter, every surface that touches that data needs a Business Associate Agreement in place. No surface in the current estate has one. This is not a wiring gap to be closed in passing – it gates the whole Execution phase.

---

## The HIPAA boundary

Binding on every Atlas integration decision, and the reason this venture cannot simply inherit portfolio defaults.

| Rule | Detail |
|---|---|
| No PHI without a BAA | No patient identifier, encounter note, diagnosis or claim detail touches any service until a signed BAA covers it. This includes Notion, Supabase, Vercel, any logging surface and any model provider. |
| No PHI in the personal estate | Never a personal workspace, never `.working/`, never a memory file, never an iMessage notification. The notification layer that serves the rest of the portfolio is not available to Atlas for anything patient-adjacent. |
| De-identified by default | Reconnaissance and design work uses synthetic or de-identified records. Real encounters enter only at the pilot, under the BAA set. |
| Model provider | Anthropic offers a BAA on commercial terms. This must be executed before any real encounter reaches a model, and it covers the API rather than the Claude Code session – Atlas manages its own key. |
| Audit trail | HIPAA requires access logging over PHI. The logging surface is itself a covered system and needs its own BAA. |

---

## Provisioning Checklist

| Surface | Status | Blocking step |
|---|---|---|
| Notion workspace | **Not provisioned** – state misfiled in the Five Points workspace, see Finding 1 | Operator creates the Atlas workspace and mints the token. Note that Notion does not offer a BAA on standard plans; the workspace holds venture operations only and never PHI. |
| Pennyone pipeline | **Not registered** – Atlas is absent from the router, see Finding 2 | Add the pipeline when the final brand identity clears art direction |
| Payment rail | **Deferred, correctly** – no revenue at Reconnaissance | Provision at pilot conversion, not before |

---

## Active Plugins

No connection is live and verified for Atlas as of 2026-08-08.

| Service | Account scope | MCP server | Status | Last verified |
|---|---|---|---|---|
| _none_ | | | | |

---

## Target-State Plugins

### Notion – Atlas workspace

| Field | Value |
|---|---|
| Workspace | Atlas – to be created |
| Scope | Projects, Tasks, EHR landscape intelligence, clinical knowledge curation, pilot management, the validation contract |
| MCP server name | `notion-atlas` |
| Status | **Not provisioned.** |
| Environment variable | `NOTION_ATLAS_TOKEN` |
| PHI rule | Venture operations only. No patient record, encounter note or clinical document enters this workspace. |

### Jane App – first EHR adapter

| Field | Value |
|---|---|
| Purpose | The Phase 1 deliverable posts structured SOAP notes into a single EHR. Jane App is the named first target. |
| Status | **Not provisioned.** API access terms, partner requirements and BAA availability all unverified as of this pass. |
| Build shape | Follows the Pennyone architecture the venture index already names – a thin FastMCP service routing one intent through multiple backend adapters. `Integrations/atlas-ehr/` with Jane App as the first adapter and ChiroTouch, Genesis, EZBIS and Prompt EMR behind the same interface. |
| Gating question | Whether Jane App grants third-party API write access at all, and on what partner terms. This is the first Reconnaissance question of the integration lane and it is unanswered. |

### Anthropic API – the clinical documentation layer

| Field | Value |
|---|---|
| Purpose | Ambient capture to structured SOAP, ICD-10 and CPT coding |
| Status | **Not provisioned.** |
| Environment variable | `ANTHROPIC_ATLAS_API_KEY` |
| Note | Atlas manages its own key independently of the Claude Code session credentials, on the Oracle precedent. A BAA must be executed before any real encounter reaches the API. |

### HIPAA-compliant infrastructure

| Surface | Requirement | Status |
|---|---|---|
| Application hosting | BAA-covered. Vercel offers one on Enterprise only – material to the hosting decision and it rules out the portfolio default. | Undecided |
| Database | BAA-covered. Supabase offers one on paid tiers; the Five Points Supabase account is not available to Atlas regardless. | Undecided |
| Logging and audit | BAA-covered access logging over PHI | Undecided |

---

## Tool-Only – No MCP Connection

| Tool | Purpose | Notes |
|---|---|---|
| Chiropractic association networks | Distribution channel | Relationship-led, per the venture thesis |
| Clinical advisory | Arlando Parker Jr., Clinical Advisor | Relationship, not a system |

---

## Secrets

| Environment variable | Service | Status |
|---|---|---|
| `NOTION_ATLAS_TOKEN` | Notion (Atlas workspace) | Not provisioned |
| `ANTHROPIC_ATLAS_API_KEY` | Anthropic (clinical documentation layer) | Not provisioned |
| Jane App credential | First EHR adapter | Vendor terms unverified; variable name follows |

Every row above must also appear in `Manual/secrets-inventory.md`.

---

## Adding a New Plugin

Follow the eight-step sequence in `New Venture/Agents/integrations.md`, with one Atlas-specific step inserted first: confirm whether the surface will touch PHI, and if so confirm the BAA is executed before the key is minted. A row moves to Active only after a live health check returns successfully.

---

*Last updated: 2026-08-08 – The Junction. Registry created; workspace misfiling and Pennyone absence recorded, the HIPAA boundary established as the gating constraint on the integration lane.*
