# Pulse 14 — artifact patch (apply in a writable session)

The `five-points-prospect-pipeline` artifact could not be resynced automatically for the **seventh** consecutive pulse. Root cause re-verified this run: its source (`~/Documents/Claude/Artifacts/five-points-prospect-pipeline/index.html`) is read-only in-session and sits outside the shell mount, and its `SEED` array is a single line now measuring **28,470 tokens** (line 203), over the file reader's 25,000-token cap. Any Read window that touches line 203 fails, so `update_artifact` — which needs the complete file with SEED verbatim — cannot be assembled. Every other region (banner, PULSE_VERSION, SENT arrays, PULSE_UPDATES, applyPulse) reads and edits cleanly; SEED is the sole obstacle. On-disk banner confirmed still at "Pulse 6 — Sun 5 Jul 2026"; `updatedAt` Jul 7.

Material CRM state barely moved since Pulse 13: **one** net-new business responder (Danial Qureshi), no new Stage-A accepts, same standing leads. Apply the three regions below in the next writable session (or after the Notion migration).

Caveat: **Michael Woods** and **Nicole DeAngelo** are round-2 additions NOT in SEED and will no-op until the CRM migrates. **Danial Qureshi** came from the seed pass (staged-12) so is likely in SEED and should apply — unverifiable this run because SEED cannot be read.

---

## 1. Banner (replace between PULSE-BANNER-START / PULSE-BANNER-END)

```html
  <!-- PULSE-BANNER-START (rewritten by each scheduled pulse) -->
  <div class="banner" style="background:#fdf6e7;border:1px solid #e3cf9a;color:#6b5416;margin-bottom:14px">
    <b>Pulse 14 &mdash; Mon 13 Jul 2026:</b> One net-new reply since yesterday &mdash; <b>Danial Qureshi</b> (Sr Value Advisor @ SAP, Enterprise AI Value Realization) answered substantively: tools don&rsquo;t fall short, it is utilization and upskilling; streamline process, cut friction and cost, &ldquo;win-wins across functional areas.&rdquo; A genuine cold-prospect engagement, not personal network &mdash; <b>answer and bridge to a call</b> (his own language is the studio&rsquo;s wedge). Still <b>7 appointment-ready leads, zero calls booked</b> &mdash; the leak is the call-ask. <b>Beatrice Sibblies&rsquo; window has been open since 6 Jul (7 days), still unpinned.</b> Stage A: 0 of 19 dental invites accepted (Day 12) &mdash; disproven, Atlanta/RE/AI-active pivot pending. Batch 2 largely unworked; nothing sent (no greenlight).
  </div>
  <!-- PULSE-BANNER-END -->
```

## 2. PULSE_VERSION (line ~254)

```js
const PULSE_VERSION = '2026-07-13-pulse-14';
```

## 3. Batch-2 SENT array (insert after SENT_JUN30, before PULSE_UPDATES)

Applied the same way as SENT_JUN30 in `applyPulse` (add a `SENT_JUL06.forEach(...)` loop mirroring the SENT_JUN30 loop, dated `2026-07-06`). These are the 37 Batch-2 recipients messaged Jul 6.

```js
const SENT_JUL06 = ["Gilad Uziely","Clyde Higgs","Michael Woods","Brooke Wright","Robert L. Morgan Jr.","Crystal Ugbesia","Gregg Lynn","Morgan Barisich","Nicole DeAngelo","Meredith Bowen","Jazzauria Williams","Darren Anglin","Shanice Stewart","Carlton Heard","Kera Felton","Arianit Gruda","Clinton Ages","Carly Hunter","Saureh Askarian","Moriah Jackson","Drew Dixon","Morgan Palmer","Chance Obialo","Emma Ridley","LaDarius Owens","Christopher Wyatt","Yooni Lee","Michelle Igori","Brittney Cunningham","Tammie Mooreland Cade","Quintunya Chapman-Hamilton","Danial Qureshi","Adam Powers","Matthew Hurwitz","Stacey Joseph","Krystal Gongora","Rashaida Melvin"];
```

## 4. PULSE_UPDATES (replace the array contents) — current ground truth

