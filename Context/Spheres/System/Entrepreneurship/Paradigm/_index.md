---
file_type: venture_index
venture: Paradigm
venture_stage: Ideation
status: active
last_updated: 2026-04-05
---

# Paradigm -- Venture Index

Health and wellness brand. Reimagining how people relate to their bodies, minds and daily rituals. Stage: Ideation.

## Navigation

| Department | Purpose | Start Here |
|---|---|---|
| Foundation/ | Philanthropy, community wellness initiatives, giving | Foundation/_index.md |
| Administration/ | Legal, compliance, regulations, brand protection | Administration/_index.md |
| Finances/ | Revenue models, projections, metrics, tax | Finances/_index.md |
| Business Development/ | Partnerships, wholesale, distribution, pipeline | Business Development/_index.md |
| Marketing & Sales/ | Brand marketing, sales channels, community engagement | Marketing & Sales/_index.md |
| Operations/ | Fulfilment, SOPs, delivery, tools, AI systems | Operations/_index.md |
| Product Development/ | Formulations, product lines, packaging, R&D | Product Development/_index.md |
| Human Resources/ | Team, contractors, advisors, culture | Human Resources/_index.md |
| Knowledge Base/ | Research, case studies, industry intelligence | Knowledge Base/_index.md |

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
venture: Paradigm
status: "{active | draft | archived}"
last_updated: "{YYYY-MM-DD}"
related_files:
  - "{path/to/related-file.md}"
---
```
