---
file_type: venture_index
venture: Athena
venture_stage: Dormant
status: active
last_updated: 2026-04-05
---

# Athena – Venture Index

Modeling agency. Currently dormant – the structure exists as scaffolding for reactivation.

> **This venture is dormant.** No active revenue, no active talent roster, no active operations. All files below are structural placeholders. When Athena reactivates, populate each department index with live data and update this file's stage to the appropriate phase.

## Navigation

| Department | Purpose | Start Here |
|---|---|---|
| Foundation/ | Philanthropy, community initiatives, cultural investment | Foundation/_index.md |
| Administration/ | Legal, compliance, contracts, talent agreements | Administration/_index.md |
| Finances/ | Revenue models, commission structures, projections | Finances/_index.md |
| Business Development/ | Brand partnerships, client acquisition, industry networking | Business Development/_index.md |
| Marketing & Sales/ | Agency positioning, talent marketing, portfolio presentation | Marketing & Sales/_index.md |
| Operations/ | Booking workflows, talent management, production coordination | Operations/_index.md |
| Product Development/ | Service tiers, representation packages, casting offerings | Product Development/_index.md |
| Human Resources/ | Internal team, scouts, bookers, contractors | Human Resources/_index.md |
| Knowledge Base/ | Industry research, market intelligence, casting trends | Knowledge Base/_index.md |

## Agent Routing

When a task arrives, load the relevant department `_index.md` first. Each department index contains: purpose, file inventory, which files to read for common tasks and what belongs vs. does not belong in that department.

### Load order for agents

1. This file – orient to the venture
2. `Operations/AI/agent-guidelines.md` – know the rules
3. Relevant department `_index.md` – find the right files
4. Specific file for the task at hand

## Active State

- Current MRR: $0
- Active talent: 0
- Active clients: 0
- Current priority: Dormant – awaiting reactivation
- Active campaign: None

## Key Registries

- Service catalogue: `Product Development/_index.md`
- Client roster: `Operations/Clientele/_clients-registry.md`
- SOP catalogue: `Operations/SOPs/_sop-registry.md`

## Frontmatter Standard

Every file in this venture uses YAML frontmatter:

```yaml
---
file_type: "{offer | sop | playbook | strategy | template | reference | registry}"
venture: Athena
status: "{active | draft | dormant | archived}"
last_updated: "{YYYY-MM-DD}"
related_files:
  - "{path/to/related-file.md}"
---
```
