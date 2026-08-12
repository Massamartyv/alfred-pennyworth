# Medicine

## Spheres Covered

Medicine – the personal health and clinical-reasoning vertical of the Mind cluster. Adjacent to Botany for the plant material, to Body for fitness and anatomy, to Soul for the inner work that health questions frequently sit next to.

---

## Domain Constants

**Mandate.** Root-cause, natural-first personal medicine practised in partnership with licensed care. The sphere exists to reason well about the health of one person over decades – to find causes rather than to silence signals, to reach for food, sleep, movement and plant material before reaching for a prescription and to route to a physician without hesitation the moment the situation calls for one. Nature first is a sequence, not an ideology. Conventional medicine is a rung on the ladder, not the enemy of it.

**The line that never moves.** Nothing in this sphere diagnoses. Differentials carry probabilities and go to a licensed physician for confirmation. Every recommendation carries an honest evidence grade. Every botanical is checked against current medications and conditions before it is spoken aloud. The red-flag list overrides all preference, always.

**Governing artefact.** `values-charter.md` is the founding file and the highest authority in the sphere. Where any other file in this folder conflicts with the charter, the charter wins.

**Operating instrument.** The `dr-thompkins` skill at `~/.claude/skills/dr-thompkins/` is how this knowledge is practised. The skill carries the consultation behaviour; this folder carries the knowledge the behaviour draws on. Neither is useful without the other.

Live state: Notion – Medicine sphere page resource databases, personal workspace.

---

## Context

### Files in this sphere

| File | What it holds |
|---|---|
| `values-charter.md` | Nature First, Truth Always – the therapeutic ladder, the evidence grades, the red-flag list, the non-negotiables. Founding artefact. |
| `consultation-frameworks.md` | The five-layer method stack – Calgary Cambridge, SOAP charting, the Lifestyle Medicine pillars as data schema, Bayesian differential reasoning, the Functional Medicine Matrix. |
| `functional-ranges.md` | Seed reference of commonly drawn markers with conventional reference ranges beside tighter functional-optimal ranges, plus what drift toward each edge tends to mean. |
| `materia-medica.md` | Seed herbal reference – primary actions, honest evidence grade, typical preparations and the interactions that matter, per botanical. |

### The record

The operating record lives in Notion, on the Medicine sphere page in Sphere Manager, as three resource databases in the personal workspace:

- **Consultations** – one entry per consultation, charted in SOAP form, carrying the differential, the ladder rung applied, the evidence grade on every recommendation and a follow-up date.
- **Lab Results** – one entry per drawn marker per draw, carrying value, units, the conventional range and the functional range in force at the time, so drift is legible across years rather than across a single panel.
- **Biometrics** – the ambient stream. Weight, resting heart rate, heart-rate variability, sleep, blood pressure and anything else tracked continuously rather than ordered.

Nothing from those three databases is mirrored into this folder. This folder holds method and reference; Notion holds the record of one life. Reading the record before recommending is not optional – the charter treats it as memory, and memory is what separates a physician from a search engine.

### Loading rule

Load `values-charter.md` on any health question, without exception. Load `consultation-frameworks.md` when a consultation is actually being conducted rather than a fact being looked up. Load `functional-ranges.md` when a lab panel is in hand. Load `materia-medica.md` before any botanical leaves the mouth. Do not preload the whole folder for a question about whether magnesium is worth taking at night.

### What this sphere is not

Not a substitute for a physician. Not a fitness programme – that is `personal-trainer` and the Body cluster. Not a nutrition or recipe surface – that is `michelin-chef` and Culinary Arts. Not inner work – that is `therapist` and the Soul cluster. Health questions touch all three; the boundary holds anyway, and the handoff is explicit when a question crosses it.

---

## Maintenance

| Trigger | Action |
|---|---|
| New lab panel drawn | Log every marker to Lab Results, then read the panel against `functional-ranges.md` as a pattern rather than marker by marker |
| Functional range contradicted by the operator personal baseline across three or more draws | Refine the working value in `functional-ranges.md` and note the reason |
| Botanical recommended for the first time | Confirm dosing and interactions against a current source before the recommendation, never from this folder alone |
| Follow-up date reached on any Consultations entry | Record the honest outcome, including no effect and made it worse |
| Annually | Review `functional-ranges.md` and `materia-medica.md` against current literature; both files are seeds, not scripture |

---

*Last updated: 2026-07-25 – sphere founded under the house-call mission.*
