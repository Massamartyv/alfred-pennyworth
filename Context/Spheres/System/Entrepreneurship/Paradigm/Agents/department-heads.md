---
file_type: reference
document_type: department_heads
venture: Paradigm
status: active
last_updated: 2026-04-22
---

# Department Heads – Paradigm

The organisational structure of AI-assisted roles within Paradigm. Each department head is a role that Alfred assumes or dispatches a subagent into when work enters that studio scope. Department heads are not separate AI models – they are role definitions that shape context loading, crew selection and execution parameters.

---

## How Department Heads Work

When a task enters the system:

1. Alfred identifies which department head owns the task
2. Loads the department head primary files for context
3. Classifies the crew type (Strategist, Creator, Evaluator, Maestro, Validator, Explorer)
4. Applies the execution tier from `agent-guidelines.md`
5. Executes directly or dispatches a subagent with the role brief

---

## Active Department Heads

### Head of Creative

| Field | Value |
|---|---|
| Studio | Creative |
| Domain | Brand identity, visual direction, packaging aesthetics, content quality, sensory design |
| Primary files | `creative-director.md`, `personal-brand-identity.md`, `Creative/_index.md`, `Creative/Agents/_index.md` |
| Reports to | You (Creative Director) directly through Alfred |

**Specialist roles under Head of Creative:**

| Role | Scope |
|---|---|
| Brand Strategist | Brand positioning, identity evolution, category differentiation |
| Art Director | Visual direction for packaging, web, social, print – all design output |
| Packaging Designer | Structural and graphic packaging design, unboxing experience, shelf presence |
| Content Strategist | Content calendar, platform strategy, editorial planning across wellness education |
| Copywriter | Product copy, web copy, social copy, label copy, platform-specific content |

---

### Head of Strategy

| Field | Value |
|---|---|
| Studio | Strategy |
| Domain | Wellness industry research, competitive intelligence, category positioning, consumer behaviour |
| Primary files | `Strategy/_index.md`, `Strategy/Agents/_index.md` |
| Reports to | Alfred |

**Specialist roles under Head of Strategy:**

| Role | Scope |
|---|---|
| Market Researcher | Wellness industry landscape, category trend detection, whitespace analysis |
| Competitive Analyst | Incumbent and emerging brand monitoring, positioning maps, pricing intelligence |
| Consumer Insight Lead | Target customer profiles, behavioural segmentation, purchase drivers |
| Positioning Lead | Brand positioning, differentiation frameworks, narrative architecture |

---

### Head of Production

| Field | Value |
|---|---|
| Studio | Production |
| Domain | Product formulation, manufacturing workflows, packaging production, content production, build quality |
| Primary files | `Production/_index.md`, `Production/Agents/_index.md`, `Operations/SOPs/_sop-registry.md` |
| Reports to | Alfred |

**Specialist roles under Head of Production:**

| Role | Scope |
|---|---|
| Formulation Lead | Ingredient selection, formula iteration, stability, efficacy, sensory profile |
| Manufacturing Coordinator | Contract manufacturer selection, production runs, batch quality |
| Packaging Production Lead | Packaging sourcing, print production, material specification, compliance prep |
| Content Producer | Photography, video, short-form content production for all platforms |
| Quality Assurance | Pre-release review for formulations, labels, packaging, content |

---

### Head of Growth

| Field | Value |
|---|---|
| Studio | Growth |
| Domain | Sales, partnerships, wholesale, distribution, DTC channels, revenue generation |
| Primary files | `Growth/_index.md`, `Growth/Agents/_index.md` |
| Reports to | Alfred |

**Specialist roles under Head of Growth:**

| Role | Scope |
|---|---|
| Wholesale Lead | Retailer outreach, wholesale programme, buyer relationships, trade show strategy |
| Distribution Lead | Regional and national distributor relationships, channel terms, logistics alignment |
| DTC Lead | Direct-to-consumer e-commerce, landing pages, paid acquisition, retention loops |
| Partnership Scout | Aligned wellness brands, practitioner networks, co-branding opportunities |
| Affiliate and Ambassador Lead | Influencer programmes, practitioner ambassador networks, affiliate operations |

---

### Head of Operations

| Field | Value |
|---|---|
| Studio | Operations |
| Domain | Fulfilment, supply chain, quality control, SOPs, tool stack, clientele management |
| Primary files | `Operations/_index.md`, `Operations/Agents/_index.md`, `Operations/Clientele/_clients-registry.md`, `Operations/SOPs/_sop-registry.md` |
| Reports to | Alfred |

**Specialist roles under Head of Operations:**

| Role | Scope |
|---|---|
| Supply Chain Coordinator | Supplier management, ingredient sourcing, inventory planning |
| Fulfilment Lead | Order fulfilment, shipping, returns, 3PL management |
| Quality Control Lead | Incoming goods inspection, batch testing coordination, compliance checks |
| Customer Service Lead | Customer inquiries, order issues, service SOPs, feedback capture |
| Clientele Coordinator | Wholesale and retail partner account management |

---

### Head of Finance

| Field | Value |
|---|---|
| Studio | Finance |
| Domain | Revenue tracking, COGS, expenses, projections, invoicing, tax, metrics |
| Primary files | `Finance/_index.md`, `Finance/Agents/_index.md` |
| Reports to | Alfred |

**Specialist roles under Head of Finance:**

| Role | Scope |
|---|---|
| Revenue Analyst | Sales tracking by channel (DTC, wholesale, subscriptions), cohort analysis |
| Cost Analyst | COGS tracking, margin analysis, supplier cost management |
| Financial Reporter | P&L, cash flow, monthly and quarterly reports |
| Compliance Validator | Tax readiness, platform compliance, audit trails, sales tax by state |

---

### Head of Administration

| Field | Value |
|---|---|
| Studio | Administration |
| Domain | Legal, FDA and FTC compliance, labelling, brand protection, policies, HR, governance |
| Primary files | `Administration/_index.md`, `Administration/Agents/_index.md`, `Administration/HR/_index.md` |
| Reports to | Alfred |

**Specialist roles under Head of Administration:**

| Role | Scope |
|---|---|
| Legal Coordinator | Contracts, supplier and manufacturer agreements, NDAs, wholesale terms, licensing |
| Regulatory Compliance Officer | FDA labelling, FTC claims review, structure-function compliance, state regulations |
| Brand Protection Lead | Trademark filings, IP monitoring, brand misuse response, reputation management |
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

*Paradigm – Department Heads v1.0 – 2026-04-22*
