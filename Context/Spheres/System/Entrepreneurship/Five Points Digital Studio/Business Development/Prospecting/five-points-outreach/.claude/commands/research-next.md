---
description: Research the next N cold prospects and write their briefs
---
Use the prospect-research skill.

Take the next $ARGUMENTS cold prospects from data/prospects.csv, rotating
across cohorts rather than working one cohort in a block. Default to 5 if
no number is given.

For each: write queue/<slug>/research.md, set status to `researched`, set
researched_date. If a prospect turns out not to be a fit, set `passed` and
record the reason in notes rather than forcing a brief.

Report what you found in one line per prospect. Flag any where the three
problems came out thin — those are candidates for `passed`.
