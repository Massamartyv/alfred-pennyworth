# The unified skill eval schema

Two schemas existed before this suite, both under `~/.claude/skills/{skill}/evals/`:

- `ui-ux-pro-max/evals/evals.json` - a trigger-accuracy schema. `should_trigger` and
  `should_not_trigger` prompt arrays, judged against the SKILL.md frontmatter description
  only, plus a hand-authored `baseline` block recording a point-in-time accuracy score.
- `journey-planner/evals/evals.json` - a prompt-and-expected-output schema. Four prompts,
  each paired with a paragraph of prose describing the full Notion project tree the skill
  should produce. No trigger judgment at all - it assumes the skill already fired and
  grades the output.

These are not two dialects of the same idea. They score two different things: routing
(would the skill load) and generation quality (is the output right). The operation brief
scopes this pass to routing only - "trigger accuracy is the scalar... output-quality
judging is out of scope for this pass" - so the routing schema is the one that survives,
on the merits:

1. **It has a clean verifier.** "Would the router load this skill given this prompt and
   this description" is a bounded, single-turn judgment with a binary answer. "Is this the
   correct 30-task Notion tree" is not checkable without either running the skill for real
   (a live Notion write, explicitly out of scope) or grading prose against prose, which is
   taste, not measurement. Karpathy's verifiability routing rule names exactly this
   distinction, and it is the reason Suite Two is scoped the way it is.
2. **It is cheaper and comparable across skills.** A trigger judgment is one short model
   call per query. An output-quality judgment on `journey-planner` requires generating a
   full trip project for each of four prompts before anything can be graded - the suite's
   fixed-cost budget could not hold five skills of that shape in one run.
3. **It matches where skill-enhancer already points.** `skill-enhancer/references/
   eval-integration.md` documents an aspirational `evals/trigger-evals.json` runner
   (`scripts/run_eval`, flat `{"query": ..., "should_trigger": bool}` array) that the same
   file admits "does not yet exist as runnable code." The trigger schema is the one house
   precedent already assumes will exist. This suite is that tooling, finally built.

## What changed from `ui-ux-pro-max`'s shape

The nested `should_trigger` / `should_not_trigger` arrays are kept - they carry more than a
flat boolean (a `route` annotation on the negative set, which matters when a query should
skip this skill but land somewhere specific). The `baseline` block is dropped. A hand-
authored, point-in-time accuracy score sitting next to the test declarations invites drift
- the moment the harness runs for real, the ledger is the authoritative record of what the
suite scored and when, and a second, unrun-derived number in the same file is a claim
competing with evidence. Eval files declare test cases; the ledger declares results.

## The schema

```json
{
  "skill": "skill-name",
  "schema_version": 1,
  "eval_type": "trigger",
  "notes": "free text - judging scope, known borderline cases, provenance",
  "queries": {
    "should_trigger": [
      { "prompt": "a realistic user message that should load this skill" }
    ],
    "should_not_trigger": [
      { "prompt": "a realistic user message that should not load this skill",
        "route": "where it should go instead, or 'none' if nothing should fire",
        "borderline": false }
    ]
  }
}
```

`route` is required on every `should_not_trigger` entry - a negative test that does not say
where the query should actually go is a weaker test, because it cannot distinguish "this
skill correctly stayed silent" from "nothing in the roster would have fired either."
`borderline` is optional and marks a query that is a genuine near-miss rather than a clean
negative, matching the judging convention already established in the `ui-ux-pro-max` file.

## Migration record

- `ui-ux-pro-max/evals/evals.json` - reshaped in place. 10 should_trigger and 10
  should_not_trigger prompts carried over unchanged; `route` added to every negative
  (inferred from the original file's own annotations, already present); `baseline` block
  removed.
- `journey-planner/evals/evals.json` - reshaped in place. The four existing prompts became
  the should_trigger set, `prompt` field renamed from `eval_name`-adjacent structure to
  match the unified shape. No should_not_trigger set existed in the source file - six were
  authored from the skill's own frontmatter exclusions ("do not fire for Five Points client
  travel logistics... meal planning... gift sourcing... non-travel project creation"). The
  four original `expected_output` paragraphs are preserved in
  `journey-planner/evals/output-quality-reference.md` rather than discarded - they are real
  authored material for the output-quality suite this pass explicitly does not build.
