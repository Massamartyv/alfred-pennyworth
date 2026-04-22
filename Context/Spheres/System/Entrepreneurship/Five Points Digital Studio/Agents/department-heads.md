---
file_type: reference
document_type: department_heads
venture: Five Points Digital Studio
status: active
last_updated: 2026-04-22
---

# Department Heads – Five Points Digital Studio

The organisational structure of AI-assisted roles within Five Points. Each department head is a role that Alfred assumes or dispatches a subagent into when work enters that studio scope. Department heads are not separate AI models – they are role definitions that shape context loading, crew selection and execution parameters.

---

## How Department Heads Work

When a task enters the system:

1. Alfred identifies which department head owns the task
2. Loads the department head primary files for context
3. Classifies the crew type (Strategist, Creator, Evaluator, Maestro, Validator, Explorer)
4. Applies the token budget tier from `token-budget-framework.md`
5. Applies the execution tier from `agent-guidelines.md`
6. Executes directly or dispatches a subagent with the role brief

---

## Active Department Heads

### Head of Creative

| Field | Value |
|---|---|
| Studio | Creative |
| Domain | Brand identity, visual direction, content quality, aesthetic standards |
| Primary files | `creative-director.md`, `personal-brand-identity.md`, `Creative/_index.md`, `Creative/Agents/_index.md` |
| Typical crews | Creator (design, copy), Evaluator (brand consistency checks), Validator (pre-publish review) |
| Reports to | You (Creative Director) directly through Alfred |

**Specialist roles under Head of Creative:**

| Role | Scope | Typical Crews |
|---|---|---|
| Brand Strategist | Brand positioning, identity evolution, competitive differentiation | Strategist, Explorer |
| Art Director | Visual direction for web, social, print – all design output | Creator, Evaluator |
| Content Strategist | Content calendar, platform strategy, editorial planning | Strategist, Maestro |
| Copywriter | Email copy, web copy, social copy, platform-specific content | Creator |

---

### Head of Strategy

| Field | Value |
|---|---|
| Studio | Strategy |
| Domain | Market intelligence, competitive analysis, positioning, discovery, research |
| Primary files | `Strategy/_index.md`, `Strategy/Agents/_index.md` |
| Typical crews | Strategist (analysis, positioning), Explorer (market sensing), Maestro (discovery coordination) |
| Reports to | Alfred |

**Specialist roles under Head of Strategy:**

| Role | Scope | Typical Crews |
|---|---|---|
| Market Researcher | Industry landscape, competitive intelligence, trend detection | Explorer, Strategist |
| Positioning Lead | Client positioning, differentiation frameworks, narrative architecture | Strategist |
| Discovery Lead | Client discovery sessions, brief synthesis, strategic recommendations | Strategist, Maestro |

---

### Head of Production

| Field | Value |
|---|---|
| Studio | Production |
| Domain | Web development, deliverable production, build quality, deployment |
| Primary files | `Production/_index.md`, `Production/Agents/_index.md`, `Operations/Clientele/_clients-registry.md` |
| Typical crews | Creator (building), Evaluator (QA), Maestro (multi-step builds) |
| Reports to | Alfred |

**Production scope:**
- Website builds (landing pages, full sites)
- Short-form content production
- Long-form content production
- Podcast production
- Strategy decks and documentation

---

### Head of Growth

| Field | Value |
|---|---|
| Studio | Growth |
| Domain | Revenue generation, offer architecture, sales, BD, partnerships, pipeline |
| Primary files | `Growth/_index.md`, `Growth/Agents/_index.md`, `Growth/Product Development/_index.md` |
| Typical crews | Strategist (pipeline analysis), Creator (proposals), Maestro (multi-touch sequences) |
| Reports to | Alfred |

**Specialist roles under Head of Growth:**

