---
name: source-inventory
type: template
schema_version: 1
---

# Source Inventory Template

A source inventory is a pre-synthesis ledger of the source set a mission draws on. It is the input-side counterpart to the validation contract: where the validation contract gates the output at Critique, the source inventory hardens the input at Reconnaissance. The agent reads and accounts for every source before it fuses anything, so the brief inherits a clean working set rather than a confident blend of stale, conflicting and duplicate material.

The deliverable is a data-room pack of four artefacts produced together: the source inventory itself, a conflict log, a missing-context list and a duplicates report.

## When this template applies

Required for any Manor Protocol mission that synthesises a corpus of pre-existing sources of mixed provenance – research-and-synthesis work where the hallucination risk enters through the inputs rather than the model. Typical triggers:

- A pile of documents of uncertain authority, currency or origin – transcripts, decks, exports, prior drafts, email threads
- Client discovery from raw intake material
- Any deliverable whose claims must trace to specific sources – legal, financial, strategic, board-facing

Not required for missions with no meaningful source set – a logo, a workout log, a language drill, a single-source rewrite. The trigger is the corpus, not the stakes. A short, single-source task carries no data room and needs none.

## Authoring rules

- One entry per source. Preserve the original – the inventory records, it never edits or deletes a source
- Each entry declares authority, currency and intended use, with the path as its evidence
- Surface, do not resolve. The conflict log and the duplicates report name the mess – the operator decides how it resolves
- Never rank a source away or silently drop it. A superseded or duplicate source stays in the inventory, marked
- The missing-context list is mandatory even when empty. Absent material is often more load-bearing than present material
- Authority values are one of: `authoritative`, `supporting`, `background`, `superseded`
- Status values are one of: `current`, `superseded`, `duplicate`, `orphaned`
- The template is the schema and stays local; instances live in `.working/{mission-name}/` and, after Critique, on the mission record as an H3 section

## The discipline: find, do not silently resolve

The failure mode this artefact exists to prevent is the agent smoothing a conflict it should have surfaced. A strong reconnaissance names the disagreement and hands it back. A weak one blends three versions of a plan into a confident paragraph nobody can trust.

This is also the one place Navigation Rule 1 is scoped rather than overridden. Notion wins on which *record* is current – a balance, a task status, a system of record. The conflict log governs which *claim* to trust mid-synthesis when two sources disagree on substance. Applying "Notion wins" to a source-material conflict is the smoothing this artefact forbids.

## Lifecycle

1. Alfred drafts the inventory during Reconnaissance, before any synthesis
2. Alfred surfaces the conflict log, missing-context list and duplicates report at Direction
3. Operator reviews the working set, resolves conflicts and confirms nothing is missing before the Direction gate clears
4. The inventory is stored at `.working/{mission-name}/source-inventory.md` during execution
5. Every Creator and Researcher dispatch reads the inventory and treats the operator-confirmed authority order as binding
6. The final writing prompt references the inventory: which source is authoritative, which is background, what is unsupported
7. The inventory is copied onto the mission record – the scoped Notion Projects entry, defined in `Agents/_index.md` – once Critique clears

## Relationship to Manor Protocol gates

The source inventory promotes the Direction gate from optional to required for that mission – the reviewed working set is the artefact gating Direction, the same way a validation contract is. It composes with the validation contract: the inventory validates the inputs, the contract validates the outputs. A mission heavy enough to carry both gates its entrance and its exit.

---

## Template

Copy the block below into `.working/{mission-name}/source-inventory.md` and fill in.

```markdown
---
mission: {mission-name}
created: {YYYY-MM-DD}
inventory_version: 1
---

## Source Inventory

S1. {path}
    - Type: transcript | deck | spreadsheet | export | email | note | pdf
    - Date: {YYYY-MM-DD or unknown}
    - Authority: authoritative | supporting | background | superseded
    - Status: current | superseded | duplicate | orphaned
    - Supports: {what claims this source can back}
    - Limits: {what it must not be used for}
    - Use: {how it should be used in the final work}

S2. {next source}
    - ...

## Conflict Log

C1. {the claim or value in tension}
    - Sources: {Sx} vs {Sy}
    - Nature: contradiction | version drift | naming mismatch | unsourced number
    - Recommended handling: {proposal, not a resolution}
    - Resolution: {left blank until the operator decides at Direction}

## Missing-Context List

M1. {what is absent}
    - Referenced by: {Sx, or "nowhere – inferred gap"}
    - Why it matters: {the claim it would support or undercut}
    - Status: needed before synthesis | useful | blocked on operator

## Duplicates Report

D1. {version family name}
    - Members: {Sx, Sy, Sz}
    - Confidence: high | medium | low
    - Suspected current: {Sx}
    - Action: surfaced for operator decision – never auto-deleted
```

If a section has no content, write a single line: `None.` Do not omit the section header.

---

## Worked example

A mission to draft a board update from a folder of mixed material:

```markdown
---
mission: q2-board-update
created: 2026-06-19
inventory_version: 1
---

## Source Inventory

S1. .working/q2-board-update/operating-plan-v3.xlsx
    - Type: spreadsheet
    - Date: 2026-06-10
    - Authority: authoritative
    - Status: current
    - Supports: revenue, runway and headcount figures
    - Limits: forward projections are modelled, not committed
    - Use: the single source for all numbers in the update

S2. .working/q2-board-update/april-board-deck.pdf
    - Type: deck
    - Date: 2026-04-15
    - Authority: background
    - Status: superseded
    - Supports: prior-quarter narrative and framing
    - Limits: numbers are stale – do not cite as current
    - Use: continuity of story only

S3. .working/q2-board-update/founder-sync-transcript.txt
    - Type: transcript
    - Date: 2026-06-12
    - Authority: supporting
    - Status: current
    - Supports: decision context behind the headcount change
    - Limits: a spoken account, not a record of decisions
    - Use: source for the "why" behind the plan

## Conflict Log

C1. Q2 revenue figure
    - Sources: S1 at $1.42M vs S2 at $1.6M
    - Nature: version drift
    - Recommended handling: trust S1 as the current model; S2 predates the May reforecast
    - Resolution:

## Missing-Context List

M1. Source for the 18-month runway claim
    - Referenced by: S3, "we are good through next year"
    - Why it matters: the update will state runway to the board
    - Status: needed before synthesis

## Duplicates Report

D1. Operating plan
    - Members: operating-plan-v3.xlsx, operating-plan-final.xlsx
    - Confidence: high
    - Suspected current: operating-plan-v3.xlsx – later mtime, matches S3 figures
    - Action: surfaced for operator decision – never auto-deleted
```

The conflict log entry is the point of the artefact. Without it, the two revenue figures would have been silently averaged or one picked at random, and the board update would have shipped with a soft number underneath.

---

*Schema version 1. Manor Protocol Phase 1 deliverable – input-side hardening. 2026-06-19. Updated 2026-07-10 – mission record made concrete; authoring rule on template vs instance location added.*
