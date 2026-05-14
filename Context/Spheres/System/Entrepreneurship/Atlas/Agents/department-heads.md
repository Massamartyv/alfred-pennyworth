---
file_type: reference
document_type: department_heads
venture: Atlas
status: active
last_updated: 2026-05-14
---

# Department Heads – Atlas

The organisational structure of AI-assisted roles within Atlas. Each department head is a role that Alfred assumes or dispatches a subagent into when work enters that studio scope. Department heads are not separate AI models – they are role definitions that shape context loading, crew selection and execution parameters.

---

## How Department Heads Work

When a task enters the system:

1. Alfred identifies which department head owns the task
2. Loads the department head primary files for context
3. Classifies the crew type (Researcher, Creator, Reviewer:Scrutiny, Reviewer:Behavioural)
4. Applies the execution tier from `agent-guidelines.md`
5. Reads `validation-contract.md` if the task touches clinical output
6. Selects model from `model-assignment.md`
7. Executes directly or dispatches a subagent with the role brief

---

## Active Department Heads

### Head of Creative

| Field | Value |
|---|---|
| Studio | Creative |
| Domain | Brand identity, voice, clinical communication standards |
| Primary files | `Creative/_index.md`, `Creative/Agents/_index.md` (to be created at art direction) |
| Reports to | You (Creative Director) directly through Alfred |

**Specialist roles under Head of Creative:**

| Role | Scope |
|---|---|
| Brand Strategist | Atlas positioning, identity evolution, category differentiation |
| Art Director | Visual direction for all design output – product UI, marketing, sales collateral |
| Clinical Voice Editor | The tone of every AI-generated artefact a doctor or patient sees; the voice of Atlas to its clinical audience |
| Product Copywriter | In-product copy, dashboard text, onboarding flows, error messaging |

---

### Head of Strategy

| Field | Value |
|---|---|
| Studio | Strategy |
| Domain | EHR landscape, competitive intelligence, chiropractic market behaviour, positioning |
| Primary files | `Strategy/_index.md`, `Knowledge Base/EHR/`, `Knowledge Base/Competitive/` |
| Reports to | Alfred |

**Specialist roles under Head of Strategy:**

| Role | Scope |
|---|---|
| EHR Landscape Analyst | Jane App, ChiroTouch, Genesis, EZBIS, Prompt EMR – API surface, market share, integration depth |
| Healthcare AI Competitive Analyst | Nuance DAX, Abridge, Suki, DeepScribe and emerging healthcare AI moves |
| Clinical Market Researcher | Chiropractic practice mix, payer behaviour, technique adoption, decision-maker profiles |
| Positioning Lead | Atlas positioning vs EHR-native AI features, vs general medical scribes |

---

### Head of Production

| Field | Value |
|---|---|
| Studio | Production |
| Domain | AI architecture, FastMCP service, EHR adapters, clinical knowledge curation, build quality |
| Primary files | `Production/_index.md`, `Knowledge Base/Clinical/`, `Knowledge Base/Coding/` |
| Reports to | Alfred |

**Specialist roles under Head of Production:**

| Role | Scope |
|---|---|
| AI Architecture Lead | FastMCP service design, crew orchestration, prompt engineering, model selection per crew |
| EHR Adapter Engineer | One file per EHR – authentication, data schemas, post-back semantics, error handling |
| Clinical Knowledge Curator | Sphere-style knowledge files for orthopedic tests, listings, technique-specific terminology, coding |
| Validation Engineer | Reviewer:Scrutiny and Reviewer:Behavioural infrastructure; contract test harness |

---

### Head of Growth

| Field | Value |
|---|---|
| Studio | Growth |
| Domain | Pilot expansion, channel architecture, partnerships, distribution |
| Primary files | `Growth/_index.md` |
| Reports to | Alfred |

**Specialist roles under Head of Growth:**

| Role | Scope |
|---|---|
| Pilot Lead | Manages pilot clinic onboarding, success criteria, conversion to paid |
| Network Channel Lead | Chiropractic associations, state boards, conference circuit, podcast appearances |
| Partnership Scout | EHR vendor partnerships (potential integration or JV plays), clinical association alliances |
| Founder Sales | First 10–50 clinics direct sales – operator-led, no SDR delegation |

---

### Head of Operations

| Field | Value |
|---|---|
| Studio | Operations |
| Domain | Pilot management, clinical advisor liaison, support, onboarding |
| Primary files | `Operations/_index.md`, `Operations/Clientele/Active/Arlando Parker Jr./` |
| Reports to | Alfred |

**Specialist roles under Head of Operations:**

| Role | Scope |
|---|---|
| Clinical Advisor Liaison | Arlando Parker Jr. relationship management; cadence, communications, scope tracking |
| Pilot Coordinator | Manages Arlando's clinic and subsequent pilot clinics through onboarding, training, success measurement |
| Support Lead | In-product support for pilot users; bug triage; escalation paths |
| Onboarding Lead | Clinic onboarding workflows – EHR connection, staff training, baseline note benchmarking |

---

### Head of Finance

| Field | Value |
|---|---|
| Studio | Finance |
| Domain | SaaS metrics, per-clinic unit economics, inference cost tracking, projections |
| Primary files | `Finance/_index.md` |
| Reports to | Alfred |

**Specialist roles under Head of Finance:**

| Role | Scope |
|---|---|
| Revenue Analyst | MRR, ARR, NRR, per-clinic expansion, cohort behaviour |
| Cost Analyst | Per-note inference cost, infrastructure cost, support cost, margin per clinic |
| Unit Economics Lead | CAC, LTV, payback period, clinic-segment economics |
| Financial Reporter | Monthly and quarterly P&L, cash flow, projections; investor-grade reporting once relevant |

---

### Head of Administration

| Field | Value |
|---|---|
| Studio | Administration |
| Domain | HIPAA compliance, BAAs, regulatory, entity formation, IP, advisor agreements |
| Primary files | `Administration/_index.md` |
| Reports to | Alfred |

**Specialist roles under Head of Administration:**

| Role | Scope |
|---|---|
| HIPAA Compliance Officer | BAAs, encryption posture, audit log architecture, breach response runbook |
| Regulatory Counsel | State chiropractic board requirements per pilot jurisdiction, telehealth interaction rules, malpractice exposure |
| IP Counsel | Patent strategy for clinical knowledge curation method, trademark filings, defensive IP |
| Entity Counsel | LLC or C-Corp formation, governance, advisor agreements (Arlando retainer / rev share), future equity instruments |

---

## Activating a Department Head

All department heads are role definitions only at venture genesis. When ready to automate:

1. Create an agent definition in `~/Alfred Pennyworth/Agents/` or in the studio's `Agents/` subfolder with the mission brief
2. Update this file to mark the department head as "Active – automated"
3. Configure the agent to read this file, `agent-guidelines.md`, `validation-contract.md` and `model-assignment.md` at session start
4. Begin logging performance data
5. Review after 30 days and adjust

---

*Atlas Department Heads v1.0 – 2026-05-14*
