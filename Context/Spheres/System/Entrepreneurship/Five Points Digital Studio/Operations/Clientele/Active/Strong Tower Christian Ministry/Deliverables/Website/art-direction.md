---
file_type: art_direction
client: Strong Tower Christian Ministry
venture: Five Points Digital Studio
workflow: Website Development
phase: Direction
date: 2026-06-22
status: locked
---

# Art Direction — Strong Tower Christian Ministry

Locked 2026-06-22 via the art-director method. Direction for a bold front-end restructure of the existing Next.js site. Hands to frontend-design for execution. This is elevation, not a rebrand: brand colours, logo and all content are preserved.

## Concept

**Rising Light, grounded by the Tower.** A strong tower is a refuge; the light rises from it; the Father loves you to life. Rendered in the visual language of Black sacred modernism — so the screen feels the way the room does, and could not be mistaken for a church template.

## Lineage — translation, not mimicry

- **Aaron Douglas / Harlem Renaissance** — concentric radiant bands of light from a single source, silhouettes reaching upward. The logo halo, generalised into a system. (Propose adding to the anti-library.)
- **Ethiopian Orthodox illumination** — gold as a ground rather than an accent, the processional cross, blue-and-gold sacred geometry. An African-Christian lineage, the opposite of generic. (Propose adding to the anti-library.)
- **Kanye Sunday Service** (compass) — contemporary proof that Black gospel + light-as-material + restraint is current and powerful.

## References — Five Points anti-library

- **Aman** — light from a source, not from everywhere; warmth held within restraint; whisper, do not announce. The lighting law for the gold.
- **Kinfolk** — frame discipline, negative space as reverence. Take the compositional rigour, not the now-diluted surface warmth.
- **Pentagram** — the editorial register: an "order of service" structure, numbered, confident, quiet weight per section.
- **Pangram Pangram** — type must read commissioned and specific, not sourced from a free font library. The diagnosis of the current generic tell.

## Type — locked

> Amended 2026-06-23: operator reviewed the build and changed the type. Display and body are now Cormorant Garamond + Inter, replacing Fraunces + Jost. The two-voice and illuminated-initial system is unchanged; only the faces moved. Direction below reflects the current lock.

- **Display: Cormorant Garamond** (high-contrast, elegant, refined; the couture register). Replaces Fraunces, which replaced Playfair Display. Sized up versus Fraunces to hold presence, since Cormorant runs lighter and smaller.
- **Body and UI: Inter** — neutral, highly legible at scale, kind to an older congregation. Replaces Jost.
- **Two-voice system:** upright Cormorant is the church speaking; italic Cormorant is the Word (scripture).
- **Illuminated initial** — oversized drop-cap on section openers, the manuscript move.
- Both faces self-hostable via `next/font/google`. Portability preserved.

## The system

- **Light and colour.** Gold becomes luminous light that blooms from a source over deep slate stone; flat gold reserved for actions only. Deepen the slate and navy grounds so the light has dark to break against. Keep the lifted brand palette as the base; add one rare garnet note for scripture moments, under 5%.
- **Motion — "dawn", not fade.** Content resolves as light breaks: a soft gold bloom settles, slow and eased; the hero radiance is concentric gold arcs expanding from behind the tower. All motion yields fully to `prefers-reduced-motion`.
- **Geometry — the ownable signature.** The halo becomes structure: section dividers are arcs of light, not straight rules. The tower silhouette recurs, cropped and architectural, light behind it. A concentric-arc motif as the recurring device.
- **Layout.** Break the symmetry. An editorial order-of-service grid: left-anchored display, numbered sections, generous negative space, scripture interludes between sections like the Word spoken over a gathering.
- **Material.** Eighty-twenty: warm stone and paper as the ground, gold-leaf light as the twenty. Subtle grain on dark sections, a faint arc watermark.
- **Voice and tone.** Warm, dignified, unhurried — Southern Black church warmth meeting editorial restraint. Copy stays; this guides tone only.

## Constraints

- Keep all content, the brand colours, the logo, the routes and the integrations.
- Next.js 16, CSS Modules, centralised tokens in `globals.css`. No Tailwind. Fraunces added via `next/font` only; no other heavy dependencies.
- WCAG AA: large legible body, contrast, visible focus, reduced-motion. Honour the older congregation.
- Portable: no Vercel-only primitives; the token block stays the single reskin surface.
- Restraint over ornament. Gaudiness is the line that is not crossed.

## Scope of the restructure

1. Rework the `globals.css` tokens — the light-and-gold system, garnet, motion tokens — and swap the type to Fraunces display + Jost body via `next/font`.
2. Introduce shared primitives: an Arc/halo divider, a Tower motif, a ScriptureInterlude band, an illuminated section-opener, and a "dawn" reveal replacing the fade reveal.
3. Rebuild the home page to the order-of-service editorial grid with dawn motion and arc geometry.
4. Propagate to the sub-pages through the shared chrome and the `global-page-hero` system.
5. Keep it green: `next build` passes, then redeploy the preview.

## Acceptance

- The site no longer reads as a template: distinctive type, dawn motion, arc geometry, asymmetric editorial layout.
- Brand colours, logo and content preserved; tokens remain the single reskin surface.
- WCAG AA holds, reduced-motion respected, build green, preview redeployed.
