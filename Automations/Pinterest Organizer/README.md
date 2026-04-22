# Pinterest Organizer

One-shot Pinterest board reorganization tool. Audits, restructures and cleans up Pinterest boards via the Pinterest API.

## Scope

**Personal.** Works against the personal Pinterest account – mood boards, aesthetic research, Culture cluster reference material.

## What It Does

- `audit` – inventory all boards, pin counts, last-activity dates
- `board <name_or_id>` – deep dive on a single board, surface duplicates and mis-categorised pins
- `batch plan.json --dry-run` – execute a reorganization plan (moves, merges, deletions)
- `destroy` – self-destruct the tool after use

## Usage

```bash
cd "~/Alfred Pennyworth/Automations/Pinterest Organizer"
pip install -r requirements.txt
python pinterest-organizer.py --token <PINTEREST_ACCESS_TOKEN> audit
```

The token is a Pinterest developer access token. Not currently stored in `.env` – passed inline or via environment on each run.

## Design Intent

This is an infrequent-use tool. It runs when the board landscape drifts from the Creative Director aesthetic standard and needs a sweep. Not a scheduled automation, not an always-on agent – a scalpel pulled out when the archive needs pruning.

## Output

Generates a JSON plan file before any destructive action. The `--dry-run` flag is the default for `batch`; explicit approval required before actual execution.
