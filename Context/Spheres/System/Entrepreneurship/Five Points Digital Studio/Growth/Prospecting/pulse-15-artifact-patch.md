# Pulse 15 — artifact patch (apply in a writable session)

The `five-points-prospect-pipeline` artifact could not be resynced automatically for the **eighth** consecutive pulse. Blocker re-verified from both ends this run: (1) the Read tool *can* reach the source at `~/Documents/Claude/Artifacts/five-points-prospect-pipeline/index.html` (banner confirmed on-disk still "Pulse 6 — Sun 5 Jul 2026", lines 120–124; `PULSE_VERSION = '2026-07-05-pulse-6'`, line 254); (2) an in-place `Edit` on the source is hard-refused — "read-only in this session… Write a modified copy under the outputs directory instead"; (3) bash cannot reach the file (outside the shell mount — `ls` returns no-such-file); (4) `SEED` remains a single line (line 203) over the reader's 25,000-token cap, so a faithful full-file rebuild — which `update_artifact` requires with SEED verbatim — cannot be assembled, and regenerating SEED from the xlsx would mint fresh ids and orphan the localStorage-keyed manual edits (destructive; not taken autonomously without Marty's greenlight). `updatedAt` still Jul 7.

Material CRM state barely moved since Pulse 14: **zero** net-new business responders, no new Stage-A accepts, same seven standing leads. Apply the three regions below in the next writable session (or after the Notion migration).

Carry-forward caveat: **Michael Woods** and **Nicole DeAngelo** are round-2 additions NOT in SEED and will no-op until the CRM migrates. **Danial Qureshi** came from the seed pass (staged-12) so is likely in SEED and should apply — unverifiable while SEED cannot be read.

---

## 1. Banner (replace between PULSE-BANNER-START / PULSE-BANNER-END)

```html
  <!-- PULSE-BANNER-START (rewritten by each scheduled pulse) -->
  <div class="banner" style="background:#fdf6e7;border:1px solid #e3cf9a;color:#6b5416;margin-bottom:14px">
    <b>Pulse 15 &mdash; Tue 14 Jul 2026:</b> No net-new business replies since yesterday. Morgan Mulherin answered warm-personal (not a lead); <b>Danial Qureshi</b> (Sr Value Advisor @ SAP, Enterprise AI Value Realization) remains the freshest business thread, still unanswered &mdash; <b>answer and bridge to a call</b> (his &ldquo;utilization, upskilling, friction, win-wins&rdquo; language is the studio&rsquo;s wedge). Still <b>7 appointment-ready leads, zero calls booked</b> &mdash; the leak is the call-ask. <b>Beatrice Sibblies&rsquo; window has been open since 6 Jul (8 days), still unpinned.</b> Stage A: 0 of 19 dental invites accepted (Day 13) &mdash; disproven; new connection Jack Linderman (Founder/CEO, PARAGON, Jul 13) is not dental. Batch 2 largely unworked; nothing sent (no greenlight).
  </div>
  <!-- PULSE-BANNER-END -->
```

## 2. PULSE_VERSION (line ~254)

```js
const PULSE_VERSION = '2026-07-14-pulse-15';
```

## 3. Batch-2 SENT array (insert after SENT_JUN30, before PULSE_UPDATES)

Applied the same way as SENT_JUN30 in `applyPulse` (add a `SENT_JUL06.forEach(...)` loop mirroring the SENT_JUN30 loop, dated `2026-07-06`). These are the 37 Batch-2 recipients messaged Jul 6.

```js
const SENT_JUL06 = ["Gilad Uziely","Clyde Higgs","Michael Woods","Brooke Wright","Robert L. Morgan Jr.","Crystal Ugbesia","Gregg Lynn","Morgan Barisich","Nicole DeAngelo","Meredith Bowen","Jazzauria Williams","Darren Anglin","Shanice Stewart","Carlton Heard","Kera Felton","Arianit Gruda","Clinton Ages","Carly Hunter","Saureh Askarian","Moriah Jackson","Drew Dixon","Morgan Palmer","Chance Obialo","Emma Ridley","LaDarius Owens","Christopher Wyatt","Yooni Lee","Michelle Igori","Brittney Cunningham","Tammie Mooreland Cade","Quintunya Chapman-Hamilton","Danial Qureshi","Adam Powers","Matthew Hurwitz","Stacey Joseph","Krystal Gongora","Rashaida Melvin"];
```

## 4. PULSE_UPDATES (replace the array contents) — current ground truth

No net-new responder this pulse. Danial Qureshi's next action remains "answer + bridge to a call" (unworked since Pulse 14). Morgan Mulherin reclassified as a warm-personal null. The seven standing appointment-ready leads and prior null reclassifications are retained; warmth-only entries persist via the once-per-version guard.

