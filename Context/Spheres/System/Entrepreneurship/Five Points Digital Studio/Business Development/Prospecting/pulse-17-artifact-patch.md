# Pulse 17 — apply-ready artifact patch (five-points-prospect-pipeline)

**Why this file exists:** the artifact source at
`/Users/martyspicer/Documents/Claude/Artifacts/five-points-prospect-pipeline/index.html`
cannot be synced by the scheduled pulse. Re-verified Pulse 17 (Jul 16) from all three angles:
1. `Read` fails on the SEED array — line 203 is a single line of 28,181 tokens, over the 25k reader cap.
2. In-place `Edit` on the source is hard-refused — "read-only in this session… Write a modified copy under the outputs directory instead."
3. `bash` cannot reach the file — it is outside every shell mount (`ls` no-such-file).
`update_artifact` requires the complete HTML with SEED verbatim, which cannot be assembled. Regenerating SEED from the xlsx would mint fresh ids and orphan the localStorage-keyed manual edits (corrupts the live CRM) — not done autonomously.

**Apply this in the next writable / live session** (paste the three region changes below), or execute the durable fix: reflow SEED to one-object-per-line, or externalize it to a fetched JSON, or run `pipeline-dashboard-build-brief.md` (Notion becomes system of record + a regenerator re-emits the artifact).

---

## 1. Banner (replace between PULSE-BANNER-START / END, lines ~121–123)

```html
    <b>Pulse 17 — Thu 16 Jul 2026:</b> No net-new replies since Jul 14. <b>Danial Qureshi</b> (Sr Value Advisor, SAP) is the best open prospect &mdash; his Jul 13 reply is still <b>unanswered</b>; answer and bridge to a call. Seven appointment-ready leads (Danial, Nicole DeAngelo, Michael Woods, Shar Caesar Douglas, Rob Coven, Christiana Brown, Michael Bland) and <b>still zero calls booked</b> &mdash; the leak is the call-ask, not the pipeline. <b>Beatrice Sibblies&rsquo;</b> &ldquo;after the holidays&rdquo; window has been open since Jul 6 (10 days) and is still unpinned &mdash; send two slots today. Jack Linderman vetted out (he pitched us; declined). Stage A: 0 of 19 dental invites accepted &mdash; disproven; re-source toward Atlanta / real estate / AI-active operators. Nothing staged or sent this pulse.
```

## 2. PULSE_VERSION (replace line ~254)

```js
const PULSE_VERSION = '2026-07-16-pulse-17';
```

## 3. Record the Batch-2 send (Jul 6) — add after SENT_JUN30 (line ~255)

Batch 2 (37 messages) was sent Jul 6 but has never been recorded in the artifact (sync blocked since Pulse 8). Add a second sent array and a loop for it in `applyPulse`. NOTE: the 25 round-2 names are NOT in the original SEED-100 and will `console.warn` / no-op until the CRM migrates; the staged-12 seed-pass names should apply.

```js
const SENT_JUL06 = ["Gilad Uziely","Clyde Higgs","Michael Woods","Brooke Wright","Robert L. Morgan Jr.","Crystal Ugbesia","Gregg Lynn","Morgan Barisich","Nicole DeAngelo","Meredith Bowen","Jazzauria Williams","Darren Anglin","Shanice Stewart","Carlton Heard","Kera Felton","Arianit Gruda","Clinton Ages","Carly Hunter","Saureh Askarian","Moriah Jackson","Drew Dixon","Morgan Palmer","Chance Obialo","Emma Ridley","LaDarius Owens","Christopher Wyatt","Yooni Lee","Michelle Igori","Brittney Cunningham","Tammie Mooreland Cade","Quintunya Chapman-Hamilton","Danial Qureshi","Adam Powers","Matthew Hurwitz","Stacey Joseph","Krystal Gongora","Rashaida Melvin"];
```

In `applyPulse`, after the existing `SENT_JUN30.forEach(...)` block, add:

```js
    SENT_JUL06.forEach(n=>{
      const r = byName[n]; if(!r) return;
      const ov = o[r.id] = o[r.id] || {};
      const cur = ov.stage || 'Not contacted';
      if(cur === 'Not contacted'){ ov.stage='Touch 1 sent'; if(!ov.lastContacted) ov.lastContacted='2026-07-06'; }
    });
```

## 4. PULSE_UPDATES — refresh appointment-ready leads + add Danial + null-out personal contacts

Replace the `PULSE_UPDATES` array body (lines ~256–281) with the following. Round-2 additions (Nicole DeAngelo, Michael Woods) are included so they apply post-migration; they no-op against the current SEED-100.