New this pulse: Danial Qureshi (net-new engaged responder #9). The seven standing appointment-ready leads and null/personal reclassifications are retained. Warmth-only entries from the Jun-30 patch persist via the once-per-version guard.

```js
const PULSE_UPDATES = [
  {name:'Danial Qureshi', stage:'Replied', apptReady:false, lastContacted:'2026-07-13', nextAction:'Answer him — affirm the win-win/friction framing and propose a short call to compare notes on where AI value actually lands', nextActionDate:'2026-07-13', addNote:'[Pulse 14 · Jul 13] Net-new responder #9. Sr Value Advisor @ SAP (Enterprise AI Value Realization). Substantive reply — "tools don''t fall short, it is utilization and upskilling; streamline processes, reduce friction and cost, win-wins across functional areas." Genuine cold-prospect engagement (professional tone, not personal network). No question back yet, so not self-declared appointment-ready, but a high-value bridge candidate — his language is the studio''s wedge.'},
  {name:'Nicole DeAngelo', stage:'In conversation', apptReady:true, lastContacted:'2026-07-10', nextAction:'Answer her "are you working with agents?" and bridge to a call before it cools to friendship', nextActionDate:'2026-07-13', addNote:'[Pulse 10–14] Cleanest buying signal in the set; drifted social Jul 10. Behaving as a warm personal contact — bridge to a Five Points call.'},
  {name:'Michael Woods', stage:'In conversation', apptReady:true, lastContacted:'2026-07-07', nextAction:'STOP the tooling volley — propose a call on his ideation→upkeep scaffolding gap', nextActionDate:'2026-07-13', addNote:'[Pulse 7–14] Atlanta founder, AI-active; named an ideation→upkeep/orchestration gap (the wedge). Bridge to the call.'},
  {name:'Shar Caesar Douglas', stage:'In conversation', apptReady:true, lastContacted:'2026-07-07', nextAction:'Bridge to a call rather than another tooling volley', nextActionDate:'2026-07-13', addNote:'[Pulse 6–14] Founder-level, AI-active, leaner-team systems mindset. Ball in her court since Marty''s Jul 7 follow-up; no call ask yet.'},
  {name:'Rob Coven', stage:'In conversation', apptReady:true, lastContacted:'2026-07-07', nextAction:'Propose a short call — he invited the exchange', nextActionDate:'2026-07-13', addNote:'[Pulse 2–14] Manages 200+ assets with AI; "open to a brief exchange". Still no call proposed 12 days on.'},
  {name:'Christiana Brown', stage:'In conversation', apptReady:true, lastContacted:'2026-07-07', nextAction:'Bridge to a call — thread slid into persona shop-talk', nextActionDate:'2026-07-13', addNote:'[Pulse 2–14] Built an AI voice coach; asked a question back. Drifted into Alfred/persona talk with no call bridge.'},
  {name:'Michael Bland', stage:'In conversation', apptReady:true, lastContacted:'2026-07-03', nextAction:'Steer from AI shop-talk to a call on automating his eXp real-estate book', nextActionDate:'2026-07-13', addNote:'[Pulse 3–14] Named gap: no automation on the real estate side yet. Thread stalled on tooling since Jul 3.'},
  {name:'Beatrice Sibblies', stage:'In conversation', apptReady:true, warmthMin:'Warm', lastContacted:'2026-07-02', nextAction:'MOST TIME-SENSITIVE — holiday window open since Jul 6 (7 days); send two concrete slots today', nextActionDate:'2026-07-13', addNote:'[Pulse 3–14] She proposed the catch-up herself. Window open since Jul 6, still unpinned.'},
  {name:'Elizma Burger', stage:'In conversation', apptReady:true, lastContacted:'2026-07-08', nextAction:'Confirm the Leo call is booked — thread resolved out of unread since Pulse 10', nextActionDate:'2026-07-13', addNote:'[Held→resolving] Out of the unread queue since Jul 8/9 after nine pulses cooling. Confirm the call landed.'},
  {name:'Tammie Mooreland Cade', apptReady:false, addNote:'[Pulse 8] Personal contact who rumbled the mass-message good-naturedly. Not a prospect.'},
  {name:'Brittney Cunningham', apptReady:false, addNote:'[Pulse 9] Personal/known contact mass-messaged in error; Marty retracted the touch. Not a prospect.'},
  {name:'Jazzauria Williams', apptReady:false, addNote:'[Pulse 10] Warm-personal reconnection, no AI answer, no business trigger. Not a prospect — bank the relationship.'},
];
```

---

*Durable fix (removes this blocker permanently): reflow SEED to one-object-per-line or externalise it to a fetched JSON the pulse can regenerate, OR execute `pipeline-dashboard-build-brief.md` (Notion becomes system-of-record; a regenerator re-emits the artifact). Either requires a context where the artifact file is writable.*
