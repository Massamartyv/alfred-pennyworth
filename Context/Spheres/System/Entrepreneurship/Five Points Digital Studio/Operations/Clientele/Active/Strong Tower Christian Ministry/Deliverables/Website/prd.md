---
file_type: vibe_coding_prd
client: Strong Tower Christian Ministry
venture: Five Points Digital Studio
workflow: Website Development
phase: Direction
date: 2026-06-22
status: draft
tier: TBD
---

# Vibe Coding PRD – Strong Tower Christian Ministry

A full rebuild of `strongtowercm.org`, replacing a dated Wix property with a fast, dignified, self-editable Next.js site. Built portable from the first commit so ownership can transfer to the church cleanly if they buy it.

This PRD is written to function as a single build prompt. Section 8 is the mega-prompt; sections 1 through 7 are the specification it draws on; sections 9 through 11 govern content, portability and acceptance.

---

## 1. Project Grounding and Objective

- **Project Name:** Strong Tower Christian Ministry Website
- **Client:** Strong Tower Christian Ministry, Florence, South Carolina
- **Primary Objective:** A warm, modern digital home for a Spirit-filled, prophetic church – inviting the newcomer, serving the member, and connecting both to worship in-person and online, with content the staff can maintain themselves.

The current site is a stale Wix build. The rebuild must feel current and alive without losing the church's warmth, and must be maintainable by non-technical staff and portable enough to hand over without friction.

---

## 2. The Vision and "The Vibe" (Aesthetic Thesis)

> The brand expression below is conceptual. The church owns a logo, colours and fonts. Section 4 now carries tokens lifted from the live logo and site CSS on 2026-06-22, pending the operator's confirmation; they are replaced wholesale at brand lock without touching components.

- **Core Feeling / Atmosphere:** Refuge and rising. The steadiness of a strong tower – shelter, safety, something solid to run to – meeting the living warmth of "He Loves You to Life." Spirit-filled and contemporary. Dignified but never stiff. Black church excellence that feels of the present moment, not the past.

- **The Tension:** Fortress and light. A grounded, sheltering base against luminous, breaking light – the prophetic, the glory, the sense of life arriving. Heavy foundation, upward lift.

- **Animation and Interaction Philosophy:** Confident and warm, never gimmicky. Content rises gently into place on scroll (a short, eased upward fade). Light breathes slowly in the hero. Nothing bounces, nothing demands. Critically, the congregation skews older: motion is subtle, fully governed by `prefers-reduced-motion`, type runs large, contrast runs high, and touch targets are generous.

- **Scriptural anchor:** Proverbs 18:10, "The name of the LORD is a strong tower; the righteous run to it and are safe." The architecture of refuge should be felt, not quoted to death.

- **Visual References:** to be confirmed with the operator at brand lock. Reference points worth pulling from: contemporary megachurch sites that balance warmth and polish, editorial spacing, and confident type at scale.

---

## 3. Global Architecture and the Stack

Mirrors the Five Points house church-site stack (see Fountain Christian Center) with one deliberate addition: an in-repo CMS, because the client chose staff self-editing.

- **Core Framework:** Next.js 16.2.0 App Router (React 19.2.4, TypeScript 5 strict)
- **Styling Architecture:** CSS Modules per component with global CSS Custom Properties (design tokens). No Tailwind. No CSS-in-JS. Vanilla CSS with intentional constraints.
- **Animation Engine:** Pure CSS transitions and keyframes. No Framer Motion. No GSAP.
- **Icons:** lucide-react
- **Fonts:** via `next/font/google` (or self-hosted at brand lock), `display: swap`
- **Content / CMS:** Keystatic in git-based mode. Content lives as MDX, JSON and YAML files inside the repo at `/content`. Editing UI at `/keystatic`. This is the one deviation from the Fountain build, which hardcoded content. See Section 9.
- **Forms / Email:** Resend via server actions (contact and prayer request)
- **Live and sermons:** YouTube Data API v3 (live status plus automatic latest-video pull)
- **Newsletter:** provider-agnostic capture behind an environment variable (see Section 10)
- **Build governance:** include `AGENTS.md` carrying the Next 16 warning ("This is NOT the Next.js you know – read `node_modules/next/dist/docs/` before writing code") and a `CLAUDE.md` that references it, per house convention.

