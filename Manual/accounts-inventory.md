# Accounts Inventory – Every Account the System Touches

**Purpose:** rebuild reference for the operating system. Pairs with `genesis.md` as the authoritative account map for a clean restore. **Last verified:** 2026-06-11.

**Rule:** credentials never appear in this file. Passwords, tokens, and API keys live exclusively in the password manager. This file holds names, routing rules, and procedures only.

---

## Email Routing Rules (authoritative)

| Address | Scope | Purpose |
|---|---|---|
| martavious@ fivepoints.studio | Business – owner-direct | Primary business identity, client-facing direct contact |
| hello@ fivepoints.studio | Business – general / admin | General inbound, admin logins where no purpose-specific address applies |
| systems@ fivepoints.studio | Business – dev tooling | GitHub, Vercel, Supabase, Stripe, and all technical platform registrations |
| opportunities@ fivepoints.studio | Business – press / vendors / hiring | Press inquiries, vendor relationships, hiring platforms |
| finance@ fivepoints.studio | Business – financial | Banking, financial platforms, payment processors |
| martavious.spicer@icloud.com | Personal – primary | Meaningful personal accounts; default account recovery for personal scope |
| martavious.spicer@gmail.com | Personal – disposable | Retail accounts, coupons, low-signal signups only |

**Recovery default:** iCloud for personal; business recovery routes to the owning business address unless the provider requires a secondary, in which case hello@ is the fallback.

---

## Account Table

| Service | Scope | Owning email | Purpose | Recovery route |
|---|---|---|---|---|
| Apple ID | Personal | martavious.spicer@icloud.com | iCloud Drive, TCC permissions, App Store, Apple ecosystem root | Recovery key escrowed in password manager |
| Anthropic / Claude | Personal | confirm | Claude Code CLI, Claude desktop app, API key powering the Catalogue app didactic panel | confirm |
| GitHub – Massamartyv | Personal | confirm | Personal and system repos: alfred-pennyworth, alfred-vault, catalogue, nextjs-starter template | iCloud (recovery codes in password manager – confirm present) |
| GitHub – studio-fivepoints | Business | systems@fivepoints.studio | Client repos for Five Points Digital Studio | systems@ (recovery codes in password manager – confirm present) |
| Vercel – personal | Personal | confirm | Massamartyv account; Headquarters team; personal project deployments; account slug: lavender-stingray | confirm |
| Vercel – Five Points | Business | systems@fivepoints.studio | systems-9970 account; studio-fivepoints team; all Five Points client deployments | systems@ |
| Notion – personal workspace | Personal | martavious.spicer@icloud.com | Life operations source of truth: Tasks, Projects, Sphere Manager, Finance Manager, Content Calendar, all personal databases | iCloud |
| Notion – Five Points workspace | Business | confirm | Venture source of truth: Five Points tasks, projects, decision log, sphere manager, client records | confirm |
| Google Workspace fivepoints.studio | Business | hello@fivepoints.studio (admin login) | Five inboxes + Drive, Calendar, Analytics, Search Console; also the GCP project hosting the fivepoints-mail service account and Gmail API | hello@ |
| Supabase – personal | Personal | confirm | Personal project databases and infrastructure | confirm |
| Supabase – Five Points | Business | systems@fivepoints.studio | Five Points project databases and infrastructure | systems@ |
| Stripe – Five Points | Business | finance@fivepoints.studio | Payments and offer architecture (Priestley ATM); note: NO personal Stripe account exists – all Stripe operations are business-scoped by rule | finance@ |
| Instantly | Business | confirm | Outbound lead-generation campaigns for Five Points new-business pipeline | confirm |
| Zernio – personal pipeline | Personal | confirm | Social syndication via Pennyone: Instagram, Threads, TikTok connected as massamartyv | confirm |
| Zernio – Five Points pipeline | Business | confirm | Social syndication via Pennyone: Instagram connected as studio.fivepoints | confirm |
| Strava | Personal | martavious.spicer@icloud.com | Fitness activity data; developer app registered for strava MCP API access (callback domain: localhost) | iCloud |
| Fullscript | Personal | martavious.spicer@icloud.com | Practitioner supplement ordering; OAuth app registered for fullscript MCP | iCloud |
| Discord developer | Personal | confirm | Discord bot token powering the discord-setup MCP | confirm |
| ElevenLabs | Personal | confirm | Podcast voice production for Marty Gras audio content | confirm |
| Perplexity Pro | Shared – research layer | confirm | Cited, current intelligence: SEO research, competitive analysis, industry trends | confirm |
| Apify – personal | Personal | confirm | Scraping and web automation; personal token scoped to personal projects | confirm |
| Apify – Five Points | Business | confirm | Scraping and web automation; Five Points token scoped to business projects | confirm |
| Substack – Epiphany newsletter | Personal / Marty Gras | confirm | Epiphany newsletter publication; primary Marty Gras written distribution channel | confirm |
| Domain registrar – fivepoints.studio | Business | confirm registrar and owning email | DNS and domain registration for fivepoints.studio | confirm |

---

## Maintenance

Review this table on every account creation or closure. Do not let drift accumulate between events.

The quarterly restore drill (`restore-drill.md`) explicitly validates this list as part of its scope – any row marked "confirm" that has not been resolved is a drill failure. Resolve confirms during the drill or immediately before it.

---

*Last updated: 2026-06-11*
