# ⚡️ Vibe Coding PRD Template

> **What is this?** A Product Requirements Document designed specifically for *Vibe Coding* (AI-assisted web development). It prioritizes universal layout constraints, environmental tech stack rules, and the "vibe" as the core prompting directives for LLMs, minimizing hallucinations and anchoring the development inside your specific design language.

---

## 1. Project Grounding & Objective
*The 10,000-foot view. This sets the initial context for the AI agent before it writes any code.*
- **Project Name:** `[Project Name]`
- **Client/Brand:** `[Client Name]`
- **Primary Objective:** `[One clear sentence on what this site must achieve, e.g., "A high-conversion landing page for a boutique architectural firm."]`

## 2. The Vision & "The Vibe" (Aesthetic Thesis)
*Instead of just hex codes, we define the aesthetic constraints and physical "feeling" of the site. This is crucial to guarantee a premium output.*

- **Core Feeling / Atmosphere:** `[e.g., "Moody, highbrow, seductive, but highly functional."]`
- **The Tension:** `[What two contrasting ideas balance the site? e.g., "Raw brutalist structure (concrete aesthetics, sharp grids) filled with warm textures (soft lighting, rounded organic corners)."]`
- **Animation & Interaction Philosophy:** `[e.g., "Smooth, deliberate. No bouncy or jarring animations. Interactions should feel heavy and expensive, rewarding the user's curiosity rather than demanding it."]`
- **Visual References:**
  - `[Inspiration URL 1]` - *What we like: [e.g., typography scaling & spacing]*
  - `[Inspiration URL 2]` - *What we like: [e.g., scroll-triggered reveal animations]*

## 3. Global Architecture & The Stack
*The non-negotiable technical boundaries. If the AI doesn't have this, it will guess and hallucinate varying tech stacks.*

- **Core Framework:** `[e.g., Next.js App Router (React), Vite + Vanilla JS, Astro]`
- **Styling Architecture:** `[e.g., Vanilla CSS with heavily structured standard design tokens. strictly NO Tailwind CSS.]`
- **Animation/Interaction Engine:** `[e.g., Framer Motion, GSAP, or pure CSS transitions]`
- **Data & Content Architecture:** `[e.g., Static markdown files, Sanity CMS, Hardcoded json]`

## 4. Universal Engineering Mandates
*Rules the AI must adhere to on every single file or component it generates.*

- **Layout & Structure Rules:**
  - `[e.g., "Always use semantic HTML5 tags (<article>, <section>, <main>)."]`
  - `[e.g., "Implement a global CSS Grid system based on 12-columns. Maximum container width of 1440px. Use fluid typography scales (clamp)."]`
  - `[e.g., "The spacer scale: adhere rigidly to a 4pt/8pt spacing system globally."]`
- **Responsive Strategy:** 
  - `[e.g., "Mobile-first approach. Ensure touch targets are at least 44x44px. Custom breakpoints at 768px and 1024px."]`
- **Component Design System:**
  - `[e.g., "Keep components small, isolated, and strictly follow the Single Responsibility Principle. Pass data via clear props."]`

## 5. Scope & Mechanics (The Map)
*The concrete deliverables.*

**Sitemap / Core Pages:**
1. **`/` (Home)**
   - *Goal:* `[Drive to consultation form]`
   - *Key Sections:* `[Hero (heavy animation), Services Grid, Social Proof, Footer]`
2. **`/about` (Story)**
   - *Goal:* `[Build extreme trust through storytelling]`
   - *Key Sections:* `[Founding Thesis, The Team, The Process]`
3. **`/[slug]` (Dynamic Content/Portfolio)**
   - *Goal:* `[Showcase individual works]`

## 6. Performance & SEO Requirements
*The invisible pillars that make the site professional.*

- **SEO Rules:** `[e.g., "Every page must have a dynamic <title>, comprehensive metadata, and complete OpenGraph tags. Strictly one <h1> per page."]`
- **Performance Budget:** `[e.g., "Images must be heavily optimized WebP formats. Target a 95+ Lighthouse score. Lazy load components below the fold."]`
- **Accessibility (A11y):** `[e.g., "All interactive elements require focus states. Contrast ratios must meet WCAG AA standards. Screen reader support is mandatory."]`

## 7. AI "Mega-Prompt" Injection
*Copy and paste this synthesized section at the start of every new Vibe Coding session for this project to prime your AI.*

> **SYSTEM PROMPT INJECTION:**
> "You are an elite, design-obsessed engineer building `[Project Name]`. You will strictly use `[Tech Stack/Framework]`. Your output must feel `[Core Feeling]`. Prioritize premium `[Styling choice, e.g., Vanilla CSS]` over utility classes. Maintain the aesthetic tension between `[Tension Element 1]` and `[Tension Element 2]`. Do not assume any brand assets yet, but build the architectural shell and global padding/margins to feel unbelievably expensive and intentionally sparse. Adhere strictly to a `[Spacing rule, e.g., 8pt grid]`."
