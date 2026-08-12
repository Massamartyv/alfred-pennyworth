---
file_type: venture_index
venture: Paradigm
venture_stage: Validation
status: active
methodology: The Manor Protocol
last_updated: 2026-07-26
---

# Paradigm – Venture Index

Health and wellness brand. Reimagining how people relate to their bodies, minds and daily rituals.

## Trajectory

Paradigm is built for scale, leverage and long-term enterprise value – a wellness brand on a billion-dollar portfolio trajectory, engineered to become a category rather than a shelf of products. The leverage is brand and formulation that travel: a sensory world people return to, with margin that compounds as the line extends from ritual to ritual and channel to channel. Near-term revenue, distribution and cohort floors are rungs on that climb, never ceilings – each one proves the model and funds the next reach. Live targets live in Notion Projects and Tasks, personal workspace – never here; this file holds the trajectory, not the numbers.

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

### Sub-Brands

| Sub-Brand | Purpose | Start Here |
|---|---|---|
| Paradigm Farms/ | Nutrition pillar – AR plant management and horticultural education; first product is the iOS app | Paradigm Farms/_index.md |

### Shared Governance

| File | Purpose |
|---|---|
| Agents/_index.md | The Manor Protocol definition |
| Agents/agent-guidelines.md | Execution tiers, red lines, approval gates |
| Agents/department-heads.md | Role definitions and specialist seats |
| Agents/integrations.md | Plugin and tool connections; the provisioning checklist |

Plugin scope is recorded in `Agents/integrations.md`, created 2026-08-08. Nothing is connected yet: no Notion workspace, no Pennyone key, no payment rail. Paradigm Farms inherits all three rather than provisioning its own – sub-brands inherit, only ventures provision.

## Paradigm Farms

Nutrition pillar of Paradigm, structured as a sub-brand on the Studio-under-Lululemon model – its own visual identity and voice register under the Paradigm marque. First product: a native iOS application for AR plant management and horticultural education (ARKit, RealityKit, Core ML, Vision framework), with visionOS as the premium tier from the same codebase and Meta Ray-Ban Display as the aspirational north star. Home gardener leads v1 messaging; young farmer follows once the AI layer proves itself. Food-as-medicine positioning carried through credible-not-fringe framing – pro-real-food language over anti-big-pharma language. Full build plan: `Paradigm Farms/Production/build-plan-v1.md`.

## Active State

Live state: Notion Projects and Tasks, personal workspace (Paradigm – Venture Operations; Paradigm Farms v1 under The Orangery mission record).

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
