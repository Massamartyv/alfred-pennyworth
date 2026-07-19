# Pulse 18 — apply-ready artifact patch (five-points-prospect-pipeline)

**Why this file exists:** the artifact source at
`/Users/martyspicer/Documents/Claude/Artifacts/five-points-prospect-pipeline/index.html`
cannot be synced by the scheduled pulse. Re-verified Pulse 18 (Jul 18): the banner region reads cleanly on the host path and is still `Pulse 6 — Sun 5 Jul 2026` (lines 120–124), but the single-line `SEED` array (line 203, ~28k tokens) exceeds the reader cap, in-place `Edit` on the source is hard-refused as read-only, and the file sits outside every shell mount. `update_artifact` requires the complete HTML with SEED verbatim, which cannot be assembled. Regenerating SEED from the xlsx would mint fresh ids and orphan the localStorage-keyed manual edits — not done autonomously.

**Eleventh consecutive blocked pulse.** Stop retrying this from the automated run. Apply the regions below in a writable/live session, or execute the durable fix: reflow SEED to one-object-per-line, externalize it to a fetched JSON, or run `pipeline-dashboard-build-brief.md` (Notion becomes system of record + a regenerator re-emits the artifact).

---

## 1. Banner (replace between PULSE-BANNER-START / END, lines ~121–123)

```html
    <b>Pulse 18 — Sat 18 Jul 2026:</b> No net-new replies since Jul 14 &mdash; four days of inbox silence. <b>Danial Qureshi</b> (Sr Value Advisor, SAP) remains the best open prospect and his Jul 13 reply is now <b>five days unanswered</b>; answer and bridge to a call. Seven appointment-ready leads and <b>still zero calls booked</b> across eleven pulses &mdash; the leak is the call-ask, not the pipeline. <b>Beatrice Sibblies&rsquo;</b> window has been open since Jul 6 (12 days) and is still unpinned. Good news: the unread queue is now <b>fully clear</b> &mdash; Eunice Orsal, Sammy Smith and Mandi Ellefson all resolved. Stage A: 0 of 19 dental invites accepted at 17 days &mdash; disproven; withdraw them and re-source toward Atlanta / real estate / AI-active operators. Nothing staged or sent this pulse.
```

## 2. PULSE_VERSION (replace line ~254)

```js
const PULSE_VERSION = '2026-07-18-pulse-18';
```

## 3. Record the Batch-2 send (Jul 6) — unchanged from pulse-17 patch

Apply the `SENT_JUL06` array and its `applyPulse` loop exactly as written in `pulse-17-artifact-patch.md` §3. Batch 2 (37 messages, sent Jul 6) is still unrecorded in the artifact.

## 4. PULSE_UPDATES — apply the pulse-17 array with these four edits

Take the `PULSE_UPDATES` array from `pulse-17-artifact-patch.md` §4 verbatim, then change the following entries:

```js
  {name:'Danial Qureshi', stage:'Replied', apptReady:true, lastContacted:'2026-07-13', nextAction:'Answer, affirm the utilization/friction/win-win framing, propose a short call — 5 days unanswered', nextActionDate:'2026-07-18', addNote:'[Pulse 14 · Jul 13] Best-quality NET-NEW cold prospect. Substantive consultative reply: "tools don\'t fall short, it\'s utilization + upskilling… streamline processes, reduce friction and cost, win-wins across functional areas." His own language IS the studio wedge. [Pulse 18] Still UNANSWERED — five days. Decay risk now material.'},

  {name:'Beatrice Sibblies', stage:'In conversation', apptReady:true, warmthMin:'Warm', lastContacted:'2026-07-02', nextAction:'MOST TIME-SENSITIVE — window open since Jul 6; send two concrete slots today', nextActionDate:'2026-07-18', addNote:'[Pulse 3] She proposed the catch-up herself ("after the holidays"). Window open since Jul 6 — 12 days unpinned as of Pulse 18. Past the point where a warm re-open is free.'},

  {name:'Elizma Burger', stage:'In conversation', apptReady:true, lastContacted:'2026-07-08', nextAction:'Confirm the Leo call is booked', nextActionDate:'2026-07-18', addNote:'[Pulse 10] Resolved out of the unread queue ~Jul 8 after nine pulses cold. [Pulse 18] Unread queue now fully clear — confirm the Leo call actually landed on the calendar.'},

  {name:'Jack Linderman', stage:'Lost', lastContacted:'2026-07-14', addNote:'[Pulse 17] VETTED OUT — founder/CEO who fit the DNA on seniority but pitched Marty his own agency services; Marty declined. Screen agency/vendor founders out of future Stage-B vets. NOTE: not in SEED-100.'},
```

All other entries carry forward unchanged.

---

*Written Pulse 18 · 2026-07-18. Supersedes pulse-17-artifact-patch.md. Ground truth also captured in lookalike-engine.md run log.*
