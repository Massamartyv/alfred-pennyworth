---
file_type: venture_index
venture: Atlas
working_code_name: true
final_identity_pending: art-direction
venture_stage: Reconnaissance
status: active
methodology: The Manor Protocol
last_updated: 2026-05-14
---

# Atlas – Venture Index

> **Working code name.** Final brand identity awaits an art-direction pass. Atlas refers to the first cervical vertebra – the bone that supports the head and bridges spine to skull. The metaphor is functional: this venture is the supportive intelligence layer above existing chiropractic systems.

AI-native chiropractic intelligence layer. A thin clinical service that sits above existing EHRs – Jane App, ChiroTouch, Genesis, EZBIS, Prompt EMR – converting ambient voice into structured SOAP notes, validated ICD-10 and CPT coding, treatment plans and downstream insurance workflows. The thesis is augmentation, not replacement: chiropractors do not switch EHRs easily, so Atlas integrates with the systems they already run.

Stage: Reconnaissance. Phase 1 deliverable is a SOAP note generator piloted at Arlando Parker Jr.'s clinic, posting into a single EHR.

## Strategic Thesis

Every healthcare AI company is converging on roughly the same five-layer stack – ambient capture, clinical documentation, insurance automation, scheduling/CRM, analytics. The defensible edge is not the architecture. The defensible edge is chiropractic-specific clinical knowledge. General medical scribes hallucinate on Gonstead listings, miss diversified technique nuance and fumble PI documentation. Atlas owns that knowledge layer.

Distribution is the under-discussed problem. Chiropractors do not buy SaaS the way oncologists do. The product needs an embedded channel from day one – pilot site, association network, founder-led sales, and partnership conversations with the EHR vendors themselves.

## Architectural Pattern

Atlas inherits the Pennyone architecture – a thin FastMCP service routing a single intent through multiple backend adapters. Pennyone hits Instagram, TikTok, X, Reddit and others via Zernio. Atlas hits Jane App, ChiroTouch, Genesis, EZBIS, Prompt EMR via direct EHR APIs. Same shape, different domain.

## The Manor Protocol

All work follows The Manor Protocol – five phases, two hard gates, creative excellence as the governing standard. Healthcare AI elevates Critique to load-bearing status. No clinical output ships without binary validation against the per-mission contract.

**Lifecycle:** Reconnaissance > Direction [gate] > Execution > Critique [gate] > Release

## Navigation

### Seven Studios

| Studio | Craft | Start Here |
|---|---|---|
| Creative/ | Brand identity, voice, clinical communication standards | Creative/_index.md |
| Strategy/ | EHR landscape, competitive intelligence, positioning, chiropractic market behaviour | Strategy/_index.md |
| Production/ | AI architecture, FastMCP service, EHR adapters, clinical knowledge curation | Production/_index.md |
| Growth/ | Pilot expansion, channel architecture, partnership development | Growth/_index.md |
| Operations/ | Pilot management, clinical advisor relationships, support workflows | Operations/_index.md |
| Finance/ | SaaS metrics, per-clinic unit economics, inference cost tracking | Finance/_index.md |
| Administration/ | HIPAA compliance, BAAs, regulatory, entity formation, IP | Administration/_index.md |

### Shared Resources

| Resource | Purpose | Start Here |
|---|---|---|
| Knowledge Base/ | Clinical knowledge, EHR intelligence, coding references, competitive landscape | Knowledge Base/_index.md |
| Foundation/ | Brand fingerprint (source of truth); community initiatives, education, chiropractic profession contribution | Foundation/_index.md |

### Shared Governance

| File | Purpose |
|---|---|
| Agents/_index.md | The Manor Protocol definition scoped to Atlas |
| Agents/agent-guidelines.md | Execution tiers, red lines, HIPAA boundaries |
| Agents/department-heads.md | Role definitions and specialist seats |
| Agents/validation-contract.md | Phase 1 binary assertions, evidence, reviewers |
| Agents/model-assignment.md | Per-mission model allocation |

Plugin scope to be determined. No `Agents/integrations.md` exists until configured. Initial integrations expected: Jane App API (first EHR adapter), Anthropic API (LLM calls), Stripe Atlas (entity formation), HIPAA-compliant log infrastructure.

## Active State

- Stage: Reconnaissance (Manor Protocol Phase 1)
- Current MRR: $0 (pre-revenue)
- Pilot site: Arlando Parker Jr. (Clinical Advisor; not a paying client)
- Phase 1 target: SOAP note generator, one EHR adapter, doctor-in-loop review
- Current priority: Discovery extraction from Arlando – primary EHR, technique style, payer mix, pilot constraints; commercial terms structuring; identity art direction
- Active campaign: None – pre-launch

## Open Direction-Gate Items

1. Final brand identity (working name Atlas pending art direction)
2. Arlando Parker Jr. commercial terms (retainer versus revenue share versus hybrid)
3. Initial EHR target (likely Jane App; confirm post-Arlando discovery)
4. Entity formation jurisdiction (Delaware C-Corp default for venture scale; revisit)
5. HIPAA infrastructure provider (BAA candidates: AWS, GCP, Azure healthcare tiers)
6. Validation contract operator approval

## Key Registries

- Validation contract: `Agents/validation-contract.md`
- Model assignment: `Agents/model-assignment.md`
- Clinical advisor: `Operations/Clientele/Active/Arlando Parker Jr./`
- Department heads: `Agents/department-heads.md`
- Clinical knowledge: `Knowledge Base/Clinical/`
- EHR intelligence: `Knowledge Base/EHR/`

## Frontmatter Standard

Every file in this venture uses YAML frontmatter:

```yaml
---
file_type: "{offer | sop | playbook | strategy | template | reference | registry | clinical_knowledge | adapter_spec | validation_contract | model_assignment}"
venture: Atlas
status: "{active | draft | archived}"
last_updated: "{YYYY-MM-DD}"
related_files:
  - "{path/to/related-file.md}"
---
```
