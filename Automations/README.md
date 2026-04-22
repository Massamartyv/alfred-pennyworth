# Automations

Scripted workflows that live on the Mac. Each automation is a self-contained folder with its own script, dependencies and README.

## Structure

```
Automations/
├── {Automation Name}/
│   ├── {automation-name}.py       -- Primary script (kebab-case, matches folder)
│   ├── requirements.txt           -- Python dependencies
│   └── README.md                  -- Scope, usage, design intent
```

## Current Automations

| Automation | Scope | Purpose | Cadence |
|---|---|---|---|
| Pinterest Organizer | Personal | Audits and reorganises Pinterest boards via the Pinterest API | On-demand (infrequent) |
| Finance Dashboard | Personal | Visual finance overview – currently a static HTML artefact; full automation build pending | On-demand (planned build) |

## Conventions

- **Folder name:** Title Case (`Pinterest Organizer/`, `Finance Dashboard/`)
- **Script name:** lowercase kebab-case matching the folder (`pinterest-organizer.py`)
- **Python dependencies:** `requirements.txt` in the automation folder
- **Environment variables:** Read from `~/Alfred Pennyworth/.env` where needed
- **README:** Required. Describes scope (personal vs venture), purpose, usage, design intent

## Adding a New Automation

1. Create `Automations/{Automation Name}/`
2. Add the primary script (kebab-case filename)
3. Add `requirements.txt` with pinned dependencies
4. Add `README.md` following the existing examples
5. If the automation is venture-scoped, document the scope and its plugin/credential routing clearly
