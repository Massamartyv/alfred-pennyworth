---
file_type: reference
document_type: department_heads
venture: Atlas
status: active
last_updated: 2026-09-10
---

# Department Heads – Atlas

The organisational structure of AI-assisted roles within Atlas. Each department head is a role that Alfred assumes or dispatches a subagent into when work enters that department's scope. Department heads are not separate AI models – they are role definitions that shape context loading, crew selection and execution parameters.

All nine departments are head-led. Foundation and Knowledge Base, shared resources under the retired seven-studio layout, carry their own heads again since The Restoration, 2026-09-10. See each department's own `Agents/_index.md` for the full roster.

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

### Head of Foundation

| Field | Value |
|---|---|
| Department | Foundation |
| Domain | Community initiatives, philanthropy, education, giving; custodian of the brand fingerprint and venture mission |
| Primary files | `Foundation/_index.md`, `Foundation/Agents/_index.md`, `Foundation/brand-fingerprint.md` |
| Reports to | Alfred |

**Specialist roles under Head of Foundation:**

| Role | Scope |
|---|---|
| Foundation Coordinator | Scopes community initiatives, aligns giving strategy with brand and budget, coordinates educational outreach |

---

### Head of Marketing & Sales

| Field | Value |
|---|---|
| Department | Marketing & Sales |
| Domain | Brand identity, voice, clinical communication standards, sales pipeline |
| Primary files | `Marketing & Sales/_index.md`, `Marketing & Sales/Agents/_index.md` (to be created at art direction) |
| Reports to | You (Creative Director) directly through Alfred |

**Specialist roles under Head of Marketing & Sales:**

| Role | Scope |
|---|---|
| Brand Strategist | Atlas positioning, identity evolution, category differentiation |
| Art Director | Visual direction for all design output – product UI, marketing, sales collateral |
| Clinical Voice Editor | The tone of every AI-generated artefact a doctor or patient sees; the voice of Atlas to its clinical audience |
| Product Copywriter | In-product copy, dashboard text, onboarding flows, error messaging |
| Founder Sales | First 10–50 clinics direct sales – operator-led, no SDR delegation |

---

### Head of Business Development

| Field | Value |
|---|---|
| Department | Business Development |
| Domain | EHR landscape, competitive positioning, chiropractic market behaviour, pilot expansion, channel architecture, partnerships |
| Primary files | `Business Development/_index.md`, `Knowledge Base/EHR/`, `Knowledge Base/Competitive/` |
| Reports to | Alfred |

**Specialist roles under Head of Business Development:**

| Role | Scope |
|---|---|
| Positioning Lead | Atlas positioning vs EHR-native AI, vs general medical scribes |
| Pilot Lead | Manages pilot clinic onboarding, success criteria, conversion to paid |
| Network Channel Lead | Chiropractic associations, state boards, conference circuit, podcast appearances |
| Partnership Scout | EHR vendor partnerships (potential integration or JV plays), clinical association alliances |

---

### Head of Product Development

| Field | Value |
|---|---|
| Department | Product Development |
| Domain | AI architecture, FastMCP service, EHR adapters, clinical knowledge curation, build quality, offer architecture |
| Primary files | `Product Development/_index.md`, `Knowledge Base/Clinical/`, `Knowledge Base/Coding/` |
| Reports to | Alfred |

**Specialist roles under Head of Product Development:**

| Role | Scope |
|---|---|
| AI Architecture Lead | FastMCP service design, crew orchestration, prompt engineering, model selection per crew |
| EHR Adapter Engineer | One file per EHR – authentication, data schemas, post-back semantics, error handling |
| Clinical Knowledge Curator | Sphere-style knowledge files for orthopedic tests, listings, technique-specific terminology, coding |
| Validation Engineer | Reviewer:Scrutiny and Reviewer:Behavioural infrastructure; contract test harness |

---

### Head of Operations

| Field | Value |
|---|---|
| Department | Operations |
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

### Head of Finances

| Field | Value |
|---|---|
| Department | Finances |
| Domain | SaaS metrics, per-clinic unit economics, inference cost tracking, projections |
| Primary files | `Finances/_index.md` |
| Reports to | Alfred |

**Specialist roles under Head of Finances:**

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
| Department | Administration |
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

### Head of Human Resources

| Field | Value |
|---|---|
| Department | Human Resources |
| Domain | Team structure, contractor onboarding, culture, advisor relationships |
| Primary files | `Human Resources/_index.md` |
| Reports to | Alfred |

**Specialist roles under Head of Human Resources:**

| Role | Scope |
|---|---|
| People Lead | Team structure, contractor onboarding, culture, advisor relationships |

---

### Head of Knowledge Base

| Field | Value |
|---|---|
| Department | Knowledge Base |
| Domain | EHR landscape, healthcare AI competitive intelligence, chiropractic market research, case studies, methodology documentation |
| Primary files | `Knowledge Base/_index.md`, `Knowledge Base/Agents/_index.md` |
| Reports to | Alfred |

**Specialist roles under Head of Knowledge Base:**

| Role | Scope |
|---|---|
| Knowledge Curator | Captures research, indexes intelligence, maintains the case study library and methodology documentation |
| Market Researcher | Chiropractic practice mix, payer behaviour, technique adoption, decision-maker profiles – formerly the Clinical Market Researcher seat |
| Competitive Analyst | EHR API surface and market share, healthcare AI vendor moves, positioning maps and pricing intelligence – formerly the EHR Landscape Analyst and Healthcare AI Competitive Analyst seats |

---

## Activating a Department Head

All department heads are role definitions only at venture genesis. When ready to automate:

1. Create an agent definition in `~/Alfred Pennyworth/Agents/` or in the department's `Agents/` subfolder with the mission brief
2. Update this file to mark the department head as "Active – automated"
3. Configure the agent to read this file, `agent-guidelines.md`, `validation-contract.md` and `model-assignment.md` at session start
4. Begin logging performance data
5. Review after 30 days and adjust

---

*Atlas Department Heads v1.0 – 2026-05-14. Reorganised from seven studios to the nine departments 2026-09-10 (The Restoration): the retired Creative department head folded into the new Head of Marketing & Sales, with Founder Sales carried in from the retired Growth department; the retired Strategy department head folded into the new Head of Business Development, with Pilot Lead, Network Channel Lead and Partnership Scout carried in from the retired Growth department; the retired Production department head folded whole into the new Head of Product Development; the finance head was renamed Head of Finances; the People Lead seat carried over from `Administration/Agents/_index.md` into the new Head of Human Resources.*
