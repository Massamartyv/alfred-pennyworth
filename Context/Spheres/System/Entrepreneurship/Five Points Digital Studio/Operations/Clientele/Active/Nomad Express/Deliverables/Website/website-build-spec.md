# ⚡️ Vibe Coding PRD: NOMAD EXPRESS LLC

> **What is this?** A Product Requirements Document designed specifically for *Vibe Coding* (AI-assisted web development). It prioritizes universal layout constraints, environmental tech stack rules, and the "vibe" as the core prompting directives for LLMs, minimizing hallucinations and anchoring the development inside your specific design language.

---

## 1. Project Grounding & Objective
*The 10,000-foot view. This sets the initial context for the AI agent before it writes any code.*
- **Project Name:** Nomad Express Website and Brand Overhaul
- **Client/Brand:** Shaka Boyce, Owner – NOMAD EXPRESS LLC
- **Primary Objective:** Build a conversion-optimized website that elevates Nomad Express from a commodity trucking perception to an elite event logistics and specialty freight authority.

## 2. The Vision & "The Vibe" (Aesthetic Thesis)
*Instead of just hex codes, we define the aesthetic constraints and physical "feeling" of the site. This is crucial to guarantee a premium output.*

- **Core Feeling / Atmosphere:** Confident without arrogance. Professional without being corporate. The voice of someone who has been to seven Super Bowls and does not need to shout about it – the work speaks. Dark, moody, high-impact.
- **The Tension:** The grit and reliability of interstate freight trucking balanced against the polished, high-stakes exclusivity of the world's biggest entertainment stages (Super Bowl, WrestleMania, FIFA). 
- **Animation & Interaction Philosophy:** Smooth, heavy, and purposeful. Subdued animations (like slow horizontal scrolling for the credibility bar and clean number counters) that emphasize authority over flashiness. No bouncy or jarring interactions.
- **Visual References:**
  - *Primary Theme:* Dark overlays masking high-stakes event staging photography.
  - *Color Palette:* Nomad Indigo (#4B5580), action-driven Nomad Ember (#B53A2D) for CTAs, grounded with Nomad Black (#1A1B2E).

## 3. Global Architecture & The Stack
*The non-negotiable technical boundaries. If the AI doesn't have this, it will guess and hallucinate varying tech stacks.*

- **Core Framework:** Next.js 14+ (App Router)
- **Styling Architecture:** Tailwind CSS (Five Points Digital standard)
- **Animation/Interaction Engine:** Framer Motion (page transitions, counters, smooth scroll)
- **Data & Content Architecture:** Hardcoded / Static markdown files for V1. Forms handled via React Hook Form + Resend. Server-Side Rendering (SSR) for heavy SEO benefits.

## 4. Universal Engineering Mandates
*Rules the AI must adhere to on every single file or component it generates.*

- **Layout & Structure Rules:**
  - Use bold geometric sans-serif (e.g., Aktiv Grotesk, Inter) for impact statements (ALL CAPS for massive impact, title case for section headers).
  - Clean, readable sans-serif at 16-18px for body text.
  - Implement a 12-column grid layout, making heavy use of dark sections (Nomad Black) juxtaposed with earthy breathing room (Nomad Cloud / Nomad Sand).
- **Responsive Strategy:** 
  - Mobile-first approach is highly critical. Freight is an urgent industry; the "Get a Quote" and Phone Number must be persistently accessible on touch screens.
- **Component Design System:**
  - Standardize Tailwind utility groupings.
  - Form fields must be built for rapid, multi-step progression.

## 5. Scope & Mechanics (The Map)
*The concrete deliverables.*

**Sitemap / Core Pages:**
1. **`/` (Home) - Primary Conversion Engine**
   - *Goal:* Establish elite authority in 3 seconds & drive to the quote form.
   - *Key Sections:* Full-bleed event hero, Scrolling Credibility Bar (Typography only), 3-Tier Services Overview, Animated "By the Numbers", Portfolio Preview, Final CTA.
2. **`/services` (What We Move)**
   - *Goal:* Detail the value ladder and equipment specs.
   - *Key Sections:* Event/Entertainment (Crown Jewel), Expedited/Time-Critical, General Freight, Equipment Specs (International MV/Reefer info).
3. **`/portfolio` (Where We Have Been)**
   - *Goal:* Visual proof of the resume.
   - *Key Sections:* Filterable Photo Grid (Sports, Broadcast, Specialty), Optional Event Timeline.
4. **`/about` (The Story)**
   - *Goal:* Establish the founder's resume and institutional trust.
   - *Key Sections:* Shaka's Growth Story, 3 Core Values, FMCSA Credentials Data Dump.
5. **`/contact` (Get a Quote)**
   - *Goal:* Capture leads instantly.
   - *Key Sections:* 3-Step Quote Form (Shipment > Freight > Contact), Direct contact info.

## 6. Performance & SEO Requirements
*The invisible pillars that make the site professional.*

- **SEO Rules:** Target local/niche queries ("Freight company near me", "event logistics DC"). Every page requires dynamic `<title>` and OpenGraph tags.
- **Performance Budget:** 
  - Lighthouse score: 95+ across all categories.
  - First Contentful Paint: < 1.5s.
  - Largest Contentful Paint: < 2.5s.
  - All event photography must utilize Next.js `<Image>` component for WebP optimization and lazy loading.
- **Accessibility (A11y):** Contrast ratios between text and dark overlays must meet strict WCAG AA standards.

## 7. AI "Mega-Prompt" Injection
*Copy and paste this synthesized section at the start of every new Vibe Coding session for this project to prime your AI.*

> **SYSTEM PROMPT INJECTION:**
> "You are an elite, design-obsessed engineer building `Nomad Express LLC`. You will strictly use `Next.js App Router and Tailwind CSS`. Your output must feel `Confident, professional, and dark-themed, acting as the voice of an elite operator who has handled logistics for seven Super Bowls.` Prioritize premium spacing and `Tailwind utilities`. Maintain the aesthetic tension between `raw, blue-collar interstate trucking` and `high-end, exclusive global entertainment events`. Do not use generic commodity language. The layout should lean into a dark base (`#1A1B2E`) with striking semantic typography. Every interaction must feel smooth and trusted—use Framer Motion for subtle, heavy reveals. Keep the primary CTA ('Get a Quote' / Phone Number) persistent and instantly accessible."
