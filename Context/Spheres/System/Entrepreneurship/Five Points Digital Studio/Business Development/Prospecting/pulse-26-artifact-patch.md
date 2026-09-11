# Pulse 26 artifact patch — apply in a writable session

**Why this file exists:** the live `five-points-prospect-pipeline` artifact
(`~/Documents/Claude/Artifacts/five-points-prospect-pipeline/index.html`) is read-only
in the automated pulse session, is outside every shell mount, and its 100-record `SEED`
array is a single line of ~28,181 tokens that exceeds the file reader's 25k cap — so the
pulse cannot assemble the full HTML that `update_artifact` requires with SEED verbatim.
This has now blocked twelve consecutive pulses. The patch below changes ONLY the two
machine-editable pulse regions; SEED and all user-editable logic are untouched.

Supersedes `pulse-18-artifact-patch.md`. Apply once, in a session where the artifact file
is writable, then call `mcp__cowork__update_artifact` (id: `five-points-prospect-pipeline`).

---

## 1. Banner — replace the PULSE-BANNER inner `<div>` (lines ~121–123)

Replace the existing banner `<div class="banner" …>…</div>` body with:

```html
  <div class="banner" style="background:#fdf6e7;border:1px solid #e3cf9a;color:#6b5416;margin-bottom:14px">
    <b>Pulse 26 — Thu 30 Jul 2026:</b> Conversion momentum, no date pinned yet. <b>Beatrice Sibblies</b> replied 29 Jul &ndash; she will be in Baltimore &ldquo;within the month, will confirm,&rdquo; Marty is up there in ~2 weeks; in-person meet warming, needs a locked date. <b>Kirsten Tucker</b> (net-new responder #10) is actively scheduling a Baltimore in-person &ndash; ball in Marty&rsquo;s court to name a week. <b>Danial Qureshi</b> (best cold prospect) still unanswered, 17 days &ndash; any reply must lead with the gap. Six standing leads still awaiting a call ask. Stage A: 0 of 19 dental invites accepted (Day 29) &ndash; withdrawal recommended. No new batch staged &ndash; hold until a meet is booked. 25 pulses, 10 responders, 0 appointments.
  </div>
```

## 2. PULSE_VERSION — in the PULSE-SYNC block (script)

```js
const PULSE_VERSION = '2026-07-30-pulse-26';
```

## 3. PULSE_UPDATES — merge/add these entries

```js
// warmthMin only raises warmth; stage/apptReady/lastContacted/nextAction/nextActionDate as noted
{ name: 'Beatrice Sibblies', stage: 'Appointment-ready', apptReady: true, lastContacted: '2026-07-29',
  nextAction: 'She replied 29 Jul — in Baltimore within the month, will confirm dates. When she confirms, propose a specific day and lock the in-person.',
  nextActionDate: '2026-08-01',
  addNote: 'Pulse 26: two-sided scheduling — first mutual in-person exchange. Meet warming around Marty’s trip; no date yet.' },

{ name: 'Kirsten Tucker', stage: 'Appointment-ready', apptReady: true, lastContacted: '2026-07-28',
  nextAction: 'Name a specific Baltimore week and lock the in-person. She is actively scheduling (a few trips coming up).',
  nextActionDate: '2026-08-01',
  addNote: 'Pulse 25/26: net-new responder #10. Warm-network founder (ItinAFairy, AI travel pilot); in-person hook working.' },

{ name: 'Danial Qureshi', stage: 'Replied', apptReady: false, lastContacted: '2026-07-13',
  nextAction: 'Answer, own the 17-day gap, affirm the utilization/friction/win-win framing, propose two specific times.',
  nextActionDate: '2026-07-31',
  addNote: 'Pulse 26: 17 days unanswered. Best-quality true-net-new cold prospect; free re-open closed at Pulse 20.' },

// Net-new DNA-fit connection pending vetting — NOT yet a lead; add only if the CRM tracks connections
{ name: 'Andrew McCann', stage: 'Connection — vet', apptReady: false, lastContacted: '',
  nextAction: 'Vet as Stage-B candidate; screen for the Jack Linderman vendor/agency failure mode (CEO of a RE agency — could be selling).',
  addNote: 'Pulse 24: CEO, Jellis Craig (real estate). Connected 26 Jul. First net-new DNA-fit connection since Jack Linderman.' }
```

## Notes / caveats carried forward
- Round-2 additions **Michael Woods** and **Nicole DeAngelo** are not in SEED-100 and will no-op until the CRM migrates; Danial came from the seed pass and is likely in SEED.
- No `SENT` array change this pulse — nothing was sent (automated run, no greenlight). The still-unrecorded Batch-2 send (`SENT_JUL06`, 37 names, 6 Jul) from `pulse-18-artifact-patch.md` still needs applying if the artifact is to reflect that wave.
- **Durable fix (do this instead of re-patching):** reflow `SEED` to one-object-per-line, or externalise it to a fetched JSON, or execute `pipeline-dashboard-build-brief.md` so Notion becomes system of record with a regenerator. Any of these ends the twelve-pulse block permanently.
