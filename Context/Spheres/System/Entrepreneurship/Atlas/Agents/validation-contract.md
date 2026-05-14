---
file_type: validation_contract
venture: Atlas
mission: Phase 1 – Chiropractic SOAP Note Generator
status: draft
direction_gate_required: true
last_updated: 2026-05-14
---

# Phase 1 Validation Contract – Atlas SOAP Note Generator

**Mission:** Accept ambient voice input from a chiropractic visit. Generate a structured SOAP note plus ICD-10 codes plus CPT codes plus treatment plan. Surface confidence scores. Post into one EHR via one adapter (initial target: Jane App, confirm post-Arlando discovery). Doctor reviews and finalises before any chart write completes.

**Pilot site:** Arlando Parker Jr.'s clinic.

**Status:** Draft. Operator approval required at Direction gate before any Execution proceeds.

This contract is a binary, evidence-bearing assertion list. Every assertion is either satisfied or not. Critique clears only when every assertion is satisfied with declared evidence. The contract is read by every Reviewer dispatch and re-read at every milestone boundary.

---

## Category A – HIPAA Boundary

### A1. Encryption posture

**Assertion:** Every patient data point processed by Atlas is encrypted in transit (TLS 1.3 minimum) and at rest (AES-256 minimum) at every step of the pipeline – ingest, processing, model call, persistence, EHR post-back.

**Evidence:** Independent penetration test report; encryption posture audit document signed by infrastructure provider.

**Owner:** AI Architecture Lead

**Reviewer:** Reviewer:Scrutiny

### A2. No PHI in logs

**Assertion:** No PHI appears in plain text in any system log, error trace, audit trail render, terminal output, or any artefact accessible outside the HIPAA-bounded data plane.

**Evidence:** Log review report across 1,000 simulated note generations using synthetic patient data; redaction test against deliberately injected PHI strings.

**Owner:** AI Architecture Lead

**Reviewer:** Reviewer:Scrutiny

### A3. BAA coverage

**Assertion:** Every external service that processes patient data is covered by a Business Associate Agreement signed and on file – including the LLM provider, infrastructure host, observability provider and the target EHR API connection.

**Evidence:** BAA registry with signed PDFs linked.

**Owner:** HIPAA Compliance Officer

**Reviewer:** Reviewer:Scrutiny

### A4. Audit log integrity

**Assertion:** Every access event involving patient data is written to an immutable, append-only audit log with timestamp, actor identifier, tokenised patient identifier and action type.

**Evidence:** Audit log schema document; integration test demonstrating append-only behaviour; sample audit log from end-to-end test run.

**Owner:** AI Architecture Lead

**Reviewer:** Reviewer:Scrutiny

---

## Category B – Clinical Accuracy

### B1. No medication hallucination

**Assertion:** No generated note contains a medication reference unless the doctor stated that medication explicitly in the ambient voice input.

**Evidence:** 100-note benchmark against synthetic visit transcripts including 20 deliberately medication-adjacent prompts; zero false-medication generations across the set.

**Owner:** AI Architecture Lead, Clinical Knowledge Curator

**Reviewer:** Reviewer:Scrutiny + Reviewer:Behavioural

### B2. Diagnosis code set membership

**Assertion:** Every ICD-10 code that appears in any generated note is a member of the curated chiropractic ICD-10 mapped set in `Knowledge Base/Coding/icd-10-chiropractic.md`.

**Evidence:** Schema validation against the curated set; integration test that rejects any code outside the set.

**Owner:** Clinical Knowledge Curator

**Reviewer:** Reviewer:Scrutiny

### B3. Procedure code set membership

**Assertion:** Every CPT code that appears in any generated note is a member of the curated chiropractic CPT mapped set in `Knowledge Base/Coding/cpt-chiropractic.md`, and the combination is valid against 2026 CMS chiropractic billing rules.

**Evidence:** Schema validation; CMS rule-pack validation; test against 50 known-good and 50 known-bad combinations.

**Owner:** Clinical Knowledge Curator

**Reviewer:** Reviewer:Scrutiny

### B4. Clinical claim traceability

**Assertion:** Every clinical claim in the generated note traces back to a specific span of the ambient voice input. The system surfaces this traceability to the doctor as part of the review surface.

