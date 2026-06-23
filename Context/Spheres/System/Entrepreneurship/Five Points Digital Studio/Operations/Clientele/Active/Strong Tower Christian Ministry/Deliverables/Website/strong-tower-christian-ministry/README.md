# Strong Tower Christian Ministry

Website for Strong Tower Christian Ministry, Florence, South Carolina. Built by Five Points Digital Studio.

Next.js 16 (App Router), TypeScript, CSS Modules with global design tokens. Content is managed in-repo via Keystatic. Built to be portable: every integration is configured through environment variables, and no hosting-provider-specific primitives are used.

## Getting started

```bash
npm install
cp .env.example .env.local   # then fill in the values
npm run dev                  # http://localhost:3000
```

The content editing UI runs at `/keystatic` once the CMS step is wired.

## Environment variables

See `.env.example` for the full list. Summary:

| Variable | Purpose |
|---|---|
| `NEXT_PUBLIC_SITE_URL` | Canonical site URL for metadata and sitemap |
| `YOUTUBE_API_KEY`, `YOUTUBE_CHANNEL_ID` | Live status and automatic sermon pull |
| `RESEND_API_KEY` | Email delivery for forms |
| `CONTACT_TO_EMAIL`, `PRAYER_TO_EMAIL` | Recipients for the contact and prayer forms |
| `NEWSLETTER_PROVIDER`, `NEWSLETTER_API_KEY`, `NEWSLETTER_LIST_ID` | Newsletter signup |
| `NEXT_PUBLIC_GIVING_URL` | The church's giving destination (swap-slot) |

## Scripts

- `npm run dev` — local development
- `npm run build` — production build
- `npm run start` — serve the production build
- `npm run lint` — lint

## Content

All public content lives in `/content` as structured files, edited through Keystatic at `/keystatic`. The files are the source of truth; there is no external database. Service times and contact details are defined once and reused across the site.

## Deployment

Deploys to any Node host. The reference deployment is Vercel. This is standard Next.js with no Vercel-only features, so it can move to Netlify, Cloudflare or a self-managed host without code changes.

## Portability and handover

This codebase is designed to transfer to the church cleanly:

1. Transfer the git repository to the church's GitHub organization.
2. Move the environment variables to the new host (see `.env.example`).
3. Reinstall the Keystatic GitHub app on the transferred repository for in-production editing.
4. Transfer or recreate the deployment (Vercel project transfer, or a fresh deploy on any host).
5. Reverify the Resend sending domain under the church's account.
6. Point the domain at the new deployment.

No content migration is required, because the content lives in the repository.

---

Built by Five Points Digital Studio.
