---
file_type: reference
document_type: department_heads
venture: Lillie and Lynette
status: active
last_updated: 2026-06-11
---

# Department Heads – Lillie and Lynette

The organisational structure of AI-assisted roles within Lillie and Lynette. Each department head is a role that Alfred assumes or dispatches a subagent into when work enters that studio scope. Department heads are not separate AI models – they are role definitions that shape context loading, crew selection and execution parameters.

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
| Domain | Brand identity, guest experience design, visual language, interior aesthetic direction, menu and offering narrative |
| Primary files | `creative-director.md`, `personal-brand-identity.md`, `Creative/_index.md`, `Creative/Agents/_index.md` |
| Reports to | You (Creative Director) directly through Alfred |

**Specialist roles under Head of Creative:**

| Role | Scope |
|---|---|
| Brand Storyteller | Naming, narrative arc, written voice across menus, signage and guest-facing copy |
| Experience Designer | Guest journey mapping, service choreography, signature moments |
| Interior and Environment Director | Spatial design direction, material palette, lighting, scent, sound |
| Visual Director | Photography, print collateral, social aesthetics, menu typography |
| Culinary and Beverage Stylist | Menu concept direction, plating standards, beverage programme narrative |

---

### Head of Strategy

| Field | Value |
|---|---|
| Studio | Strategy |
| Domain | Hospitality industry research, competitive intelligence, venue and market positioning, guest behaviour analysis |
| Primary files | `Strategy/_index.md`, `Strategy/Agents/_index.md` |
| Reports to | Alfred |

**Specialist roles under Head of Strategy:**

| Role | Scope |
|---|---|
| Industry Researcher | Hospitality trends, emerging formats, category shifts, reference brands |
| Market and Venue Analyst | Geographic analysis, neighbourhood dynamics, venue economics |
| Guest Behaviour Analyst | Segment mapping, booking patterns, spend behaviour, loyalty drivers |
| Competitive Intelligence | Adjacent concepts, local competitive set, positioning gaps |

---

### Head of Production

| Field | Value |
|---|---|
| Studio | Production |
| Domain | Service delivery production, event production, experience fabrication, content production |
| Primary files | `Production/_index.md`, `Production/Agents/_index.md`, `Operations/SOPs/_sop-registry.md` |
| Reports to | Alfred |

**Specialist roles under Head of Production:**

| Role | Scope |
|---|---|
| Service Production Lead | Shift-level choreography, floor plan execution, pacing and flow |
| Event Producer | Private events, curated experiences, venue takeovers, pop-ups |
| Experience Fabricator | Signature moments, installations, tactile guest elements |
| Content Producer | Photography shoots, video, menus, printed collateral production |
| Quality Assurance | Pre-service and post-service review, standards enforcement |

---

### Head of Growth

| Field | Value |
|---|---|
| Studio | Growth |
| Domain | Sales, partnerships, venue sourcing, distribution pipeline, guest acquisition |
| Primary files | `Growth/_index.md`, `Growth/Agents/_index.md` |
| Reports to | Alfred |

**Specialist roles under Head of Growth:**

| Role | Scope |
|---|---|
| Venue Sourcing Lead | Property scouting, landlord relationships, location due diligence |
| Partnership Lead | Brand collaborations, co-branded events, complementary hospitality partners |
| Sales Lead | Private event sales, booking conversion, corporate accounts |
| Guest Acquisition Lead | Paid channels, referral programmes, loyalty, PR-led acquisition |
| Distribution and Platform Lead | Reservation platforms, directory presence, aggregator relationships |

---

### Head of Operations

| Field | Value |
|---|---|
| Studio | Operations |
| Domain | Day-to-day service delivery, SOPs, tool administration, guest and vendor clientele management |
| Primary files | `Operations/_index.md`, `Operations/Agents/_index.md`, `Operations/SOPs/_sop-registry.md`, `Operations/Clientele/_clients-registry.md` |
| Reports to | Alfred |

**Specialist roles under Head of Operations:**

| Role | Scope |
|---|---|
| Service Operations Lead | Daily service management, shift oversight, guest flow |
| Vendor and Procurement Lead | Supplier relationships, sourcing, purchase order workflow |
| Systems Administrator | Tool configuration, POS, reservations, inventory, integrations |
| Clientele Coordinator | Guest profile maintenance, VIP recognition, vendor relationship tracking |
| Health and Safety Lead | Food safety, cleaning standards, incident protocols |

---

### Head of Finance

| Field | Value |
|---|---|
| Studio | Finance |
| Domain | Revenue, cost of service, expenses, projections, tax, metrics |
| Primary files | `Finance/_index.md`, `Finance/Agents/_index.md` |
| Reports to | Alfred |

**Specialist roles under Head of Finance:**

| Role | Scope |
|---|---|
| Revenue Analyst | Booking revenue, event revenue, retail revenue, cohort analysis |
| Cost Controller | Cost of goods sold, labour cost, prime cost monitoring |
| Financial Reporter | P&L, cash flow, monthly and quarterly reports |
| Capital Strategist | Funding requirements, investor readiness, projections |
| Compliance Validator | Sales tax, liquor tax, payroll tax, audit readiness |

---

### Head of Administration

| Field | Value |
|---|---|
| Studio | Administration |
| Domain | Legal, licensing, food and beverage compliance, insurance, HR |
| Primary files | `Administration/_index.md`, `Administration/Agents/_index.md`, `Administration/HR/_index.md` |
| Reports to | Alfred |

**Specialist roles under Head of Administration:**

| Role | Scope |
|---|---|
| Legal Coordinator | Contracts, leases, vendor agreements, IP filings, NDA templates |
| Licensing and Permits Lead | Food service, liquor, health, entertainment, zoning, signage |
| Compliance Officer | Health code, ADA, labour law, alcohol regulation, data protection |
| Insurance and Risk Lead | General liability, liquor liability, property, workers compensation |
| People Lead (HR) | Team structure, hiring plans, contractor agreements, culture documentation |

---

## Activating a Department Head

All department heads are currently role definitions only. When ready to automate:

1. Create an agent definition in `~/Alfred Pennyworth/Agents/` with the mission brief
2. Update this file to mark the department head as "Active – automated"
3. Configure the agent to read this file and `agent-guidelines.md` at session start
4. Begin logging performance data
5. Review after 30 days and adjust

---

*Lillie and Lynette – Department Heads v1.1 – 2026-06-11 – crew taxonomy migrated to five-crew model*
