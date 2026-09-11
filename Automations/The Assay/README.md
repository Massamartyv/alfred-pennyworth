# The Assay

The measurement layer the Alfred operating system did not have. The Whetstone sharpens;
the Assay measures what the sharpening was worth. Built under the operation brief at
`.working/the-assay/00-operation-brief.md`, 2026-09-10.

## What it is

A surface-agnostic evaluation harness. One frozen dispatcher (`the-assay.sh`), a small
registry of suites, and one editable surface per suite - a fixture set, a skill roster, a
payload set. Every suite declares a fixed-cost wall-clock budget, prints exactly one
scalar, and appends one line to an append-only verdict ledger. Reference shape:
karpathy/autoresearch, per the operation brief - a frozen harness, one editable surface
per experiment, a fixed-cost run, a single scalar metric, refusal where no clean verifier
exists.

**Autonomy Tier 0.** The harness proposes and measures. It never applies a change, never
writes to Notion, never sends, publishes or commits. Nothing here has an auto-apply path.

**Language choice.** The top-level dispatcher and the deterministic suites (gates, and the
run.sh entry points generally) are bash, matching `Automations/Whetstone/monitor-check.sh`
and the Guards layer's own tonal model - the thing being tested is bash, so the drill calls
it directly rather than through a translation layer. Suites Two and Three do the actual
data-heavy work (JSON parsing, parallel subprocess dispatch, payload validation) in Python,
called through a three-line bash `run.sh` wrapper so every suite presents the same entry
point to the harness regardless of implementation language underneath.

## How to run it

```bash
Automations/The\ Assay/the-assay.sh              # run every registered suite
Automations/The\ Assay/the-assay.sh gates          # run one suite
Automations/The\ Assay/the-assay.sh --quiet skills # scalar line and failures only
Automations/The\ Assay/the-assay.sh --list         # list registered suites and budgets
```

Exit codes: 0 every run suite passed, 1 at least one suite failed or was unscoreable, 2 bad
usage. Full run takes roughly two minutes end to end - suite one finishes in about a
second, suite three in about a second, suite two (the only model-judged suite) takes most
of the wall clock because it makes one small `claude -p --model haiku` call per declared
query.

## How to add a suite

1. Create `suites/{name}/run.sh`, executable, following the suite contract: print any
   number of report lines, print exactly one line beginning `SCALAR: ` before exiting, and
   exit 0 (pass), 1 (fail) or 3 (unscoreable - no clean verifier exists for what was asked).
2. Add one row to the registry inside `the-assay.sh`: `name:budget_seconds:runner_path`.
   This is the only edit `the-assay.sh` itself should ever need for a new suite - the
   dispatcher is frozen precisely so that adding coverage never means touching the loop
   that runs it.
3. Keep the suite's fixed-cost budget honest. Deterministic suites get seconds. Model-
   judged suites declare a turn ceiling (see `suites/skills/runner.py`'s
   `PER_SKILL_QUERY_CAP`) in addition to the wall-clock backstop the harness enforces.

## The three suites

### Suite one - gates and monitors (`suites/gates/`)

Seeded-fault drills against the real gate layer: `Automations/Guards/state-patterns.grep`,
`agent-receipt.sh`, `working-sweep.sh`, and `Automations/Whetstone/monitor-check.sh`.
Deterministic, no model call. Every drill calls the *real* gate script against a fixture
built fresh in a temp directory each run (via `CLAUDE_PROJECT_DIR` override) - never
against a copy of the gate, and never against the live estate's own `.working/` or
`.claude/cache/`. 13 drills, currently 13/13.

**Proof of coupling.** `suites/gates/run.sh --prove-red` (not run by the default harness
pass, invoked directly) temporarily renames `agent-receipt.sh` aside, re-runs the drill
that depends on it, confirms the drill goes red, and restores the script via output that
also runs on early exit. This is the literal "remove a gate, show the drill red" proof the
operation brief asks for, made repeatable rather than performed once by hand. It never
touches anything outside `Automations/Guards/agent-receipt.sh` and always restores it in
the same invocation.

