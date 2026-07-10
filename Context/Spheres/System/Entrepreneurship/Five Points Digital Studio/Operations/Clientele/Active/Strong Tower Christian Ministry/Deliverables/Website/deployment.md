# Strong Tower Christian Ministry — deployment record

First deploy: 2026-06-22. Built from `prd.md`, verified locally (green `next build`, all routes 200), then deployed to the Five Points Vercel team.

## Image-led redesign pass (2026-06-22)

Second deploy, per `redesign-handoff.md`: the visual elevation using `ui-ux-pro-max`. Logo demoted in favour of a typographic Fraunces wordmark; the site made image-led with interim atmospheric photography. Verified locally (green `next build`, 19 routes, screenshots at desktop and mobile) and redeployed as a preview.

- Preview URL: https://strong-tower-christian-ministry-v56ioevbw-studio-fivepoints.vercel.app (latest; supersedes `o3s741k1f`, `msq58j5yu`, `eluzqq8yh`)
- Target: preview (not production); the first deploy's live URL and the church domain are untouched.
- Spacing system pass — formalised an 8-point grid as named tokens (`--space-*`) in `globals.css`; brought the hero rhythm and section internals onto the grid with space proportional to the larger type; section padding now steps down responsively (128 → 80 → 64) and the sub-page hero clearance steps down on mobile.
- Imagery toned toward the palette per operator note — desaturation plus a subtle slate/gold soft-light wash so the photos sit quieter and read less like stock.
- Type changed per operator note — display + body moved from Fraunces + Jost to **Cormorant Garamond + Inter** (the couture register). Display sized up to compensate for Cormorant's lighter weight; `text-wrap: balance` added to headlines for clean wraps; wordmark weight raised. See `art-direction.md` (Type amended 2026-06-23).

What changed:
- New `Wordmark` component (Fraunces "Strong Tower" with a rising tower-and-arcs light glyph) leads in the nav and footer; the logo emblem is removed from the home hero.
- Home hero rebuilt as a full-bleed photographic composition with a legibility scrim; imagery added to the Welcome and Watch bands.
- Interim photography committed under `public/images/`, catalogued and marked for replacement in `public/images/CREDITS.md`.
- Brand colours, content, routes, integrations, stack, accessibility and portability unchanged. Tokens remain the single reskin surface.

Note: `npm run lint` is broken independently of this work — `eslint-config-next` throws a circular-structure error under ESLint 9's flat-config compat layer. `next build` runs clean and is the gate.

## Typography and layout refinement (2026-07-03)

Third design pass, run with the frontend-design skill on operator instruction after reviewing the promoted build. Fonts (Cormorant Garamond + Inter), palette, content and routes unchanged; the pass reworked how type is deployed:

- Tokenised type scale in `globals.css` (`--text-display/h1/h2/h3/h4/scripture/lead` plus `--measure-lead/heading`); all nine sub-page modules swapped from hand-rolled drifting `clamp()` values onto the shared ramp.
- Removed the illuminated drop cap (rendered with a broken first word) and its utility.
- Home welcome band rebalanced: 5/6 grid with a fluid gap, image at 3:4, lead measure capped at 56ch.
- New `.link-arrow` editorial link replaces outlined secondary buttons for tertiary actions; `.btn-secondary` restyled quieter (neutral border, blue on hover).
- Heading voice tightened globally (line-height 1.08, -0.01em, balanced wraps); eyebrow and section-index unified to one label style; container narrowed 1400 → 1280 for a tighter editorial measure; hardcoded spacings normalised onto the `--space-*` grid.

Verified in a local preview at desktop and mobile (clean console), `next build` green, deployed to production. Full URL: https://strong-tower-christian-ministry-1boaesfiy-studio-fivepoints.vercel.app

## Production promotion (2026-07-03)

The image-led redesign (including the Cormorant Garamond + Inter type change and toned imagery) was promoted from preview to production so the public URL serves the redesigned build, ahead of the operator emailing the link to the church. Verified anonymously post-deploy: 200, Wordmark in nav/footer, photographic hero and worship imagery rendering, no `logo.png` in any rendered surface.

## Vercel

- Team: `studio-fivepoints`
- Project: `strong-tower-christian-ministry`
- Deployment id: `dpl_6fPdu4u3zVsR3Zi54NqDT1xrTg1z` (production, 2026-07-03; supersedes `dpl_3xtw5ssWvjst4txf6iD66QzMZt9y`)
- Live URL: https://strong-tower-christian-ministry.vercel.app
- Full URL: https://strong-tower-christian-ministry-9b5zzv6aa-studio-fivepoints.vercel.app
- Inspector: https://vercel.com/studio-fivepoints/strong-tower-christian-ministry
- Auth: deployed with `VERCEL_FIVEPOINTS_TOKEN` (venture env), `--scope studio-fivepoints`. The `.vercel/` link in the codebase is gitignored.

The church domain `strongtowercm.org` is untouched and still served by Wix. No DNS cutover has happened. This Vercel URL is an internal preview on the Five Points subdomain.

## Environment variables to set in Vercel before launch

All optional at build time — the site degrades gracefully without them. Set in the Vercel project settings before go-live:

- `YOUTUBE_API_KEY`, `YOUTUBE_CHANNEL_ID` — live status and sermon auto-pull on /watch
- `RESEND_API_KEY`, `RESEND_FROM`, `CONTACT_TO_EMAIL`, `PRAYER_TO_EMAIL` — contact and prayer forms
- `NEWSLETTER_PROVIDER`, `NEWSLETTER_API_KEY`, `NEWSLETTER_LIST_ID` — newsletter signup
- `NEXT_PUBLIC_GIVING_URL` — giving swap-slot (the church's giving destination)
- `NEXT_PUBLIC_SITE_URL` — set to the final domain for correct metadata and sitemap

## Redeploy

From the codebase directory:

```bash
VERCEL_TOKEN=$VERCEL_FIVEPOINTS_TOKEN vercel deploy --scope studio-fivepoints       # preview
VERCEL_TOKEN=$VERCEL_FIVEPOINTS_TOKEN vercel deploy --prod --scope studio-fivepoints # production
```

## Pending before production cutover

- Brand confirmation and vector logo
- Content CONFIRM flags resolved (see page comments)
- Live integration keys set
- Keystatic CMS layered in
- JSON-LD structured data added via a sanitiser-approved path
- DNS cutover from Wix to Vercel (produce `dns-cutover.md` at that stage)