```js
const PULSE_UPDATES = [
  {name:'Danial Qureshi', stage:'Replied', apptReady:true, lastContacted:'2026-07-13', nextAction:'Answer, affirm the utilization/friction/win-win framing, propose a short call', nextActionDate:'2026-07-16', addNote:'[Pulse 14 · Jul 13] Best-quality NET-NEW cold prospect. Substantive consultative reply: "tools don\'t fall short, it\'s utilization + upskilling… streamline processes, reduce friction and cost, win-wins across functional areas." His own language IS the studio wedge. Did not self-declare a call, but the cleanest bridge in the set. Still UNANSWERED as of Pulse 17.'},
  {name:'Nicole DeAngelo', stage:'In conversation', apptReady:true, lastContacted:'2026-07-10', nextAction:'Bridge to a call before the thread fully cools to friendship', nextActionDate:'2026-07-16', addNote:'[Pulse 10 · Jul 9] Substantive AI-usage answer + unprompted "Are you working with agents?" — cleanest buying signal in the set. [Pulse 12] Thread drifted social (NYC move); behaving as a personal friend, not a cold prospect. Ball in Marty\'s court. NOTE: not in SEED-100 — no-ops until migration.'},
  {name:'Michael Woods', stage:'In conversation', apptReady:true, lastContacted:'2026-07-07', nextAction:'STOP the tooling volley — bridge to a call on scaffolding his ideation→upkeep gap', nextActionDate:'2026-07-16', addNote:'[Pulse 7–9] Atlanta founder (dscvr), AI-active; named the ideation→upkeep/orchestration gap — squarely the agentic-scaffolding offer. Thread drifted into LLM/Codex shop-talk. NOTE: not in SEED-100 — no-ops until migration.'},
  {name:'Shar Caesar Douglas', stage:'In conversation', apptReady:true, lastContacted:'2026-07-07', nextAction:'Bridge to a call rather than another tooling volley', nextActionDate:'2026-07-16', addNote:'[Pulse 6] Ex-CMO TIDAL, Epiphany Society; AI-active, leaner-team systems mindset. [Pulse 9] Marty followed up Jul 7 (Substack synchronicity); ball in her court, still no call ask.'},
  {name:'Rob Coven', stage:'In conversation', apptReady:true, lastContacted:'2026-07-07', nextAction:'Propose a short call — he invited the exchange', nextActionDate:'2026-07-16', addNote:'[Pulse 2] Manages 200+ assets with AI; wants deeper context + long-term continuity; "open to a brief exchange." [Pulse 9] Marty followed up Jul 7; ball in Rob\'s court, still no call ask.'},
  {name:'Christiana Brown', stage:'In conversation', apptReady:true, lastContacted:'2026-07-07', nextAction:'Bridge to a call — thread slid into persona/Alfred shop-talk', nextActionDate:'2026-07-16', addNote:'[Pulse 2] Built an AI voice coach for admissions training; friction = knowing when NOT to use AI. [Pulse 9] Advanced Jul 7 into persona shop-talk; ball in her court, no call bridged.'},
  {name:'Michael Bland', stage:'In conversation', apptReady:true, lastContacted:'2026-07-03', nextAction:'STOP tooling talk — call on automating his eXp real-estate book', nextActionDate:'2026-07-16', addNote:'[Pulse 3–5] Named gap: no good automation on the real estate side yet. Thread stalled in tooling talk since Jul 3; ball in his court.'},
  {name:'Beatrice Sibblies', stage:'In conversation', apptReady:true, warmthMin:'Warm', lastContacted:'2026-07-02', nextAction:'MOST TIME-SENSITIVE — window open since Jul 6; send two concrete slots today', nextActionDate:'2026-07-16', addNote:'[Pulse 3] She proposed the catch-up herself ("after the holidays"). Window open since Jul 6 — 10 days unpinned as of Pulse 17.'},
  {name:'Elizma Burger', stage:'In conversation', apptReady:true, lastContacted:'2026-07-08', nextAction:'Confirm the Leo call is booked', nextActionDate:'2026-07-16', addNote:'[Pulse 10] Resolved out of the unread queue ~Jul 8 after nine pulses cold — confirm the Leo call is actually booked.'},
  {name:'Dan Mall', stage:'In conversation', lastContacted:'2026-06-30', nextAction:'Ball in his court — light nudge if still quiet', addNote:'[Pulse 1] Guarded curiosity, engaged after the design-systems re-hook. Warmest non-appointment thread.'},
  {name:'Chris Cornell', stage:'Replied', warmthMin:'Warm', lastContacted:'2026-07-01', nextAction:'Low signal — hold', addNote:'[Pulse 2] Replied "I agree" only.'},
  {name:'Doug Gollan', stage:'Nurture', lastContacted:'2026-07-01', nextAction:'Revisit in a quarter', addNote:'[Pulse 1] Polite decline — AI use "proprietary". Relationship banked.'},
  {name:'Morgan Bright', stage:'Lost', lastContacted:'2026-06-30', addNote:'[Pulse 1] Declined — no AI in the practice; IC, not the decision-maker.'},
  {name:'Mordecai Brownlee', stage:'Touch 1 sent', lastContacted:'2026-06-30', addNote:'[Pulse 1] Auto out-of-office only — not a genuine reply.'},
  {name:'Sophia Danner Okotie', stage:'Replied', lastContacted:'2026-07-08', nextAction:'Low signal — hold', addNote:'[Pulse 10] "Thank you" only; Marty asked about Besida\'s anniversary. Ball in her court.'},
  {name:'Tammie Mooreland Cade', stage:'Lost', lastContacted:'2026-07-06', addNote:'[Pulse 8] Personal contact ("mama"/"son") — good-naturedly rumbled the mass-message. Not a prospect; exclude from prospect treatment. NOTE: staged-12; in SEED only if present.'},
  {name:'Brittney Cunningham', stage:'Lost', lastContacted:'2026-07-07', addNote:'[Pulse 9] Personal/known contact mass-messaged in error; Marty retracted the touch. Not a prospect.'},
  {name:'Jazzauria Williams', stage:'Lost', lastContacted:'2026-07-09', addNote:'[Pulse 10] Warm-personal reconnection, no AI answer, no business trigger. Relationship banked, not a prospect. NOTE: not in SEED-100.'},
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

---

*Written Pulse 17 · 2026-07-16. Supersedes pulse-15-artifact-patch.md. Ground truth also captured in lookalike-engine.md run log.*