**A genuine catch made while building this suite:** the first version of the
`state-patterns.grep` drill matched the pattern file with plain `grep -E`, and the drill
came back green for the wrong reason - it reported the tripwire caught a seeded "Status:"
line, but a diagnostic run showed the pattern file's own entries are lowercase and the drill
was not actually invoking case-insensitive matching, so it was silently failing to catch
the seeded fault while still, by coincidence of an earlier bug, reporting green. Reading
`.githooks/pre-commit` showed the live tripwire always runs `grep -E -i -f`. The fix was
one flag. Left in the ledger and named here because it is exactly the kind of failure this
mission exists to catch - a check whose language does not match the thing it verifies.

### Suite two - skills (`suites/skills/`)

Trigger accuracy: does the router load a skill when it should and skip it when it should
not, judged against the SKILL.md frontmatter description alone, one `claude -p --model
haiku` call per query from a neutral working directory (never this repo's own root - see
`judge.sh`'s header for why). Five skills, one unified schema - see `schema.md` for the
reconciliation of the two grammars that existed before this pass, and `registry-notes.md`
for why these five. Currently running around 77-78 of 78 correct per pass (0.80 is the
provisional pass bar - see the handoff for why that number and not a higher one).

This is the one genuinely model-judged suite in the harness, and it is not perfectly
reproducible run to run - two consecutive full runs during this build scored 77/78 and
78/78, both on the same 78 declared queries. That variance is the nature of a
semantic judgment call made by a model rather than a deterministic grep or exit code, and
it is reported honestly rather than smoothed - the ledger keeps every run, so the variance
itself becomes visible over time instead of being hidden inside a single number.

### Suite three - Notion writes (`suites/notion/`)

Schema-correctness validation on captured write payloads - never a live workspace call.
Five checkable classes with clean deterministic verifiers: property-type mismatches
(multi_select/relation not the JSON-array-string shape the enhanced connector requires, or
a non-ISO date), icon-convention violations (emoji, or a built-in-icon URL naming an icon
confirmed not to exist), heading-level violations (H1/H2 instead of the house H3-only
standard), link-protocol violations (a Link/URL property storing the protocol instead of
the bare domain), and missing-required violations (no Sphere relation, no template_id).
Eight fixtures, one clean control and seven malformed across those five classes (one of
the seven is a compound fixture proving three classes do not mask each other). 8/8.

## What this deliberately refuses to score

- **Skill output quality.** Suite Two judges only whether a skill fires, never whether its
  output is good. `journey-planner`'s four original prompt/expected-output pairs are
  preserved at `~/.claude/skills/journey-planner/evals/output-quality-reference.md` rather
  than discarded, ready to seed a future suite - grading generated prose against expected
  prose is a taste call, not a clean verifier, and this pass does not pretend otherwise.
- **A live Notion workspace.** Suite Three validates payload shape against fixtures only.
  Whether the target page, database or relation actually exists in either workspace is a
  separate mission by the operation brief's own scope line.
- **Anything without a clean verifier, generally.** Any suite that cannot decide pass/fail
  without a human judgment call reports `unscoreable` (exit 3) rather than inventing a
  number. No suite in this pass currently hits that path in normal operation - Suite Two's
  `runner.py` hits it only if the `claude` CLI is missing or no skill in the registry
  produces a valid eval file, both defensive paths, not the steady state.

## The verdict ledger

`ledger/verdicts.tsv` - append-only, one line per suite run: timestamp, suite, scalar,
budget used, budget declared, pass/fail/unscoreable. Machine-derived, never hand-edited.
This lives under the harness home by explicit carve-out from the operation brief's own
"no state to local files" constraint - it is not a Status/Stage/Pending block in tracked
markdown, and its only author is `lib/ledger.sh`. It already carries real history from this
build, including the two failures caught while fixing the portable timeout wrapper (macOS
ships no `timeout` binary) and the `state-patterns.grep` case-sensitivity bug above - left
in place rather than cleared, because an append-only ledger that gets reset before anyone
reads it is not actually append-only.

## What this harness is not

Not a blocking CI gate. Two triggers run it, both added by operator ruling on 2026-09-10:
the gates suite runs in `.githooks/pre-commit` on every commit (warn-only, about one second,
does not append to the ledger), and the full three-suite run happens weekly inside the
`whetstone-retrospective` scheduled task, which appends to the ledger and alerts via iMessage
on any failed or unscoreable suite. Not a skill-output grader. Not a live-Notion adapter. Not an auto-apply mechanism of any kind -
Tier 0 holds until an operator explicitly opens Tier 1, and this harness's own pass-rate
curve is the stated precondition for that ruling.
