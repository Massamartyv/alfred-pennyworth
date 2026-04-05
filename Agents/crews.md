# Crews -- Universal Agent Classification

Crews are the six types of work that any agent in the Alfred OS ecosystem can perform. They are not agents themselves. They are classifications that determine how a task is executed -- what the agent's mandate is, what its output type looks like and how it is evaluated.

When a task enters the system, Alfred determines the crew type before dispatching. A single workflow may chain multiple crew types in sequence.

---

## The Six Crews

### I. Strategist -- Researcher

Research, analyse, synthesise intelligence and produce strategic recommendations.

**Output types:** Research briefs, competitive analyses, strategic memos, data synthesis, recommendations with supporting evidence

**When to dispatch:** The task requires gathering and synthesising information before a decision can be made. The output is intelligence, not a deliverable.

**Evaluation criteria:** Accuracy of sources, depth of analysis, clarity of recommendations, actionability of insights

---

### II. Creator -- Builder

Build, write, design and produce tangible output.

**Output types:** Copy, code, designs, proposals, templates, content, documentation, deliverables

**When to dispatch:** The task requires producing something that did not exist before. The output is a deliverable, not a recommendation.

**Evaluation criteria:** Quality of craft, adherence to brand standards, completeness, readiness for review

---

### III. Evaluator -- Grader

Review, audit and grade output against defined criteria.

**Output types:** Audit reports, quality grades, revision lists, pass/fail assessments, feedback with specific citations

**When to dispatch:** Output exists and needs to be assessed before it moves forward. The Evaluator never produces the deliverable -- only judges it.

**Evaluation criteria:** Thoroughness of review, specificity of feedback, accuracy of grading against stated criteria

---

### IV. Maestro -- Orchestrator

Coordinate multi-step workflows, sequence dependencies and manage handoffs between crew types.

**Output types:** Workflow plans, dependency maps, sequenced task lists, status reports across multiple workstreams

**When to dispatch:** The task is too complex for a single crew dispatch. Multiple steps with dependencies need to be sequenced and tracked.

**Evaluation criteria:** Logical sequencing, completeness of dependency mapping, clarity of handoff points

---

### V. Validator -- Approver / Compliance

Check output against standards, flag violations and gate deliverables before they ship.

**Output types:** Compliance reports, approval/rejection decisions, violation flags, brand consistency checks

**When to dispatch:** Output needs to pass through a quality gate before reaching a client, audience or external system. The Validator does not fix problems -- it identifies them and sends work back.

**Evaluation criteria:** Completeness of standard coverage, accuracy of violation detection, clarity of remediation guidance

---

### VI. Explorer -- Market Sensor

Scout trends, sense shifts, analyse the competitive landscape and surface opportunities.

**Output types:** Trend reports, market signals, competitive intelligence, opportunity briefs, early warning flags

**When to dispatch:** The task is forward-looking. Not analysing what exists, but sensing what is emerging or shifting.

**Evaluation criteria:** Timeliness of signals, relevance to current strategy, quality of pattern recognition, actionability of opportunities surfaced

---

## Crew Chaining

Most non-trivial work chains multiple crews. Common patterns:

| Pattern | Sequence | Example |
|---|---|---|
| Research-to-build | Strategist then Creator | Research a prospect, then write their proposal |
| Build-and-check | Creator then Evaluator then Validator | Write copy, grade it, check brand compliance |
| Full cycle | Strategist then Creator then Evaluator then Validator | Research, build, grade, approve |
| Sensing loop | Explorer then Strategist | Spot a trend, then analyse its implications |
| Orchestrated campaign | Maestro dispatching all five others | Multi-channel campaign requiring research, creation, evaluation, validation and market sensing |

---

## Crews vs Department Heads

Crews classify **what type of work** is being done.
Department heads classify **which domain** the work belongs to.

A Head of Creative might dispatch a Strategist crew for brand research and a Creator crew for ad copy. A Head of Finance might dispatch a Strategist crew for revenue analysis and a Validator crew for compliance checks.

The two systems are orthogonal. Crews travel horizontally across all departments. Department heads provide vertical structure within a venture.

---

*Alfred OS -- Universal Crew Classification v1.0 -- April 2026*
