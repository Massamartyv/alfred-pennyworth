# Brand Assets — Strong Tower Christian Ministry

Source-of-truth catalogue for Strong Tower brand material. The codebase is the live source for anything shipped on the site; this directory holds originals, archives and material not yet placed.

The client has an existing brand. The logo and type identity were lifted from the live site on 2026-06-22, pending the operator's confirmation. Higher-fidelity source files are still requested from the client.

---

## Logo

| File | Purpose | Status |
|---|---|---|
| `Logo/logo-master.png` | The operator-preferred transparent cut (448px after trim) — canonical for all placements | Present (supplied 2026-07-29) |
| `Logo/logo-master-light.png` | Dark-ground variant — neutral ink recoloured to cream, gold and blue untouched | Present (derived 2026-07-29) |
| `Logo/logo-source-2250.png` | The full 2250px client artwork on its white ground — the high-resolution source | Present (supplied 2026-07-29) |
| `Logo/logo-wix-lifted-2026-06-22.png` | The 173px raster lifted from the old Wix site — superseded, retained for the record | Archived |
| `Logo/logo-original.png` | Logo lifted from the live site (173x174, RGBA, transparent) | Superseded 2026-07-29 |
| `Logo/logo-600.png` | 600px render for reference | Superseded 2026-07-29 |
| `Logo/logo.svg` | Vector source for retina use | Still requested from client; the raster set covers current needs |

Shipped to the codebase 2026-07-29: `public/logo.png` (colour), `public/logo-light.png` (dark-ground cream), `src/app/icon.png` (favicon), `src/app/apple-icon.png` (180px on the warm-white field, since iOS flattens transparency onto black). Site placements render at 46px (nav emblem) and 190px (footer crest), both within the master's resolution.

The logo depicts a slate-blue tower topped by a gold cross, wrapped in a gold halo/crescent, with the wordmark "Strong Tower" in an elegant script and serif over "Christian Ministry". Lifted from Wix media; request the original vector from the client for crisp retina and dark-background placement.

---

## Photography

Awaiting supply. The current Wix site uses low-resolution stock; source or commission real service, leadership and community photography.

Conventions:
- Unsorted material lands in `Photography/Source/` first and stays there until triaged
- Curated, named, categorised files live under `Photography/{Worship, Leadership, Community, ...}/`
- Anything rendered on the live site lives in the codebase under `public/images/{category}/`; the codebase is canonical for production assets

---

## Brand Tokens (lifted 2026-06-22, pending operator confirmation)

Lifted from the live logo and site CSS. Fine-tune at confirmation, then these become the codebase token values.

**Colour** – read off the logo:
- Tower blue (primary): ~#5E7EA8, deep ~#3C5A86, light ~#9DB2CE
- Gold (cross and halo, the light): ~#C6A24E, light ~#DCC27A, deep ~#A8842E
- Near-black wordmark: #1A1A1A on a warm-white field #FBFAF8
- Deep slate-navy for fortress/dark sections: #1C2A3F

**Typography** – from the live site CSS:
- Live fonts: Futura Light, Didot Italic, Avenir Light
- Free portable translation: Playfair Display (display, = Didot) + Jost (structural and body, = Futura/Avenir)

Hex values are eyeball reads from the logo; confirm or correct before brand lock.

---

## Open Gaps

- Vector logo source (SVG) from the client – current files are raster, lifted from the site
- Operator confirmation of the lifted hex palette and font translation
- Real photography for worship, leadership and community
- Confirmation of any leaders beyond Pastor Kelsey M. Goodson and Prophetess Angela Goodson
