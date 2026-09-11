---
name: queue-management
description: Track prospect state, enforce the daily cap, and report pipeline status. Use for any read or write of data/prospects.csv or data/state.json.
---

# Queue management

## Files

`data/prospects.csv` — columns:

    slug,name,company,cohort,role,channel,status,researched_date,
    drafted_date,sent_date,replied_date,notes

`data/state.json`:

    {
      "daily_cap": 15,
      "sent_today": 0,
      "last_reset": "2026-09-08",
      "totals": {"researched":0,"drafted":0,"sent":0,"replied":0,"booked":0}
    }

## Rules

- Reset `sent_today` when `last_reset` is not today.
- Refuse to draft beyond the daily cap. Say the cap is reached and stop.
  The cap protects his accounts and the quality of the messages both.
- Never advance a status past `drafted` on your own. Only `/log-send`
  and `/log-reply`, run by Marty, move a prospect forward.
- Never change a `hold` or `passed` status without Marty saying so.
- Work cohorts in rotation, not in blocks. Cohort A, then B, then C,
  then D, then round again. Fifteen messages of one type in one day
  reads as a campaign to anyone who compares notes.

## Status report format

    PIPELINE — <date>
    Cold <n> · Researched <n> · Drafted <n> · Sent <n> · Replied <n> · Booked <n>
    Sent today: <n>/<cap>

    AWAITING MARTY
    <slug> — <name> — drafted <date>

    NEXT UP
    <slug> — <name> — <cohort>

    STALE
    Sent over 10 days ago, no reply. Do not chase automatically.
