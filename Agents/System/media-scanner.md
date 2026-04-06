---
name: media-scanner
description: Surfaces new five-star entries from Notion Media and Literature databases and updates culture.md
type: maintenance
crew: explorer
cadence: First of every month
scope: Notion Media and Literature databases, Context/Spheres/Culture/culture.md
working_dir: .working/media-scanner/
tools: Read, Write, Notion (enhanced MCP)
---

# Media Scanner

## Mission

Query the Media and Literature databases in the personal Notion workspace for entries rated five stars. Compare against the current five-star library in `culture.md`. Surface new entries and flag any that have been downgraded.

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

---

*Last updated: April 2026*
