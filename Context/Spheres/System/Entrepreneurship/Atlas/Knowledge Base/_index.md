---
file_type: reference
venture: Atlas
status: active
last_updated: 2026-05-14
---

# Knowledge Base – Atlas

The defensible knowledge layer of Atlas. Every clinical artefact, every code, every technique definition, every EHR integration spec and every competitive intelligence file lives here. This is the moat – curated chiropractic-specific knowledge that general medical AI systems do not have.

The Knowledge Base mirrors the sphere graduation pattern from the personal Alfred operating system. Each domain earns its own file when it grows past a paragraph in the cluster index. Files load on demand based on the task.

---

## What Belongs Here

- Clinical knowledge – orthopedic tests, technique-specific terminology, listings, rehab protocols
- Coding references – chiropractic ICD-10 set, chiropractic CPT set, Medicare rules, payer-specific patterns
- Documentation standards – SOAP formatting, personal injury documentation, workers comp documentation
- EHR intelligence – per-vendor API surface, market share, integration depth, decision-maker profiles
- Competitive landscape – healthcare AI vendors, chiropractic-specific tooling, adjacent threats
- Methodologies – the curation method itself, training data construction, benchmark assembly

## What Does Not Belong Here

- Active product development files – those go in Production
- Pilot clinic relationships – those go in Operations/Clientele
- Brand and identity work – that goes in Creative
- Financial models – those go in Finance

---

## Subdirectories

| Folder | Contents | Status |
|---|---|---|
| Agents/ | Specialist roster, workflow registry, quality criteria | Scaffold present |
| Clinical/ | Orthopedic tests, listings, techniques, rehab protocols | Empty – Phase 1 priority |
| Coding/ | Chiropractic ICD-10, CPT, Medicare, payer rules | Empty – Phase 1 priority |
| Documentation/ | SOAP standards, PI documentation, workers comp documentation | Empty – Phase 1 priority |
| EHR/ | Per-vendor API surface and integration intelligence | Empty – Strategy + Production load |
| Competitive/ | Healthcare AI landscape, chiropractic-specific tooling | Empty – Strategy load |
| Methodologies/ | Curation method, training data construction, benchmark assembly | Empty – Production load |

---

## Clinical/ Scaffold (Phase 1 Priority)

The clinical sphere graduation list for Phase 1. Files are authored by the Clinical Knowledge Curator under Opus, with Arlando Parker Jr. as the Reviewer:Behavioural authority.

| File | Scope |
|---|---|
| `orthopedic-tests.md` | Kemp test, SLR, Yeoman, FABER, Spurling and the full chiropractic orthopedic test set – name, technique, indication, interpretation, ICD-10 link |
| `chiropractic-listings.md` | Listing nomenclature across techniques – the language for naming subluxation patterns |
| `diversified-technique.md` | Diversified-specific terminology, common adjustment language, plan-of-care patterns |
| `gonstead-technique.md` | Gonstead-specific terminology, listings, instrumentation references |
| `activator-technique.md` | Activator-specific terminology, indication patterns |
| `thompson-technique.md` | Thompson terminology, drop-piece references, indication patterns |
| `rehab-protocols.md` | Common chiropractic rehab prescriptions – exercises, frequency, progression |
| `postural-assessment.md` | Postural exam terminology, common findings, ICD-10 links |
| `outcome-assessments.md` | Oswestry, NDI, VAS, PSFS – structured capture and scoring |

## Coding/ Scaffold (Phase 1 Priority)

| File | Scope |
|---|---|
| `icd-10-chiropractic.md` | The full chiropractic ICD-10 mapped set – every code Atlas may emit |
| `cpt-chiropractic.md` | The full chiropractic CPT mapped set – every code Atlas may emit |
| `medicare-compliance.md` | Medicare documentation requirements, AT modifier rules, GA/GY/GZ modifiers, frequency limitations |
| `commercial-payer-patterns.md` | Common commercial payer denial patterns and how to avoid them |
| `personal-injury-coding.md` | PI-specific coding considerations |
| `workers-comp-coding.md` | Workers compensation coding considerations |

## Documentation/ Scaffold (Phase 1 Priority)

| File | Scope |
|---|---|
| `soap-note-standards.md` | The structural standard Atlas generates against |
| `personal-injury-documentation.md` | PI documentation requirements – attorney-facing exposure |
| `workers-comp-documentation.md` | Workers comp documentation requirements |
| `medicare-documentation.md` | Medicare documentation defensibility |
| `re-exam-standards.md` | Re-exam structure and timing |

## EHR/ Scaffold (Strategy + Production)

| File | Scope |
|---|---|
| `jane-app.md` | Jane API surface, authentication, schemas, post-back semantics, integration depth |
| `chirotouch.md` | ChiroTouch API surface and integration considerations |
| `genesis.md` | Genesis API surface and integration considerations |
| `ezbis.md` | EZBIS API surface and integration considerations |
| `prompt-emr.md` | Prompt EMR API surface and integration considerations |

## Competitive/ Scaffold (Strategy)

| File | Scope |
|---|---|
| `nuance-dax.md` | Microsoft Nuance Dragon Ambient Experience – primary care play |
| `abridge.md` | Abridge – ambient clinical AI competitor |
| `suki-ai.md` | Suki – hospital system AI scribe |
| `deepscribe.md` | DeepScribe – ambient scribe |
| `healthcare-ai-landscape.md` | The broader healthcare AI ecosystem – who wins where |
| `ehr-native-ai.md` | What the EHR vendors themselves are building |

---

## Curation Cadence

Clinical and Coding files are the highest-priority Phase 1 work. The order of curation:

1. `Coding/icd-10-chiropractic.md` and `Coding/cpt-chiropractic.md` – these are the membership sets that the validation contract checks against
2. `Coding/medicare-compliance.md` – the highest regulatory exposure
3. `Clinical/orthopedic-tests.md` – the test names and ICD-10 links the model needs at runtime
4. `Documentation/soap-note-standards.md` – the structural target
5. Arlando's primary technique file (whichever of Diversified/Gonstead/Activator/Thompson he uses)
6. The remainder, in priority order set by pilot need

Every Clinical and Coding file passes through Reviewer:Behavioural (Arlando-graded) before Critique clearance.

---

## Current State

Scaffold structure only. No clinical content authored yet. First curation pass begins post Direction-gate approval of the validation contract.
