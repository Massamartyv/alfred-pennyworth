# Pulse 30 — apply-ready artifact patch (supersedes pulse-29)

Apply in the next **writable** session (source `~/Documents/Claude/Artifacts/five-points-prospect-pipeline/index.html` is read-only + outside every shell mount + single-line SEED over reader cap, so an automated pulse cannot rebuild it). Only the two marked pulse regions change; SEED and user-editable logic stay untouched.

Material CRM state is IDENTICAL to Pulses 26–29: 0 net-new responders, 0 thread movement, 0 Stage-A accepts, 960 connections. The only deltas from the pulse-29 patch are the banner date and Danial's day count (20 → 21).

## 1. PULSE-BANNER-START/END block (lines ~120–124)

```html
<!-- PULSE-BANNER-START (rewritten by each scheduled pulse) -->
<div class="banner" style="background:#fdf6e7;border:1px solid #e3cf9a;color:#6b5416;margin-bottom:14px">
  <b>Pulse 30 — Mon 3 Aug 2026:</b> Fourth straight static day — no new replies, no new connections since 29 Jul. Two live in-person threads still waiting on a date: <b>Kirsten Tucker</b> (ball in Marty&rsquo;s court — name a Baltimore week) and <b>Beatrice Sibblies</b> (waiting on her to confirm her window). <b>Danial Qureshi</b> now 21 days unanswered — best cold prospect. Nine standing appointment-ready leads, still <b>0 booked</b>. Stage A: 0 of 19 dental invites accepted (Day 33) — withdraw recommended. No batch staged; hold new candidates until a meet is booked. Recommend reducing pulse to weekly until a date is pinned.
</div>
<!-- PULSE-BANNER-END -->
```

## 2. PULSE-SYNC-START/END block (in `<script>`)

- `PULSE_VERSION = '2026-08-03-pulse-30'`
- SENT arrays: unchanged (no sends since Batch 2, Jul 6).
- `PULSE_UPDATES` deltas (warmthMin only ever raises warmth):
  - **Beatrice Sibblies** — stage Replied, apptReady true, lastContacted 2026-07-29, nextAction "When she confirms her Baltimore window, propose a specific day and lock the in-person — do not let it drift", nextActionDate 2026-08-04.
  - **Kirsten Tucker** — stage Replied, apptReady true, lastContacted 2026-07-28, nextAction "Name a specific Baltimore week and lock the in-person (ball in Marty's court — lowest-friction first booking)", nextActionDate 2026-08-04.
  - **Danial Qureshi** — stage Replied, apptReady true (bridge candidate), lastContacted 2026-07-06, addNote "21 days unanswered as of Pulse 30; free re-open closed Pulse 20 — lead any reply by owning the gap", nextAction "Answer, affirm the utilization/friction/win-win framing, propose two specific times".

Caveat carried forward: Michael Woods and Nicole DeAngelo are round-2 additions NOT in SEED and will no-op until the CRM migrates; Danial and the staged-12 names came from the seed pass and should apply.

Durable fix (all require a writable session): reflow `SEED` to one-object-per-line, externalise it to a fetched JSON, or execute `pipeline-dashboard-build-brief.md` (Notion system-of-record + regenerator).
