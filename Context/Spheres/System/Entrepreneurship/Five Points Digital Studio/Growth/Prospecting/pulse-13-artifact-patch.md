# Pulse 13 — artifact patch (apply in a writable session)

The `five-points-prospect-pipeline` artifact could not be resynced automatically for the sixth consecutive pulse: its source (`~/Documents/Claude/Artifacts/five-points-prospect-pipeline/index.html`) is read-only in-session and sits outside the shell mount, and its `SEED` array is a single 28k-token line that exceeds the file reader's cap, so `update_artifact` (which needs the full file, SEED verbatim) cannot be assembled. Everything except SEED is readable.

When next in a session where that file is writable (or after the durable Notion migration lands), apply the three pulse regions below. They replace only the marked pulse blocks — do NOT touch SEED or user-editable logic. `localStorage` manual edits survive because `applyPulse` runs once per `PULSE_VERSION`.

Caveat: **Michael Woods** and **Nicole DeAngelo** are round-2 additions NOT present in SEED, so their `PULSE_UPDATES` entries will `console.warn`/no-op until the CRM migrates off SEED. Left in below so they apply automatically once SEED includes them.

---

## 1. Banner (replace between PULSE-BANNER-START / PULSE-BANNER-END)

```html
  <!-- PULSE-BANNER-START (rewritten by each scheduled pulse) -->
  <div class="banner" style="background:#fdf6e7;border:1px solid #e3cf9a;color:#6b5416;margin-bottom:14px">
    <b>Pulse 13 &mdash; Sun 12 Jul 2026:</b> No net-new business replies since yesterday. <b>7 appointment-ready leads still standing, zero calls booked</b> &mdash; the leak is the call-ask, not targeting. <b>Beatrice Sibblies&rsquo; &ldquo;after the holidays&rdquo; window has been open since 6 Jul (6 days) and is still unpinned &mdash; most time-sensitive action.</b> Nicole DeAngelo drifted social; Michael Woods &amp; Shar Caesar Douglas stuck in tooling volleys; Rob Coven, Christiana Brown &amp; Michael Bland still awaiting a call ask. Stage A: 0 of 19 dental invites accepted (Day 11) &mdash; disproven, pivot to Atlanta/RE/AI-active pending. Batch 2 largely unworked; nothing sent (no greenlight).
  </div>
  <!-- PULSE-BANNER-END -->
```

## 2. PULSE_VERSION (line ~254)

```js
const PULSE_VERSION = '2026-07-12-pulse-13';
```

## 3. Add Batch-2 SENT array (insert after SENT_JUN30, before PULSE_UPDATES)

Applied the same way as SENT_JUN30 in `applyPulse` (add a second `SENT_JUL06.forEach(...)` loop mirroring the SENT_JUN30 loop, dated `2026-07-06`). These are the 37 Batch-2 recipients messaged Jul 6.

```js
const SENT_JUL06 = ["Gilad Uziely","Clyde Higgs","Michael Woods","Brooke Wright","Robert L. Morgan Jr.","Crystal Ugbesia","Gregg Lynn","Morgan Barisich","Nicole DeAngelo","Meredith Bowen","Jazzauria Williams","Darren Anglin","Shanice Stewart","Carlton Heard","Kera Felton","Arianit Gruda","Clinton Ages","Carly Hunter","Saureh Askarian","Moriah Jackson","Drew Dixon","Morgan Palmer","Chance Obialo","Emma Ridley","LaDarius Owens","Christopher Wyatt","Yooni Lee","Michelle Igori","Brittney Cunningham","Tammie Mooreland Cade","Quintunya Chapman-Hamilton","Danial Qureshi","Adam Powers","Matthew Hurwitz","Stacey Joseph","Krystal Gongora","Rashaida Melvin"];
```

## 4. PULSE_UPDATES (replace the array contents) — current ground truth

The seven standing appointment-ready leads plus null/personal reclassifications. Warmth-only entries from the Jun-30 patch are retained by the once-per-version guard and need not be repeated.

