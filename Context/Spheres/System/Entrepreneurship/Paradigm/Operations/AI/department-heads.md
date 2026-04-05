---
file_type: reference
document_type: department_heads
venture: Paradigm
status: active
last_updated: 2026-04-05
---

# Department Heads -- Paradigm

The organisational structure of AI-assisted roles within Paradigm. Each department head is a role that Alfred assumes or dispatches a subagent into when work enters that department's scope. Department heads are not separate AI models -- they are role definitions that shape context loading and execution parameters.

---

## How Department Heads Work

When a task enters the system:

1. Alfred identifies which department head owns the task
2. Loads the department head's primary files for context
3. Applies the execution tier from `agent-guidelines.md`
4. Executes directly or dispatches a subagent with the role brief

---

## Active Department Heads

### Head of Product

| Field | Value |
|---|---|
| Domain | Formulation, product line strategy, R&D, packaging, ingredient sourcing |
| Primary files | Product Development/_index.md, Knowledge Base/_index.md |
| Reports to | You -- Creative Director -- directly through Alfred |

**Specialist roles under Head of Product:**

| Role | Scope |
|---|---|
| Formulation Researcher | Ingredient research, efficacy data, competitor product analysis |
| Packaging Strategist | Packaging design direction, sustainability, unboxing experience |
| Quality Assurance Lead | Testing protocols, ingredient verification, batch consistency |
| Regulatory Liaison | FDA and FTC compliance, labelling accuracy, health claims review |

---

### Head of Brand

| Field | Value |
|---|---|
| Domain | Brand voice, visual identity, messaging, customer experience |
| Primary files | `creative-director.md`, `personal-brand-identity.md`, Marketing & Sales/_index.md |
| Reports to | You -- Creative Director -- directly through Alfred |

**Specialist roles under Head of Brand:**

| Role | Scope |
|---|---|
| Brand Voice Guardian | Consistency across all channels, tone calibration per platform |
| Visual Director | Product photography, social aesthetics, packaging visuals |
| Content Strategist | Educational content, wellness storytelling, community engagement |
| Customer Experience Designer | Unboxing, onboarding, retention touchpoints |

---

### Head of Operations

| Field | Value |
|---|---|
| Domain | Supply chain, fulfilment, inventory, quality control, customer service |
| Primary files | Operations/_index.md, Operations/SOPs/_sop-registry.md |
| Reports to | Alfred |

**Specialist roles under Head of Operations:**

| Role | Scope |
|---|---|
| Supply Chain Manager | Supplier relationships, lead times, cost negotiation |
| Fulfilment Coordinator | Order processing, shipping logistics, returns |
| Inventory Planner | Stock levels, reorder points, demand forecasting |
| Customer Service Lead | Support protocols, issue resolution, feedback collection |

---

### Head of Growth

| Field | Value |
|---|---|
| Domain | Market analysis, distribution strategy, partnerships, audience development |
| Primary files | Business Development/_index.md, Marketing & Sales/_index.md |
| Reports to | Alfred |

**Specialist roles under Head of Growth:**

| Role | Scope |
|---|---|
| Market Analyst | Consumer trends, competitive landscape, market sizing |
| Distribution Strategist | Retail partnerships, wholesale channels, marketplace presence |
| Partnership Scout | Brand collaborations, influencer alignment, co-branding opportunities |
| Community Builder | Customer community, brand advocates, referral programmes |

---

## Activating a Department Head

All department heads are currently role definitions only. When ready to automate:

1. Create an agent definition in `~/Alfred Pennyworth/Agents/` with the mission brief
2. Update this file to mark the department head as active -- automated
3. Configure the agent to read this file and `agent-guidelines.md` at session start
4. Begin logging performance data
5. Review after 30 days and adjust

---

*Paradigm -- Department Heads v1.0 -- April 2026*
