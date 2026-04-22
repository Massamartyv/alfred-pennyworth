---
file_type: reference
document_type: department_heads
venture: Athena
status: dormant
last_updated: 2026-04-05
---

# Department Heads – Athena

The organisational structure of AI-assisted roles within Athena. Each department head is a role that Alfred assumes or dispatches a subagent into when work enters that department's scope. Department heads are not separate AI models – they are role definitions that shape context loading and execution parameters.

---

## How Department Heads Work

When a task enters the system:

1. Alfred identifies which department head owns the task
2. Loads the department head's primary files for context
3. Applies the execution tier from `agent-guidelines.md`
4. Executes directly or dispatches a subagent with the role brief

---

## Active Department Heads

### Head of Talent

| Field | Value |
|---|---|
| Domain | Talent roster management, scouting pipeline, talent development, portfolio curation |
| Primary files | Operations/Clientele/_clients-registry.md, Business Development/_index.md |
| Reports to | Alfred |

**Scope:**
- Talent discovery and scouting pipeline management
- Portfolio curation and comp card development
- Talent scheduling and availability tracking
- Career development guidance and trajectory planning

---

### Head of Bookings

| Field | Value |
|---|---|
| Domain | Client bookings, casting coordination, production logistics, day-of management |
| Primary files | Operations/_index.md, Operations/SOPs/_sop-registry.md |
| Reports to | Alfred |

**Scope:**
- Booking requests and casting call coordination
- Client communication and relationship management
- Production day logistics and scheduling
- Post-booking follow-up and feedback collection

---

### Head of Brand

| Field | Value |
|---|---|
| Domain | Agency identity, talent marketing, visual standards, public presence |
| Primary files | Marketing & Sales/_index.md |
| Reports to | Alfred |

**Scope:**
- Agency brand positioning and visual identity
- Talent marketing materials – portfolios, comp cards, social content
- Agency website and digital presence
- Industry event strategy and representation

---

### Head of Finance

| Field | Value |
|---|---|
| Domain | Commission tracking, invoicing, talent payments, financial projections |
| Primary files | Finances/_index.md |
| Reports to | Alfred |

**Scope:**
- Commission calculations and disbursement tracking
- Client invoicing and payment collection
- Talent payment processing and statements
- Cash flow projections and financial reporting

---

## Activating a Department Head

All department heads are currently role definitions only. When ready to automate:

1. Create an agent definition in `~/Alfred Pennyworth/Agents/` with the mission brief
2. Update this file to mark the department head as active
3. Configure the agent to read this file and `agent-guidelines.md` at session start
4. Begin logging performance data
5. Review after 30 days and adjust

---

*Athena – Department Heads v1.0 – April 2026*
