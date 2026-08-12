# Pulse 28 artifact patch — apply in a writable session

**Why this file exists:** the live `five-points-prospect-pipeline` artifact
(`~/Documents/Claude/Artifacts/five-points-prospect-pipeline/index.html`) is read-only
in the automated pulse session, is outside every shell mount (verified firsthand this run —
only `.claude`, `.local-plugins`, `Alfred Pennyworth`, `outputs`, `uploads` are mounted), and its
100-record `SEED` array is a single line of **28,209 tokens** (verified this run, grown from
28,181 at Pulse 26) that exceeds the file reader's 25k cap — so the pulse cannot assemble the
full HTML that `update_artifact` requires with SEED verbatim. `update_artifact.updatedAt` is
still 2026-07-07, confirming the artifact has never synced past Pulse 7. This has now blocked
**fourteen consecutive pulses**. The patch below changes ONLY the two machine-editable pulse
regions; SEED and all user-editable logic are untouched.

Supersedes `pulse-27-artifact-patch.md`. Apply once, in a session where the artifact file
is writable, then call `mcp__cowork__update_artifact` (id: `five-points-prospect-pipeline`).

---

## 1. Banner — replace the PULSE-BANNER inner `<div>` (lines ~121–123)

```html
  <div class="banner" style="background:#fdf6e7;border:1px solid #e3cf9a;color:#6b5416;margin-bottom:14px">
    <b>Pulse 28 — Sat 1 Aug 2026:</b> Second static day. No net-new replies since Pulse 26 (29 Jul); no thread movement, no new connections in 24h. <b>Beatrice Sibblies</b> &ndash; still awaiting her Baltimore dates (&ldquo;within the month, will confirm&rdquo;, 29 Jul); Marty up there in ~2 weeks; two-sided in-person meet warm but no locked date. <b>Kirsten Tucker</b> (responder #10) still awaiting Marty to name a Baltimore week &ndash; actively scheduling, ball in Marty&rsquo;s court. <b>Danial Qureshi</b> (best cold prospect) now 19 days unanswered &ndash; any reply must lead with the gap. Six standing leads still awaiting a call ask. Stage A: 0 of 19 dental invites accepted (Day 31) &ndash; withdrawal recommended. No new batch staged &ndash; hold until a meet is booked. 28 pulses, 10 responders, 0 appointments booked. Case for weekly cadence stands.
  </div>
```

## 2. PULSE_VERSION — in the PULSE-SYNC block (script)

```js
const PULSE_VERSION = '2026-08-01-pulse-28';
```

## 3. PULSE_UPDATES — merge/add these entries

```js
// warmthMin only raises warmth; stage/apptReady/lastContacted/nextAction/nextActionDate as noted
{ name: 'Beatrice Sibblies', stage: 'Appointment-ready', apptReady: true, lastContacted: '2026-07-29',
  nextAction: 'Awaiting her Baltimore dates ("within the month, will confirm"). When she confirms, propose a specific day and lock the in-person — do not let it drift into another warm volley.',
  nextActionDate: '2026-08-02',
  addNote: 'Pulse 28: unchanged since Pulse 26 two-sided exchange. Ball in her court to confirm her window. Most valuable standing lead.' },

{ name: 'Kirsten Tucker', stage: 'Appointment-ready', apptReady: true, lastContacted: '2026-07-28',
  nextAction: 'Name a specific Baltimore week and lock the in-person. She is actively scheduling (a few trips coming up).',
  nextActionDate: '2026-08-02',
  addNote: 'Pulse 28: unchanged since Pulse 25/26. Ball in Marty’s court to name a week.' },

{ name: 'Danial Qureshi', stage: 'Replied', apptReady: false, lastContacted: '2026-07-13',
  nextAction: 'Answer, own the 19-day gap, affirm the utilization/friction/win-win framing, propose two specific times.',
  nextActionDate: '2026-08-02',
  addNote: 'Pulse 28: 19 days unanswered. Best-quality true-net-new cold prospect; free re-open closed at Pulse 20.' }
```

## Notes / caveats carried forward
- Material CRM state is unchanged from Pulses 26–27 (0 net-new replies, 0 movement, 0 accepts, same standing leads, connections 960); the only deltas this run are the banner date and Danial's day count (18 → 19).
- Round-2 additions **Michael Woods** and **Nicole DeAngelo** are not in SEED-100 and will no-op until the CRM migrates; Danial came from the seed pass and is likely in SEED.
- **Andrew McCann** (CEO, Jellis Craig — real estate; connected 26 Jul) still unvetted; screen for the Jack Linderman vendor/agency failure mode before treating as a lead.
- The still-unrecorded Batch-2 send (`SENT_JUL06`, 37 names, 6 Jul) from `pulse-18-artifact-patch.md` still needs applying if the artifact is to reflect that wave.
- **Durable fix (do this instead of re-patching):** reflow `SEED` to one-object-per-line, or externalise it to a fetched JSON, or execute `pipeline-dashboard-build-brief.md` so Notion becomes system of record with a regenerator. Any of these ends the fourteen-pulse block permanently.