---

## 4. Universal Engineering Mandates

### Layout and Structure
- Semantic HTML5 throughout: `<header>`, `<nav>`, `<main>`, `<section>`, `<article>`, `<footer>`
- Max container width: 1400px via `--max-width`
- Section padding: generous vertical rhythm via `--spacing-section` (target 8rem desktop, reduced on mobile)
- Container inline padding: 2rem via `--spacing-container`
- Fluid typography using `clamp()`; base body size larger than default for legibility
- One `<h1>` per page, logical heading hierarchy throughout

### Responsive Strategy
- Mobile-first. Primary breakpoint 768px, secondary 1024px
- Touch targets minimum 44 by 44 pixels
- Single-column mobile layouts, reduced section padding

### Component Design System
- Each component is a paired `.tsx` and `.module.css` file
- Server components by default; client components only where state or browser APIs are required
- Components isolated, no shared CSS module imports between components
- All public content read from `/content` at build time; no content hardcoded in JSX

### Colour Tokens — LIFTED from logo 2026-06-22, pending confirmation

Read off the live logo: a slate-blue tower, a gold cross and halo, a near-black wordmark on white. The palette maps onto the fortress-and-light thesis exactly – blue is the tower, gold is the light. Names stay; values are fine-tuned at confirmation. This table is the entire reskin surface.

| Token | Value | Usage |
|---|---|---|
| `--bg-field` | #FBFAF8 | Page background (warm white) |
| `--bg-fortress` | #1C2A3F | Deep slate-navy – dark sections, footer, nav on scroll |
| `--bg-accent` | #EEF1F6 | Soft blue-grey accent backgrounds |
| `--brand-blue` | #5E7EA8 | Tower blue – primary brand |
| `--brand-blue-deep` | #3C5A86 | Deeper tower blue |
| `--brand-blue-light` | #9DB2CE | Light tower blue |
| `--accent-gold` | #C6A24E | Gold – cross and halo, the light; CTAs, highlights |
| `--accent-gold-light` | #DCC27A | Lighter gold |
| `--accent-gold-deep` | #A8842E | Deeper gold |
| `--text-main` | #1A1A1A | Primary body text |
| `--text-inverse` | #F7F5F0 | Text on dark backgrounds |
| `--text-muted` | #5F6B7A | Secondary slate text |
| `--border-subtle` | rgba(28,42,63,0.10) | Subtle dividers |
| `--border-medium` | rgba(28,42,63,0.18) | Medium borders |

The hex values are eyeball reads from the logo; fine-tune at confirmation.

### Typography — LIFTED from live site 2026-06-22, pending confirmation

The live site runs Futura Light, Didot Italic and Avenir Light – a deliberate geometric-sans-with-elegant-italic pairing. Translated to a free, self-hostable stack that preserves that identity:
- Display and accent (their Didot italic): Playfair Display, italic for scripture and script moments
- Structural and body (their Futura / Avenir light): Jost, sized up for an older readership
- If legibility testing flags Jost at small sizes, swap body to Inter while keeping Jost for structure

---

## 5. Scope and Mechanics (The Map)

Sitemap. Eleven routes. Lean v1 can collapse `/watch` to absorb live, and fold `/prayer` into `/contact`, if the operator wants fewer pages.

1. **`/` (Home)** – Hero with tagline and service times, who-we-are, latest sermon (auto-pulled), a Plan Your Visit pull, a giving call, location with map, newsletter capture.
2. **`/about`** – Story, mission and vision (verbatim copy already in hand), leadership pull.
3. **`/what-we-believe`** – Confession of Faith and Sonship, both drafted by Five Points for pastoral approval. The doctrinal home of the site.
4. **`/leadership`** – Pastor Kelsey M. Goodson and Prophetess Angela Goodson, structured to accept more leaders.
5. **`/watch`** – Live embed when the channel is streaming; otherwise the latest sermon plus an archive grid, pulled automatically from YouTube.
6. **`/events`** ("What's Happening @ The Tower") – Upcoming events, managed in the CMS.
7. **`/visit`** (Plan Your Visit) – What to expect, service times, directions, "what should I wear / bring the kids" warmth for first-timers.
8. **`/get-involved`** – Ministries, groups and ways to serve. Public, no login. Replaces the empty Wix Groups and unused Members area.
9. **`/give`** – Giving section wired as a single swap-slot (Section 10). Graceful placeholder until the church selects a processor.
10. **`/prayer`** – Private prayer-request form routed to the church by email. A distinctive that fits a prophetic ministry.
11. **`/contact`** – Contact form, phone, email, embedded map.