**Evidence:** Traceability UI screenshot; integration test that verifies every claim is tagged with source span.

**Owner:** AI Architecture Lead

**Reviewer:** Reviewer:Scrutiny

### B5. Technique fidelity

**Assertion:** The plan of care and the technique-specific language in the generated note match the doctor's stated technique (Diversified, Gonstead, Activator, Thompson or mixed). The note does not introduce technique terms the doctor did not use.

**Evidence:** 50-note benchmark across all four technique styles, scored by Arlando for technique fidelity; minimum threshold 95% accuracy.

**Owner:** Clinical Knowledge Curator

**Reviewer:** Reviewer:Behavioural (Arlando-graded)

---

## Category C – Note Integrity

### C1. SOAP structure

**Assertion:** Every generated note contains four sections – Subjective, Objective, Assessment, Plan – in the doctor's chosen format, with no missing sections and no field-name drift.

**Evidence:** Schema validation across 100 generated notes.

**Owner:** AI Architecture Lead

**Reviewer:** Reviewer:Scrutiny

### C2. Outcome assessment capture

**Assertion:** When the doctor states a recognised outcome assessment (Oswestry, Neck Disability Index, VAS), the note captures the score in a structured field tied to the patient record.

**Evidence:** Test set of 30 visits containing outcome assessments; 100% capture rate.

**Owner:** Clinical Knowledge Curator

**Reviewer:** Reviewer:Scrutiny

---

## Category D – EHR Adapter Fidelity

### D1. Round-trip integrity

**Assertion:** Notes posted into the target EHR retain every field generated by Atlas without silent drop, transformation or schema loss. Atlas reads back the posted note and verifies field-by-field match before marking the post complete.

**Evidence:** End-to-end test against EHR sandbox with 50 notes; zero silent transformations.

**Owner:** EHR Adapter Engineer

**Reviewer:** Reviewer:Scrutiny

### D2. Atomic post-back

**Assertion:** Post-back to the EHR succeeds completely or rolls back completely. No partial writes. No orphaned records.

**Evidence:** Failure-injection test demonstrating rollback behaviour under simulated EHR API errors.

**Owner:** EHR Adapter Engineer

**Reviewer:** Reviewer:Scrutiny

---

## Category E – Human Verification

### E1. Doctor-in-loop enforcement

**Assertion:** No note is finalised in the EHR without explicit doctor review and approval. The system has no autonomous finalisation path in Phase 1.

**Evidence:** Code audit confirming no auto-finalise branch exists; UI confirmation of mandatory review step.

**Owner:** AI Architecture Lead

**Reviewer:** Reviewer:Scrutiny

### E2. Confidence scoring

**Assertion:** Every field in the generated note carries a confidence score. Fields below a configurable threshold are flagged for mandatory doctor review before the note can be approved.

**Evidence:** UI screenshot showing per-field confidence; threshold configuration document.

**Owner:** AI Architecture Lead

**Reviewer:** Reviewer:Scrutiny

---

## Category F – Regulatory Posture

### F1. State chiropractic board alignment

**Assertion:** Documentation generated by Atlas meets the documentation requirements of the chiropractic board in the pilot state.

**Evidence:** Legal opinion from regulatory counsel; documentation requirement checklist with each item satisfied.

**Owner:** Regulatory Counsel, HIPAA Compliance Officer

**Reviewer:** Reviewer:Scrutiny

---

## Critique Gate Clearance

The Critique gate for Phase 1 clears when:

1. All 14 assertions above are satisfied with declared evidence on file
2. Reviewer:Scrutiny has signed off on every Scrutiny-owned assertion
3. Reviewer:Behavioural has signed off on every Behavioural-owned assertion
4. The operator has reviewed the evidence dossier and approved release

No exceptions. No partial clearance. No "we will fix it in the next release."

---

## Contract Modification

This contract is locked once approved at the Direction gate. Modifications require:

1. A written change proposal naming the assertion being changed
2. The rationale and the new evidence requirement
3. Operator approval via a re-run of the Direction gate
4. Version bump and prior-version preservation in `Archive/`

---

*Atlas Phase 1 Validation Contract v1.0 (draft) – 2026-05-14*