```js
const PULSE_UPDATES = [
  {name:'Danial Qureshi', stage:'Replied', apptReady:false, lastContacted:'2026-07-13', nextAction:'Answer him — affirm the win-win/friction framing and propose a short call on where AI value actually lands in the P&L', nextActionDate:'2026-07-14', addNote:'[Pulse 14–15] Net-new responder #9. Sr Value Advisor @ SAP (Enterprise AI Value Realization). Substantive cold-prospect reply — "tools don''t fall short, it is utilization and upskilling; streamline processes, reduce friction and cost, win-wins across functional areas." No question back yet, but the highest-value new thread in weeks; his language is the studio''s wedge. Still unanswered as of Pulse 15.'},
  {name:'Nicole DeAngelo', stage:'In conversation', apptReady:true, lastContacted:'2026-07-10', nextAction:'Answer her "are you working with agents?" and bridge to a call before it cools to friendship', nextActionDate:'2026-07-14', addNote:'[Pulse 10–15] Cleanest buying signal in the set; drifted social Jul 10. Behaving as a warm personal contact — bridge to a Five Points call.'},
  {name:'Michael Woods', stage:'In conversation', apptReady:true, lastContacted:'2026-07-07', nextAction:'STOP the tooling volley — propose a call on his ideation→upkeep scaffolding gap', nextActionDate:'2026-07-14', addNote:'[Pulse 7–15] Atlanta founder, AI-active; named an ideation→upkeep/orchestration gap (the wedge). Bridge to the call.'},
  {name:'Shar Caesar Douglas', stage:'In conversation', apptReady:true, lastContacted:'2026-07-07', nextAction:'Bridge to a call rather than another tooling volley', nextActionDate:'2026-07-14', addNote:'[Pulse 6–15] Founder-level, AI-active, leaner-team systems mindset. Ball in her court since Marty''s Jul 7 follow-up; no call ask yet.'},
  {name:'Rob Coven', stage:'In conversation', apptReady:true, lastContacted:'2026-07-07', nextAction:'Propose a short call — he invited the exchange', nextActionDate:'2026-07-14', addNote:'[Pulse 2–15] Manages 200+ assets with AI; "open to a brief exchange". Still no call proposed 13 days on.'},
  {name:'Christiana Brown', stage:'In conversation', apptReady:true, lastContacted:'2026-07-07', nextAction:'Bridge to a call — thread slid into persona shop-talk', nextActionDate:'2026-07-14', addNote:'[Pulse 2–15] Built an AI voice coach; asked a question back. Drifted into Alfred/persona talk with no call bridge.'},
  {name:'Michael Bland', stage:'In conversation', apptReady:true, lastContacted:'2026-07-03', nextAction:'Steer from AI shop-talk to a call on automating his eXp real-estate book', nextActionDate:'2026-07-14', addNote:'[Pulse 3–15] Named gap: no automation on the real estate side yet. Thread stalled on tooling since Jul 3.'},
  {name:'Beatrice Sibblies', stage:'In conversation', apptReady:true, warmthMin:'Warm', lastContacted:'2026-07-02', nextAction:'MOST TIME-SENSITIVE — holiday window open since Jul 6 (8 days); send two concrete slots today', nextActionDate:'2026-07-14', addNote:'[Pulse 3–15] She proposed the catch-up herself. Window open since Jul 6, still unpinned after 8 days.'},
  {name:'Elizma Burger', stage:'In conversation', apptReady:true, lastContacted:'2026-07-08', nextAction:'Confirm the Leo call is booked — thread resolved out of unread since Pulse 10', nextActionDate:'2026-07-14', addNote:'[Held→resolving] Out of the unread queue since Jul 8/9 after nine pulses cooling. Confirm the call landed.'},
  {name:'Morgan Mulherin', apptReady:false, addNote:'[Pulse 12–15] SVP, National Property Practice. Warm-personal reconnection (world travel, "so excited to be home!"). No AI answer, no business trigger. Not a prospect — bank the relationship.'},
  {name:'Tammie Mooreland Cade', apptReady:false, addNote:'[Pulse 8] Personal contact who rumbled the mass-message good-naturedly. Not a prospect.'},
  {name:'Brittney Cunningham', apptReady:false, addNote:'[Pulse 9] Personal/known contact mass-messaged in error; Marty retracted the touch. Not a prospect.'},
  {name:'Jazzauria Williams', apptReady:false, addNote:'[Pulse 10] Warm-personal reconnection, no AI answer, no business trigger. Not a prospect — bank the relationship.'},
];
```

---

*Durable fix (removes this blocker permanently): reflow SEED to one-object-per-line or externalise it to a fetched JSON the pulse can regenerate, OR execute `pipeline-dashboard-build-brief.md` (Notion becomes system-of-record; a regenerator re-emits the artifact). Either requires a context where the artifact file is writable. Note for the operator: regenerating SEED from the xlsx is possible but would mint fresh record ids and orphan the localStorage manual edits — do this deliberately, not as a side effect.*
