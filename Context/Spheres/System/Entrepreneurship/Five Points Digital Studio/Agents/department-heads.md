---
file_type: reference
document_type: department_heads
venture: Five Points Digital Studio
status: active
last_updated: 2026-09-10
---

# Department Heads – Five Points Digital Studio

The organisational structure of AI-assisted roles within Five Points. Each department head is a role that Alfred assumes or dispatches a subagent into when work enters that department's scope. Department heads are not separate AI models – they are role definitions that shape context loading, crew selection and execution parameters.

---

## How Department Heads Work

When a task enters the system:

1. Alfred identifies which department head owns the task
2. Loads the department head primary files for context
3. Classifies the crew type (Researcher, Creator, Reviewer, Mediator, Broadcaster)
4. Applies the token budget tier from `token-budget-framework.md`
5. Applies the execution tier from `agent-guidelines.md`
6. Executes directly or dispatches a subagent with the role brief

---

## Active Department Heads

### Head of Foundation

| Field | Value |
|---|---|
| Department | Foundation |
| Domain | Brand fingerprint, standing doctrine, venture mission, community, philanthropy, pro bono |
| Primary files | `Foundation/_index.md`, `Foundation/Agents/_index.md`, `Foundation/brand-fingerprint.md` |
| Typical crews | Researcher (giving strategy), Broadcaster (community coordination) |
| Reports to | You (Creative Director) directly through Alfred |

**Specialist roles under Head of Foundation:**

| Role | Scope | Typical Crews |
|---|---|---|
| Community Steward | Identifies pro bono opportunities aligned with values, manages philanthropic commitments, coordinates community outreach | Researcher, Broadcaster |

---

### Head of Administration

| Field | Value |
|---|---|
| Department | Administration |
| Domain | Legal, compliance, policies, brand protection, governance |
| Primary files | `Administration/_index.md`, `Administration/Agents/_index.md` |
| Typical crews | Reviewer:Scrutiny (compliance checks), Creator (policy drafting) |
| Reports to | Alfred |

**Specialist roles under Head of Administration:**

| Role | Scope | Typical Crews |
|---|---|---|
| Legal Coordinator | Contract templates, service agreements, NDAs, SOWs | Creator, Reviewer:Scrutiny |
| Compliance Officer | Business registration, insurance, data protection, regulatory | Reviewer:Scrutiny |

---

### Head of Finances

| Field | Value |
|---|---|
| Department | Finances |
| Domain | Revenue tracking, expenses, projections, invoicing, financial compliance |
| Primary files | `Finances/_index.md`, `Finances/Agents/_index.md` |
| Typical crews | Researcher (financial analysis), Reviewer:Scrutiny (compliance), Creator (reports) |
| Reports to | Alfred |

**Specialist roles under Head of Finances:**

| Role | Scope | Typical Crews |
|---|---|---|
| Revenue Analyst | MRR tracking, cohort analysis, revenue recognition, forecasting | Researcher |
| Financial Reporter | P&L, cash flow statements, monthly and quarterly reports | Creator |
| Compliance Validator | Tax readiness, regulatory compliance, audit trails | Reviewer:Scrutiny |

**Finances scope:**
- Revenue tracking and MRR monitoring
- Expense categorisation and budgeting
- Invoice generation and tracking
- Cash flow projections
- Tax preparation support

---

### Head of Business Development

| Field | Value |
|---|---|
| Department | Business Development |
| Domain | ICP, prospecting and outreach, partnerships, pipeline, channels, positioning and market strategy |
| Primary files | `Business Development/_index.md`, `Business Development/Agents/_index.md`, `Business Development/positioning-prospecting-directive.md` |
| Typical crews | Researcher (pipeline analysis, market research), Broadcaster (multi-touch sequences) |
| Reports to | Alfred |

**Specialist roles under Head of Business Development:**

| Role | Scope | Typical Crews |
|---|---|---|
| Business Development Lead | Outbound sequences, partnership development, pipeline generation | Researcher |
| Positioning Lead | Client positioning, differentiation frameworks, narrative architecture, audience and buyer-behaviour research | Researcher |

---

### Head of Marketing & Sales

| Field | Value |
|---|---|
| Department | Marketing & Sales |
| Domain | Brand identity, visual direction, content quality, aesthetic standards, sales process, discovery, proposals, pricing |
| Primary files | `creative-director.md`, `personal-brand-identity.md`, `Marketing & Sales/_index.md`, `Marketing & Sales/Agents/_index.md` |
| Typical crews | Creator (design, copy, proposals), Reviewer:Scrutiny (brand consistency checks, pre-publish review), Mediator (deal negotiation) |
| Reports to | You (Creative Director) directly through Alfred |

**Specialist roles under Head of Marketing & Sales:**

| Role | Scope | Typical Crews |
|---|---|---|
| Brand Strategist | Brand positioning, identity evolution, competitive differentiation | Researcher |
| Art Director | Visual direction for web, social, print – all design output | Creator, Reviewer:Scrutiny |
| Content Strategist | Content calendar, platform strategy, editorial planning | Researcher, Broadcaster |
| Copywriter | Email copy, web copy, social copy, platform-specific content | Creator |
| Sales Lead | Discovery calls, closing, objection handling, negotiation | Researcher, Mediator |
| Proposal Architect | Proposal drafting from offer templates, value stack construction | Creator |

