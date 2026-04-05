---
file_type: venture_index
venture: Marty Gras
venture_stage: Launch
status: active
last_updated: 2026-04-05
---

# Marty Gras -- Venture Index

Personal media company. The Architect of Vibe. Podcast, Epiphany newsletter on Substack and cultural curation across all platforms.

## Navigation

| Department | Purpose | Start Here |
|---|---|---|
| Foundation/ | Philanthropy, community, cultural initiatives | Foundation/_index.md |
| Administration/ | Legal, compliance, policies, brand protection | Administration/_index.md |
| Finances/ | Revenue models, subscriptions, sponsorships, merch | Finances/_index.md |
| Business Development/ | Audience growth, partnerships, collaborations | Business Development/_index.md |
| Marketing & Sales/ | Content distribution, social strategy, engagement | Marketing & Sales/_index.md |
| Operations/ | Content pipeline, production workflows, tools, SOPs | Operations/_index.md |
| Product Development/ | Content products -- newsletter, podcast, social | Product Development/_index.md |
| Human Resources/ | Team, contractors, collaborators | Human Resources/_index.md |
| Knowledge Base/ | Cultural references, audience insights, research | Knowledge Base/_index.md |

## Agent Routing

When a task arrives, load the relevant department `_index.md` first. Each department index contains: purpose, file inventory, which files to read for common tasks and what belongs vs. does not belong in that department.

### Load order for agents

1. This file -- orient to the venture
2. `Operations/AI/agent-guidelines.md` -- know the rules
3. Relevant department `_index.md` -- find the right files
4. Specific file for the task at hand

## Active State

- Current MRR: $0
- Active clients: N/A -- audience, not clients
- Current priority: To be set
- Active campaign: None

## Key Registries

- Content products: `Product Development/_index.md`
- Collaborator and sponsor roster: `Operations/Clientele/_clients-registry.md`
- SOP catalogue: `Operations/SOPs/_sop-registry.md`

## Frontmatter Standard

Every file in this venture uses YAML frontmatter:

```yaml
---
file_type: "{content_product | sop | playbook | strategy | template | reference | registry}"
venture: Marty Gras
status: "{active | draft | archived}"
last_updated: "{YYYY-MM-DD}"
related_files:
  - "{path/to/related-file.md}"
---
```