```js
const PULSE_UPDATES = [
  {name:'Nicole DeAngelo', stage:'In conversation', apptReady:true, lastContacted:'2026-07-10', nextAction:'Answer her "are you working with agents?" and bridge to a call before it cools to friendship', nextActionDate:'2026-07-12', addNote:'[Pulse 10–13] Cleanest buying signal in the set ("are you working with agents?"); drifted social Jul 10. Behaving as a warm personal contact — bridge to a Five Points call.'},
  {name:'Michael Woods', stage:'In conversation', apptReady:true, lastContacted:'2026-07-07', nextAction:'STOP the tooling volley — propose a call on his ideation→upkeep scaffolding gap', nextActionDate:'2026-07-12', addNote:'[Pulse 7–13] Atlanta founder, AI-active; named an ideation→upkeep/orchestration gap (the wedge). Four+ exchanges deep on tooling — bridge to the call.'},
  {name:'Shar Caesar Douglas', stage:'In conversation', apptReady:true, lastContacted:'2026-07-07', nextAction:'Bridge to a call rather than another tooling volley', nextActionDate:'2026-07-12', addNote:'[Pulse 6–13] Founder-level, AI-active, leaner-team systems mindset. Ball in her court since Marty''s Jul 7 follow-up; no call ask yet.'},
  {name:'Rob Coven', stage:'In conversation', apptReady:true, lastContacted:'2026-07-07', nextAction:'Propose a short call — he invited the exchange', nextActionDate:'2026-07-12', addNote:'[Pulse 2–13] Manages 200+ assets with AI; "open to a brief exchange". Still no call proposed 11 days on.'},
  {name:'Christiana Brown', stage:'In conversation', apptReady:true, lastContacted:'2026-07-07', nextAction:'Bridge to a call — thread slid into persona shop-talk', nextActionDate:'2026-07-12', addNote:'[Pulse 2–13] Built an AI voice coach; asked a question back. Drifted into Alfred/persona talk with no call bridge.'},
  {name:'Michael Bland', stage:'In conversation', apptReady:true, lastContacted:'2026-07-03', nextAction:'Steer from AI shop-talk to a call on automating his eXp real-estate book', nextActionDate:'2026-07-12', addNote:'[Pulse 3–13] Named gap: no automation on the real estate side yet. Thread stalled on tooling since Jul 3.'},
  {name:'Beatrice Sibblies', stage:'In conversation', apptReady:true, warmthMin:'Warm', lastContacted:'2026-07-02', nextAction:'MOST TIME-SENSITIVE — holiday window open since Jul 6; send two concrete slots today', nextActionDate:'2026-07-12', addNote:'[Pulse 3–13] She proposed the catch-up herself. Window open since Jul 6 (6 days), still unpinned.'},
  {name:'Elizma Burger', stage:'In conversation', apptReady:true, lastContacted:'2026-07-08', nextAction:'Confirm the Leo call is booked — thread resolved out of unread since Pulse 10', nextActionDate:'2026-07-12', addNote:'[Held→resolving] Out of the unread queue since Jul 8/9 after nine pulses cooling. Confirm the call landed.'},
  {name:'Tammie Mooreland Cade', apptReady:false, addNote:'[Pulse 8] Personal contact ("mama"/"son") who rumbled the mass-message good-naturedly. Not a prospect — exclude from prospect treatment.'},
  {name:'Brittney Cunningham', apptReady:false, addNote:'[Pulse 9] Personal/known contact mass-messaged in error; Marty retracted the touch. Not a prospect.'},
  {name:'Jazzauria Williams', apptReady:false, addNote:'[Pulse 10] Warm-personal reconnection, no AI answer, no business trigger. Not a prospect — bank the relationship.'},
];
```

---

*Durable fix (removes this blocker permanently): reflow SEED to one-object-per-line or externalise it to a fetched JSON the pulse can regenerate, OR execute `pipeline-dashboard-build-brief.md` (Notion becomes system-of-record; a regenerator re-emits the artifact). Either requires a context where the artifact file is writable.*
