---
file_type: venture_index
venture: Lillie and Lynette
venture_stage: Ideation
status: active
last_updated: 2026-04-05
---

# Lillie and Lynette -- Venture Index

Hospitality company. Rooted in warmth, refinement and the art of making people feel genuinely welcomed. Named with intention -- built to scale.

## Navigation

| Department | Purpose | Start Here |
|---|---|---|
| Foundation/ | Philanthropy, community, hospitality-driven giving | Foundation/_index.md |
| Administration/ | Legal, compliance, licensing, policies | Administration/_index.md |
| Finances/ | Revenue models, projections, metrics, tax | Finances/_index.md |
| Business Development/ | Partnerships, venue sourcing, pipeline | Business Development/_index.md |
| Marketing & Sales/ | Brand positioning, guest acquisition, pricing | Marketing & Sales/_index.md |
| Operations/ | SOPs, service delivery, vendor management, tools | Operations/_index.md |
| Product Development/ | Hospitality offerings, experiences, service tiers | Product Development/_index.md |
| Human Resources/ | Team, contractors, hiring, culture | Human Resources/_index.md |
| Knowledge Base/ | Industry research, case studies, methodologies | Knowledge Base/_index.md |

## Agent Routing

When a task arrives, load the relevant department `_index.md` first. Each department index contains: purpose, file inventory, which files to read for common tasks and what belongs vs. does not belong in that department.

### Load order for agents

1. This file -- orient to the venture
2. `Operations/AI/agent-guidelines.md` -- know the rules
3. Relevant department `_index.md` -- find the right files
4. Specific file for the task at hand

## Active State

- Current MRR: $0
- Active clients: 0
- Current priority: To be set
- Active campaign: None

## Key Registries

- Offer catalogue: `Product Development/_index.md`
- Client roster: `Operations/Clientele/_clients-registry.md`
- SOP catalogue: `Operations/SOPs/_sop-registry.md`

## Frontmatter Standard

Every file in this venture uses YAML frontmatter:

```yaml
---
file_type: "{offer | sop | playbook | strategy | template | reference | registry}"
venture: Lillie and Lynette
status: "{active | draft | archived}"
last_updated: "{YYYY-MM-DD}"
related_files:
  - "{path/to/related-file.md}"
---
```
