---
file_type: venture_index
venture: "{Venture Name}"
status: template
methodology: The Manor Protocol
last_updated: 2026-04-22
---

# {Venture Name} – Venture Index

{Description}. Stage: {Stage}.

## The Manor Protocol

All work follows The Manor Protocol – five phases, two hard gates, creative excellence as the governing standard. Full definition in `Agents/_index.md`.

**Lifecycle:** Reconnaissance > Direction [gate] > Execution > Critique [gate] > Release

## Navigation

### Seven Studios

| Studio | Craft | Start Here |
|---|---|---|
| Creative/ | Brand identity, visual direction, aesthetics, content standards | Creative/_index.md |
| Strategy/ | Industry research, competitive intelligence, positioning, market behaviour | Strategy/_index.md |
| Production/ | Product and content development, manufacturing coordination, build quality | Production/_index.md |
| Growth/ | Sales, partnerships, distribution, channel architecture, revenue generation | Growth/_index.md |
| Operations/ | Delivery, supply chain, quality control, SOPs, clientele management | Operations/_index.md |
| Finance/ | Revenue, costs, expenses, projections, tax, metrics | Finance/_index.md |
| Administration/ | Legal, compliance, brand protection, governance, HR | Administration/_index.md |

### Shared Resources

| Resource | Purpose | Start Here |
|---|---|---|
| Knowledge Base/ | Research, case studies, industry intelligence, methodologies | Knowledge Base/_index.md |
| Foundation/ | Community initiatives, philanthropy, education, giving | Foundation/_index.md |

### Shared Governance

| File | Purpose |
|---|---|
| Agents/_index.md | The Manor Protocol definition |
| Agents/agent-guidelines.md | Execution tiers, red lines, approval gates |
| Agents/department-heads.md | Role definitions and specialist seats |

Plugin scope to be determined on copy. No `Agents/integrations.md` exists until configured.

## Active State

- Current MRR: {MRR amount}
- Active clients: {client count}
- Current priority: {priority}
- Active campaign: {campaign name}

## Key Registries

- Offer catalogue: `Growth/Offers/_offers-registry.md` (to be created)
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
