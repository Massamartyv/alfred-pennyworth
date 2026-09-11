# The Almanac – design specification

Working notes from the 2026-08-12 session, drawn from the operator's own handwritten architecture and 11 rulings taken at the widget. Moved here from `.working/day-schedule/` on 2026-09-09 when the instrument shipped, so the design of record lives beside the thing it governs and survives the monthly sweep. State lives on the mission record: https://app.notion.com/p/The-Almanac-3ba1896165cf81ab80cac051406cc7b8

## The governing principle

**Modularity inside fixed containers.** The blocks never move, so the day is trackable. What sits inside them does move, so it never feels rigid. In the operator's words: the day is trackable but does not feel fixed to any rigid schedule, even when it is the routine of the season.

Everything below is downstream of that sentence. Where a design choice threatens it, the principle wins.

## The six blocks

Six equal four-hour blocks tile the full 24 hours from the 05:00 wake. None left over, no gaps, no overlaps.

| # | Name | Hours | Renders | Character |
|---|---|---|---|---|
| I | Morning Routine | 05:00 – 09:00 | yes | Wake, prayer and manifestation, journal, plants and pets, training, supplements |
| II | Administration | 09:00 – 13:00 | yes | Language learning, email, administrative duties, team meetings, sales outreach, focus work. Deep work plus internal admin |
| III | Collaboration | 13:00 – 17:00 | yes | External meetings, content, team building and recruitment, focus work. Next-day scheduling at the close |
| IV | Social | 17:00 – 21:00 | yes | Dinner, daily cleaning, instrument practice, social commitments |
| V | Evening Routine | 21:00 – 01:00 | no | First rest block. Nightlife and going out eat into this one by design |
| VI | Night Owl | 01:00 – 05:00 | no | Second rest block. The operator should be home before it begins |

The two rest blocks are defined but do not render. The calendar carries the four waking blocks; rest is the absence of a block on the surface while remaining part of the model.

## What renders, and what does not

**Renders as a container event:** blocks I through IV, every day.

**Renders as an event inside a block:** Next Actions from the personal Notion Tasks database. Only pomodoro-sized Next Actions – parent tasks stay at goal level, per the standing task-breakdown doctrine.

**Renders as an event, sourced as an ordinary task:** the modular commitments – training, running, cleaning. They are Notion Tasks like any other, with a default position by convention rather than by rule. Training defaults to the morning and cleaning to the evening; both may be placed anywhere the day allows.

**Never renders:** skincare, meditation, reading, and anything else purely habitual. The operator's reasoning is sound and worth preserving – something you will either do or not do gains nothing from being scheduled, and loses something by appearing as a thing you failed to tick.

## Settled rulings, 2026-08-12

| Question | Ruling |
|---|---|
| Authority | Notion rules, the calendar renders. A one-way projection on the state-cache pattern; edits made in Calendar.app are lost at the next render |
| Block model | Six equal four-hour blocks from 05:00. Container events, with tasks as separate events inside them |
| Names | The operator's own, with roman numerals retained – the same ordering device he uses inside each block |
| Modular commitments | Ordinary Notion tasks. One source, one mechanism, nothing bespoke |
| Rest blocks | Defined but unrendered |
| Seasonality | The structure is invariant. Cut and bulk change contents and timing, never the blocks |
| Ritual | An interactive Sunday session. Not a scheduled agent – scheduling is judgment, and this estate's scheduled tasks have failed silently three times this year |
| Week start | Monday |
| Scope | Personal tasks only for now; the blocks render in full regardless, so the day keeps its true shape. Five Points tasks flow in once the Navigation Rule 2 boundary is ruled |
| Destination | The existing Personal calendar |

## The signature rule

The operator was warned that rendering onto Personal risks a re-render clearing something placed by hand, and ruled for Personal regardless. The risk is engineered out rather than argued:

- Every event written by the renderer carries a signature line in its `description`.
- The render clears only events bearing that signature inside the target window. Anything without it is invisible to the clear, whatever its title or time.
- The signature is checked, never inferred from position or naming.

Operator-placed events are therefore safe by construction rather than by care, and a partially failed render is recoverable – re-running clears exactly its own output and nothing else.

## Constraints inherited from the calendar bridge

Rebuilt over AppleScript on 2026-08-12. Two properties shape this design:

1. **Recurring events cannot be read as occurrences.** Calendar.app exposes only the master event with its original start date. A weekly repeating template could be written but never read back, so the week is written as discrete events each Sunday. The operator's chosen ritual sidesteps this by construction.
2. **Writes reach the whole series.** No single occurrence of a recurring event can be edited or deleted, so rendered events must be non-recurring. The Sunday model already satisfies this.

## Storage

The scheduled time lives on the personal Tasks database as **`Scheduled`** – a date property carrying a time, created 2026-08-12 and deliberately matching `Publish Date` on the Content Calendar so the two function identically. Pennyone reads one to schedule a post; The Almanac reads the other to place a task.

The block is **derived from the hour, never stored**. There is no second copy of the truth to drift out of step, and moving a task between blocks means changing one value rather than two.

`Due Date` is untouched and keeps its own meaning. A task due Friday may be scheduled Tuesday, and conflating the two would break the first task planned ahead of its deadline.

## Unfinished work

A Next Action that goes unworked returns to the Sunday session unscheduled, alongside everything else wanting time. It does not roll forward on its own. The operator decides whether it earns a slot again or was never really the work – which is the judgment the session exists for, and it stops unwanted tasks riding the calendar for months looking busy.

Implemented as `almanac.sh sweep`, which clears the `Scheduled` value on any open task whose time has passed.

## Build record, 2026-09-09

The gate behind the Domesday remainder was lifted by the operator and the design built as specified. Four decisions were taken at the widget that the August rulings did not cover:

| Question | Ruling |
|---|---|
| Destination | A dedicated `Almanac` calendar rather than Personal. The August ruling predated sight of the calendar list; a separate surface makes a re-render structurally incapable of touching a hand-placed event and lets the whole scaffold be toggled off in one click, which serves the governing principle |
| Task duration | 30 minutes, eight to a block |
| First render | Immediately, the remainder of the week rather than waiting for the first Sunday |
| The ritual | Alfred drafts a placed week, the operator edits. His judgment spends itself on the disagreements rather than on data entry |

Delivered: `almanac.py` and `almanac.sh` in this folder; the `almanac` skill at `~/.claude/skills/almanac/`. Two defects were found and fixed in the course of the build – the apple-calendar bridge could not escape newlines for AppleScript, so any multiline event note failed to compile; and the renderer's clear matched on start date rather than overlap, which duplicated a block on every mid-block re-render. Both are documented in the README under Two invariants.
