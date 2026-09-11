# Crews – Universal Agent Classification

Crews are the five types of work that any agent in the Alfred operating system ecosystem can perform. They are not agents themselves. They are classifications that determine how a task is executed – what the agent's mandate is, what its output type looks like and how it is evaluated.

When a task enters the system, Alfred determines the crew type before dispatching. A single workflow may chain multiple crew types in sequence, and a single agent may carry multiple crew tags when its work spans more than one type.

The three-crew taxonomy expanded to five on 2026-05-14. Mediator and Broadcaster were promoted from coordination patterns to formal crews, inspired by Factory's five multi-agent strategies (AI Engineer, 2026). The earlier collapse from six to three on 2026-04-29 – retiring Maestro, merging Strategist and Explorer into Researcher, merging Evaluator and Validator into Reviewer – held; the new additions cover work types that the three-crew model deferred as coordination patterns and that the operating system now treats as first-class.

---

## The Five Crews

### I. Researcher

Research, analyse, synthesise intelligence, scout trends and surface opportunities.

**Output types:** Research briefs, competitive analyses, strategic memos, data synthesis, trend reports, market signals, opportunity briefs, recommendations with supporting evidence.

**When to dispatch:** The task requires gathering and synthesising information before a decision can be made, OR the task is forward-looking – sensing what is emerging or shifting in the landscape. The output is intelligence, not a deliverable.

**Evaluation criteria:** Accuracy of sources, depth of analysis, clarity of recommendations, actionability of insights, timeliness of signals, quality of pattern recognition.

---

### II. Creator

Build, write, design and produce tangible output.

**Output types:** Copy, code, designs, proposals, templates, content, documentation, deliverables.

**When to dispatch:** The task requires producing something that did not exist before. The output is a deliverable, not a recommendation.

**Evaluation criteria:** Quality of craft, adherence to brand standards, completeness, readiness for review.

---

### III. Reviewer

Review, audit, grade and validate output against defined criteria. Gate deliverables before they ship.

**Output types:** Audit reports, quality grades, revision lists, pass/fail assessments, compliance reports, approval/rejection decisions, violation flags, brand consistency checks, feedback with specific citations.

**When to dispatch:** Output exists and needs to be assessed before it moves forward. The Reviewer never produces the deliverable – only judges it. Includes both substantive review (does the work hold up) and compliance gating (does it meet the standard).

**Evaluation criteria:** Thoroughness of review, specificity of feedback, accuracy of grading against stated criteria, completeness of standard coverage.

#### Tiers

Reviewer is a single crew with two tiers dispatched as distinct subtypes. Mechanical compliance and end-user verification are different jobs and require different cost profiles.

| Tier | Speed | Domain | Examples |
|---|---|---|---|
| Reviewer:Scrutiny | Fast, deterministic | Mechanical checks | Lint, type check, tests, fresh code review per feature, brand-fingerprint compliance, grammar nazi pass, Notion schema correctness, link integrity, sphere alignment |
| Reviewer:Behavioural | Slow, expensive | End-to-end verification | Spawn the application and interact with it, read-as-end-user pass on content, dry-run automations against test targets |

**Triggers:**

- Reviewer:Scrutiny – required for every Critique-gated artefact
- Reviewer:Behavioural – required when the artefact has user-facing state: shipped code, published content, sent communications, deployed automations

**Behavioural pattern for content.** A dedicated agent reads the artefact in fresh context as if they were the end-user – an Epiphany subscriber, a Conversation listener, an Instagram viewer. The agent reports back on whether the hook works, whether the message lands, whether the call to action is clear. A focus group of one, agent-driven.

Mission planning declares which tier each milestone requires. Tier markers carry through to the agent type tables in `_index.md` and to each agent's frontmatter.

---

### IV. Mediator

Resolve contention over shared resources. Surface tradeoffs, optimise across multiple stakeholders and find win-wins where they genuinely exist.

