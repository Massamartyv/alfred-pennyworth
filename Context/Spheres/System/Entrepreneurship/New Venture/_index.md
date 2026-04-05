---
file_type: venture_index
venture_name: "{Venture Name}"
venture_stage: "{Ideation | Launch | Growth | Scale | Mature}"
last_updated: "{YYYY-MM-DD}"
---

# {Venture Name} -- Venture Index

## Navigation

| Department | Purpose | Start Here |
|---|---|---|
| Foundation/ | Philanthropy, community initiatives, giving | Foundation/_index.md |
| Administration/ | Legal templates, compliance, policies | Administration/_index.md |
| Finances/ | Revenue models, projections, metrics, tax | Finances/_index.md |
| Business Development/ | ICP, outreach, partnerships, pipeline | Business Development/_index.md |
| Marketing & Sales/ | Sales process, proposals, pricing, brand | Marketing & Sales/_index.md |
| Operations/ | SOPs, delivery, client work, tools | Operations/_index.md |
| Product Development/ | Offers, tiers, bundles | Product Development/_index.md |
| Human Resources/ | Team, contractors, hiring, culture | Human Resources/_index.md |
| Knowledge Base/ | Case studies, research, methodologies | Knowledge Base/_index.md |

## Agent Routing

When a task arrives, load the relevant department `_index.md` first. Each department index contains: purpose, file inventory, which files to read for common tasks, and what belongs vs. does not belong in that department.

**Load order for agents:**
1. This file -- orient to the venture
2. `Operations/AI/agent-guidelines.md` -- know the rules
3. Relevant department `_index.md` -- find the right files
4. Specific file for the task at hand

## Active State

- Current MRR: {amount}
- Active clients: {count}
- Current priority: {description}
- Active campaign: {name and file path}

## Key Registries

- Offer catalog: `Product Development/_index.md`
- Client roster: `Operations/Clientele/_clients-registry.md`
- SOP catalog: `Operations/SOPs/_sop-registry.md`

## Frontmatter Standard

Every file in this venture uses YAML frontmatter:

```yaml
---
file_type: "{offer | sop | playbook | strategy | template | reference | registry}"
status: "{active | draft | archived}"
owner: "{person or agent name}"
last_updated: "{YYYY-MM-DD}"
related_files:
  - "{path/to/related-file.md}"
---
```
