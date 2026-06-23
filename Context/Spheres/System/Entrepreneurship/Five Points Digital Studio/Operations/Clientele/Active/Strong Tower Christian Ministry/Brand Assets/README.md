# Brand Assets — Strong Tower Christian Ministry

Source-of-truth catalogue for Strong Tower brand material. The codebase is the live source for anything shipped on the site; this directory holds originals, archives and material not yet placed.

The client has an existing brand. The logo and type identity were lifted from the live site on 2026-06-22, pending the operator's confirmation. Higher-fidelity source files are still requested from the client.

---

## Logo

| File | Purpose | Status |
|---|---|---|
| `Logo/logo-original.png` | Logo lifted from the live site (173x174, RGBA, transparent) | Present (lifted 2026-06-22) |
| `Logo/logo-600.png` | 600px render for reference and web use | Present |
| `Logo/logo-production.png` | Web-optimised version shipped to the codebase | Pending |
| `Logo/logo.svg` | Vector source for retina and dark-background use | Requested from client |

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
