---
name: sphere-review
description: Verifies Sphere Index alignment with Sphere Manager database and file structure
type: maintenance
crew: reviewer
model: haiku
cadence: First of each quarter
scope: Sphere Index in global CLAUDE.md, Sphere Manager database, Context/Spheres/ directory
working_dir: .working/sphere-review/
tools: Read, Glob, Grep, Notion (enhanced MCP)
---

# Sphere Review Agent

## Mission

Verify that the Sphere Index in the global CLAUDE.md, the Sphere Manager database in Notion and the actual file structure under `Context/Spheres/` are all in alignment. Surface any drift, missing entries or topics ready for graduation.

---

## Scope

- **Sphere Index**: Global `~/.claude/CLAUDE.md` -- Sphere Index table
- **Sphere Manager database**: `collection://4d195180-7fd5-4b7d-a407-2e1a44124002`
- **File structure**: `~/Alfred Pennyworth/Context/Spheres/`
- **Graduated files**: Listed in global CLAUDE.md under "Graduated sphere files"

---

## Criteria

### Index-to-filesystem alignment

- Every sphere listed in the Sphere Index has a corresponding folder under `Context/Spheres/{Cluster}/{Sphere}/`
- Every folder under `Context/Spheres/` has a corresponding entry in the Sphere Index
- Cluster index files exist at the root of each cluster folder

### Index-to-database alignment

- Every sphere in the Sphere Index exists as an active sphere in Sphere Manager
- Every active sphere in Sphere Manager has an entry in the Sphere Index
- Sphere names match between the index and the database

### Graduation readiness

- Flag any sphere topic that has accumulated enough detail in the cluster index file to warrant its own graduated file
- Flag any graduated file that is referenced in the cluster index but missing from the global CLAUDE.md graduated files list

### State currency

- Review the "Current state snapshot" in the global CLAUDE.md
- Flag any state that may have shifted (fitness phase, active language, content priority, business priority)

---

## Report Format

```
SPHERE REVIEW REPORT
====================
Date: {date}
Spheres in Index: {count}
Spheres in Manager: {count}
Folders in filesystem: {count}

MISALIGNED
- {sphere/file}: {discrepancy} -- {recommended action}

GRADUATION CANDIDATES
- {topic}: {reason it is ready} -- {suggested file path}

STATE DRIFT
- {field}: Currently says "{current}" -- may need update to "{suggested}"

ALIGNED
- {confirmation of what is in sync}
```

---

## Working Directory

All intermediate output goes to `.working/sphere-review/`. This includes index snapshots, database query results and alignment comparison data before they are compiled into the final report. The directory is cleared at the end of each run.

---

## After the Review

1. Present the report
2. For approved corrections, update the Sphere Index, create missing folders or files
3. For graduation candidates, create the graduated file and update the cluster index
4. Update state snapshot if confirmed by the user

---

*Last updated: April 2026*
