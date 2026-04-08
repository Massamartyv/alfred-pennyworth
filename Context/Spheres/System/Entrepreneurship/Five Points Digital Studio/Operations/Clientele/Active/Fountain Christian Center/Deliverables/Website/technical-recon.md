---
file_type: technical_recon
client: Fountain Christian Center
venture: Five Points Digital Studio
workflow: Website Development
phase: Reconnaissance
date: 2026-04-08
status: retroactive
---

# Technical Reconnaissance -- Fountain Christian Center

Retroactive audit of existing codebase at `Deliverables/Website/fountain-christian-center/`.

---

## Tech Stack

| Layer | Choice |
|---|---|
| Framework | Next.js 16.2.0 (App Router) |
| Runtime | React 19.2.4 |
| Language | TypeScript 5 (strict mode) |
| Styling | CSS Modules + Global CSS Custom Properties (no Tailwind) |
| Fonts | Cormorant Garamond (headings), Inter (body) via next/font/google |
| External APIs | YouTube Data API v3 (livestream status) |
| CMS | None -- all content hardcoded |
| Deployment | Not configured |

Dependencies are minimal: three production (next, react, react-dom), five devDependencies. No UI libraries, no form libraries, no state management.

---

## Site Architecture

Four pages implemented, two referenced but missing:

| Page | Status | Content |
|---|---|---|
| `/` (Home) | Built | Hero, service times, history and mission, leadership, ministry widgets |
| `/about` | Built | Church legacy (1947 founding), core values, leadership |
| `/ministries` | Built | Four ministry cards with descriptions and CTAs |
| `/contact` | Built (broken) | Contact form (non-functional), service times sidebar, location info |
| `/live` | Missing | Referenced by LiveButton, no route exists |
| `/give` | Missing | Referenced by Navigation, dead link |

One API route: `/api/live-status` -- YouTube livestream check with five-minute cache.

---

## Design System

