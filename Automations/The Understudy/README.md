# The Understudy

Keeps the Notion Reference Library mirror in step with the canonical markdown corpus.

Named for what the mirror is: it knows the whole part and performs when the principal is
unavailable. It never rewrites the part.

## The direction of travel

The markdown corpus at `Context/Reference Library/` is canonical. Notion is the reading and capture
surface, for use away from the Mac. When the two disagree, the markdown wins. This script only ever
writes markdown into Notion; it never writes Notion into markdown.

References captured in Notion are the exception, and they are handled by hand rather than by script:
a row added from the phone has no `Card` value and is reported by `--harvest`. Alfred writes it up as
a proper card in the corpus, then the next `--push` links the two by path.

## Usage

```bash
python3 "the-understudy.py"            # report drift, write nothing
python3 "the-understudy.py" --push     # create missing rows, patch changed properties
python3 "the-understudy.py" --push --bodies   # also rewrite every page body
python3 "the-understudy.py" --harvest  # list Notion rows with no card on disk
```

`--bodies` deletes and rewrites the body of all 255 pages and takes several minutes. Reach for it only
after a change to the card body format, not as routine maintenance.

## What it compares

Title, Type, Status, Sphere relations, Pull for, Themes, Domains and Added. Page bodies are not
compared, because nothing edits them but this script.

## Anchoring

The `Card` property on every Notion row holds the card path relative to the corpus root, for example
`Creators/edward-tufte.md`. That path is the join key in both directions. It is machine-maintained
and should never be hand-edited.

## Vocabulary

`vocabulary.py` holds the controlled Pull-for set of 55 handles, the 18 Themes, and the legacy map
from the 698-term vocabulary the corpus carried before 2026-09-14. The map is retained so the
migration stays reproducible and so a card written against the old vocabulary can still be resolved.

Cards carry the controlled vocabulary in their `pull_for` and `themes` frontmatter fields. The prose
**Pull for** line in the card body is the original authored wording and is not a retrieval surface.

## Requirements

`NOTION_PERSONAL_TOKEN` in `~/Alfred Pennyworth/.env`. No other credentials.

## Cadence

Run the check after any batch of card writing, and as part of the monthly heartbeat. The script is
idempotent and safe to run at any time.
