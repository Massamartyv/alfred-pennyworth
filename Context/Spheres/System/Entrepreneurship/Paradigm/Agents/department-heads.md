---
file_type: reference
document_type: department_heads
venture: Paradigm
status: active
last_updated: 2026-09-10
---

# Department Heads – Paradigm

The organisational structure of AI-assisted roles within Paradigm. Each department head is a role that Alfred assumes or dispatches a subagent into when work enters that department scope. Department heads are not separate AI models – they are role definitions that shape context loading, crew selection and execution parameters.

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

### Head of Foundation

Foundation is a head-led department again since The Restoration, 2026-09-10. The Foundation Coordinator role activates when community wellness initiatives are scoped and scheduled.

| Field | Value |
|---|---|
| Department | Foundation |
| Domain | Community wellness initiatives, philanthropy, educational outreach, giving strategy |
| Primary files | `Foundation/_index.md`, `Foundation/Agents/_index.md` |
| Reports to | Alfred |

**Specialist roles under Foundation:**

| Role | Scope |
|---|---|
| Foundation Coordinator | Scopes community wellness initiatives, aligns giving strategy with brand and budget, coordinates educational outreach |

---

### Head of Administration

| Field | Value |
|---|---|
| Department | Administration |
| Domain | Legal, FDA and FTC compliance, labelling, brand protection, policies, governance |
| Primary files | `Administration/_index.md`, `Administration/Agents/_index.md` |
| Reports to | Alfred |

**Specialist roles under Head of Administration:**

| Role | Scope |
|---|---|
| Legal Coordinator | Contracts, supplier and manufacturer agreements, NDAs, wholesale terms, licensing |
| Regulatory Compliance Officer | FDA labelling, FTC claims review, structure-function compliance, state regulations |
| Brand Protection Lead | Trademark filings, IP monitoring, brand misuse response, reputation management |

People, contractor and culture work reports to Head of Human Resources, not Administration – HR has left Administration for its own department.

---

### Head of Finances

| Field | Value |
|---|---|
| Department | Finances |
| Domain | Revenue tracking, COGS, expenses, projections, invoicing, tax, metrics |
| Primary files | `Finances/_index.md`, `Finances/Agents/_index.md` |
| Reports to | Alfred |

**Specialist roles under Head of Finances:**

| Role | Scope |
|---|---|
| Revenue Analyst | Sales tracking by channel (DTC, wholesale, subscriptions), cohort analysis |
| Cost Analyst | COGS tracking, margin analysis, supplier cost management |
| Financial Reporter | P&L, cash flow, monthly and quarterly reports |
| Compliance Validator | Tax readiness, platform compliance, audit trails, sales tax by state |

---

### Head of Business Development

| Field | Value |
|---|---|
| Department | Business Development |
| Domain | Wholesale, distribution, partnerships, affiliates and ambassadors, sales pipeline, positioning, consumer insight |
| Primary files | `Business Development/_index.md`, `Business Development/Agents/_index.md` |
| Reports to | Alfred |

**Specialist roles under Head of Business Development:**

| Role | Scope |
|---|---|
| Wholesale Lead | Retailer outreach, wholesale programme, buyer relationships, trade show strategy |
| Distribution Lead | Regional and national distributor relationships, channel terms, logistics alignment |
| Partnership Scout | Aligned wellness brands, practitioner networks, co-branding opportunities |
| Affiliate and Ambassador Lead | Influencer programmes, practitioner ambassador networks, affiliate operations |
| Consumer Insight Lead | Target customer profiles, behavioural segmentation, purchase drivers |
| Positioning Lead | Brand positioning, differentiation frameworks, narrative architecture |

---

### Head of Marketing & Sales

| Field | Value |
|---|---|
| Department | Marketing & Sales |
| Domain | Brand identity, visual direction, packaging aesthetics, content quality, sensory design, DTC channel, sales process |
| Primary files | `creative-director.md`, `personal-brand-identity.md`, `Marketing & Sales/_index.md`, `Marketing & Sales/Agents/_index.md` |
| Reports to | You (Creative Director) directly through Alfred |

**Specialist roles under Head of Marketing & Sales:**

| Role | Scope |
|---|---|
| Brand Strategist | Brand positioning, identity evolution, category differentiation |
| Art Director | Visual direction for packaging, web, social, print – all design output |
| Packaging Designer | Structural and graphic packaging design, unboxing experience, shelf presence |
| Content Strategist | Content calendar, platform strategy, editorial planning across wellness education |
| Copywriter | Product copy, web copy, social copy, label copy, platform-specific content |
| DTC Lead | Direct-to-consumer e-commerce, landing pages, paid acquisition, retention loops |

---

### Head of Operations

| Field | Value |
|---|---|
| Department | Operations |
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

### Head of Product Development

| Field | Value |
|---|---|
| Department | Product Development |
| Domain | Product formulation, manufacturing workflows, packaging production, content production, build quality, offer architecture |
| Primary files | `Product Development/_index.md`, `Product Development/Agents/_index.md`, `Operations/SOPs/_sop-registry.md` |
| Reports to | Alfred |

**Specialist roles under Head of Product Development:**

| Role | Scope |
|---|---|
| Formulation Lead | Ingredient selection, formula iteration, stability, efficacy, sensory profile |
| Manufacturing Coordinator | Contract manufacturer selection, production runs, batch quality |
| Packaging Production Lead | Packaging sourcing, print production, material specification, compliance prep |
| Content Producer | Photography, video, short-form content production for all platforms |
| Quality Assurance | Pre-release review for formulations, labels, packaging, content |

---

### Head of Human Resources

| Field | Value |
|---|---|
| Department | Human Resources |
| Domain | Team structure, contractor onboarding, culture, advisor relationships, hiring plans |
| Primary files | `Human Resources/_index.md`, `Human Resources/Agents/_index.md` |
| Reports to | Alfred |

**Specialist roles under Head of Human Resources:**

| Role | Scope |
|---|---|
| People Lead | Team structure, contractor onboarding, culture, advisor relationships |

---

### Head of Knowledge Base

Knowledge Base is a head-led department again since The Restoration, 2026-09-10. The Knowledge Curator role serves every other department.

| Field | Value |
|---|---|
| Department | Knowledge Base |
| Domain | Ingredient science, case studies, industry research, competitive intelligence, methodologies |
| Primary files | `Knowledge Base/_index.md`, `Knowledge Base/Agents/_index.md` |
| Reports to | Alfred |

**Specialist roles under Knowledge Base:**

| Role | Scope |
|---|---|
| Knowledge Curator | Captures research, indexes ingredient science, maintains case study library and methodology documentation |
| Market Researcher | Wellness industry landscape, category trend detection, whitespace analysis |
| Competitive Analyst | Incumbent and emerging brand monitoring, positioning maps, pricing intelligence |

---

## Activating a Department Head

All department heads are currently role definitions only. When ready to automate:

1. Create an agent definition in `~/Alfred Pennyworth/Agents/` with the mission brief
2. Update this file to mark the department head as "Active – automated"
3. Configure the agent to read this file and `agent-guidelines.md` at session start
4. Begin logging performance data
5. Review after 30 days and adjust

---

*Paradigm – Department Heads v2.0 – 2026-09-10 – The Restoration: nine departments restored, replacing the seven-studio shape ratified 2026-04-07. Growth split across Business Development, Marketing & Sales and Product Development; Strategy split across Business Development and Knowledge Base; Production folded into Product Development; HR promoted out of Administration into its own department. Previously v1.1 – 2026-06-11 – crew taxonomy migrated to five-crew model.*
