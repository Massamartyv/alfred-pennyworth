---
file_type: vibe_coding_prd
client: Fountain Christian Center
venture: Five Points Digital Studio
workflow: Website Development
phase: Direction
date: 2026-04-08
status: retroactive
tier: Custom
---

# Vibe Coding PRD – Fountain Christian Center

Retroactive PRD documenting the design decisions already made and establishing the specification for any further work on this site.

---

## 1. Project Grounding and Objective

- **Project Name:** Fountain Christian Center Website
- **Client:** Fountain Christian Center, Brooklyn, New York
- **Primary Objective:** A dignified, warm digital home for a historic Brooklyn church – communicating legacy, inviting community, and connecting congregants to worship experiences both in-person and online.

The church was founded in 1947. The site must carry that weight of history without feeling dated. It should feel like walking into a well-maintained sanctuary – not a startup landing page.

---

## 2. The Vision and "The Vibe" (Aesthetic Thesis)

- **Core Feeling / Atmosphere:** Reverent but alive. Warm, grounded, unhurried. The spiritual equivalent of afternoon light through stained glass onto dark wood. Not clinical. Not trendy. Timeless.

- **The Tension:** Institutional dignity (the weight of a 77-year-old Black church) balanced with contemporary craft (modern typography, clean spacing, ambient motion). The site should feel like it was built by someone who respects both tradition and design.

- **Animation and Interaction Philosophy:** Subtle and ambient. The animated background provides living texture (a slow-drifting radial glow with grain overlay) without competing for attention. Page hero sections fade in gently (1.2 seconds). Navigation responds to scroll with a soft blur transition. Nothing bounces. Nothing demands. The site breathes.

- **Visual References:**
  - The existing palette, internally named "Sunday Service," draws from earth tones: cream, warm browns, near-black. Think aged paper, dark leather pews, morning light.
  - Typography pairing of Cormorant Garamond (light weight, uppercase, wide-tracked) and Inter (clean sans-serif body) establishes a Pentagram-adjacent editorial sensibility applied to a sacred context.

---

## 3. Global Architecture and the Stack

- **Core Framework:** Next.js 16.2.0 App Router (React 19.2.4, TypeScript 5 strict)
- **Styling Architecture:** CSS Modules per component with global CSS Custom Properties (design tokens). No Tailwind. No CSS-in-JS. Vanilla CSS with intentional constraints.
- **Animation and Interaction Engine:** Pure CSS transitions and keyframe animations. No Framer Motion. No GSAP. Animations are ambient, not interactive – CSS handles this elegantly.
- **Data and Content Architecture:** Currently hardcoded in component files. No CMS. Future consideration: Notion as headless CMS for leadership bios, service times and ministry descriptions to enable client self-service.

---

## 4. Universal Engineering Mandates

### Layout and Structure Rules
- Semantic HTML5 throughout: `<header>`, `<nav>`, `<main>`, `<section>`, `<article>`, `<footer>`
- Max container width: 1400px (`--max-width`)
- Section padding: 8rem vertical (`--spacing-section`)
- Container inline padding: 2rem (`--spacing-container`)
- Fluid typography using `clamp()` functions
- All headings: Cormorant Garamond, font-weight 300, uppercase, letter-spacing 0.05em minimum
- Body text: Inter, font-weight 400, letter-spacing 0.02em, line-height 1.6
- Border radius: 0 to 2px. Sharp corners throughout. No rounded pill shapes.

### Responsive Strategy
- Primary breakpoint at 768px (navigation and grid collapse)
- Secondary breakpoint at 900px (service times grid)
- Touch targets minimum 44 by 44 pixels
- Mobile: single-column layouts, reduced section padding

### Component Design System
- Each component is a paired `.tsx` and `.module.css` file
- Server components by default. Client components only when state or browser APIs are required.
- Props used for customisation (HeroSection is parameterised). Data hardcoded within components when static.
- Components are isolated – no shared CSS module imports between components

### Colour Tokens

| Token | Value | Usage |
|---|---|---|
| `--bg-primary` | #F5F0EB | Page background (cream) |
| `--bg-dark` | #1A1A18 | Dark sections, navigation on scroll |
| `--bg-accent` | #C4B5A2 | Accent backgrounds |
| `--accent-warm` | #8C7B6B | Warm brown borders, highlights |
| `--accent-highlight` | #D4C5B0 | Lighter accent |
| `--text-main` | #1A1A18 | Primary body text |
| `--text-inverse` | #F5F0EB | Text on dark backgrounds |
| `--text-muted` | #7A7267 | Secondary text |
| `--border-subtle` | rgba(26, 26, 24, 0.08) | Subtle dividers |
| `--border-medium` | rgba(26, 26, 24, 0.15) | Medium borders |

