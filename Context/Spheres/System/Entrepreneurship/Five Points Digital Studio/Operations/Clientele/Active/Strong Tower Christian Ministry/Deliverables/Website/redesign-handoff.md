---
file_type: redesign_handoff
client: Strong Tower Christian Ministry
venture: Five Points Digital Studio
workflow: Website Development
date: 2026-06-22
status: executed 2026-06-22
for: a fresh session redesigning the site with ui-ux-pro-max
---

# Redesign Handoff — Strong Tower Christian Ministry Website

## TL;DR

A fresh session is to **redesign this site using the `ui-ux-pro-max` skill — not frontend-design**. The current build is functional, on-brand and on-concept, but the operator's read is that it "still looks pretty basic." Push the visual design substantially further. Two hard new directives from the operator:

1. **Stop leaning on the logo.** The brand mark is weak. Use it sparingly; lead the brand with a typographic wordmark and with photography.
2. **Make it image-led.** Real photography, placed with editorial judgment across the site — not literally scattered, but present and intentional where it earns its place.

This is execution elevation on a sound foundation, not a teardown. Brand colours, content, routes, integrations, stack, accessibility and portability are fixed (see below).

## How to start

1. Read this file fully.
2. Read, in order:
   - `Deliverables/Website/art-direction.md` — the locked concept, "Rising Light, grounded by the Tower."
   - `Deliverables/Website/prd.md` — the spec.
   - `Deliverables/Website/technical-recon.md` — the church facts.
   - `Deliverables/Website/deployment.md` — how it ships.
3. Read the current design system in the codebase: `src/app/globals.css`, `src/app/page.tsx`, `src/app/page.module.css`.
4. **Invoke `ui-ux-pro-max`** and feed it this handoff plus art-direction.md and the codebase path. It is a local skill and is permitted. (The previous pass used frontend-design; the operator wants ui-ux-pro-max this time.)
5. Redesign within the fixed constraints. Keep `next build` green. Deploy a preview and set it beside the live build for the operator.

## Operator directives — the point of this handoff

### Rise well above "basic"
The Rising Light direction is sound; the execution needs real design ambition. Treat the current build as a reference to surpass, not a finished artefact. ui-ux-pro-max may reinterpret the execution freely within the locked concept; evolving the concept itself needs operator sign-off.

### Logo — sparingly
The tower/cross/halo mark is not strong. Do not plaster it.
- **Reduce:** the large home-hero emblem (a 200px logo inside a halo) — replace with imagery and/or the wordmark. Reconsider the footer logo in favour of a wordmark.
- **Keep:** a small mark in the nav is acceptable; the favicon is fine.
- **Lead with a typographic wordmark** — "Strong Tower" set in Fraunces — and with photography, not the mark.
- A logo redraw may be warranted; route that to the `design` skill or a human as a separate track, and flag it to the operator. The vector logo is still requested from the church.

### Imagery — lead with it, authentically
The site currently has no photography (a known gap). The redesign should feature real images placed with editorial judgment.
- **Authenticity line:** use real Strong Tower photography wherever possible — congregation, worship, leadership, the building. Do **not** present stock photos of an obviously different congregation as Strong Tower, and do **not** use AI-generated people. For a real church both read as false, and both are against the operator's taste.
- **Request from the church (now a priority):** worship and service photography, portraits of Pastor Kelsey M. Goodson and Prophetess Angela Goodson and any other leaders, community and fellowship images, the building exterior and interior, and Florence/place.
- **Interim, until real photos arrive:** lean on atmospheric, architectural and textural imagery that evokes without misrepresenting — light through windows, sky and architecture, hands in worship cropped or abstract, warm interior texture — from properly licensed libraries, clearly marked for replacement. A strong type-and-light composition beats a fake-congregation stock photo.
- **Placement (judgment, editorial):** a strong hero image or image-and-type composition; a worship or community image in the welcome and about bands; real portraits on `/leadership` and the home leadership pull; a warm image on `/visit`; sermon thumbnails already arrive from YouTube on `/watch`. Treat each image as a considered element with negative space — the Kinfolk, Aman and Cereal discipline in the reference library — not decoration.
- **Implementation:** use `next/image`. `next.config.ts` already allows `static.wixstatic.com`, `i.ytimg.com` and `img.youtube.com`; add any new image host to `remotePatterns`. Optimise to WebP, lazy below the fold, priority above. Store real assets under `public/images/{category}/` and catalogue them in `Brand Assets/`.

