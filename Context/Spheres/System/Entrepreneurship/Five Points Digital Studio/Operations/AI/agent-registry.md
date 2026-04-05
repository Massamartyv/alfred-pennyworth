---
file_type: registry
registry_type: agent_seats
venture: Five Points Digital Studio
status: active
last_updated: 2026-04-03
---

# Agent Registry

The roster of agent seats operating within Five Points Digital Studio. Each seat is a defined role with a department scope, typical task tiers, and performance tracking.

---

## How Agent Seats Work

An agent seat is not a separate AI model. It is a **role definition** that shapes how Alfred (or a dispatched subagent) operates within a specific department. When a task enters the system, it is routed to the appropriate seat based on department scope. The seat determines:

- Which files to load for context
- Which token budget tier applies (per `Operations/AI/token-budget-framework.md`)
- Which execution tier governs approval (per `Operations/AI/agent-guidelines.md`)
- Which plugins are in scope (per `Operations/AI/integrations.md`)

---

## Active Seats

### Sales Director

| Field | Value |
|---|---|
| Department scope | Marketing & Sales, Business Development |
| Primary files | Marketing & Sales/_index.md, Business Development/_index.md |
| Typical tiers | Light: follow-up emails, CRM updates. Standard: proposals, pitch outlines. Heavy: competitive research, territory plans. |
| Status | Placeholder -- seat definition only, not yet automated |

---

### Project Manager

| Field | Value |
|---|---|
| Department scope | Operations |
| Primary files | Operations/_index.md, Operations/Clientele/_clients-registry.md |
| Typical tiers | Light: task creation, reminders, deadline flags. Standard: weekly status reports, meeting briefs. Heavy: SOPs, project post-mortems. |
| Status | Placeholder -- seat definition only, not yet automated |

---

### Finance Manager

| Field | Value |
|---|---|
| Department scope | Finances |
| Primary files | Finances/_index.md |
| Typical tiers | Light: invoice runs, expense logging. Standard: monthly P&L, cash flow reports. Heavy: annual forecasting, margin analysis. |
| Status | Placeholder -- seat definition only, not yet automated |

---

### Content Strategist

| Field | Value |
|---|---|
| Department scope | Marketing & Sales (content), Knowledge Base |
| Primary files | Marketing & Sales/_index.md, Knowledge Base/_index.md |
| Typical tiers | Light: calendar updates, trend flags. Standard: content briefs, performance reviews. Heavy: content strategy roadmaps. |
| Status | Placeholder -- seat definition only, not yet automated |

---

### Copywriter

| Field | Value |
|---|---|
| Department scope | Marketing & Sales (copy), Operations (delivery) |
| Primary files | Marketing & Sales/_index.md, Administration/brand-voice.md (when created) |
| Typical tiers | Light: social captions, email subject lines. Standard: blog posts, email sequences, case studies. Heavy: brand narrative documents. |
| Status | Placeholder -- seat definition only, not yet automated |

---

### Marketing Manager

| Field | Value |
|---|---|
| Department scope | Business Development, Marketing & Sales |
| Primary files | Business Development/_index.md, Marketing & Sales/_index.md |
| Typical tiers | Light: SEO keyword flags, funnel status. Standard: lead magnet drafts, campaign briefs. Heavy: full campaign plans. |
| Status | Placeholder -- seat definition only, not yet automated |

---

### Systems Engineer

| Field | Value |
|---|---|
| Department scope | Operations (tools and infrastructure), Operations/AI (integrations) |
| Primary files | Operations/_index.md, Operations/AI/integrations.md |
| Typical tiers | Light: health checks, integration status. Standard: automation documentation. Heavy: infrastructure architecture docs. |
| Status | Placeholder -- seat definition only, not yet automated |

---

### HR/Admin Coordinator

| Field | Value |
|---|---|
| Department scope | Human Resources, Administration |
| Primary files | Human Resources/_index.md, Administration/_index.md |
| Typical tiers | Light: scheduling, filing, reminders. Standard: onboarding packets. Heavy: compliance audits. |
| Status | Placeholder -- seat definition only, not yet automated |

---

## Performance Log Template

When agent seats become automated, each session logs the following:

| Field | Description |
|---|---|
| Session ID | Unique identifier for the session |
| Agent seat | Which seat executed the task |
| Task ID | Reference to the task in the Task Queue |
| Task tier | Light, Standard, or Heavy |
| Input tokens | Tokens consumed reading context |
| Output tokens | Tokens consumed generating output |
| Budget status | Under, at, or over tier ceiling |
| Outcome | Completed, budget-exceeded, escalated, failed |
| Timestamp | ISO 8601 |

Performance logs will be stored per quarter at: `Operations/AI/Logs/YYYY-QN-agent-performance.md`

---

## Quarterly Review Cadence

At the end of each quarter:
1. Review token consumption patterns per seat and per task type.
2. Identify tasks that consistently over- or under-consume relative to their tier.
3. Recalibrate tier classifications in `token-budget-framework.md` if patterns warrant it.
4. Flag any seat that is underutilized or overloaded relative to department needs.

---

## Activating a Seat

When ready to automate a seat:
1. Create an agent definition in `~/Alfred Pennyworth/Agents/` with the mission brief.
2. Update this registry entry from "Placeholder" to "Active."
3. Configure the agent to read this registry and `token-budget-framework.md` at session start.
4. Begin logging performance data to `Operations/AI/Logs/`.
5. Review after 30 days and adjust tier defaults if needed.

---

*Five Points Digital Studio -- Agent Registry v1.0 -- April 2026*
