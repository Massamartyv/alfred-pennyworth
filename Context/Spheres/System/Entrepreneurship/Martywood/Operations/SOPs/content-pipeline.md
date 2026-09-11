---
file_type: sop
sop_id: MW-000
name: Content Pipeline
venture: Martywood
trigger: Any idea entering the system, from any capture rail
owner: Operations
status: active
last_updated: 2026-09-09
---

# MW-000 – Content Pipeline

The master pipeline governing every piece of Martywood content across all three properties – Marty V, Marty Gras and Epiphany. Property-specific SOPs sit beneath this one and inherit its gates.

## Governing principle

Each stage owns a defined set of fields on the Content Calendar row. A stage is complete when its fields are populated, not when it feels finished. The exit gate of every stage is therefore checkable rather than judged, and each stage consumes the artefact the previous stage produced.

Nothing is lost by a piece dying. A piece may be killed at any stage, and the research already banked stays on the row.

## Shape

```
Act 0 – Capture           outside Notion, three rails
   |
   v  the sweep
Act 1 – Ideation          Status: Idea
   |
   v  the commitment gate
Act 2 – Pre-Production    Status: Research -> Planned
   |
   v  the green light
Act 3 – Production        Status: Recording -> Editing
   |
   v  the lock
Act 4 – Post-Production   Status: Scheduled -> Published -> Reviewed
   |
   v  feeds the Storytelling Format Bank, which feeds the next Act 2
```

The `Phase` property on the Content Calendar derives the act from Status by formula. It is never edited by hand. Group a board by `Phase` for the four-act view and by `Status` for the working queue.

---

## Act 0 – Capture

Capture lives outside Notion by design. A capture stage inside Notion reproduces the friction that makes capture fail.

### The three rails

| Rail | When | Rule |
|---|---|---|
| Voice memo | Fastest. Phone in hand, thought in motion, no interface | Speak the thought and the reason it matters. Stop. Do not compose |
| Apple Notes | The thought needs a few lines to hold its shape, without reasoning it out | Capture folder only. One thought per note. Title is the thought |
| Pen and paper | No device, no power, no signal. Journal, field notepad, napkin | Date the page. Nothing else is required |

### Standing rules

- Capture never edits, never organises and never judges. Those are Act 1 and Act 2 jobs.
- One thought per capture. Two thoughts is two captures.
- A capture is not in the system until the sweep lands it. The rails are a holding pen, not a home.

### The sweep

Runs on command. Voice memos are transcribed and Apple Notes read from the Capture folder; each becomes an Idea row on the Content Calendar with the raw capture preserved in the page body. Paper is swept by photographing the page into the Capture folder. Swept captures are marked so nothing lands twice.

---

## Act 1 – Ideation

**Status:** Idea
**Purpose:** A standing pool of options, not a stage of work.

Ideas sit here indefinitely. Most should die here, and dying here is the cheapest possible outcome. Nothing is scheduled, researched or promised while a piece is in the pool.

**Work:** None. Periodic culling only.

**Exit gate – the commitment gate.** A piece leaves the pool only when the hook, the pillar and the value can be stated in one sitting, without research. If they cannot, the idea is not ready or is not good. It stays in the pool or it is deleted.

**Fields owed at exit:** Hook, Pillars, Value, Sphere.

**Artefact handed forward:** A stated promise to an audience.

---

## Act 2 – Pre-Production

**Status:** Research, then Planned
**Purpose:** Turn a promise into a plan that can be executed without further thinking.

### Research

The anti-library pass. Establish what already exists on this ground, what the strongest existing version does and where the unsaid thing sits. Select the storytelling shell from the Format Bank rather than inventing structure from scratch.

**Fields owed:** Topics, Emotion Invoked, Format, Guests where relevant.

**Artefact handed forward:** A reference set and a chosen format shell.

### Planned

Build the piece on paper. Outline or shot list written into the page body. Next actions broken to pomodoro size in Tasks, per the standing GTD rule.

**Fields owed:** Type, Platform, Playlist, Scenes, Shoot Date, Publish Date, Tasks.

**Artefact handed forward:** A shot list or outline, and a booked shoot date.

**Exit gate – the green light.** Three conditions, all binary: the format shell is chosen, the outline is written, the shoot date is booked. No camera is picked up without all three.

---

## Act 3 – Production

**Status:** Recording, then Editing
**Purpose:** Execute the plan. No new decisions of substance are made in this act. Anything requiring a fresh decision is a signal that Act 2 was left incomplete.

### Recording

Capture to the shot list. Shoot dates are batched across the slate rather than run one piece at a time.

**Fields owed:** Media, Shoot Date confirmed as actual rather than intended.

**Artefact handed forward:** The rushes.

### Editing

Assemble to the format shell. The hook stated at the commitment gate is the thing the opening must deliver; if the edit will not carry it, the hook is rewritten on the row rather than quietly abandoned.

**Fields owed:** Caption.

**Artefact handed forward:** An exported master.

**Exit gate – the lock.** An exported master exists and the caption carries the hook.

---

## Act 4 – Post-Production

**Status:** Scheduled, then Published, then Reviewed
**Purpose:** Deliver the piece and learn from it. The act is not finished at publication.

### Scheduled

Queued through Pennyone for syndication, Substack for Epiphany, the audio host for the Conversation.

**Pre-check, mandatory:** scan the Hook field across the last 14 days for a duplicate hook before anything is queued.

**Fields owed:** Publish Date confirmed, Pennyone Log.

### Published

Live.

**Fields owed:** Link.

### Reviewed

The closing bookend, and the reason the pipeline compounds. Metrics are reconciled and a verdict written into the page body: did the hook earn the second second, did the format shell perform, what would be done differently.

**Fields owed:** Views, Saves, Shares, Comments, Follows, and the written verdict.

**Exit gate:** Metrics reconciled and verdict written. A piece is finished only here.

**Artefact handed forward:** Performance accrues to the chosen shell in the Storytelling Format Bank, which is what the next Act 2 Research pass reads. Strong pieces spawn children through the Repurposed Content relation.

---

## Decision points

| Point | Question | Default |
|---|---|---|
| Commitment gate | Can the hook, pillar and value be stated without research? | No, so it stays in the pool |
| Green light | Are shell, outline and shoot date all present? | No, so it returns to Planned |
| Lock | Does the caption carry the stated hook? | Rewrite the caption, not the hook |
| Scheduling | Has this hook run inside 14 days? | Hold and re-hook |
| Review | Did the shell perform against its bank average? | Record the verdict either way |

## Escalation

- A piece stalled in one status for more than 30 days is surfaced for a kill-or-commit ruling.
- A shoot date passing without recording moves the piece back to Planned rather than leaving it in Recording.
- A published piece unreviewed after 30 days is surfaced at the review cadence.

## Success criteria

- No capture older than one week sits unswept on any rail.
- No piece in Production carries an unanswered structural question.
- Every published piece reaches Reviewed.
- The Format Bank accrues performance data on every shell used.