**Output types:** Tradeoff analyses, allocation recommendations, prioritisation matrices, conflict-resolution memos, brokered agreements, decision framings with weighted criteria, multi-stakeholder option trees, dependency reconciliations.

**When to dispatch:** Two or more concerns must be balanced against each other and the right answer is not obvious from any single viewpoint. Pricing an offer when value, market positioning and margin pull in different directions. Allocating attention across competing initiatives when each has a credible claim. Vendor or platform selection when each option dominates on a different axis. Reconciling Researcher findings that point to incompatible conclusions. Resource scheduling when Creator dispatches parallelise on overlapping inputs.

**Evaluation criteria:** Clarity of the tradeoffs surfaced, fairness of the framing across stakeholders, defensibility of the recommended path, transparency about what is being given up, completeness of stakeholder representation, durability of the resolution.

**Distinction from Reviewer.** Reviewer audits a single artefact against a fixed standard. Mediator reconciles multiple inputs against each other when no single standard adjudicates. Reviewer says "this passes or fails." Mediator says "given these positions, this is the best path forward and these are the costs."

---

### V. Broadcaster

Distribute shared context, status and signal. Keep coherence across multi-agent missions, multi-mission state and multi-channel output.

**Output types:** Briefings, status reports, syndication packages, milestone announcements, gate-clearance notifications, context propagations, multi-channel distribution packages, coherence audits across distributed state, dependency-aware update bundles.

**When to dispatch:** Many parties – agents, ventures, channels, audiences – need the same picture or the same update. Producing the weekly portfolio briefing. Pushing a state change downstream when an upstream decision shifts. Broadcasting a Manor Protocol gate clearance so dependent crews can start work. Distributing finished content across all six syndication platforms with platform-appropriate framing. Sending the milestone signal that lets a Mediator know its tradeoff has been resolved upstream.

**Evaluation criteria:** Coherence of the broadcast across recipients, accuracy of context conveyed, completeness of distribution, fidelity of cross-channel adaptation, timeliness of signal, prevention of stale state.

**Distinction from Creator.** Creator produces a new artefact. Broadcaster routes existing artefacts and state to where they need to be heard. A briefing that is freshly written is Creator work; the act of distributing it to the portfolio is Broadcaster work. Many agents – Watchtower, Penny-one – chain Creator and Broadcaster inside a single run.

---

## Crew Chaining

Most non-trivial work chains multiple crews. Common patterns:

| Pattern | Sequence | Example |
|---|---|---|
| Research-to-build | Researcher then Creator | Research a prospect, then write their proposal |
| Build-and-check | Creator then Reviewer | Write copy, grade it, check brand compliance |
| Full cycle | Researcher then Creator then Reviewer | Research, build, grade, approve |
| Sensing loop | Researcher (forward-looking) then Researcher (deep analysis) | Spot a trend, then analyse its implications |
| Decide-and-signal | Mediator then Broadcaster | Resolve a tradeoff, then notify dependent crews |
| Build-and-syndicate | Creator then Broadcaster | Produce content, then distribute across all channels |
| Audit-then-mediate | Reviewer then Mediator | Multiple Reviewer findings conflict – Mediator reconciles before the gate |
| Research-to-mediate | Researcher then Mediator | Surface options, then resolve which to pursue |

Multi-step orchestration is what Alfred-as-orchestrator already does. It is not a separate crew.

---

## Crews vs Department Heads

Crews classify **what type of work** is being done.
Department heads classify **which domain** the work belongs to.

A Head of Marketing & Sales might dispatch a Researcher crew for brand research, a Creator crew for ad copy, a Mediator crew when two campaign directions compete and a Broadcaster crew to syndicate the chosen direction across channels. A Head of Finances might dispatch a Researcher crew for revenue analysis, a Reviewer crew for compliance checks and a Mediator crew when investment options must be ranked.

The two systems are orthogonal. Crews travel horizontally across all departments. Department heads provide vertical structure within a venture.

---

*Alfred operating system – Universal Crew Classification v3.0 – Mediator and Broadcaster crews added 2026-05-14*
