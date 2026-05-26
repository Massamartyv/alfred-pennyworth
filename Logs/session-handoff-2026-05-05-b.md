# Session Handoff – 2026-05-05 (b)
## Five Points Offer Suite Operationalisation – Multi-Agent Execution

**Mandate:** Apply the 10-layer Offer Operationalisation Framework to the entire Five Points offer suite. Use Human Construct (already complete through Layer 4 example) as the reference. Deploy a multi-agent team. Prioritise correctness, cohesion and depth over speed.

**Resume from:** A fresh Claude Code session at `~/Alfred Pennyworth/`. Full Opus context. Reference this file path explicitly to the new Alfred.

---

## What Just Happened

The session that produced this handoff resolved the entire MCP infrastructure stack and proved the Layer 4 Stripe architecture end-to-end on a single offer (Human Construct). Two-thirds of the elapsed time was infrastructure repair, one-third was offer work. The infrastructure is now stable and the offer architecture pattern is proven.

### Infrastructure repaired

Three rounds of Claude Desktop restarts diagnosed a chain of `.mcp.json` issues:

1. The file lacked the required `mcpServers` wrapper key. Claude Desktop silently ignored it. Fixed.
2. The Vercel package `@vercel/mcp` does not exist on npm – Vercel publishes adapter libraries, not a CLI server. Removed the entry. To be revisited via the hosted endpoint at `mcp.vercel.com` if needed.
3. **Root cause for everything else:** Claude Desktop launches under macOS launchd, not from a shell. Its parent process never has `.env` values, so `${VAR}` substitution in `.mcp.json` substitutes against an empty namespace and leaves the literal placeholder. Every project MCP was receiving `NOTION_TOKEN=${NOTION_FIVEPOINTS_TOKEN}` as a 30-character literal string. Notion-fivepoints returned 401 because the literal string is not a valid token. Stripe alone crashed at startup because its validator rejects keys that do not begin with `sk_` or `rk_`. Pennyone, instantly, strava all "loaded" but were silently broken.

**The canonical fix:** every `.mcp.json` entry now uses a `/bin/bash -c` wrapper that sources `.env` directly before exec'ing the server. Variable renames (NOTION_TOKEN, STRIPE_SECRET_KEY) are handled inline. This bypasses Claude Desktop's substitution entirely and is robust against any future change in how Claude Desktop handles env.

The current `.mcp.json` is the canonical reference – do not regress it.

### Offer work completed (Human Construct)

Layers 1, 2, 3 are locked with operator sign-off (from the 2026-05-04 session). Layer 4 design landed and was approved with five gating decisions resolved:

