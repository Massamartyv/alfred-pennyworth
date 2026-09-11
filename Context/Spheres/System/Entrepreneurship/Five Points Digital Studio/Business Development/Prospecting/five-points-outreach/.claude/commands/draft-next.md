---
description: Draft messages for researched prospects, up to the daily cap
---
Use the message-drafting skill.

Draft for the next $ARGUMENTS prospects with status `researched`. Default
to 5. Respect the daily cap in data/state.json — if drafting N would
exceed it, draft up to the cap and say so.

Write queue/<slug>/draft.md, set status to `drafted`, set drafted_date.

Then print every draft in full so Marty can read them in one pass without
opening files. He edits, he sends, he runs /log-send.