Earth-tone palette anchored by cream (#F5F0EB) and near-black (#1A1A18). Warm brown accents (#8C7B6B, #C4B5A2). Typography pairing is elegant -- Cormorant Garamond at light weights for headings (all uppercase, wide letter-spacing) with Inter for body. Fluid clamp-based sizing. Section padding at 8rem. Max-width 1400px. Sharp corners throughout (border-radius: 0 to 2px).

The visual identity communicates institutional dignity and warmth. The design decisions are consistent and intentional.

---

## Component Inventory (10 components)

| Component | Type | Purpose |
|---|---|---|
| Navigation | Client | Fixed header with scroll-triggered blur effect, logo, nav links, live button |
| LiveButton | Client | YouTube livestream status polling (five-minute intervals), conditional pulsing indicator |
| AnimatedBackground | Server | Fixed ambient layer -- radial gradient glow with SVG noise grain, 40-second drift animation |
| HeroSection | Server | Parameterised hero -- accepts heading, subtext, quote toggle, images via props |
| ServiceTimes | Server | Four service cards in a grid layout with image placeholder |
| HistoryMission | Server | Church founding narrative, mission statement, stat cards (1947, Brooklyn) |
| Leadership | Server | Four-member staff grid with placeholder portraits |
| Widgets | Server | Two ministry highlight cards (Midday Motivation, Sister to Sister) |
| Footer | Server | Brand tagline, three link columns, embedded filtered Google Maps |
| Contact form | In-page | HTML5 form with inputs but no backend handler |

Server-heavy architecture: only Navigation and LiveButton require client-side hydration.

---

## Critical Gaps

1. **Contact form is non-functional** -- no action attribute, no API route, no client-side submission handler, no feedback to users
2. **Two navigation links are dead** -- `/live` and `/give` pages do not exist
3. **No security headers** -- next.config.ts is empty, missing X-Frame-Options, HSTS, X-Content-Type-Options, Referrer-Policy
4. **No structured data** -- no JSON-LD, no Schema.org markup of any kind
5. **No OpenGraph or social meta tags** -- social shares will show nothing
6. **No sitemap or robots.txt**
7. **Service times duplicated** in ServiceTimes.tsx and contact/page.tsx with no shared data source
8. **All content hardcoded** -- no CMS, no data files, all content lives in component JSX
9. **No environment configuration** -- no .env.example, no deployment configuration
10. **Accessibility gaps** -- no skip-to-content link, no prefers-reduced-motion, missing focus indicators on navigation

---

## Strengths

- Clean, minimal dependency footprint
- Intentional and consistent design system
- Proper semantic HTML (header, nav, section, article, footer)
- Optimised font loading with display: swap
- Server-component heavy architecture -- minimal client-side JavaScript
- Responsive design across all implemented pages
- Well-organised CSS module structure

---

## Client Intelligence

### Leadership (current)

| Name | Title | Key Details |
|---|---|---|
| Bishop Charles D. Locklear, Jr. | Senior Pastor (since 2021) | Husband of JoAnn. Installed as Pastor of Administration in 2008 with his wife. Became Senior Pastor in 2021. |
| Pastor JoAnn Locklear | Senior Associate Pastor | Joined FCC in 1994. Served as Usher, Trustee, Outreach Director, Youth Director (10+ years). Preached initial sermon 1997. Ordained Evangelist 2003. Associate Degree in Christian Ministry and Administration (UCMI). Bachelor of Theology (Family Bible Ministries Worldwide). Mother of three (Chamar, Ebony, Isaiah), nine grandchildren. Known for administrative excellence and youth mentorship. |
| Bishop Sylvester Watts, D.D. | Bishop (retired/founding generation) | Born in Douglas, Georgia. Fifth of seven children. Licensed to preach 1983. Ordained 1984 (United Fellowship Assembly). Installed as Pastor August 1990 (ninth pastor of FCC). Doctor of Divinity 2005. Consecrated Bishop 2006. Led the transformation from Fountain Church of Christ to Fountain Christian Center Inc. Secured 501(c)(3) status in 1997. Married to Vena since 1967. One daughter Cassandra, three grandchildren. |
| Pastor Vena Watts | First Lady / Shepherd Mother | Native of Cheraw, South Carolina. Licensed to preach 2003. Ordained Elder 2006. Installed Associate Pastor of Auxiliaries 2008. Ministers alongside Bishop Watts. Focused on women's ministry and prayer. |
| Elder Alberta Champelle | Elder | Referenced in both codebase and original site copy |

**Note:** The current codebase lists four leaders (Rev. Charles D. Locklear Jr., Bishop Sylvester Watts, Pastor Vena Watts, Elder Alberta Champelle) but misses Pastor JoAnn Locklear entirely. Her bio and role as Senior Associate Pastor must be added.

### Church History

Founded 1947 by Rev. Leon O'Neil at 897 Gates Avenue, Brooklyn, as Fountain Christian Church. Moved to 11 Sumner Avenue (now Marcus Garvey Boulevard) in 1962 with a marching band procession. Nine pastors across 77 years:

1. Rev. Leon O'Neil (founder, 1947)
2. Rev. Jehovah Rice
3. Rev. James T. Reeder
4. Elder Stephen Cooper
5. Elder Willie S. Rouse
6. Rev. Max Berl Graham (joined a diocese, church name changed to Fountain Church of Christ, Disciples of Church in the 1960s)
7. Dr. E.W. Holden (first pastor to hold a doctorate)
8. Elder Clenso Allen (1982 to 1990, departed to pastor Calvary Unified Free Will Baptist Church)
9. Bishop Sylvester Watts (installed August 1990, led for 31 years)

The transition from Watts to Locklear happened through a structured elevation -- Charles and JoAnn Locklear were installed as Pastors of Administration in 2008, and Bishop Charles Locklear became Senior Pastor in 2021.

The heritage section of the website should honour the full pastoral lineage and past contributors (auxiliaries, founders of the Pastor's Aide, Floral Club, Welcome Committee, Usher Boards, Missionary Board, Mother's Board, Bugle Corps, Fountain Masonic Lodge).

### Mission Statement

"To build a strong body of believers by teaching the Word of God, in its simplicity. By teaching the practical application of God's Word, people grow spiritually and help others develop in their Christian walk with God, thus positively affecting their everyday lives."

### Ministry and Department Structure (from membership form)

17 active ministries and departments: Adjutants, Admin Staff, Children's Church, Choir and Musicians, Clergy, Janitorial/Saxton, Kitchen Committee, Media, Prayer (Noon Day/Friday), Sunday School, Trustee Financial, Ushers, Young Adults, Outreach, Special Events, Culinary, None. The current site only surfaces four ministries (Worship Arts, Christian Education, Community Outreach, Prayer and Intercessory). The full structure is significantly deeper.

### Service Schedule (from original site)

| Service | Day | Time |
|---|---|---|
| Sunday Worship | Sunday | Not specified in copy |
| Youth Sunday | Sunday | Not specified |
| Midday Motivation (Noon-day Inspiration and Prayer) | Wednesday | 12:00 PM |
| Bible Study | Wednesday | 7:30 PM |
| Friday Night Prayer Line | Friday | 7:00 to 7:30 PM |

Teleconference access: (646) 558-8656, Meeting Code: 792-998-6999, Pass Code: 030923

### Existing Content Not Yet on New Site

- **Bishop's Gala** -- annual celebration event at Russo's on the Bay (ticketed, $160 adults, $85 children)
- **Sister to Sister** -- women's ministry sessions (co-ed discussions on trauma, mental health, church community)
- **Monthly Partnership Seed** -- recurring giving programme ($28, $38, $48 or $58/month), separate from tithes
- **Tithes section** -- Malachi 3:8-12 KJV as the anchor text, with a donation amount input
- **Membership form** -- comprehensive intake with children info, ministry participation multi-select, volunteer willingness
- **The Bishop's Gala** -- dedicated page on old site, not yet replicated

### Giving and Payment Infrastructure

The church already uses an existing payment processor for donations and tithes. The `/give` page should link to or embed this existing system rather than building a new payment flow. A button that routes to their current processor is sufficient.

---

## Creative Direction (Client Voice)

### The Feeling

"Sunday service choir feel with a modern luxurious energy that is organised and captures the essence of the full history of this Brooklyn-based church and their heritage. It should feel like it is honouring the heritage but not lost in the time period of where they were founded. It should feel modern, clean, but not stiff. Flowy."

### The Hero Vision

A "water fountain Bellagio fountain effect" during the hero section of the homepage. The expressed vision:

- Feel like the **Northern Lights** -- how light behaves
- Still feel **fluid like water**
- Serve as a **guiding light** matching the Sunday service choir energy
- Take inspiration from the **Jesus is King tour** creative direction -- how light plays in an artistic way
- Feel **based in Brooklyn** -- cleanliness and modernity woven into the tapestry of the legacy

This is the most specific creative direction from the client. The current `AnimatedBackground` component (radial gradient glow with grain) is a starting point but does not yet achieve the Bellagio/Northern Lights/JIK light-play ambition. The hero animation needs to evolve.

### Heritage

"The website should have a section for history and dedicate that section to the retired members of the lineage of the administration or leaders of the church. Make sure that section gets the respect and reverence that it deserves and that the valour and the contributions of past ancestors and past contributors of the church community are recognised and appreciated."

---

## Infrastructure Requirements for Production

- Vercel project creation (Five Points team account)
- Domain configuration (client to provide or Five Points to manage)
- YouTube API key and channel ID as environment variables
- Contact form backend: API route with email delivery (Resend, SendGrid or similar)
- Decision on `/live` page: embed YouTube player or continue linking to YouTube directly
- Decision on `/give` page: link to existing payment processor (church already has one)
- Membership form: replicate or link to existing form functionality
- Heritage/history section: dedicated page or expanded section honouring the full pastoral lineage
