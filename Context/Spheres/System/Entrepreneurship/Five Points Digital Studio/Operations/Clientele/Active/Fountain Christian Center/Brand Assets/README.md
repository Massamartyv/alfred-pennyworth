# Brand Assets — Fountain Christian Center

Source-of-truth catalogue for FCC brand material. The codebase is the live source for anything currently shipped on the site; this directory holds originals, archives and material not yet placed.

---

## Logo

| File | Purpose | Notes |
|---|---|---|
| `Logo/logo-original.png` | Original logo file as supplied | MD5 `179c8daf5062322fbb660051734b87eb`. Kept for historical reference. |
| `Logo/logo-production.png` | Mirror of `public/logo.png` in the live codebase | MD5 `bfdec2d58db1be2d691ade6fa97c4754`. The version currently shipped. |

The two files differ. The codebase version is treated as canonical for anything user-facing; the original is preserved here in case the source is needed for reference or rework.

---

## Photography

Four FCC photos curated and categorised. The original supply was 25 mixed images; non-FCC material (Favor of God International Worship Center) and one neighbourhood scene unrelated to the church were removed during triage on 2026-05-04.

### `Photography/Worship/`

- `liturgical-worship.jpg` – Minister in white liturgical vestments with wooden cross pendant, arms wide in worship. Modern sanctuary interior. Subject is not Bishop Locklear; identity not confirmed.

### `Photography/Leadership/`

- `bishop-locklear-formal.jpg` – Bishop Locklear (centre) with two other men in formal evening wear at a "Keepers of the Dream" function. Not an FCC event; usable as ambient leadership imagery.

### `Photography/Community/`

- `pastoral-visit-senior-birthday.jpg` – Bishop Locklear visiting an elder congregant at a birthday celebration. NY Yankees caps, atrium / senior-care setting.
- `pastoral-visit-multigenerational.jpg` – Wider frame from the same event: a younger woman bridging two seated elders, including the same gentleman from the previous shot plus an elderly woman.

### Currently shipped to production

The three leader headshots live in the codebase at `Deliverables/Website/fountain-christian-center/public/images/leaders/`:

- `bishop-charles-locklear.jpg`
- `pastor-joann-locklear.jpg`
- `pastor-alberta-champelle.jpg`

These are not duplicated here — the codebase owns build-time assets. If higher-resolution source files are ever supplied separately, they should land here first and a derivative pushed to the codebase.

---

## Open gaps

- Bishop Watts portrait for the in-memoriam page. Expected destination: `Deliverables/Website/fountain-christian-center/public/images/legacy/bishop-watts-memorial.jpg`. The `HAS_PORTRAIT` flag in the memorial page is currently `false`, falling back to a placeholder until the portrait is supplied.
- Sunrise and Sunset dates for Bishop Watts on the memorial page.
- Imagery for the empty `public/images/` subfolders in the codebase: `banners/`, `legacy/`, `ministries/`, `widgets/`.
- A logo SVG. The two PNGs are raster; vector source would help with retina rendering and dark-background placement.

---

## Conventions

- New supplies of unsorted material land in `Photography/Source/` first and stay there until triaged.
- Curated, named, categorised files live under `Photography/{Worship, Leadership, Community, …}/` once categorised.
- Anything actively rendered on the live site lives in the codebase under `public/images/{category}/`. The codebase is canonical for production assets.
- This directory is the archive and the staging ground; the codebase is the live source.
