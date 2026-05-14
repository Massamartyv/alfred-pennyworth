---
file_type: reference
document_type: department_heads
venture: "{Venture Name}"
status: template
last_updated: 2026-05-14
---

# Department Heads – {Venture Name}

The organisational structure of AI-assisted roles within {Venture Name}. Each department head is a role that Alfred assumes or dispatches a subagent into when work enters that studio scope. Department heads are not separate AI models – they are role definitions that shape context loading, crew selection and execution parameters.

---

## How Department Heads Work

When a task enters the system:

1. Alfred identifies which department head owns the task
2. Loads the department head primary files for context
3. Classifies the crew type (Researcher, Creator, Reviewer, Mediator, Broadcaster)
4. Applies the execution tier from `agent-guidelines.md`
5. Executes directly or dispatches a subagent with the role brief

---

## Active Department Heads

### Head of Creative

| Field | Value |
|---|---|
| Studio | Creative |
| Domain | Brand identity, visual direction, aesthetics, content quality |
| Primary files | `creative-director.md`, `personal-brand-identity.md`, `Creative/_index.md`, `Creative/Agents/_index.md` |
| Reports to | You (Creative Director) directly through Alfred |

**Specialist roles under Head of Creative:**

| Role | Scope |
|---|---|
| Brand Strategist | Brand positioning, identity evolution, category differentiation |
| Art Director | Visual direction for all design output across touchpoints |
| Content Strategist | Content calendar, platform strategy, editorial planning |
| Copywriter | Product copy, web copy, social copy, platform-specific content |

---

### Head of Strategy

| Field | Value |
|---|---|
| Studio | Strategy |
| Domain | Industry research, competitive intelligence, positioning, market behaviour |
| Primary files | `Strategy/_index.md`, `Strategy/Agents/_index.md` |
| Reports to | Alfred |

**Specialist roles under Head of Strategy:**

| Role | Scope |
|---|---|
| Market Researcher | Industry landscape, category trend detection, whitespace analysis |
| Competitive Analyst | Incumbent and emerging competitor monitoring, positioning maps, pricing intelligence |
| Consumer Insight Lead | Target customer profiles, behavioural segmentation, purchase drivers |
| Positioning Lead | Brand positioning, differentiation frameworks, narrative architecture |

---

### Head of Production

| Field | Value |
|---|---|
| Studio | Production |
| Domain | Product development, manufacturing workflows, packaging production, content production, build quality |
| Primary files | `Production/_index.md`, `Production/Agents/_index.md`, `Operations/SOPs/_sop-registry.md` |
| Reports to | Alfred |

**Specialist roles under Head of Production:**

| Role | Scope |
|---|---|
| Development Lead | Core product or offering development, iteration, specification |
| Production Coordinator | Supplier or manufacturer selection, production runs, batch quality |
| Content Producer | Photography, video, short-form content production for all platforms |
| Quality Assurance | Pre-release review across products, assets, packaging, content |

---

### Head of Growth

| Field | Value |
|---|---|
| Studio | Growth |
| Domain | Sales, partnerships, distribution, channel architecture, revenue generation |
| Primary files | `Growth/_index.md`, `Growth/Agents/_index.md` |
| Reports to | Alfred |

**Specialist roles under Head of Growth:**

| Role | Scope |
|---|---|
| Sales Lead | Direct sales pipeline, outreach, deal management |
| Partnership Scout | Aligned brands, networks and co-branding opportunities |
| Channel Lead | DTC, wholesale or distribution strategy depending on venture model |
| Affiliate and Ambassador Lead | Influencer programmes, referral networks, affiliate operations |

---

### Head of Operations

| Field | Value |
|---|---|
| Studio | Operations |
| Domain | Delivery, supply chain, quality control, SOPs, tool stack, clientele management |
| Primary files | `Operations/_index.md`, `Operations/Agents/_index.md`, `Operations/Clientele/_clients-registry.md`, `Operations/SOPs/_sop-registry.md` |
| Reports to | Alfred |

**Specialist roles under Head of Operations:**

| Role | Scope |
|---|---|
| Delivery Coordinator | Order fulfilment, logistics, returns, partner management |
| Quality Control Lead | Incoming quality inspection, compliance checks, standards enforcement |
| Customer Service Lead | Client inquiries, issue resolution, service SOPs, feedback capture |
| Clientele Coordinator | Account management for active clients and partners |

---

### Head of Finance

| Field | Value |
|---|---|
| Studio | Finance |
| Domain | Revenue tracking, costs, expenses, projections, invoicing, tax, metrics |
| Primary files | `Finance/_index.md`, `Finance/Agents/_index.md` |
| Reports to | Alfred |

**Specialist roles under Head of Finance:**

| Role | Scope |
|---|---|
| Revenue Analyst | Sales tracking by channel, cohort analysis |
| Cost Analyst | Cost tracking, margin analysis, supplier cost management |
| Financial Reporter | P&L, cash flow, monthly and quarterly reports |
| Compliance Validator | Tax readiness, platform compliance, audit trails |

---

### Head of Administration

| Field | Value |
|---|---|
| Studio | Administration |
| Domain | Legal, compliance, brand protection, governance, policies, HR |
| Primary files | `Administration/_index.md`, `Administration/Agents/_index.md`, `Administration/HR/_index.md` |
| Reports to | Alfred |

**Specialist roles under Head of Administration:**

| Role | Scope |
|---|---|
| Legal Coordinator | Contracts, supplier agreements, NDAs, licensing |
| Compliance Officer | Regulatory compliance, claims review, industry-specific rules |
| Brand Protection Lead | Trademark filings, IP monitoring, brand misuse response |
| People Lead | Team structure, contractor onboarding, culture, advisor relationships |

---

## Activating a Department Head

All department heads are currently role definitions only. When ready to automate:

1. Create an agent definition in `~/Alfred Pennyworth/Agents/` with the mission brief
2. Update this file to mark the department head as "Active – automated"
3. Configure the agent to read this file and `agent-guidelines.md` at session start
4. Begin logging performance data
5. Review after 30 days and adjust

---

*{Venture Name} – Department Heads v1.0 – 2026-04-22*