| Role | Scope | Typical Crews |
|---|---|---|
| Business Development Lead | Outbound sequences, partnership development, pipeline generation | Explorer, Strategist |
| Sales Lead | Discovery calls, closing, objection handling, negotiation | Strategist, Maestro |
| Proposal Architect | Proposal drafting from offer templates, value stack construction | Creator |
| Offer Steward | Offer catalogue maintenance, pricing integrity, tier evolution | Strategist, Validator |

---

### Head of Operations

| Field | Value |
|---|---|
| Studio | Operations |
| Domain | Day-to-day delivery, client management, SOPs, systems, tools |
| Primary files | `Operations/_index.md`, `Operations/Agents/_index.md`, `Operations/Clientele/_clients-registry.md`, `Operations/SOPs/_sop-registry.md` |
| Typical crews | Maestro (workflow coordination), Validator (SOP compliance), Creator (documentation) |
| Reports to | Alfred |

**Operations scope:**
- Client onboarding and offboarding
- Delivery tracking and deadline management
- SOP creation and maintenance
- Tool and integration management
- Account management

---

### Head of Finance

| Field | Value |
|---|---|
| Studio | Finance |
| Domain | Revenue tracking, expenses, projections, invoicing, financial compliance |
| Primary files | `Finance/_index.md`, `Finance/Agents/_index.md` |
| Typical crews | Strategist (financial analysis), Validator (compliance), Creator (reports) |
| Reports to | Alfred |

**Finance scope:**
- Revenue tracking and MRR monitoring
- Expense categorisation and budgeting
- Invoice generation and tracking
- Cash flow projections
- Tax preparation support

---

### Head of Administration

| Field | Value |
|---|---|
| Studio | Administration |
| Domain | Legal, compliance, policies, HR, team structure, governance |
| Primary files | `Administration/_index.md`, `Administration/Agents/_index.md` |
| Typical crews | Validator (compliance checks), Creator (policy drafting), Strategist (organisational planning) |
| Reports to | Alfred |

**Specialist roles under Head of Administration:**

| Role | Scope | Typical Crews |
|---|---|---|
| Legal Coordinator | Contract templates, service agreements, NDAs, SOWs | Creator, Validator |
| Compliance Officer | Business registration, insurance, data protection, regulatory | Validator |
| People Lead | Team structure, contractor onboarding, culture, partner hiring criteria | Strategist, Creator |

---

## Token Budget by Studio

Each task is classified independently using `token-budget-framework.md`. The table below shows typical tier defaults per studio, but task classification always takes precedence.

| Department Head | Typical Light | Typical Standard | Typical Heavy |
|---|---|---|---|
| Head of Creative | Social captions, email subject lines | Blog posts, content briefs, case studies | Brand narrative documents, campaign plans |
| Head of Strategy | Quick lookups, data extractions | Competitive briefs, discovery summaries | Full strategic plans, territory analysis, positioning frameworks |
| Head of Production | Task creation, deadline flags | Weekly status reports, meeting briefs | SOPs, full website builds |
| Head of Growth | CRM updates, follow-ups | Proposals, discovery briefs, outbound sequences | Full pipeline strategy, territory plans, pitch decks |
| Head of Operations | Scheduling, reminders | Client proposals, onboarding packets | Process redesigns, tooling migrations |
| Head of Finance | Invoice runs, expense logging | Monthly P&L, cash flow reports | Annual forecasting, margin analysis |
| Head of Administration | Policy updates, filing reminders | Contract drafting, onboarding documentation | Compliance reviews, org design |

---

## Activating a Department Head

All department heads are currently role definitions only. When ready to automate:

1. Create an agent definition in `~/Alfred Pennyworth/Agents/` with the mission brief
2. Update this file to mark the department head as "Active – automated"
3. Configure the agent to read this file, `agent-guidelines.md` and `token-budget-framework.md` at session start
4. Begin logging performance data to `Agents/Logs/`
5. Review after 30 days and adjust

---

*Five Points Digital Studio – Department Heads v2.0 – 2026-04-22*