---

### Head of Operations

| Field | Value |
|---|---|
| Department | Operations |
| Domain | Day-to-day delivery, client management, SOPs, systems, tools, deliverable builds, deployment |
| Primary files | `Operations/_index.md`, `Operations/Agents/_index.md`, `Operations/Clientele/_clients-registry.md`, `Operations/SOPs/_sop-registry.md` |
| Typical crews | Broadcaster (workflow coordination), Reviewer:Scrutiny (SOP and QA compliance), Creator (documentation, builds) |
| Reports to | Alfred |

**Specialist roles under Head of Operations:**

| Role | Scope | Typical Crews |
|---|---|---|
| Client Success Lead | Onboarding, account management, retention, offboarding | Broadcaster, Creator |
| SOP Architect | Standard operating procedure design, maintenance, rollout | Creator, Reviewer:Scrutiny |
| Systems and Tools Lead | Tool stack, automation workflows, integration management | Researcher, Creator |
| Technical Scout | Audits the client's existing digital footprint, competitor site performance and technical constraints | Researcher |
| Solutions Architect | Writes the Vibe Coding PRD, translates brand direction into a build specification | Creator |
| Engineer | Builds the site to the PRD specification | Creator |
| QA Engineer | Runs the build against the technical quality rubric | Reviewer:Scrutiny |
| Release Engineer | Deploys to production, configures DNS, runs smoke tests, hands off for client delivery | Broadcaster |

**Operations scope:**
- Client onboarding and offboarding
- Delivery tracking and deadline management
- SOP creation and maintenance
- Website builds, media production and deliverable production
- Tool and integration management
- Account management

---

### Head of Product Development

| Field | Value |
|---|---|
| Department | Product Development |
| Domain | Offers, tiers, bundles, offer strategy and audits, the venture's own products and builds |
| Primary files | `Product Development/_index.md`, `Product Development/Agents/_index.md` |
| Typical crews | Researcher (pricing analysis), Reviewer:Scrutiny (catalogue integrity) |
| Reports to | Alfred |

**Specialist roles under Head of Product Development:**

| Role | Scope | Typical Crews |
|---|---|---|
| Offer Steward | Offer catalogue maintenance, pricing integrity, tier evolution | Researcher, Reviewer:Scrutiny |

---

### Head of Human Resources

| Field | Value |
|---|---|
| Department | Human Resources |
| Domain | Team structure, contractor onboarding, culture, partner hiring criteria |
| Primary files | `Human Resources/_index.md`, `Human Resources/Agents/_index.md` |
| Typical crews | Researcher, Creator |
| Reports to | Alfred |

---

### Head of Knowledge Base

| Field | Value |
|---|---|
| Department | Knowledge Base |
| Domain | Case studies, research, methodologies, industry and competitive intelligence, AI learnings |
| Primary files | `Knowledge Base/_index.md`, `Knowledge Base/Agents/_index.md` |
| Typical crews | Researcher, Creator (Release-stage capture) |
| Reports to | Alfred |

**Specialist roles under Head of Knowledge Base:**

| Role | Scope | Typical Crews |
|---|---|---|
| Knowledge Curator | Captures case studies from delivered work, indexes research, maintains methodology library | Researcher, Creator |

---

## Token Budget by Department

Each task is classified independently using `token-budget-framework.md`. The table below shows typical tier defaults per department, but task classification always takes precedence.

| Department Head | Typical Light | Typical Standard | Typical Heavy |
|---|---|---|---|
| Head of Foundation | Filing reminders, giving-strategy lookups | Community initiative briefs | Giving-strategy documents |
| Head of Administration | Policy updates, filing reminders | Contract drafting | Compliance reviews |
| Head of Finances | Invoice runs, expense logging | Monthly P&L, cash flow reports | Annual forecasting, margin analysis |
| Head of Business Development | CRM updates, follow-ups, quick research lookups | Outbound sequences, competitive briefs | Full pipeline strategy, territory plans, positioning frameworks |
| Head of Marketing & Sales | Social captions, email subject lines | Blog posts, content briefs, proposals, discovery briefs | Brand narrative documents, campaign plans, full pipeline strategy |
| Head of Operations | Task creation, deadline flags, component updates | Weekly status reports, meeting briefs, page builds | SOPs, full website builds, infrastructure architecture |
| Head of Product Development | Offer reference lookups, tier comparisons | Offer documentation updates, bundle descriptions | New offer development, pricing strategy analysis |
| Head of Human Resources | Scheduling, filing, reminders | Onboarding packets | Compliance audits, org design |
| Head of Knowledge Base | Trend flags, methodology references | Content briefs, case study drafts | Research reports, methodology documentation |

---

## Activating a Department Head

All department heads are currently role definitions only. When ready to automate:

1. Create an agent definition in `~/Alfred Pennyworth/Agents/` with the mission brief
2. Update this file to mark the department head as "Active – automated"
3. Configure the agent to read this file, `agent-guidelines.md` and `token-budget-framework.md` at session start
4. Begin logging performance data to `Agents/Logs/`
5. Review after 30 days and adjust

---

*Five Points Digital Studio – Department Heads v3.0 – 2026-09-10 – rebuilt around the nine departments, reversing the 2026-04-07 seven-studio ruling.*