## Fixed — do not change

- **Brand colours** — the lifted palette: tower blue `#5E7EA8` (deep `#3C5A86`, light `#9DB2CE`), gold-as-light `#C6A24E`, deep slate-navy `#1C2A3F`, warm white `#FBFAF8`, near-black text, rare garnet `#6E1F2A` for scripture only. Tokens in `globals.css` are the single reskin surface.
- **Content** — all copy and the 11 routes. Doctrine drafts and CONFIRM flags are pending (see Open work).
- **Stack** — Next.js 16 App Router, TypeScript strict, CSS Modules with global tokens. No Tailwind, no CSS-in-JS. Fraunces (display) + Jost (body) via `next/font`. No heavy new dependencies without reason.
- **Integrations** — YouTube live and sermon pull, Resend contact and prayer forms, newsletter, giving swap-slot, map. Keep them working; all degrade gracefully until keyed.
- **Accessibility** — WCAG AA, large legible body for an older congregation, visible focus, full `prefers-reduced-motion`.
- **Portability** — no Vercel-only primitives; content in-repo; every integration behind an env var; tokens stay the reskin surface.

## The lay of the land

- **Codebase root:** `/Users/martyspicer/Alfred Pennyworth/Context/Spheres/System/Entrepreneurship/Five Points Digital Studio/Operations/Clientele/Active/Strong Tower Christian Ministry/Deliverables/Website/strong-tower-christian-ministry`
- **Live (public):** https://strong-tower-christian-ministry.vercel.app — the by-hand Rising Light restructure.
- **Latest preview (gated):** the frontend-design craft pass (film grain, hero page-load stagger, breathing halo, Fraunces optical sizing, order-of-service ticks, micro-interactions). Preview-protected by Vercel; the operator views it signed into studio-fivepoints.

### Current design system
Fraunces + Jost; gold-as-light tokens; "dawn" scroll reveal; a halo-arc primitive (`HaloArc`); scripture interludes (`ScriptureInterlude`); an order-of-service home; radiant dark heroes with film grain.

### File map
- `src/app/layout.tsx` — root layout, fonts, metadata, nav + footer + skip link. (No JSON-LD yet — see Open work.)
- `src/app/globals.css` — design tokens and global classes. The reskin surface.
- `src/app/page.tsx` + `page.module.css` — home, order-of-service grid.
- `src/lib/site.ts` — single source of truth for church data: services, contact, nav, scripture, giving URL.
- `src/lib/youtube.ts`, `src/lib/email.ts` — integration helpers.
- `src/components/` — Navigation (+ LiveButton), Footer, Newsletter, RevealSection, HaloArc, ScriptureInterlude, SocialIcons.
- `src/app/{about,what-we-believe,leadership,watch,events,visit,get-involved,give,prayer,contact}/` — the pages. Contact and prayer carry `actions.ts`, a client form and `types.ts`.
- `src/app/api/{live-status,newsletter}/route.ts`, `src/app/sitemap.ts`, `src/app/robots.ts`.

### References (Five Points anti-library)
Aman (light from a source, warmth within restraint), Kinfolk (negative space, frame discipline), Pentagram (editorial / order-of-service), Pangram Pangram (type reads commissioned, not free-shelf). Translation sources in art-direction.md: Aaron Douglas, Ethiopian Orthodox illumination, Kanye Sunday Service.

## Build, verify, deploy

```bash
CODE="/Users/martyspicer/Alfred Pennyworth/Context/Spheres/System/Entrepreneurship/Five Points Digital Studio/Operations/Clientele/Active/Strong Tower Christian Ministry/Deliverables/Website/strong-tower-christian-ministry"

npm --prefix "$CODE" install
npm --prefix "$CODE" run build          # must be green

# Five Points Vercel token lives in ~/Alfred Pennyworth/.env as VERCEL_FIVEPOINTS_TOKEN
VERCEL_TOKEN="$TOKEN" vercel deploy --cwd "$CODE" --scope studio-fivepoints --yes          # preview
VERCEL_TOKEN="$TOKEN" vercel deploy --prod --cwd "$CODE" --scope studio-fivepoints --yes   # production
```

