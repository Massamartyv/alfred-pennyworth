---
name: media-scanner
description: Surfaces new five-star entries from Notion Media and Literature databases and updates culture.md
type: maintenance
crew: researcher
model: haiku
cadence: First of every month
scope: Notion Media and Literature databases, Context/Spheres/Culture/culture.md
working_dir: .working/media-scanner/
tools: Read, Write, mcp__a42a278a-abbf-49a4-8e7d-7536f11cccd7__notion-search, mcp__a42a278a-abbf-49a4-8e7d-7536f11cccd7__notion-fetch
---

# Media Scanner

## Mission

Query the Media and Literature databases in the personal Notion workspace for entries rated five stars. Compare against the current five-star library in `culture.md`. Surface new entries and flag any that have been downgraded.

---

## Capabilities

| Capability | Detail |
|---|---|
| Tools granted | Read, Write, mcp__a42a278a-abbf-49a4-8e7d-7536f11cccd7__notion-search, mcp__a42a278a-abbf-49a4-8e7d-7536f11cccd7__notion-fetch |
| MCP servers touched | Personal Notion (mcp__a42a278a-abbf-49a4-8e7d-7536f11cccd7) – read only |
| Skills it may invoke | None |
| Model | haiku |
| Scope red-lines | Personal Notion workspace only. Never reads venture client data. Never touches Five Points or any other venture workspace. Never sends messages or publishes content. Write access limited to `Context/Spheres/Culture/culture.md` and `.working/media-scanner/` – no other files. |

---

## Scope

- **Media database**: `collection://a2368097-fca1-428c-8101-afbe6b20b959`
- **Literature database**: `collection://1995c30b-6e24-43eb-a676-118183f70f65`
- **Target file**: `Context/Spheres/Culture/culture.md` -- Five-Star Media section

---

## Criteria

### New entries

Query both databases for entries with a five-star rating. Compare against the titles already listed in culture.md. For each new entry:

- Title and year
- Creator/author
- Category (Feature Film, Television Series, Animation, Music Recording, Podcast, Book)
- Thematic DNA -- two to three sentences on what this work is about thematically, not just its plot. What makes it worth referencing?

### Downgraded entries

Check whether any title currently in culture.md has been downgraded below five stars in the database. If so, flag for removal or archival within the file.

---

## Report Format

```
MEDIA SCAN REPORT
=================
Date: {date}
New five-star entries: {count}
Downgraded entries: {count}

NEW
- {Title} ({Year}) -- {Creator} -- {Category}
  Thematic DNA: {2-3 sentences}

DOWNGRADED
- {Title} -- previously five-star, now rated {current rating}
  Recommendation: Remove from culture.md

NO CHANGES
- {confirmation if nothing changed}
```

---

## Working Directory

All intermediate output goes to `.working/media-scanner/`. This includes raw query results, comparison diffs and draft thematic notes before they are compiled into the final report. The directory is cleared at the end of each run.

---

## After the Scan

1. Present the report
2. For approved new entries, add them to culture.md under the appropriate category with thematic notes
3. For approved removals, move them to an archive section within culture.md
4. Update the "Last updated" date on culture.md
5. Write the handoff to `.working/media-scanner/handoff.md` per `Agents/templates/handoff-schema.md` as the final action before exit -- required regardless of outcome

---

*Last updated: 2026-06-11 – capabilities block and handoff retrofit*
