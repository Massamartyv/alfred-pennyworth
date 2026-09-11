---
file_type: reference
venture: Atlas
status: active
last_updated: 2026-09-10
---

# Product Development – Atlas

The execution engine. Where the AI architecture is designed, the FastMCP service is built, the EHR adapters are written and the clinical knowledge is curated – and where the offer itself, tiers and pricing structure, is designed. Product Development owns build quality across every artefact Atlas ships – software, knowledge files, integrations, offers.

---

## What Belongs Here

- AI architecture – FastMCP service design, crew orchestration, prompt engineering
- EHR adapter implementation – one adapter per target EHR
- Clinical knowledge curation (active development) – the files that ship as the knowledge layer
- Voice ingest pipeline – audio capture, transcription, structured extraction
- Validation harness – the code that runs Reviewer:Scrutiny and Reviewer:Behavioural
- Schema definitions for SOAP, ICD-10, CPT and EHR-specific payloads
- Quality assurance workflows prior to release
- Offer architecture – tiers, bundles, transaction models
- Pricing and packaging strategy – pricing models, tier structures, per-clinic economics

## What Does Not Belong Here

- Brand and aesthetic direction – that goes in Marketing & Sales
- Pilot onboarding and clinical advisor relationships – those go in Operations
- HIPAA compliance posture and BAAs – that goes in Administration
- Sales pipeline execution and channel architecture – those go in Marketing & Sales and Business Development
- Reference clinical knowledge (curated, locked) – that lives in Knowledge Base after Critique clearance

## Subdirectories

| Folder | Contents | Status |
|---|---|---|
| Agents/ | Specialist roster, workflow registry, quality criteria | Scaffold |
| Architecture/ | FastMCP service design, crew orchestration, prompt architecture | Empty – Phase 1 priority |
| Adapters/ | Per-EHR adapter specifications and implementation notes | Empty – Phase 1 priority |
| Knowledge Curation/ | Active drafts of clinical knowledge files before Critique | Empty |
| Validation/ | Test harness, benchmark sets, evaluation scripts | Empty |
| Schemas/ | SOAP, ICD-10, CPT, EHR-specific data schemas | Empty |
| Offers/ | Offer catalogue, pricing tiers, transaction models | Empty – design pending pilot data |
| Pricing/ | Pricing models, tier structures, per-clinic economics | Empty |

## Architectural Pattern

Atlas inherits the Pennyone architecture from the Alfred operating system:

```
atlas/                                  (modeled on Integrations/pennyone)
├── server.py                           – FastMCP entry; voice + text intake
├── adapters/                           – one file per EHR
│   ├── jane.py
│   ├── chirotouch.py
│   ├── genesis.py
│   ├── ezbis.py
│   └── prompt_emr.py
├── crews/
│   ├── researcher.py                   – patient context, prior notes, eligibility
│   ├── creator.py                      – SOAP draft, ICD-10, CPT, plan
│   └── reviewer/
│       ├── scrutiny.py                 – coding validity, compliance, schema
│       └── behavioural.py              – clinician read-through
├── knowledge/                          – curated clinical knowledge loaded at runtime
│   ├── orthopedic-tests.md
│   ├── chiropractic-listings.md
│   ├── diversified-technique.md
│   ├── gonstead-technique.md
│   ├── icd-10-chiropractic.md
│   ├── cpt-chiropractic.md
│   ├── medicare-compliance.md
│   └── pi-documentation.md
├── contracts/                          – validation contracts loaded at runtime
│   ├── hipaa.md
│   ├── clinical-accuracy.md
│   └── coding-validity.md
└── audit/                              – append-only audit log writer
```

The implementation lives at `~/Alfred Pennyworth/Integrations/atlas/` once Phase 1 build begins. The repository for the venture itself lives separately under the Five Points or Atlas GitHub organisation pending entity formation.

## Phase 1 Build Sequence

1. Curate `Knowledge Base/Coding/icd-10-chiropractic.md` and `Coding/cpt-chiropractic.md` – the validation membership sets must exist before any code can reference them
2. Curate `Knowledge Base/Clinical/orthopedic-tests.md` and the technique file matching Arlando's primary style
3. Stand up the FastMCP scaffold at `Integrations/atlas/`
4. Build the first EHR adapter against sandbox credentials (initial target: Jane App)
5. Build the Creator crew – ambient voice in, structured SOAP draft + codes + plan out
6. Build Reviewer:Scrutiny – schema validation, code-set membership checks
7. Build Reviewer:Behavioural – clinician read-through
8. Wire the validation harness against the Phase 1 contract
9. End-to-end sandbox test with synthetic visit data
10. Arlando pilot deployment under doctor-in-loop

## Active State

Live state: Notion Projects and Tasks, Five Points workspace.

## Key Registries

- Offer catalogue: `Offers/_offers-registry.md` (to be created)

---

*Folded 2026-09-10 (The Restoration) from the retired Production studio, carried whole (AI architecture, EHR adapters, clinical knowledge curation, validation harness, schemas, architectural pattern, Phase 1 build sequence), the offer-catalogue piece of the retired Growth studio (Offers/ subdirectory, offer architecture), and the pricing piece of the retired Strategy studio (Pricing/ subdirectory, pricing and packaging strategy).*
