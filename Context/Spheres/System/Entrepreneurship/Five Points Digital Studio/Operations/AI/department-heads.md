---
file_type: reference
document_type: department_heads
venture: Five Points Digital Studio
status: active
last_updated: 2026-04-05
---

# Department Heads -- Five Points Digital Studio

The organisational structure of AI-assisted roles within Five Points. Each department head is a role that Alfred assumes or dispatches a subagent into when work enters that department's scope. Department heads are not separate AI models -- they are role definitions that shape context loading, crew selection and execution parameters.

---

## How Department Heads Work

When a task enters the system:

1. Alfred identifies which department head owns the task
2. Loads the department head's primary files for context
3. Classifies the crew type (Strategist, Creator, Evaluator, Maestro, Validator, Explorer)
4. Applies the token budget tier from `token-budget-framework.md`
5. Applies the execution tier from `agent-guidelines.md`
6. Executes directly or dispatches a subagent with the role brief

---

## Active Department Heads

### Head of Creative

| Field | Value |
|---|---|
| Domain | Brand identity, visual direction, content quality, aesthetic standards |
| Primary files | `creative-director.md`, `personal-brand-identity.md`, Marketing & Sales/_index.md |
| Typical crews | Creator (design, copy), Evaluator (brand consistency checks), Validator (pre-publish review) |
| Reports to | You (Creative Director) directly through Alfred |

**Specialist roles under Head of Creative:**

| Role | Scope | Typical Crews |
|---|---|---|
| Brand Strategist | Brand positioning, identity evolution, competitive differentiation | Strategist, Explorer |
| Art Director | Visual direction for web, social, print -- all design output | Creator, Evaluator |
| Content Strategist | Content calendar, platform strategy, editorial planning | Strategist, Maestro |
| Copywriter | Email copy, web copy, social copy, platform-specific content | Creator |

---

### Head of Production (Production Executive)

| Field | Value |
|---|---|
| Domain | Web development, deliverable production, build quality, deployment |
| Primary files | Product Development/_index.md, Operations/Clientele/_clients-registry.md |
| Typical crews | Creator (building), Evaluator (QA), Maestro (multi-step builds) |
| Reports to | Alfred |

**Production scope:**
- Website builds (landing pages, full sites)
- Short-form content production
- Long-form content production
- Podcast production
- Strategy decks and documentation

---

### Head of Operations (Operations Executive)

| Field | Value |
|---|---|
| Domain | Day-to-day delivery, client management, SOPs, systems, tools |
| Primary files | Operations/_index.md, Operations/Clientele/_clients-registry.md, Operations/SOPs/_sop-registry.md |
| Typical crews | Maestro (workflow coordination), Validator (SOP compliance), Creator (documentation) |
| Reports to | Alfred |

**Operations scope:**
- Client onboarding and offboarding
- Delivery tracking and deadline management
- SOP creation and maintenance
- Tool and integration management
- Account management

---

### Head of Finance (Finance Executive)

| Field | Value |
|---|---|
| Domain | Revenue tracking, expenses, projections, invoicing, financial compliance |
| Primary files | Finances/_index.md |
| Typical crews | Strategist (financial analysis), Validator (compliance), Creator (reports) |
| Reports to | Alfred |

**Finance scope:**
- Revenue tracking and MRR monitoring
- Expense categorisation and budgeting
- Invoice generation and tracking
- Cash flow projections
- Tax preparation support

---

## Token Budget by Department

Each task is classified independently using `token-budget-framework.md`. The table below shows typical tier defaults per department, but the task classification always takes precedence.

| Department Head | Typical Light | Typical Standard | Typical Heavy |
|---|---|---|---|
| Head of Creative | Social captions, email subject lines | Blog posts, content briefs, case studies | Brand narrative documents, campaign plans |
| Head of Production | Task creation, deadline flags | Weekly status reports, meeting briefs | SOPs, full website builds |
| Head of Operations | CRM updates, reminders, scheduling | Client proposals, onboarding packets | Competitive research, territory plans |
| Head of Finance | Invoice runs, expense logging | Monthly P&L, cash flow reports | Annual forecasting, margin analysis |

---

## Activating a Department Head

All department heads are currently role definitions only. When ready to automate:

1. Create an agent definition in `~/Alfred Pennyworth/Agents/` with the mission brief
2. Update this file to mark the department head as "Active -- automated"
3. Configure the agent to read this file, `agent-guidelines.md` and `token-budget-framework.md` at session start
4. Begin logging performance data to `Operations/AI/Logs/`
5. Review after 30 days and adjust

---

*Five Points Digital Studio -- Department Heads v1.0 -- April 2026*