Global elements:
- **Navigation** – fixed header, scroll blur, logo, links, a Live indicator that appears when streaming.
- **Footer** – tagline, link columns, service times, address, socials, newsletter capture.
- **Newsletter** – capture component in the footer and inline on Home and Visit.

---

## 6. Performance and SEO Requirements

### Performance Budget
- Lighthouse 90+ on Performance, Best Practices, SEO and Accessibility for key pages
- LCP under 2.5s, CLS under 0.1, INP under 200ms
- Images: WebP, responsive `srcset`, lazy below the fold, priority above it
- Static generation for all content pages; dynamic only for live status and form actions

### SEO
- Dynamic `<title>` and meta description per page
- Complete OpenGraph and Twitter Card tags per page
- JSON-LD: `Church` (Organization), `LocalBusiness` (NAP for Florence local SEO), `Event` (services), `BreadcrumbList`
- Auto-generated `sitemap.ts` and `robots.ts`, canonical URLs

### Accessibility (load-bearing for this congregation)
- WCAG 2.1 AA: contrast 4.5:1 body, 3:1 large
- Skip-to-content link, visible focus indicators everywhere
- `prefers-reduced-motion` disables ambient and scroll motion
- Labelled inputs, ARIA error states on forms
- Meaningful alt text on every image
- Comfortably large base type

### Security (house standard, via `next.config.ts`)
- `X-Frame-Options: DENY`, `X-Content-Type-Options: nosniff`, `Referrer-Policy: strict-origin-when-cross-origin`
- `Strict-Transport-Security: max-age=63072000; includeSubDomains; preload`
- `X-DNS-Prefetch-Control: on`, `Permissions-Policy: camera=(), microphone=(), geolocation=()`

---

## 7. Integrations

| Integration | Mechanism | Env var(s) | Portability note |
|---|---|---|---|
| Live status | `/api/live-status` polling YouTube Data API v3, ~5 min cache | `YOUTUBE_API_KEY`, `YOUTUBE_CHANNEL_ID` | Standard fetch, host-agnostic |
| Sermon auto-pull | Build-time / ISR fetch of latest channel uploads | same as above | No manual upkeep |
| Contact form | Server action to Resend | `RESEND_API_KEY`, `CONTACT_TO_EMAIL` | Swap key/recipient on handover |
| Prayer request | Server action to Resend, private recipient | `RESEND_API_KEY`, `PRAYER_TO_EMAIL` | Same |
| Newsletter | Provider-agnostic POST (default Resend Audiences) | `NEWSLETTER_PROVIDER`, `NEWSLETTER_API_KEY`, `NEWSLETTER_LIST_ID` | Provider swappable without code change |
| Giving | Button/embed reading one URL | `STRONG_TOWER_GIVING_URL` | Placeholder-safe; one-line swap |
| Map | Embedded Google Maps iframe, branded filter | none | Static |

YouTube channel handle is `@strongtowerchristianminist4397`; resolve to a channel ID during the build.

---

## 8. AI Mega-Prompt Injection

> **SYSTEM PROMPT INJECTION:**
> "You are an elite, design-obsessed engineer building the Strong Tower Christian Ministry website. Use Next.js 16 App Router with TypeScript strict mode and CSS Modules with global CSS Custom Properties — read `node_modules/next/dist/docs/` before writing code, as Next 16 has breaking changes. Your output must feel like refuge and rising: the steadiness of a strong tower meeting the living warmth of 'He Loves You to Life.' Spirit-filled, contemporary, dignified, never stiff. Hold the tension between fortress and light — a grounded sheltering base against luminous breaking light. All public content is read from `/content` via Keystatic; hardcode nothing. Prioritise vanilla CSS with structured design tokens over utility classes. The colour and type tokens in Section 4 are lifted from the church's live brand and centralised in one global file so the entire site reskins by editing that file alone. This congregation skews older: large type, high contrast, generous touch targets, and all motion governed by `prefers-reduced-motion`. Animations are subtle and ambient — content rises gently on scroll, light breathes in the hero, nothing bounces, nothing demands. Adhere to a 1400px max-width, 8rem section rhythm, semantic HTML5, one `<h1>` per page, the house security headers, JSON-LD for a church and local business, an auto-generated sitemap and robots file, and WCAG 2.1 AA throughout. Build every third-party dependency behind an environment variable so the site is fully portable and can be handed to the client without a rewrite. Ship `.env.example` documenting every variable, plus `AGENTS.md` and `CLAUDE.md` per house convention."

