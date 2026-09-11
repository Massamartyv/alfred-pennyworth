---
file_type: venture_index
venture: "{Venture Name}"
status: template
methodology: The Manor Protocol
last_updated: 2026-09-10
---

# {Venture Name} – Venture Index

{Description}. Stage: {Stage}.

## Trajectory

{Venture Name} is built for scale, leverage and long-term enterprise value – a venture on a billion-dollar portfolio trajectory from its first day, never a lifestyle business. The leverage is whatever compounds here – owned assets, brand, catalogue or infrastructure that accrue value rather than churn. Near-term revenue and milestone floors are rungs on that climb, never ceilings – each one funds the next and none of them is the destination. Live targets live in Notion Projects and Tasks, {workspace} workspace – never here; this file holds the trajectory, not the numbers.

## The Manor Protocol

All work follows The Manor Protocol – five phases, two hard gates, creative excellence as the governing standard. Full definition in `Agents/_index.md`.

**Lifecycle:** Reconnaissance > Direction [gate] > Execution > Critique [gate] > Release

## Navigation

### Nine Departments

| Department | Craft | Start Here |
|---|---|---|
| Foundation/ | Community initiatives, philanthropy, education, giving | Foundation/_index.md |
| Administration/ | Legal, compliance, brand protection, governance | Administration/_index.md |
| Finances/ | Revenue, costs, expenses, projections, tax, metrics | Finances/_index.md |
| Business Development/ | ICP, prospecting and outreach, partnerships, pipeline, channels, positioning and market strategy | Business Development/_index.md |
| Marketing & Sales/ | Brand identity and creative direction, visual and content standards, marketing, sales process, discovery, proposals, pricing | Marketing & Sales/_index.md |
| Operations/ | Delivery, supply chain, quality control, SOPs, clientele management | Operations/_index.md |
| Product Development/ | Product and content development, build quality, offers, tiers, bundles | Product Development/_index.md |
| Human Resources/ | Team, contractors, hiring, culture | Human Resources/_index.md |
| Knowledge Base/ | Research, case studies, industry intelligence, methodologies | Knowledge Base/_index.md |

### Sub-Brands

None at the template stage. A sub-brand copies the `New Sub-Brand/` template folder from `Entrepreneurship/` into this venture root, renames it and registers here in a Sub-Brands table. Structure and graduation criteria live in that template's `_index.md`.

### Shared Governance

| File | Purpose |
|---|---|
| Agents/_index.md | The Manor Protocol definition |
| Agents/agent-guidelines.md | Execution tiers, red lines, approval gates |
| Agents/department-heads.md | Role definitions and specialist seats |
| Agents/integrations.md | Plugin and tool connections; the provisioning checklist |

Plugin scope is provisioned on copy, not deferred. `Agents/integrations.md` ships with the template carrying a three-row provisioning checklist – Notion workspace, Pennyone pipeline, payment rail. Work it from the top on first use.

## Active State

Live state: Notion Projects and Tasks, {workspace} workspace ({Venture Name} – Venture Operations).

## Key Registries

- Offer catalogue: `Product Development/Offers/_offers-registry.md` (to be created)
- Client roster: `Operations/Clientele/_clients-registry.md`
- SOP catalogue: `Operations/SOPs/_sop-registry.md`
- Department heads: `Agents/department-heads.md`

## Frontmatter Standard

Every file in this venture uses YAML frontmatter:

```yaml
---
file_type: "{offer | sop | playbook | strategy | template | reference | registry}"
venture: "{Venture Name}"
status: "{active | draft | archived}"
last_updated: "{YYYY-MM-DD}"
related_files:
  - "{path/to/related-file.md}"
---
```
