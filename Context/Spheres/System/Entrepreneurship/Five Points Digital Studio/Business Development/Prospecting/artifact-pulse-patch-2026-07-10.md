# Artifact pulse patch — Pulse 11 (2026-07-10)

The `five-points-prospect-pipeline` artifact is on-disk at Pulse 6 and cannot be
synced by the automated pulse (source is read-only in-session; the 28,181-token
single-line `SEED` array exceeds the reader cap, so `update_artifact` cannot be
handed a faithful full-file rebuild). Apply the three replacements below in a
session where `~/Documents/Claude/Artifacts/five-points-prospect-pipeline/index.html`
is writable — OR do the durable refactor first (reflow `SEED` to one object per
line / externalise to JSON), which unblocks every future pulse.

Nothing changed in the outreach since Pulse 6 except thread state and the
Stage-A verdict, so only the pulse regions need updating. Do NOT touch `SEED`.

---

## 1) Banner — replace the `<div class="banner" ...>...</div>` between the PULSE-BANNER markers (lines ~121–123)

```html
  <div class="banner" style="background:#fdf6e7;border:1px solid #e3cf9a;color:#6b5416;margin-bottom:14px">
    <b>Pulse 11 &ndash; Fri 10 Jul 2026:</b> No new replies overnight. <b>7 appointment-ready leads, still 0 calls booked</b> &ndash; the bottleneck is the call-ask, not targeting. Freshest: <b>Nicole DeAngelo</b> asked &ldquo;are you working with agents?&rdquo; &ndash; answer it and bridge to a call. <b>Beatrice Sibblies&rsquo;</b> holiday window has been open since 6 Jul &ndash; pin two slots today (most time-sensitive). Michael Woods &amp; Shar: stop the tooling volley, propose a time. Rob Coven, Christiana Brown &amp; Michael Bland still awaiting a call ask. Elizma Burger&rsquo;s Leo thread appears resolved. Stage A: 0 of 19 dental invites &ndash; disproven; pivot to Atlanta/RE/AI-active. Batch 2 (37 sent) still largely unworked; nothing staged &ndash; hold.
  </div>
```

## 2) Version — replace line ~254

```js
const PULSE_VERSION = '2026-07-10-pulse-11';
```

## 3) PULSE_UPDATES — replace the whole `const PULSE_UPDATES = [ ... ];` block (lines ~256–281)

(Refreshes the six in-SEED appointment-ready / resolved leads to Pulse 11 state
and carries the rest forward unchanged. Michael Woods and Nicole DeAngelo are
round-2 lookalikes and are NOT in the top-100 SEED, so they cannot render as rows
— they are tracked in the banner and the run log only until SEED is extended.)

```js
const PULSE_UPDATES = [
  {name:'Shar Caesar Douglas', stage:'In conversation', apptReady:true, lastContacted:'2026-07-07', nextAction:'Stop the tooling volley — propose a specific call time', nextActionDate:'2026-07-10', addNote:'[Pulse 11 · Jul 10] Ball in her court after Marty’s Jul 7 Substack "Epiphany" follow-up. Appointment-ready, still no call ask.'},
  {name:'Rob Coven', stage:'In conversation', apptReady:true, lastContacted:'2026-07-07', nextAction:'Propose a short call — he invited the exchange', nextActionDate:'2026-07-10', addNote:'[Pulse 11 · Jul 10] Ball in his court after Marty’s Jul 7 "coveted conversations" note. Appointment-ready ~9 days, still no call ask.'},
  {name:'Christiana Brown', stage:'In conversation', apptReady:true, lastContacted:'2026-07-07', nextAction:'Bridge to a call — thread drifted into persona shop-talk', nextActionDate:'2026-07-10', addNote:'[Pulse 11 · Jul 10] Jul 7: "I’ll have to check out making my own persona on Claude." Ball in her court. Appointment-ready, no call ask.'},
  {name:'Michael Bland', stage:'In conversation', apptReady:true, lastContacted:'2026-07-03', nextAction:'Stop the tooling volley — bridge to a call on automating his eXp book', nextActionDate:'2026-07-10', addNote:'[Pulse 11 · Jul 10] Four+ exchanges deep on tooling; named gap (automate the real estate book) untouched. Appointment-ready, no call ask.'},
  {name:'Beatrice Sibblies', stage:'In conversation', apptReady:true, warmthMin:'Warm', lastContacted:'2026-07-02', nextAction:'MOST TIME-SENSITIVE — pin two concrete slots today; window open since Jul 6', nextActionDate:'2026-07-10', addNote:'[Pulse 11 · Jul 10] She proposed the catch-up herself; "after the holidays" window open since Jul 6 and still unpinned.'},
  {name:'Elizma Burger', stage:'In conversation', lastContacted:'2026-07-08', nextAction:'Confirm the Leo call is booked', nextActionDate:'2026-07-10', addNote:'[Pulse 11 · Jul 10] RESOLVED out of the unread queue on/around Jul 8 after nine pulses cold — Marty engaged. Confirm the call is on the calendar.'},
  {name:'Dan Mall', stage:'In conversation', lastContacted:'2026-06-30', nextAction:'Ball in his court — light nudge if quiet', addNote:'[Pulse 1] Guarded curiosity, engaged after the design-systems re-hook. Warmest non-appointment thread.'},
  {name:'Chris Cornell', stage:'Replied', warmthMin:'Warm', lastContacted:'2026-07-01', nextAction:'Low signal — hold', addNote:'[Pulse 2] Replied "I agree" only; AI question re-asked Jul 1.'},
  {name:'Doug Gollan', stage:'Nurture', lastContacted:'2026-07-01', nextAction:'Revisit in a quarter', addNote:'[Pulse 1] Polite decline — AI use "proprietary". Warm reaction to the gracious close; relationship banked.'},
  {name:'Morgan Bright', stage:'Lost', lastContacted:'2026-06-30', addNote:'[Pulse 1] Declined — no AI in the practice; IC, not the decision-maker.'},
  {name:'Mordecai Brownlee', stage:'Touch 1 sent', lastContacted:'2026-06-30', addNote:'[Pulse 1] Auto out-of-office only — not a genuine reply.'},
  {name:'Taruna Kanani', addNote:'[Held] Do not auto-send — resolve the open meeting question (Juan vs her) first.'},
  {name:'Megan Carlo', addNote:'[Held] Job-application thread (MoMA role) — handle personally, no BD message.'},
  {name:'Aty Biswese', warmthMin:'Warm'},
  {name:'MaryAnne Gilmartin', warmthMin:'Warm'},
  {name:'Heather Gibbons', warmthMin:'Warm'},
  {name:'Richard Trinh', warmthMin:'Warm'},
  {name:'Kirsten Tucker', warmthMin:'Warm'},
  {name:'Beatrice Dixon', warmthMin:'Warm'},
  {name:'Ancel Briley', warmthMin:'Warm'},
  {name:'LaTrice Lyle', warmthMin:'Warm'},
  {name:'Callie Stanton', warmthMin:'Warm'},
  {name:'Ambre Reed', warmthMin:'Warm'},
  {name:'Donte Wilder', warmthMin:'Warm'},
];
```

`SENT_JUN30` is unchanged (no new sends this pulse — no greenlight). No new SENT
array needed until a batch is approved and sent.