---

## 9. Content and CMS Architecture

The portability principle: content lives in the repository, never in an external database. Keystatic is an editing skin over in-repo files; the files are the source of truth.

- **Storage:** `/content` as MDX, JSON and YAML, committed to the repo
- **Admin UI:** `/keystatic`, git-based mode
- **Editing host:** local mode for build and internal edits now; GitHub mode for staff self-serve in production (the only external piece is a Keystatic GitHub app installed on the repo, which travels with the repo on transfer)
- **Singletons:** Site Settings (service times, address, phone, email, socials, taglines, giving URL), Home, About, What We Believe (Confession of Faith plus Sonship), Visit, Give
- **Collections:** Events, Leaders, Ministries/Groups, Sermons (optional manual features layered over the YouTube auto-pull)
- **Single source of truth:** service times and NAP defined once in Site Settings and consumed everywhere. No duplication (a defect noted in the Fountain build).

---

## 10. Portability and Handover

The controlling requirement: moving this from Five Points infrastructure to the church's must be a checklist, not a rebuild.

- **Content** in-repo via Keystatic, so there is no CMS database to export or migrate.
- **Every integration behind an env var** (Section 7). Handover swaps accounts, not code.
- **No Vercel-proprietary primitives.** No Vercel KV, Postgres, Blob or Edge Config. Standard Next.js that redeploys to Netlify, Cloudflare or any Node host.
- **Static-first.** Only live status and form actions are dynamic; everything else is statically generated.
- **Giving as a swap-slot.** One environment value; placeholder-safe until set.

**Handover package (produced at the Release phase):**
1. Transfer the git repo to the church's GitHub organisation
2. Reinstall the Keystatic GitHub app on the transferred repo
3. Hand over env vars via a secure channel; document in `.env.example`
4. Transfer the Vercel project to the church's Vercel team, or redeploy fresh on their host
5. Reverify the Resend sending domain under the church's account
6. `dns-cutover.md` runbook for pointing `strongtowercm.org` at the new deployment

---

## 11. Acceptance Criteria

The build is done when:

- [ ] All routes build and render; no dead links anywhere
- [ ] Lighthouse 90+ on Performance, Best Practices, SEO and Accessibility on Home, About, Watch and Contact
- [ ] Contact and prayer forms deliver email via Resend with visible success and error states
- [ ] The Live indicator appears when the YouTube channel is streaming and is hidden otherwise
- [ ] `/watch` shows the newest channel videos automatically, with no manual step
- [ ] The giving button routes to `STRONG_TOWER_GIVING_URL`, and degrades gracefully when unset
- [ ] Editing a field in `/keystatic` changes the corresponding public page
- [ ] Security headers present; `sitemap.xml` and `robots.txt` served; JSON-LD validates
- [ ] WCAG AA verified: contrast, focus states, skip link, `prefers-reduced-motion`, alt text
- [ ] All brand tokens centralised in one file; swapping them reskins the entire site
- [ ] Runs locally on `npm run dev`; `.env.example` documents every variable
- [ ] No content hardcoded in components; all of it reads from `/content`

---

## Open Inputs (blocking a clean one-shot)

1. **Brand kit** – logo files, exact hex colours, font names. Or authorise lift-and-confirm from the current site.
2. **Confession of Faith and Sonship** – Five Points drafts, pastor approves. Drafting can begin on the operator's word.
3. **Giving processor** – church to select; placeholder holds until then.
4. **Leadership roster** – confirm whether anyone beyond the two Goodsons appears.