Vercel preview deployments on this team are protection-gated — they answer 401 anonymously. The operator views previews signed into studio-fivepoints, or asks to disable protection on the project. The church domain `strongtowercm.org` is still on Wix; no cutover has happened.

## Open / pending work

- Brand kit confirmation and a vector logo — and likely a logo redraw (see Logo directive).
- **Real photography from the church** — now a priority, because the redesign is image-led.
- Content CONFIRM flags: founding history; leader photos and full roster; visit specifics (parking, childcare, service length); the ministry list; pastoral approval of the Confession of Faith and Sonship.
- Live integration keys in Vercel: YouTube, Resend, newsletter, giving URL.
- Keystatic CMS — the chosen staff-editing layer, a fast-follow.
- JSON-LD structured data — deferred: the standard Next.js inline-script approach for JSON-LD is gated by a security hook; add it through a sanitiser-approved path or a dedicated structured-data component the hook accepts.
- DNS cutover from Wix to Vercel when ready.

## Permissions note

`Skill(anthropic-skills:frontend-design)` was on the deny list in `~/.claude/settings.json`; the operator authorised removing it for the last pass. For this work, use **`ui-ux-pro-max`** (local, allowed) per the operator's instruction.

---

## Outcome — executed 2026-06-22

Redesign pass run with `ui-ux-pro-max`. Build green (`next build`, 19 routes), verified at desktop and mobile, preview deployed. See `deployment.md` for the deploy record.

**Both directives delivered:**
- **Logo demoted.** New `Wordmark` component — "Strong Tower" in Fraunces with a rising tower-and-arcs light glyph, the brand's own signature — now leads the nav and footer. The 200px logo-in-halo home-hero emblem is gone. No `logo.png` remains in any rendered surface; favicon untouched.
- **Image-led.** The home hero is now a full-bleed photographic composition (light through architecture) under a legibility scrim, with the tagline leading in Fraunces. Real imagery threaded into the Welcome band (worship, gold) and the Watch band (congregation, faint beneath the dark ground). Photos are punctuation against the type-and-light system, not wallpaper.

**Interim imagery** — atmospheric/architectural only, no AI people, no fake-congregation stock. Four files under `public/images/`, curated by eye from Unsplash, catalogued and marked for replacement in `public/images/CREDITS.md`. **Priority: replace with real Strong Tower photography at brand lock.**

**Fixed constraints held:** brand colours, content, the 11 routes, the stack, integrations, accessibility (WCAG AA, reduced-motion, large type), portability. Tokens remain the single reskin surface.

**What ui-ux-pro-max could not do here:** its `scripts/` and `data/` are dangling symlinks on this machine (point to `/Users/martyspicer/src/ui-ux-pro-max/`, which does not exist), so the design-system query engine did not run. The curated references (`ux-rules.md`, `pre-delivery-checklist.md`) loaded fine and carried the UX discipline; the brand system was already locked in `art-direction.md`. Worth repairing the symlinks if the engine is wanted later.

**Still open** (unchanged from below): real photography from the church; brand kit + vector logo, with a logo redraw a candidate for the `design` skill; content CONFIRM flags; live integration keys; Keystatic; JSON-LD via a sanitiser-approved path; DNS cutover. `npm run lint` is broken independently (eslint-config-next vs ESLint 9 flat-config); `next build` is the gate and is clean.

### Post-review adjustments (operator, same session)

1. **Imagery toned toward the palette.** Desaturation plus a subtle slate/gold soft-light wash so the interim photos sit quieter and read less like stock.
2. **Type changed** — display + body moved from Fraunces + Jost to **Cormorant Garamond + Inter** (the couture register the operator chose from a four-way specimen). This overrides the font line in the "Fixed" stack above, on the operator's call. Display sized up to compensate for Cormorant's lighter weight; `text-wrap: balance` on headlines; wordmark weight raised. `art-direction.md` Type section amended to match. Two-voice (upright = church, italic = the Word) and the illuminated initial are unchanged.

Both verified by render and redeployed. Latest preview in `deployment.md`.
