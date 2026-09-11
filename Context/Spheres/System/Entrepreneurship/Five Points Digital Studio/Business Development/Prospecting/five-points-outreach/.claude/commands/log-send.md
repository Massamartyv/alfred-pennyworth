---
description: Record that a message was sent by hand
---
Marty sent a message. Arguments: <slug> [any edits he made]

Set status `sent`, set sent_date, increment sent_today in state.json.

If he pasted his edited version, diff it against the draft and append
what changed to reference/voice-guide.md under **Observed corrections**.
That is how the drafts stop needing editing.
