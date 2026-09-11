---
file_type: reference
document_type: department_heads
venture: "{Venture Name}"
status: template
last_updated: 2026-09-10
---

# Department Heads – {Venture Name}

The organisational structure of AI-assisted roles within {Venture Name}. Each department head is a role that Alfred assumes or dispatches a subagent into when work enters that department scope. Department heads are not separate AI models – they are role definitions that shape context loading, crew selection and execution parameters.

---

## How Department Heads Work

When a task arrives:

1. Alfred identifies which department head owns the task
2. Loads the department head primary files for context
3. Classifies the crew type (Researcher, Creator, Reviewer, Mediator, Broadcaster)
4. Applies the execution tier from `agent-guidelines.md`
5. Executes directly or dispatches a subagent with the role brief

---

## Active Department Heads

### Head of Foundation

| Field | Value |
|---|---|
| Department | Foundation |
| Domain | Community initiatives, philanthropy, education, giving |
| Primary files | `Foundation/_index.md`, `Foundation/Agents/_index.md` |
| Reports to | Alfred |

**Specialist roles under Head of Foundation:**

| Role | Scope |
|---|---|
| Foundation Coordinator | Scopes community initiatives, aligns giving strategy with brand and budget, coordinates educational outreach |

---

### Head of Administration

| Field | Value |
|---|---|
| Department | Administration |
| Domain | Legal, compliance, brand protection, governance |
| Primary files | `Administration/_index.md`, `Administration/Agents/_index.md` |
| Reports to | You (Creative Director) directly through Alfred |

**Specialist roles under Head of Administration:**

| Role | Scope |
|---|---|
| Legal Coordinator | Contracts, supplier agreements, NDAs, licensing |
| Compliance Officer | Regulatory compliance, claims review, industry-specific rules |
| Brand Protection Lead | Trademark filings, IP monitoring, brand misuse response |

---

### Head of Finances

| Field | Value |
|---|---|
| Department | Finances |
| Domain | Revenue tracking, costs, expenses, projections, invoicing, tax, metrics |
| Primary files | `Finances/_index.md`, `Finances/Agents/_index.md` |
| Reports to | Alfred |

**Specialist roles under Head of Finances:**

| Role | Scope |
|---|---|
| Revenue Analyst | Sales tracking by channel, cohort analysis |
| Cost Analyst | Cost tracking, margin analysis, supplier cost management |
| Financial Reporter | P&L, cash flow, monthly and quarterly reports |
| Compliance Validator | Tax readiness, platform compliance, audit trails |

---

### Head of Business Development

| Field | Value |
|---|---|
| Department | Business Development |
| Domain | ICP, prospecting and outreach, partnerships, pipeline, channels, positioning and market strategy |
| Primary files | `Business Development/_index.md`, `Business Development/Agents/_index.md` |
| Reports to | Alfred |

**Specialist roles under Head of Business Development:**

| Role | Scope |
|---|---|
| Prospecting Lead | Outreach, pipeline generation, lead qualification |
| Partnership Scout | Aligned brands, networks and co-branding opportunities |
| Channel Lead | DTC, wholesale or distribution strategy depending on venture model |
| Positioning Lead | Brand positioning, differentiation frameworks, narrative architecture, market strategy |

---

### Head of Marketing & Sales

| Field | Value |
|---|---|
| Department | Marketing & Sales |
| Domain | Brand identity and creative direction, visual and content standards, marketing, sales process, discovery, proposals, pricing |
| Primary files | `creative-director.md`, `personal-brand-identity.md`, `Marketing & Sales/_index.md`, `Marketing & Sales/Agents/_index.md` |
| Reports to | You (Creative Director) directly through Alfred |

**Specialist roles under Head of Marketing & Sales:**

| Role | Scope |
|---|---|
| Brand Strategist | Brand positioning, identity evolution, category differentiation |
| Art Director | Visual direction for all design output across touchpoints |
| Content Strategist | Content calendar, platform strategy, editorial planning |
| Copywriter | Product copy, web copy, social copy, platform-specific content |
| Sales Process Lead | Discovery, proposals, pricing, deal management |

---

### Head of Operations

| Field | Value |
|---|---|
| Department | Operations |
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

### Head of Product Development

| Field | Value |
|---|---|
| Department | Product Development |
| Domain | Core product and content development, manufacturing coordination, build quality, offers, tiers and bundles |
| Primary files | `Product Development/_index.md`, `Product Development/Agents/_index.md`, `Product Development/Offers/_offers-registry.md` |
| Reports to | Alfred |

**Specialist roles under Head of Product Development:**

| Role | Scope |
|---|---|
| Development Lead | Core product or offering development, iteration, specification |
| Production Coordinator | Supplier or manufacturer selection, production runs, batch quality |
| Content Producer | Photography, video, short-form content production for all platforms |
| Quality Assurance | Pre-release review across products, assets, packaging, content |

---

### Head of Human Resources

| Field | Value |
|---|---|
| Department | Human Resources |
| Domain | Team structure, contractors, hiring, culture, advisor relationships |
| Primary files | `Human Resources/_index.md`, `Human Resources/Agents/_index.md` |
| Reports to | Alfred |

**Specialist roles under Head of Human Resources:**

| Role | Scope |
|---|---|
| People Lead | Team structure, contractor onboarding, culture, advisor relationships |

---

### Head of Knowledge Base

| Field | Value |
|---|---|
| Department | Knowledge Base |
| Domain | Industry research, competitive intelligence, case studies, methodology documentation |
| Primary files | `Knowledge Base/_index.md`, `Knowledge Base/Agents/_index.md` |
| Reports to | Alfred |

**Specialist roles under Head of Knowledge Base:**

| Role | Scope |
|---|---|
| Knowledge Curator | Captures research, indexes intelligence, maintains case study library and methodology documentation |
| Market Researcher | Industry landscape, category trend detection, whitespace analysis |
| Competitive Analyst | Incumbent and emerging competitor monitoring, positioning maps, pricing intelligence |
| Consumer Insight Lead | Target customer profiles, behavioural segmentation, purchase drivers |

---

## Activating a Department Head

All department heads are currently role definitions only. When ready to automate:

1. Create an agent definition in `~/Alfred Pennyworth/Agents/` with the mission brief
2. Update this file to mark the department head as "Active – automated"
3. Configure the agent to read this file and `agent-guidelines.md` at session start
4. Begin logging performance data
5. Review after 30 days and adjust

---

*{Venture Name} – Department Heads v2.0 – 2026-09-10*