| Question | Decision |
|---|---|
| Test vs live mode | Live (only `sk_live_` key in `.env`); test work uses clearly-marked draft customers/invoices that are deleted after verification |
| Webhook destination | Supabase Edge Function on Five Points project |
| Tax behaviour | `tax_code: txcd_20030000` (consulting) on product, `tax_behavior: exclusive` on invoice items, Stripe Tax engine for location-based calculation. **Tax setup itself has unresolved questions – see Pending Operator Decisions below.** |
| Customer creation point | At scoping, post-qualification |
| Coupon stacking | Capped at one stackable concession per invoice (avoids Stripe's compounding maths) |

Layer 4 example built end-to-end against live Stripe, math verified to the dollar:

- Coupon `hc_intake_5` created (5% off, once duration, full metadata) – **persists in Stripe**
- Product `prod_USqqPx1mKnAgyC` "Human Construct – Build" created with tax_code and full metadata – **persists in Stripe**
- Test customer + draft invoice + line item created → math verified ($27,500 − 5% = $26,125 exactly) → all three deleted → catalogue objects retained

This is the proven pattern for every other Build product across the suite.

### Notion infrastructure built

- FP **Decision Log** database created at `35784316-643e-81af-8fcd-c87a9e3bd68d` (data_source `35784316-643e-81c4-a03c-000bd3edb316`). Mirrors personal canonical schema with two FP additions: Type select (Decision blue / Issue red) per the handoff request, and Studio select (9 options matching the seven-studio + two-shared-resources venture filing standard).
- FP Tasks DB extended with **Execution Mode** select (Agent / Human / Hybrid).
- Both indexed in `MEMORY.md`.

---

## Resume Protocol

1. Open Claude Code at `~/Alfred Pennyworth/`.
2. **Verify MCP state.** Confirm via ToolSearch that the following are loaded: `notion-fivepoints`, `stripe-fivepoints`, `supabase-fivepoints`, `pennyone`, `instantly`, `strava`. If any missing, see Infrastructure State below for restart playbook.
3. **Read this handoff in full.** Then read the four Human Construct layer artefacts in `.working/` so the reference template is in working memory:
   - `human-construct-direction.md`
   - `human-construct-pricing.md`
   - `human-construct-phasing.md`
   - `human-construct-stripe-integration.md`
   - (also `human-construct-reconnaissance.md` for the industry research)
4. **Mark a session chapter** titled "Offer Suite Operationalisation – Pillar Dispatch".
5. **Dispatch the 5 Pillar Orchestrators in parallel** via Agent calls (Opus each). The orchestration brief for each Pillar Orchestrator is in this file under "Pillar Orchestrator Briefs" – pass that section verbatim to each Opus.
6. **Hold the parent thread for cross-pillar coherence.** As the Pillar Orchestrators report back, manage suite-wide consistency (pricing ladders, ATM rung mapping, naming conventions, coupon reuse).
7. **Surface blockers to operator** through the chain immediately when they arise. Do not let agents spin on questions only the operator can answer.
8. **Lock the work** through Manor Protocol gates – Direction and Critique are operator-touched.
9. **Write the next handoff** at session end.

---

## The Mandate – What the Next Session Is Doing

Apply the 10-layer Offer Operationalisation Framework to every offer in the Five Points Digital Studio suite. The framework was designed in the prior 2026-05-04 session and proven against Human Construct.

**Outcomes expected by end of next session:**

- Every offer in the catalogue has its 10-layer artefact set drafted in `.working/offer-suite/{pillar}/{offer-slug}/`.
- All Stripe catalogue objects (products, prices, coupons) created and live.
- All offers placed in the Priestley ATM (Audit → Blueprint → Silver → Gold → Platinum) with the rung explicitly named.
- Pricing ladders coherent across the suite.
- Naming consistent.
- Webhook architecture stubbed (URLs pending Layer 5 Edge Function build).
- A Decision Log entry in the FP Notion Decision Log for every significant architecture choice made.
- A new handoff for whatever is left.

**Out of scope for the next session (deferred to a later one):**

- Layer 5 Notion Project / Task templates and the Edge Function that drives webhook automation. Layer 5 work happens after the suite is laid out at Layers 1-4.
- Live Stripe transaction testing against real prospects.
- The Vercel MCP integration question.
- Tax setup beyond the `tax_code` and `tax_behavior` already chosen.

---

## The Agent Team Architecture

### Layer 0 – Orchestrator (the next session's main thread)

**Role:** COO equivalent. Coordinates the Pillar Orchestrators. Holds suite-wide context. Surfaces blockers up to the operator.

**Tasks:**
- Read this handoff, the four Human Construct artefacts, and key memory files.
- Dispatch the 5 Pillar Orchestrators in a single message (parallel Agent calls).
- Track each Pillar Orchestrator's progress and gate results.
- Reconcile cross-pillar coherence – pricing tiers ladder, ATM rungs map, naming consistent, coupons reused not duplicated.
- Send blockers to operator.
- Lock the work via Critique gate.
- Write the next handoff.

### Layer 1 – Pillar Orchestrators (5x Opus, parallel)

One per pillar. Each receives a Pillar Orchestrator Brief (below). Each holds its own pillar-scoped context, dispatches Sonnet sub-agents per offer in their pillar, reviews and critiques the Sonnet output through the Manor Protocol, and reports back to Layer 0.

The five pillars (per Human Construct's Layer 1 Direction document, with sub-pillar refinements visible in current Stripe catalogue):

| Pillar | Domain | Sample Existing Offers in Stripe |
|---|---|---|
| 1 – AI Education | AI workshops, seminars, courses, certifications | (none in Stripe yet – build from spec) |
| 2 – AI Operations | Operational intelligence, automation, agent infrastructure consulting | (Total Transformation includes elements – needs disaggregation) |
| 3 – Content Engine | Content production, paid media, social media management, marketing automation | (Brand Launchpad Silver and AI Powered Brand Ecosystem Gold include elements) |
| 4 – Brand and Design | Brand identity, brand system, website design, app UI/UX design | 4.2 Full Website Design Gold, 4.3 App UI/UX Design Gold |
| 5 – Digital Platforms | Web development, application development, custom builds | 5.1 Rapid Site Build Silver, 5.1 Custom Website Development Gold, 5.1 Digital Platform Build Platinum, 5.2 MVP Application Build Gold, 5.2 Full Application Development Platinum |

Plus the **Strategic Advisory** track (Human Construct sits here, Platinum core) – treat as completed reference, not a pillar to operationalise from scratch.

### Layer 2 – Sonnet Executors (multiple per Pillar Orchestrator)

The Pillar Orchestrator dispatches one Sonnet executor per offer in their pillar. Each Sonnet runs the full 10-layer framework on its assigned offer, drafting artefacts to `.working/offer-suite/{pillar}/{offer-slug}/layer-{n}.md`.

Sonnet executors do not commit work to Notion or Stripe. They produce drafts. The Pillar Orchestrator reviews and locks. Material writes to Notion and Stripe happen via the Pillar Orchestrator (or back through the Layer 0 thread for cross-pillar artefacts like shared coupons).

Recommended dispatch pattern for each Sonnet executor:

```
Subagent type: general-purpose
Model: sonnet
Prompt: <below>
```

Sonnet executor prompt template (adapt per offer):

> You are operationalising one offer in the Five Points Digital Studio catalogue. Your offer is {offer name and pillar}.
>
> The 10-layer Offer Operationalisation Framework, plus the reference template (Human Construct), are documented in:
> - `~/Alfred Pennyworth/Logs/session-handoff-2026-05-05-b.md` (this file's section "The 10-Layer Framework")
> - `~/Alfred Pennyworth/.working/human-construct-direction.md` through `human-construct-stripe-integration.md` (reference)
>
> Your task: draft Layers 1 through 4 for {offer name}. Place each artefact at `.working/offer-suite/{pillar}/{offer-slug}/layer-{n}.md`. Do not write to Notion or Stripe. Do not finalise anything. Return a one-page summary of what you drafted, with explicit gating questions for the Pillar Orchestrator.
>
> Quality bar: every layer artefact must be at the same depth, voice and rigour as the Human Construct reference. Match the British English spelling, no em dashes, no Oxford comma, no contractions, en dashes for ranges. Voice is Alfred – composed, precise, direct, no filler.
>
> Surface blockers explicitly. The Pillar Orchestrator will route them up the chain.

---

## Pillar Orchestrator Briefs

Pass each of these verbatim (adapted with `{pillar_n}`) when dispatching the 5 Pillar Orchestrators.

### Common preamble (use for all 5)

> You are the Pillar Orchestrator for Five Points Digital Studio's Pillar {N} – {Pillar Name}. You are running an Opus thread that coordinates the operationalisation of every offer in your pillar.
>
> **Read first:**
> 1. `~/Alfred Pennyworth/Logs/session-handoff-2026-05-05-b.md` (the parent handoff)
> 2. `~/Alfred Pennyworth/.working/human-construct-direction.md` through `human-construct-stripe-integration.md` (reference template – your offers should match this depth)
> 3. `~/Alfred Pennyworth/.claude/CLAUDE.md` and `~/.claude/CLAUDE.md` for voice, conventions, and Manor Protocol gates
>
> **Your tasks:**
> 1. **Inventory.** List every offer that exists in your pillar. Source: existing Stripe catalogue (use `mcp__stripe-fivepoints__list_products`), the reconnaissance file `human-construct-reconnaissance.md`, and any Notion artefacts under FP Sphere "Offers" or similar. Surface offers that should exist but do not yet (gaps in the ATM ladder).
> 2. **ATM Mapping.** Place each offer in the Priestley Ascending Transaction Model: Audit, Blueprint, Silver, Gold, Platinum. Flag overlaps and gaps. Reference: `MEMORY.md` entry "Priestley ATM as Five Points offer architecture".
> 3. **Dispatch.** For each offer, dispatch a Sonnet Executor sub-agent (template in the parent handoff) to draft Layers 1-4 of the 10-layer framework. Send all dispatches in parallel.
> 4. **Critique.** Review each Sonnet's draft against the Human Construct reference. Use the Manor Protocol Critique gate – flag gaps, push back on weak Direction artefacts, validate pricing math, ensure phasing is realistic.
> 5. **Lock.** Once your offers' Layers 1-4 are drafted to standard, write a pillar-level summary at `.working/offer-suite/{pillar}/_pillar-summary.md` and report back to the parent thread.
>
> **Escalation triggers (send up the chain immediately):**
> - Pricing decision requires operator judgment (new value triggers, ceiling above $100K, floor below $5K)
> - Scope boundary requires operator definition (what's included vs separate engagement)
> - Two offers overlap to a degree that risks cannibalisation
> - Naming or positioning requires operator brand voice
> - A Stripe write would touch existing customer transaction data
> - Tax/legal questions
>
> **Do not do without operator approval:**
> - Finalise any invoice
> - Modify or delete any existing Stripe customer
> - Set the webhook endpoint URL (waiting on Layer 5)
> - Retire or archive any existing Stripe product (the catalogue contains pre-Priestley offers; their fate is operator's call, not yours)
>
> **Voice and conventions:**
> - British English spelling, no em dashes, no Oxford comma, no contractions
> - Direct, no filler, no ceremony
> - Use en dashes for ranges
> - Romance possessives ("of the company" not "company's")
> - Use numerals for 10+, write out under 10
> - Always run a confidence check on yourself: are you at 80%+ on operator intent? If not, ask before spending tokens.
>
> Return your final report as a structured markdown summary.

### Pillar 1 – AI Education

Domain: AI workshops, seminars, courses, certifications, learning experiences. Where Five Points teaches the AI literacy that enables the buyer to engage downstream with the Operations and Strategic Advisory tiers.

Initial offer hypothesis (to be confirmed/extended by the inventory):

| ATM Rung | Offer | Format | Notes |
|---|---|---|---|
| Audit | AI Literacy Snapshot | 60-min assessment + report | Builds the funnel |
| Blueprint | AI Roadmap Workshop | Half-day session, customised report | Premium audit, sets up Silver/Gold |
| Silver | AI Foundations Cohort | 4-week cohort, group-format | Recurring, scalable |
| Gold | AI for Founders Intensive | Bespoke 1-1 multi-week intensive | Higher touch |
| Platinum | (typically not at this rung – education is sub-Platinum) | – | Confirm |

Initial dispatches: assume 4-5 offers across the ATM rungs.

### Pillar 2 – AI Operations

Domain: Operational intelligence consulting, business process automation, agent infrastructure design, AI workflow integration, internal AI deployment. Where Five Points builds the operational backbone (downstream of education, upstream of full Strategic Advisory).

Initial offer hypothesis:

| ATM Rung | Offer | Format | Notes |
|---|---|---|---|
| Audit | AI Operations Audit | 2-3 day operational assessment | Funnel entry |
| Blueprint | Operations Architecture Blueprint | 2-week design engagement | Premium audit |
| Silver | Targeted Automation Build | 4-6 weeks, scope-capped | One workflow, one team |
| Gold | Operations Overhaul | 8-12 weeks, multi-workflow | Department-scale automation |
| Platinum | (consider if it exists or gets routed to Human Construct) | – | Confirm boundary |

Important: this pillar overlaps with Human Construct (Strategic Advisory Platinum). The boundary needs precise definition – operator should weigh in if the inventory surfaces ambiguity.

### Pillar 3 – Content Engine

Domain: Content production, paid media, social media management, marketing automation, content strategy. Where Five Points builds and runs the marketing machine.

Initial offer hypothesis:

| ATM Rung | Offer | Format | Notes |
|---|---|---|---|
| Audit | Content Audit | Single deep-dive | Funnel entry |
| Blueprint | Content Strategy Blueprint | 2-3 week strategy engagement | Premium audit |
| Silver | Content Strategy and Launch | One-time strategy + initial production | Existing in bundle |
| Gold | Content Engine setup + monthly retainer | First month included in Gold bundle | Existing |
| Gold continuity | Monthly Content Retainer | Recurring | Build separate pricing tiers |
| Platinum | Full Marketing Operations | Bespoke retained | Premium tier |

This pillar has the most potential SKU complexity (paid media, organic, content production are all somewhat distinct). Inventory carefully.

### Pillar 4 – Brand and Design

Domain: Brand identity, brand systems, website design, app UI/UX design, design systems. The visual and identity layer.

Existing in Stripe:
- 4.2 Full Website Design – Gold (`prod_UDN8Aa0jXr84WM`)
- 4.3 App UI/UX Design – Gold (`prod_UDN8RJTl5Xj6ic`)

Initial offer hypothesis:

| ATM Rung | Offer | Format | Notes |
|---|---|---|---|
| Audit | Brand Audit | – | Funnel entry |
| Blueprint | Brand Strategy Blueprint | – | Premium audit |
| Silver | Brand Identity Sprint, Website Design Sprint | Existing in Brand Launchpad bundle | Confirm and extract |
| Gold | Comprehensive Brand Identity, Full Website Design | Existing | Confirm pricing |
| Gold | App UI/UX Design | Existing | Confirm pricing |
| Platinum | Bespoke brand and design system | – | Confirm if needed |

### Pillar 5 – Digital Platforms

Domain: Web development, application development, custom platforms, technical builds. The execution layer of the digital experience.

Existing in Stripe:
- 5.1 Rapid Site Build – Silver (`prod_UDN83nqcqCE9En`)
- 5.1 Custom Website Development – Gold (`prod_UDN90jAXDYSHjH`)
- 5.1 Digital Platform Build – Platinum (`prod_UDN9qYPdxO8K3r`)
- 5.2 MVP Application Build – Gold (`prod_UDNAkApFj5YmxQ`)
- 5.2 Full Application Development – Platinum (`prod_UDNAYifeHJ3CRI`)

This pillar has the most existing structure. Initial dispatches: validate pricing against Layer 2 framework, run Layers 1-4 on each, surface ATM mapping (Audit and Blueprint rungs are missing here – operator may want them).

---

## The 10-Layer Framework (Reference)

The framework was provided as a master prompt at the start of the prior 2026-05-04 session. The full reference is the Human Construct artefact set in `.working/`. Summary of the layers:

| Layer | Name | What It Establishes | Reference |
|---|---|---|---|
| 1 | **Direction** | Positioning, promise, scope (in/out), prerequisites, engagement shape, success criteria, ATM rung, differentiation | `human-construct-direction.md` |
| 2 | **Pricing Strategy** | Floor, ceiling, value triggers, posted-price strategy, payment structure, irreducible recurring unit, concession policy, margin and LTV math | `human-construct-pricing.md` |
| 3 | **Phasing and Milestones** | Named phases, phase activities, internal milestones, client-facing milestones, payment-release mapping, decision-point protocol | `human-construct-phasing.md` |
| 4 | **Stripe Integration** | Products, prices, coupons, customer-creation point, invoice mechanics, webhook events for downstream automation | `human-construct-stripe-integration.md` |
| 5 | Notion Project and Task Architecture | Project template, task template auto-generation on Stripe webhook, glossary tag relations, execution mode per task | (deferred – build after suite-wide Layer 4 lands) |
| 6 | Email and Communications Sequences | Sales, activation, delivery, offboarding, post-engagement comms | (deferred) |
| 7 | SOP and Resource Library | SOPs per phase, foundational SOPs (Onboarding, Project Delivery, QA, Offboarding) | (deferred) |
| 8 | Team, Roles, RACI, Agentic Assignment | Per-phase role identification, agent-first default, activation status | (deferred) |
| 9 | QA Checkpoints | Internal QA per phase, client-facing approval gates, brand and craft standards, escalation path | (deferred) |
| 10 | Post-Engagement and Reflection Ritual | Retention, upsell logic, case study capture, referral mechanic, post-engagement reflection | (deferred) |

The next session's mandate is **Layers 1-4 across the entire suite**. Layers 5-10 come in a subsequent session, after the suite-wide architecture is laid out.

The QA Interrogation – the 12-question challenge before sign-off – also defers to the post-Layer-4 phase per offer.

---

## Manor Protocol Gates

The Manor Protocol lifecycle: **Reconnaissance → Direction [gate] → Execution → Critique [gate] → Release**.

Two operator-touched gates on every offer:

1. **Direction gate.** After Layer 1 Direction is drafted, before Layers 2-4 execute. Operator confirms positioning, promise, scope, ATM rung. The Pillar Orchestrator presents Direction summaries up the chain; the parent thread surfaces them to the operator in batches (avoid 12 separate questions; batch by pillar).
2. **Critique gate.** After Layers 2-4 are drafted and the Pillar Orchestrator has run its review. Operator confirms or pushes back on pricing, phasing, Stripe architecture per offer. Again batched by pillar.

These gates are non-negotiable. Even with the operator's standing approval to "move forward," significant choices (a $200K ceiling, a new payment structure, a previously-unseen offer category) must surface explicitly.

---

## Quality Bar

- **Cohesion.** Pricing tiers ladder cleanly across the ATM. A Gold offer in Pillar 5 should be priced sensibly relative to a Gold offer in Pillar 4. Operator's mental model is one studio, not five disconnected catalogues.
- **Voice.** Every artefact, every Stripe metadata field, every Notion description must hold the Alfred voice. British English, no em dashes, no Oxford comma, no contractions, en dashes for ranges. Direct, composed, no filler.
- **Depth.** Every Direction artefact has the same rigour as `human-construct-direction.md`. Every Pricing artefact has full margin math. Every Phasing artefact has decision-point protocols. No skimping for speed.
- **Coupon reuse.** The five HC coupons (`hc_intake_5`, `hc_multiventure_25`, `hc_evo_bundle_5`, `hc_evo_quarterly_10`, `hc_evo_annual_25`) may be reused across offers where applicable. Do not duplicate. Where a new concession is genuinely offer-specific, name it with the offer-slug prefix.
- **Stripe metadata.** Every Stripe product carries: `offer_rung`, `atm_position`, `pillar`, `delivery_format`, `visibility`. Every coupon carries: `offer`, `applies_to`, `concession_type`. This is what makes the Notion linkage possible later.
- **Decision Log.** Every significant architectural choice gets a Decision Log entry in the FP Notion Decision Log (`35784316-643e-81af-8fcd-c87a9e3bd68d`). Title Case verb-led titles. Three-tier reasoning depth scaled to Reversibility. Status: Done makes the entry immutable.
- **Confidence threshold.** Default trigger for asking the operator: confidence below 80% on intent. Use the AskUserQuestion widget (in batches) – it costs ~50 tokens and saves multiples of that in re-work.

---

## Escalation Protocol

Send up the chain (Sonnet → Pillar Orchestrator → Layer 0 → Operator) when:

- Pricing decision requires operator judgment that exceeds the prior layers' established frameworks
- A scope boundary needs operator definition
- Two offers overlap meaningfully (cannibalisation risk)
- A live Stripe write would touch existing customer transaction data (anything beyond catalogue object creation)
- Webhook destination URL needs to be set
- Naming or positioning requires operator brand voice
- Tax or legal question
- Confidence below 80% on operator intent

The escalation should arrive at the operator level **batched by pillar**, not as a stream. Avoid the operator answering 30 single questions when 5 grouped questions per pillar serve them better.

---

## Infrastructure State

### MCP Configuration

`.mcp.json` at `~/Alfred Pennyworth/.mcp.json` uses bash wrappers on every entry. Do not regress this. The current shape per server:

```json
"<server>": {
  "type": "stdio",
  "command": "/bin/bash",
  "args": [
    "-c",
    "set -a; source '/Users/martyspicer/Alfred Pennyworth/.env'; set +a; <env aliasing if needed>; exec <real command>"
  ]
}
```

The six servers loaded: `notion-fivepoints`, `supabase-fivepoints`, `stripe-fivepoints`, `pennyone`, `instantly`, `strava`.

If a server is missing on the next session, the resolution path:

1. Run `direnv allow` from project root if not already done.
2. Quit Claude Code/Desktop fully and relaunch.
3. If still missing, inspect the running process env via `ps -ef -E | grep <server>` and confirm the bash wrapper sourced `.env` correctly.
4. If still broken, the issue is likely package-specific – reproduce manually with `bash -c "set -a; source .env; set +a; exec <command>"` and read the stderr.

### Five Points Notion Workspace

Built 2026-05-05 in this session:

- **Headquarters page** (venture root): `473d1e6e-c5be-4cdc-9df0-f58ddfd1a863`
- **Decision Log database**: `35784316-643e-81af-8fcd-c87a9e3bd68d` (data_source `35784316-643e-81c4-a03c-000bd3edb316`). Full canonical schema mirroring personal + Type extension (Decision/Issue, Issue red) + Studio select (9 options for the 7-studio + 2-shared resources structure).
- **Tasks database**: `c12b060f-63a8-4c3a-b7d4-27eed30da695` (data_source `9306f4bf-3e09-48a6-81fd-472de71bcd2a`). Pre-existing, business-evolved variant of personal Tasks. **Execution Mode property added this session** (Agent / Human / Hybrid select).
- **Projects database**: `4a9f9bab-7026-414e-9820-40925b56a7b6` (data_source `9fb39ce7-b133-4535-aeed-6f150ac4df0e`)
- **Sphere Manager (FP-scoped)**: `6c85d630-fcfb-4489-97f9-5ba3d495729d` (data_source `503a63eb-b15c-48ea-bfc1-e663b5dacf3a`)

The Notion FP integration's bot is "Alfred Pennyworth" inside workspace "Five Points Digital Studio" (`81184a5b-89f4-4103-b2e7-6cb7dba96853`).

### Five Points Stripe

- Account: `acct_1PfTxpDH3f10EsHc`, Five Points Digital Studio, **live mode**
- API key in `.env`: `STRIPE_FIVEPOINTS_SECRET_KEY` (prefix `sk_live_*`)

Existing catalogue objects (created in this session):

- Coupon `hc_intake_5`: 5% off, once duration, name "Quarterly Intake Commitment 5%", metadata `{offer: human_construct, applies_to: build_invoice_1, concession_type: in_window_commitment}`
- Product `prod_USqqPx1mKnAgyC`: "Human Construct – Build", tax_code `txcd_20030000`, metadata for offer rung, ATM position, delivery tier, visibility, capacity

Pre-existing legacy products (operator's call on whether to retire):

- `prod_UDNAzu0ECI2hqn` "The Total Transformation – Platinum" (predecessor to Human Construct, may be retired)
- `prod_UDNAQ5u05NUMzO` "Bundle — AI Powered Brand Ecosystem — Gold" (cross-pillar)
- `prod_UDNAWtZLLrIOi2` "Bundle — The Brand Launchpad — Silver" (cross-pillar)
- `prod_UDNAYifeHJ3CRI` "5.2 — Full Application Development — Platinum"
- `prod_UDNAkApFj5YmxQ` "5.2 — MVP Application Build — Gold"
- `prod_UDN9qYPdxO8K3r` "5.1 — Digital Platform Build — Platinum"
- `prod_UDN90jAXDYSHjH` "5.1 — Custom Website Development — Gold"
- `prod_UDN83nqcqCE9En` "5.1 — Rapid Site Build — Silver"
- `prod_UDN8RJTl5Xj6ic` "4.3 — App UI/UX Design — Gold"
- `prod_UDN8Aa0jXr84WM` "4.2 — Full Website Design — Gold"

Note: `list_products` returned 10 by default. There may be more if the page size is exceeded. Run a paged list to confirm full inventory.

### Other

- direnv: allowed for `~/Alfred Pennyworth/`. `.envrc` exists, `.env` exists, both in permission-denied path under user settings (cannot read directly, can source via bash).
- Pennyone health: personal pipeline 7 platforms ok, FP pipeline 1 platform (Instagram). Marty Gras, Paradigm, Lillie and Lynette have no key set yet.
- Instantly: 402 Payment Required – Instantly workspace has no active paid plan. Blocks Layer 6 (Email Sequences). **Operator deferred this**.
- Vercel: removed from `.mcp.json`. To be revisited.

---

## Locked Decisions (this session)

In addition to the Five Decisions listed at the top, the following architectural choices are locked and should not be reopened by Pillar Orchestrators without operator approval:

1. **Five Points Decision Log is a standalone FP-workspace database**, not cross-shared from personal. Built fresh with the Type extension (Decision/Issue) and Studio property (9 options matching venture filing standard).
2. **FP Tasks database extended with Execution Mode**, kept as the venture-existing DB rather than being rebuilt.
3. **Two-product Stripe architecture for Human Construct**: Build (custom-priced) + Evolution (3 preset prices). Pattern recommended for other Build/Continuity offers across the suite.
4. **`hc_intake_5` coupon is reusable** for any offer's "in-window quarterly intake commitment" concession, not Human Construct exclusive. Pillar Orchestrators may apply it to other offers' intake invoices.
5. **Coupon stacking capped at one per invoice** in policy. Multiple concessions on a single invoice get the second applied as manual line-item discount.
6. **Customer creation point: at scoping post-qualification**, across all offers.
7. **Webhook destination: Supabase Edge Function on Five Points project**, single endpoint dispatching to Notion. URL itself is pending Layer 5 build.
8. **Tax: tax_code `txcd_20030000` (consulting), tax_behavior `exclusive`**, Stripe Tax engine for location-based calculation. Tax setup details pending operator legal/accounting input.

---

## Pending Operator Decisions

The next session should batch these and surface them to the operator at appropriate Manor Protocol gates.

### Already-known pending

1. **Tax setup multi-state.** Five Points business is registered in **Cheyenne, Wyoming**. Operations currently from **Georgia**, moving soon to **New York**. Operator stated they do not have a deep understanding of Stripe Tax. The next session should not finalise Stripe Tax configuration without:
   - Confirming Stripe Tax is enabled on the account
   - Choosing whether the company collects and remits per state (likely yes for NY) or operates as service-only (likely no sales tax in most states for consulting)
   - Reviewing the Wyoming registration vs operating-state nexus implications
   - Recommend: operator should consult their accountant before final tax setup. The current `tax_behavior: exclusive` and `tax_code: consulting` choice is sensible default; do not change without the legal review.

2. **Vercel MCP integration path.** Removed from `.mcp.json` because `@vercel/mcp` does not exist. To be revisited via `mcp.vercel.com` hosted endpoint or via a third-party package like `@robinson_ai_systems/vercel-mcp`. Not blocking suite operationalisation.

3. **Instantly billing.** Workspace on free tier, 402 Payment Required. Blocks Layer 6 Email Sequences when that work begins.

4. **Pennyone keys for Marty Gras, Paradigm, Lillie and Lynette.** No keys set in `.env`. Pillar Orchestrators may not need these; flag if they do.

### To be surfaced by the Pillar Orchestrators

Each Pillar Orchestrator will likely surface:

- The fate of legacy Stripe products (retire vs migrate vs reposition)
- The Audit and Blueprint rungs for pillars where they are missing
- Any pricing decisions outside established ranges
- Any boundary disputes with Human Construct (especially Pillar 2 AI Operations)
- The Bundle SKU strategy (cross-pillar bundles like "Brand Launchpad" – do they survive the rebuild?)

---

## Reference Paths

### Layer artefacts (existing)

- `~/Alfred Pennyworth/.working/human-construct-direction.md`
- `~/Alfred Pennyworth/.working/human-construct-pricing.md`
- `~/Alfred Pennyworth/.working/human-construct-phasing.md`
- `~/Alfred Pennyworth/.working/human-construct-stripe-integration.md`
- `~/Alfred Pennyworth/.working/human-construct-reconnaissance.md`

### Where new artefacts go

- `~/Alfred Pennyworth/.working/offer-suite/pillar-1-ai-education/{offer-slug}/layer-{n}.md`
- `~/Alfred Pennyworth/.working/offer-suite/pillar-2-ai-operations/{offer-slug}/layer-{n}.md`
- `~/Alfred Pennyworth/.working/offer-suite/pillar-3-content-engine/{offer-slug}/layer-{n}.md`
- `~/Alfred Pennyworth/.working/offer-suite/pillar-4-brand-and-design/{offer-slug}/layer-{n}.md`
- `~/Alfred Pennyworth/.working/offer-suite/pillar-5-digital-platforms/{offer-slug}/layer-{n}.md`
- Pillar summaries: `~/Alfred Pennyworth/.working/offer-suite/pillar-{n}/_pillar-summary.md`
- Suite-wide summary: `~/Alfred Pennyworth/.working/offer-suite/_suite-summary.md`

### Memory and configuration

- Memory index: `~/.claude/projects/-Users-martyspicer-Alfred-Pennyworth/memory/MEMORY.md`
  - "Priestley ATM as Five Points offer architecture" (`priestley_atm.md`)
  - "25k Battle Plan status" (`battle_plan_status.md`) – note: stale, do not anchor decisions on it
  - "Agent owns the platform" (`agent_owns_platform.md`)
  - "Five Points workspace – key IDs" (in MEMORY.md directly)
- Global instructions: `~/.claude/CLAUDE.md`
- Project instructions: `~/Alfred Pennyworth/.claude/CLAUDE.md`
- MCP config: `~/Alfred Pennyworth/.mcp.json`
- Env: `~/Alfred Pennyworth/.env` (gitignored, requires direnv or bash sourcing)

### Prior handoffs (for continuity context)

- `~/Alfred Pennyworth/Logs/session-handoff-2026-05-04.md` – initial Human Construct Layers 1-3 + the MCP gate diagnosis chain
- `~/Alfred Pennyworth/Logs/session-handoff-2026-05-05.md` – Blueprint Sports venture conception (separate work, ignore for this mandate)

---

## Final Notes for the Resuming Alfred

Three things matter most.

**First.** The infrastructure is now stable. Do not waste a single token rediagnosing the substitution issue. The bash wrapper in `.mcp.json` is the canonical fix. If something breaks, read the prior handoff (`session-handoff-2026-05-04.md`) for the diagnostic chain that got us here.

**Second.** The Human Construct Layer 1-4 artefacts are the gold-standard reference. Pillar Orchestrators should treat them as the depth, voice, and rigour to match. Sonnet executors should read them before drafting. Any artefact that does not match this standard should be rejected at the Pillar Orchestrator's Critique gate and re-drafted.

**Third.** The operator's stated priority: "I don't want to sacrifice security, in-depth understanding, and thoroughness for speed." Multi-agent execution is the chosen mechanism for getting speed without sacrificing depth. Do not under-utilise the agent team. A single Opus thread trying to do all of this alone is the wrong shape. Dispatch wide.

The operator has authorised this work to run autonomously up to the Manor Protocol gates. Surface blockers in batches. Be precise about what you need from them and why. The cleaner the gate questions, the faster the gate clears, the less the operator's attention is taxed.

Ship it well.

---

*Handoff complete. Resume by reading this file end-to-end, then dispatching the 5 Pillar Orchestrators per the briefs above.*
