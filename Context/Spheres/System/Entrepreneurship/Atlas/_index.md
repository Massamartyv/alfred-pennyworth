---
file_type: venture_index
venture: Atlas
working_code_name: true
final_identity_pending: art-direction
venture_stage: Reconnaissance
status: active
methodology: The Manor Protocol
last_updated: 2026-09-10
---

# Atlas – Venture Index

> **Working code name.** Final brand identity awaits an art-direction pass. Atlas refers to the first cervical vertebra – the bone that supports the head and bridges spine to skull. The metaphor is functional: this venture is the supportive intelligence layer above existing chiropractic systems.

AI-native chiropractic intelligence layer. A thin clinical service that sits above existing EHRs – Jane App, ChiroTouch, Genesis, EZBIS, Prompt EMR – converting ambient voice into structured SOAP notes, validated ICD-10 and CPT coding, treatment plans and downstream insurance workflows. The thesis is augmentation, not replacement: chiropractors do not switch EHRs easily, so Atlas integrates with the systems they already run.

Stage: Reconnaissance. Phase 1 deliverable is a SOAP note generator piloted at Arlando Parker Jr.'s clinic, posting into a single EHR.

## Movement

Governed by the Movement Doctrine – `Context/values-hierarchy.md` §5.5, ratified 2026-09-09 from the operator's forced-choice values hierarchy. In the work domain the terminal value is Impact, and Impact resolves to movement rather than accumulation.

Every commitment this venture opens declares in advance which two of the three units it moves, and the quarter it is judged in.

- **Sovereignty bought** – months of runway, hours reclaimed, distance closed to $25,000 a month. Revenue is not itself movement; the freedom it purchases is, and the figure must be stated in those terms or it does not count.
- **Someone else changed** – a client, reader or listener whose situation differs because the work exists.
- **Work in the world** – a thing shipped and live where people meet it.

Two of three, or the work is thin and gets called thin. Judged at quarter close: moved, or named and re-declared exactly once. A second failure kills the work or hands it off. Scale, margin and enterprise value are the supporting case, never the frame. Billion-dollar trajectory is the benchmark that says whether the quarter's movement was real or trivial, not the goal pursued.

Live declarations: Notion Projects, Atlas workspace once provisioned. Until then declarations buffer to `.working/session-buffer/`, never to the Five Points workspace, per Plugin Routing rule 9.

## Strategic Thesis

Every healthcare AI company is converging on roughly the same five-layer stack – ambient capture, clinical documentation, insurance automation, scheduling/CRM, analytics. The defensible edge is not the architecture. The defensible edge is chiropractic-specific clinical knowledge. General medical scribes hallucinate on Gonstead listings, miss diversified technique nuance and fumble PI documentation. Atlas owns that knowledge layer.

Distribution is the under-discussed problem. Chiropractors do not buy SaaS the way oncologists do. The product needs an embedded channel from day one – pilot site, association network, founder-led sales, and partnership conversations with the EHR vendors themselves.

## Architectural Pattern

Atlas inherits the Pennyone architecture – a thin FastMCP service routing a single intent through multiple backend adapters. Pennyone hits Instagram, TikTok, X, Reddit and others via Zernio. Atlas hits Jane App, ChiroTouch, Genesis, EZBIS, Prompt EMR via direct EHR APIs. Same shape, different domain.

## The Manor Protocol

All work follows The Manor Protocol – five phases, two hard gates, creative excellence as the governing standard. Healthcare AI elevates Critique to load-bearing status. No clinical output ships without binary validation against the per-mission contract.

**Lifecycle:** Reconnaissance > Direction [gate] > Execution > Critique [gate] > Release

## Navigation

### Nine Departments

| Department | Craft | Start Here |
|---|---|---|
| Foundation/ | Brand fingerprint (source of truth); community initiatives, education, chiropractic profession contribution | Foundation/_index.md |
| Administration/ | HIPAA compliance, BAAs, regulatory, entity formation, IP | Administration/_index.md |
| Finances/ | SaaS metrics, per-clinic unit economics, inference cost tracking | Finances/_index.md |
| Business Development/ | EHR landscape, competitive positioning, chiropractic market behaviour, pilot pipeline, channel architecture, partnership development | Business Development/_index.md |
| Marketing & Sales/ | Brand identity, voice, clinical communication standards, sales pipeline | Marketing & Sales/_index.md |
| Operations/ | Pilot management, clinical advisor relationships, support workflows | Operations/_index.md |
| Product Development/ | AI architecture, FastMCP service, EHR adapters, clinical knowledge curation, offer architecture | Product Development/_index.md |
| Human Resources/ | Team, contractors, advisors, culture | Human Resources/_index.md |
| Knowledge Base/ | Clinical knowledge, EHR intelligence, coding references, competitive landscape | Knowledge Base/_index.md |

### Shared Governance

| File | Purpose |
|---|---|
| Agents/_index.md | The Manor Protocol definition scoped to Atlas |
| Agents/agent-guidelines.md | Execution tiers, red lines, HIPAA boundaries |
| Agents/department-heads.md | Role definitions and specialist seats |
| Agents/validation-contract.md | Phase 1 binary assertions, evidence, reviewers |
| Agents/model-assignment.md | Per-mission model allocation |
| Agents/integrations.md | Plugin and tool connections; the HIPAA boundary |

Plugin scope is recorded in `Agents/integrations.md`, created 2026-08-08. Nothing is connected yet, which is appropriate at Reconnaissance. Expected first integrations: Jane App API as the first EHR adapter, Anthropic API for the clinical documentation layer, BAA-covered hosting, database and logging, and a payment rail at pilot conversion. **The HIPAA boundary in that file gates the whole integration lane** – no surface touching protected health information is provisioned before a Business Associate Agreement covers it, and no surface in the current estate has one.

## Active State

Live state: Notion Projects and Tasks – **currently misfiled in the Five Points workspace** (Atlas – Arlando Parker Jr. Pilot Terms). Atlas is a sovereign venture and a peer brand, not a Five Points asset. Under the 2026-08-08 one-workspace-per-venture ruling it provisions its own workspace and these records migrate out. Recorded in `Agents/integrations.md`, Finding 1.

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

*Last updated: 2026-09-10 – The Restoration: reverted from the seven-studio-plus-shared-resources shape to the nine original departments. Creative folded into Marketing & Sales, Strategy split across Business Development, Product Development and Knowledge Base, Production folded whole into Product Development, Growth split across Business Development, Marketing & Sales and Product Development, and the HR subfolder formerly under Administration became the standalone Human Resources department. Previously 2026-09-05 – Last updated line added at the September heartbeat; content unchanged since 2026-08-08.*
