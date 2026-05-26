# V8 – Sunday 21:00 ET Weekly Review Trigger – Operator Build Sheet

**Date:** 2026-05-23
**Trigger:** Validation Contract V8. Sunday 21:00 ET dispatch fires the Weekly Review ritual.
**Phase 1 path:** Notion AI Custom Agent. No External Agents API dependency, no waitlist.
**Phase 2 path:** Swap to Claude Code agent once V7 waitlist clears.

---

## Why two phases

V7 wires Claude Code as a registered External Agent inside the personal workspace. That gives the Custom Agent the option to dispatch Claude Code as its skill executor – which is the richer end state because Claude Code can read the Habits, Fitness Journal, Currently Reading and Reflections views, pre-populate Movement 3 numbers, draft Movement 4 prompts and surface candidate Movement 5 issues from the week.

V7 is blocked on Notion's External Agents API waitlist as of 2026-05-18. Until that clears, V8 runs with Notion AI as the skill executor. Notion AI is less powerful – it can create the page from template, set properties, and send a reminder – but it cannot reach outside the workspace or compose the rich pre-population.

The handoff between phases is a single skill swap inside the same Custom Agent. The schedule and trigger do not change.

---

## Phase 1 – Notion AI Custom Agent

### Build steps

1. Open Notion. Settings → AI → Custom Agents → New agent.
2. **Name:** `Weekly Review Trigger`.
3. **Icon:** 📅 (calendar week).
4. **Description:** `Dispatches the Sunday Weekly Review ritual. Creates a new entry in Reflections from the New Weekly Review template, sets the date, and notifies Martavious.`
5. **Skill 1: Create the Weekly Review entry.**
   - Action: Create page in Reflections database.
   - Template: New Weekly Review (`33218961-65cf-8054-b34b-e9637d01a769`).
   - Properties to set:
     - **Date:** today (Sunday)
     - **Category:** Review Session
     - **Prompt:** `Weekly Review – <ISO week number>` (e.g. `Weekly Review – W21`)
     - **Spheres:** Personal Development sphere relation (`a84f0ae6-11ac-497f-91d8-12c5415ef68d`)
6. **Skill 2: Send Notion notification.**
   - Action: Send mention notification to Martavious.
   - Message: `Sunday Weekly Review is ready. The fresh entry is in Reflections. The ritual lives at the top of the page; the deck is below. Start with Movement 0.`
   - Include link: the freshly-created page URL.
7. **Trigger / Schedule.**
   - Frequency: Weekly.
   - Day: Sunday.
   - Time: 21:00 America/New_York.
   - Timezone: confirm ET, not UTC.
8. **Save and enable.**

### First scheduled run

The first Sunday after build will fire automatically. Confirm:
- A new entry appears in Reflections that Sunday at 21:00 ET.
- The entry is categorised Review Session and dated correctly.
- A Notion notification arrives with a link to the new entry.

If anything misses, the Custom Agent's run log shows what happened.

---

## Phase 2 – Swap to Claude Code agent

**Prerequisite:** V7 unblocks. Notion CLI installed (done 2026-05-23), Claude Code registered as External Agent in personal workspace.

### Swap steps

1. Open the `Weekly Review Trigger` Custom Agent in Notion.
2. **Replace Skill 1 and Skill 2 with Skill 1': Dispatch Claude Code.**
   - Action: Call External Agent → Claude Code.
   - Prompt to Claude Code:
     ```
     Run the Sunday Weekly Review ritual. Create a new entry in the
     Reflections database (data source f0025f83-7a12-4a50-b00b-9c4a225ed7dc)
     from the New Weekly Review template (33218961-65cf-8054-b34b-e9637d01a769).
     Set Date to today, Category to Review Session, Prompt to
     "Weekly Review – W<isoweek>".

     Then pre-populate Movement 3 by reading:
     - Habits data source (098c6a57-2776-4949-bfbd-085cdd5a5880) for the
       past seven days, count days held for stillness, morning pages,
       keystone behaviour, Five-Minute Journal.
     - Fitness Journal (9084eeda-48b5-4793-80f2-03a97bfd4c63) for sessions
       count, strength-to-endurance ratio.
     - Literature (1995c30b-6e24-43eb-a676-118183f70f65) for reading days.
     - Content (ad36d098-c55c-46f9-b133-b3bfbd5cd81f) for Pennyone shipments.

     Then surface a candidate Movement 4 reflection prompt based on the
     past week's Reflections (Type-grouped from Reflections this week view).

     Finally, send Martavious a Notion notification with the entry URL
     and a one-line preview of the candidate Movement 4 prompt.
     ```
3. **Trigger / Schedule** – unchanged from Phase 1.
4. **Save.**

### Verification

- Following Sunday: confirm Claude Code session ran, entry was created and pre-populated, notification arrived.
- If the dispatch fails, the Custom Agent run log shows the External Agent error; debug Claude Code authentication and workspace permissions.

---

## Notion CLI ready state

Installed at `/opt/homebrew/bin/ntn`, version 0.14.1, as of 2026-05-23.

Authentication step pending operator: run `ntn login` in a terminal, complete OAuth in the browser, confirm the personal workspace shows in `ntn whoami`. This is independent of External Agents API waitlist – the CLI itself works against the standard Notion API today.

---

## Open loops at session end

- **Waitlist application** – submit at the Notion Developer Platform sign-up. Track when access lands.
- **Phase 1 build** – operator runs the eight steps in the Notion UI. Should take five to ten minutes.
- **First Sunday verification** – confirm the trigger fires on the first Sunday after build.
- **Phase 2 swap** – triggered by waitlist clearance.
