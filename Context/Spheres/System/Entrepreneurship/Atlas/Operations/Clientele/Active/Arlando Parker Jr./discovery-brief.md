---
file_type: discovery_brief
venture: Atlas
recipient: Arlando Parker Jr.
recipient_role: Clinical Advisor
phase: Reconnaissance
status: draft
direction_gate_required: true
last_updated: 2026-05-14
related_files:
  - "Operations/Clientele/Active/Arlando Parker Jr./_index.md"
  - "Agents/validation-contract.md"
  - "Business Development/_index.md"
---

# Atlas – Phase 1 Discovery Brief

**Recipient:** Arlando Parker Jr., Clinical Advisor
**Author:** Atlas operator
**Date issued:** 2026-05-14
**Return expected:** Within seven calendar days of receipt
**Estimated time to complete:** 45 to 60 minutes

---

## Purpose

This brief is the Reconnaissance instrument for Atlas Phase 1. The Phase 1 deliverable is a chiropractic SOAP note generator that takes ambient voice input, produces a structured note plus validated ICD-10 and CPT codes, and posts the result into one EHR for doctor review and finalisation. The pilot site is your clinic.

Before Phase 1 build proceeds, ten clinical and operational inputs need to be resolved. These inputs shape the first EHR adapter, the order in which clinical knowledge files are curated, the validation thresholds, the pilot success metrics, the term sheet structure and the regulatory posture. Each answer below has direct downstream consequence on the build plan.

The brief is structured as four sections. Each question carries a short rationale so the strategic weight of the answer is clear. Open prose is welcome. Bullet points are welcome. If a question does not apply, say so and the rationale will adjust accordingly.

---

## Section A – Clinical Practice Profile

### A1. Primary EHR

**Question:** Which EHR system does the clinic currently run? If more than one system is in use, name each and indicate the primary.

**Why this matters.** This determines the first adapter target. Atlas is built as a thin service above existing EHRs rather than a replacement, so the choice of first integration sets the build sequence for the entire venture. Jane App, ChiroTouch, Genesis, EZBIS and Prompt EMR each carry distinct API surfaces and integration depth. The first adapter informs every subsequent one.

**Answer:**

_(open)_

---

### A2. Technique style

**Question:** What is the primary technique style in use? If the clinic uses a blended approach, indicate the dominant style and the secondary styles by approximate weighting.

Options to consider: Diversified, Gonstead, Activator, Thompson, Sacro-Occipital, Cox flexion-distraction, Network Spinal, applied kinesiology, instrument-assisted, or a mixed approach with named components.

**Why this matters.** This determines which clinical knowledge file is curated first and at what depth. Generic medical AI systems hallucinate on technique-specific listings, miss diversified adjustment nuance and fumble technique-coded plan language. The clinical knowledge curation work scopes directly to the technique profile of the pilot site, and the technique fidelity assertion (Validation Contract B5) tunes to your sign-off.

**Answer:**

_(open)_

---

### A3. Payer mix

**Question:** What is the approximate payer mix across active patients? A rough percentage breakdown across the categories below is sufficient.

Categories to consider:

- Medicare
- Personal Injury (PI)
- Commercial insurance
- Workers compensation
- Cash and self-pay
- Other (specify)

**Why this matters.** This shapes coding priorities for Phase 1. Medicare-heavy practices need conservative CPT selection, exhaustive medical necessity documentation and modifier accuracy. PI-heavy practices need narrative-rich documentation and outcome assessment capture. Cash-heavy practices loosen coding pressure and shift weight toward plan-of-care clarity. The validation contract assertions for diagnosis and procedure code set membership tune to the payer-mix profile of the pilot.

**Answer:**

_(open)_

---

### A4. Patient volume and visit cadence

**Question:** What is the approximate weekly patient visit volume across the clinic? Average visit duration and the typical mix of new-patient versus established-patient visits is useful context.

**Why this matters.** This calibrates the inference cost model, the throughput requirements for the FastMCP service and the pilot success metrics. A 200-visit-per-week clinic running 12-minute established visits has a different operational profile than a 50-visit-per-week clinic running 30-minute integrated visits. The model assignment for runtime SOAP generation tunes to this volume profile.

**Answer:**

_(open)_

---

## Section B – Pilot Parameters

### B1. Pilot success criteria

**Question:** What does success look like at the end of Phase 1 from the clinical seat? Specifically, what observable change in your daily workflow, documentation quality or end-of-day burden would mark this as a clear win?

**Why this matters.** The validation contract carries 14 binary assertions for clinical and technical clearance. Those clear the Critique gate. Pilot success is a separate measure – it answers whether the system is worth running in the clinic at all, from the clinician's seat. Phase 1 success metrics anchor the term sheet, the expansion case and the eventual product positioning. Concrete is more useful than aspirational here.

**Answer:**

_(open)_

---

