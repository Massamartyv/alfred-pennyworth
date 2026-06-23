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

## Vercel

- Team: `studio-fivepoints`
- Project: `strong-tower-christian-ministry`
- Deployment id: `dpl_3xtw5ssWvjst4txf6iD66QzMZt9y`
- Live URL: https://strong-tower-christian-ministry.vercel.app
- Full URL: https://strong-tower-christian-ministry-pwb61ad1q-studio-fivepoints.vercel.app
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
