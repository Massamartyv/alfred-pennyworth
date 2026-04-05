---
file_type: reference
document_type: department_heads
venture: Lillie and Lynette
status: active
last_updated: 2026-04-05
---

# Department Heads -- Lillie and Lynette

The organisational structure of AI-assisted roles within Lillie and Lynette. Each department head is a role that Alfred assumes or dispatches a subagent into when work enters that department's scope. Department heads are not separate AI models -- they are role definitions that shape context loading and execution parameters.

---

## How Department Heads Work

When a task enters the system:

1. Alfred identifies which department head owns the task
2. Loads the department head's primary files for context
3. Applies the execution tier from `agent-guidelines.md`
4. Executes directly or dispatches a subagent with the role brief

---

## Active Department Heads

### Head of Concept and Experience

| Field | Value |
|---|---|
| Domain | Hospitality concept, guest experience design, service philosophy, aesthetic direction |
| Primary files | `creative-director.md`, Product Development/_index.md |
| Reports to | You -- Creative Director -- directly through Alfred |

**Specialist roles under Head of Concept and Experience:**

| Role | Scope |
|---|---|
| Experience Designer | Guest journey mapping, service touchpoints, ambience |
| Culinary Director | Menu concept, flavour profiles, food and beverage vision |
| Brand Architect | Visual identity, spatial aesthetic, brand voice for hospitality |
| Event Programmer | Curated event concepts, themed experiences, private bookings |

---

### Head of Operations

| Field | Value |
|---|---|
| Domain | Service delivery, vendor management, procurement, quality assurance |
| Primary files | Operations/_index.md, Operations/SOPs/_sop-registry.md |
| Reports to | Alfred |

**Specialist roles under Head of Operations:**

| Role | Scope |
|---|---|
| Service Standards Manager | SOP development, training protocols, quality benchmarks |
| Vendor Relations | Supplier sourcing, procurement, contract management |
| Facilities Coordinator | Venue maintenance, health and safety, regulatory compliance |
| Guest Relations | VIP management, feedback handling, loyalty programmes |

---

### Head of Growth

| Field | Value |
|---|---|
| Domain | Market analysis, partnerships, investor relations, expansion strategy |
| Primary files | Business Development/_index.md, Marketing & Sales/_index.md |
| Reports to | Alfred |

**Specialist roles under Head of Growth:**

| Role | Scope |
|---|---|
| Market Analyst | Competitive landscape, demographic research, location viability |
| Partnership Scout | Vendor partnerships, co-branding opportunities, strategic alliances |
| Investor Relations | Funding strategy, pitch materials, capital planning |
| Expansion Strategist | Multi-location planning, market entry, scaling framework |

---

### Head of Finance and Administration

| Field | Value |
|---|---|
| Domain | Financial planning, budgeting, legal compliance, licensing |
| Primary files | Finances/_index.md, Administration/_index.md |
| Reports to | Alfred |

**Specialist roles under Head of Finance and Administration:**

| Role | Scope |
|---|---|
| Financial Planner | Revenue modelling, cost forecasting, capital requirements |
| Licensing Coordinator | Permits, health department, liquor licensing, regulatory filings |
| Compliance Monitor | Health and safety, food safety, labour law, insurance |
| Budget Analyst | Operating cost tracking, margin analysis, vendor cost optimisation |

---

## Activating a Department Head

All department heads are currently role definitions only. When ready to automate:

1. Create an agent definition in `~/Alfred Pennyworth/Agents/` with the mission brief
2. Update this file to mark the department head as active -- automated
3. Configure the agent to read this file and `agent-guidelines.md` at session start
4. Begin logging performance data
5. Review after 30 days and adjust

---

*Lillie and Lynette -- Department Heads v1.0 -- April 2026*