### B2. Pilot constraints

**Question:** What constraints should the build plan respect? Three sub-questions:

1. **Timeline.** Are there clinical, business or personal windows in the next six months that the pilot timeline should work around?
2. **Staff training appetite.** How much new-system learning load can the clinic absorb? Is there a chiropractic assistant or front-office team member who would lead day-to-day pilot operations, or would this sit primarily with you?
3. **Risk tolerance.** Where on the spectrum does the clinic sit between "ship it and iterate from production feedback" and "do not let anything touch a real chart until every edge case is exhausted"?

**Why this matters.** Each answer changes the build plan. Timeline shapes milestone sequencing. Training appetite determines how much of the interface surface needs to optimise for clinician-only operation versus team operation. Risk tolerance calibrates the synthetic-versus-live data ratio in pre-pilot testing and the doctor-in-loop verification depth at launch.

**Answer:**

_(open)_

---

## Section C – Commercial Framing

### C1. Retainer, revenue share or hybrid

**Question:** Across the three commercial structures proposed in the dossier – monthly retainer only, revenue share only, or hybrid retainer plus revenue share – which structure aligns with your preference? Specific numbers are not required at this stage. The shape is what matters.

For context, the dossier carries the hybrid structure as the working default, reflecting the most common arrangement for clinical advisors at venture-stage healthcare companies. The hybrid gives the advisor a baseline that holds steady regardless of monetisation pace, plus upside that scales with venture success.

**Why this matters.** The answer anchors the term sheet, which is drafted at the Direction gate and presented to you for negotiation and counsel review before signature. Structural preference informs the negotiation register before any number is named.

**Answer:**

_(open)_

---

## Section D – Regulatory and Risk Posture

### D1. State chiropractic board jurisdiction

**Question:** In which state is the clinic licensed to practice, and therefore which state chiropractic board governs documentation standards for the pilot?

**Why this matters.** Documentation requirements vary materially across state chiropractic boards – frequency of re-examination, signature requirements, retention timelines, scope-of-practice annotations and audit posture all change by jurisdiction. Validation contract assertion F1 requires a regulatory counsel opinion against the documentation requirements of the pilot state. The state determines the counsel scope and the assertion's evidence requirements.

**Answer:**

_(open)_

---

### D2. Patient consent posture for AI-assisted documentation

**Question:** Does the clinic have existing patient consent language that already covers AI-assisted documentation, or would new consent language need to be drafted and adopted before the pilot proceeds? If existing language is in place, a copy of the relevant clause is useful.

**Why this matters.** Ambient voice capture for clinical documentation is a category that most pre-2024 consent forms do not contemplate. If the clinic already has updated consent language, the pilot can move faster. If new consent is required, the build plan absorbs the legal drafting timeline and the consent-collection workflow at pilot launch.

**Answer:**

_(open)_

---

### D3. Malpractice and cyber liability coverage

**Question:** What is the clinic's current coverage posture for malpractice and cyber liability? Specifically:

1. Malpractice carrier and policy limits
2. Cyber liability carrier and policy limits, if separately held
3. Whether the existing carriers have been notified of the intent to run an AI-assisted documentation pilot, and whether their response has been received

**Why this matters.** Two coverage questions sit at the boundary between Atlas and the clinic. First, whether the existing clinic malpractice carrier requires notification or rider for AI-assisted documentation. Second, whether Atlas extends its own coverage to indemnify clinical output, and at what limits. The combination of clinic-side and Atlas-side coverage informs the term sheet, the BAA structure and the regulatory counsel scope.

**Answer:**

_(open)_

---

## What Happens After Submission

1. **Operator review.** The returned brief is read, gaps surfaced, follow-up questions sent within 48 hours of receipt.
2. **Direction-gate package.** The brief, the validation contract and the term sheet draft are assembled into the Direction-gate package and presented for operator approval.
3. **Direction-gate decision.** Approval clears the path for Phase 1 Execution: FastMCP scaffold, first EHR adapter, clinical knowledge curation in the dominant technique style, validation infrastructure and the pre-pilot synthetic test set.
4. **Pilot kickoff conversation.** Once Direction clears, a 60-minute conversation is scheduled to align on pilot success metrics, communication cadence, weekly review structure and the curation queue for clinical knowledge files.

Phase 1 build estimated timeline from Direction-gate clearance to live pilot is 90 to 120 days, contingent on EHR API access timelines and the consent posture answer above.

---

## Return Format

Reply with the completed brief in any format that suits – inline in this document, as a separate document, voice memo with rough notes, or a 45-minute call where these are walked through verbally and the operator captures responses against the brief.

Voice memo and call options carry the same weight as written answers. The questions matter more than the format.

---

*Atlas Phase 1 Discovery Brief v1.0 (draft) – 2026-05-14 – Tier 2 (Execute Then Notify) – Operator review pending before send*
