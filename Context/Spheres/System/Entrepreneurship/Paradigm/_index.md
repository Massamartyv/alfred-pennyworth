---
file_type: venture_index
venture: Paradigm
venture_stage: Validation
status: active
methodology: The Manor Protocol
last_updated: 2026-07-10
---

# Paradigm – Venture Index

Health and wellness brand. Reimagining how people relate to their bodies, minds and daily rituals. Stage: Ideation.

## The Manor Protocol

All work follows The Manor Protocol – five phases, two hard gates, creative excellence as the governing standard. Full definition in `Agents/_index.md`.

**Lifecycle:** Reconnaissance > Direction [gate] > Execution > Critique [gate] > Release

## Navigation

### Seven Studios

| Studio | Craft | Start Here |
|---|---|---|
| Creative/ | Brand identity, visual direction, packaging, aesthetic standards | Creative/_index.md |
| Strategy/ | Wellness industry research, competitive intelligence, positioning, consumer behaviour | Strategy/_index.md |
| Production/ | Product formulation, manufacturing, packaging production, content production | Production/_index.md |
| Growth/ | Sales, partnerships, wholesale, distribution, DTC channels | Growth/_index.md |
| Operations/ | Fulfilment, supply chain, quality control, SOPs, clientele management | Operations/_index.md |
| Finance/ | Revenue, COGS, expenses, projections, tax, metrics | Finance/_index.md |
| Administration/ | Legal, FDA and FTC compliance, labelling, brand protection, HR | Administration/_index.md |

### Shared Resources

| Resource | Purpose | Start Here |
|---|---|---|
| Knowledge Base/ | Ingredient science, case studies, industry research, methodologies | Knowledge Base/_index.md |
| Foundation/ | Brand fingerprint (source of truth); community wellness initiatives, philanthropy, education | Foundation/_index.md |

### Shared Governance

| File | Purpose |
|---|---|
| Agents/_index.md | The Manor Protocol definition |
| Agents/agent-guidelines.md | Execution tiers, red lines, approval gates |
| Agents/department-heads.md | Role definitions and specialist seats |

Plugin scope is still to be determined. No `Agents/integrations.md` exists yet.

## Active State

Live state: Notion Projects and Tasks, personal workspace (Paradigm – Venture Operations).

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
venture: Paradigm
status: "{active | draft | archived}"
last_updated: "{YYYY-MM-DD}"
related_files:
  - "{path/to/related-file.md}"
---
```