---

## 5. Scope and Mechanics

### Sitemap

**1. `/` (Home)**
- Goal: Immediate warmth and invitation. Communicate identity, service schedule and spiritual personality within a single scroll.
- Key Sections:
  - Hero (full-height, animated background, mission statement in Cormorant Garamond, quote mark decoration)
  - Service Times (four-card grid: Sunday Worship, Youth Sunday, Midday Motivation, Bible Study)
  - History and Mission (founding narrative, 1947 stat card, Brooklyn stat card)
  - Leadership (four-member staff grid with portrait placeholders)
  - Ministry Widgets (Midday Motivation, Sister to Sister – two highlighted programmes)

**2. `/about` (Our Story)**
- Goal: Depth of legacy. Tell the founding story without overwhelming.
- Key Sections:
  - Page hero (dark background, badge with pulse indicator, page title in Cormorant Garamond)
  - Core values grid (4 values in a two-column layout)
  - Leadership section (reused from homepage)

**3. `/ministries` (Ministries)**
- Goal: Present the church's four ministries with enough detail to invite participation.
- Key Sections:
  - Page hero with contextual badge
  - Four ministry article cards (Worship Arts, Christian Education, Community Outreach, Prayer and Intercessory Ministry)
  - Each card: heading, description, CTA link

**4. `/contact` (Contact Us)**
- Goal: Make it easy to reach the church and find it physically.
- Key Sections:
  - Page hero
  - Two-column layout: contact form (left) + service times and location sidebar (right)
  - Form fields: name, email, phone, subject (select), message
  - Map embed (Google Maps, grayscale filtered)

**5. `/live` (Watch Live) – NOT YET BUILT**
- Goal: Connect congregants to the livestream experience.
- Decision needed: embed YouTube player directly or link out to YouTube channel

**6. `/give` (Give) – NOT YET BUILT**
- Goal: Enable online giving.
- Decision needed: external giving platform (Tithe.ly, Pushpay) or embedded widget

---

## 6. Performance and SEO Requirements

### Performance Budget
- Lighthouse Performance: 90+ (Custom tier target)
- LCP under 2.5 seconds
- CLS under 0.1
- INP under 200 milliseconds
- Images: WebP format, responsive srcset, lazy loading below fold, priority loading above fold
- Fonts: display: swap (already implemented)

### SEO Rules
- Dynamic `<title>` per page (partially implemented – ministries has custom title, about and contact inherit root)
- Meta description per page
- One `<h1>` per page with logical heading hierarchy
- Complete OpenGraph and Twitter Card tags per page
- JSON-LD structured data: Church (Organization), LocalBusiness, Event (service times), BreadcrumbList
- Auto-generated XML sitemap via sitemap.ts
- Configured robots.txt
- Canonical URLs

### Accessibility
- WCAG 2.1 AA compliance
- Skip-to-content link
- Visible focus indicators on all interactive elements
- Colour contrast meeting AA minimums (4.5:1 normal, 3:1 large)
- `prefers-reduced-motion` support – disable ambient animations
- Form labels with associated inputs, ARIA error states
- Meaningful alt text on all images

---

## 7. AI Mega-Prompt Injection

> **SYSTEM PROMPT INJECTION:**
> "You are an elite, design-obsessed engineer building the Fountain Christian Center website. You will strictly use Next.js 16 App Router with TypeScript strict mode and CSS Modules with global CSS Custom Properties. Your output must feel reverent, warm and unhurried – like afternoon light through stained glass onto dark wood. Prioritise vanilla CSS with structured design tokens over utility classes. Maintain the aesthetic tension between institutional dignity (the weight of a 77-year-old Black church) and contemporary craft (modern typography, clean spacing, ambient motion). All headings use Cormorant Garamond at weight 300, uppercase, with wide letter-spacing. Body text uses Inter. The colour palette is earth-toned: cream (#F5F0EB), near-black (#1A1A18), warm browns (#8C7B6B, #C4B5A2). Adhere strictly to 8rem section padding, 1400px max-width, and semantic HTML5. Every animation must be subtle and ambient – nothing bounces, nothing demands. The site breathes."
