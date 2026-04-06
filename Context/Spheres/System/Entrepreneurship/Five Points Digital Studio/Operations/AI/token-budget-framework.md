---
file_type: reference
document_type: operational_framework
venture: Five Points Digital Studio
status: active
last_updated: 2026-04-03
---

# Token Budget Framework
## Five Points Digital Studio -- Task Complexity Model

---

## Overview

Token budgets are standardized by **task complexity**, not by agent identity. The task is the unit of measurement. Every task in the system is classified as Light, Standard, or Heavy. The classification travels with the task. The agent does not choose its own budget.

---

## The Three Tiers

### Light -- 5,000 output tokens
Routine, short-output tasks. The work is mechanical and the output is brief.

**Examples:**
- Follow-up email draft
- Task creation in Notion
- Calendar invite scheduling
- CRM status update
- Expense categorization
- Reminder setting
- File organization
- Deadline flagging

**Rule of thumb:** If the output is under 500 words and requires no synthesis across multiple sources, it is Light.

---

### Standard -- 15,000 output tokens
Synthesis tasks with substantive output. The work requires pulling from multiple inputs and producing something with structure and reasoning.

**Examples:**
- Client proposal draft
- Weekly status report
- Blog post draft
- Content brief
- Monthly P&L summary
- Email sequence (3-5 emails)
- Meeting brief with recommendations
- Competitive positioning summary
- Case study draft

**Rule of thumb:** If the output is 500 to 3,000 words and requires connecting multiple data points or sources, it is Standard.

---

### Heavy -- 30,000 output tokens
Deep reasoning across multiple sources. The work requires extended analysis, strategic thinking, or comprehensive documentation.

**Examples:**
- Brand strategy document
- Competitive intelligence report
- SOP draft for a new agent seat
- Multi-channel campaign plan
- Quarterly business review document
- Full pitch deck content
- Content strategy roadmap
- Pricing strategy analysis

**Rule of thumb:** If the output exceeds 3,000 words or requires reasoning across five or more sources, it is Heavy.

---

## Universal Hard Ceiling

**100,000 output tokens per session.**

No task, no agent, no circumstance exceeds this. This is the kill switch for pathological runaway loops. It exists independently of the three tiers and cannot be overridden.

---

## Rules

### Classification
- Every task in the Task Queue is classified as Light, Standard, or Heavy at creation.
- The classification is set by the task creator (you or Alfred), not by the executing agent.
- When in doubt, classify down. Underspending is free. Overspending is disruptive.

### Projection
- Before every API call, the agent calculates projected token usage against the task budget.
- If the projection exceeds the tier ceiling, the agent stops with a structured reason before the call is made.
- The stop reason includes: task ID, current token count, projected overage, and suggested action (break into subtasks or request tier upgrade).

### Tracking
- Input tokens and output tokens are logged per session in the department heads performance log.
- Over time, this data reveals which task types consistently under- or over-consume.
- Quarterly review: recalibrate tier thresholds if usage patterns shift significantly.

### Escalation
- If an agent hits its tier ceiling mid-task and the work is genuinely incomplete:
  1. The agent saves workflow state.
  2. The agent logs the task as `budget-exceeded` in the Task Queue.
  3. The task surfaces for human review.
  4. You decide: authorize a tier upgrade for that specific task, or break it into smaller tasks that each fit within a tier.
- Tier upgrades are per-task, not per-agent. Upgrading one proposal from Standard to Heavy does not change the default for future proposals.

### Multi-Step Tasks
- Some workflows span multiple tasks (e.g. a campaign plan might involve research, strategy, copy, and scheduling).
- Each step is classified independently. The research step might be Heavy. The scheduling step is Light.
- The total budget for a multi-step workflow is the sum of its individual task budgets, not a single classification.

---

## Quick Reference

| Tier | Output Tokens | Word Count Guide | Complexity Signal |
|------|--------------|------------------|-------------------|
| Light | 5,000 | Under 500 words | Routine, single-source, mechanical |
| Standard | 15,000 | 500 to 3,000 words | Synthesis, multi-source, structured |
| Heavy | 30,000 | 3,000+ words | Deep reasoning, strategic, comprehensive |
| **Ceiling** | **100,000** | **N/A** | **Universal kill switch** |

---

## Classification Cheat Sheet by Agent Seat

| Agent Seat | Typical Light Tasks | Typical Standard Tasks | Typical Heavy Tasks |
|-------|-------------------|----------------------|-------------------|
| Sales Director | Follow-up emails, CRM updates | Proposals, pitch outlines | Competitive research, territory plans |
| Project Manager | Task creation, reminders, deadline flags | Weekly status reports, meeting briefs | SOPs, project post-mortems |
| Finance Manager | Invoice runs, expense logging | Monthly P&L, cash flow reports | Annual forecasting, margin analysis |
| Content Strategist | Calendar updates, trend flags | Content briefs, performance reviews | Content strategy roadmaps |
| Copywriter | Social captions, email subject lines | Blog posts, email sequences, case studies | Brand narrative documents |
| Marketing Manager | SEO keyword flags, funnel status | Lead magnet drafts, campaign briefs | Full campaign plans |
| Systems Engineer | Health checks, integration status | Automation documentation | Infrastructure architecture docs |
| HR/Admin Coordinator | Scheduling, filing, reminders | Onboarding packets | Compliance audits |

---

*Five Points Digital Studio -- Task Complexity Framework v1.0 -- April 2026*
