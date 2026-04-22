---
file_type: quality_criteria
department: Production
venture: Five Points Digital Studio
methodology: The Manor Protocol
last_updated: 2026-04-08
---

# Technical Quality Rubric

The six non-negotiable criteria that govern all Production output from this studio. Every build is evaluated against all six during the Critique phase. Failure on any single criterion sends the work back to Execution with specific revision notes.

---

## 1. Code Quality

**The question:** Is the code clean, maintainable and faithful to the PRD's engineering mandates?

### Excellent
- Strict TypeScript throughout – no `any` types, no type assertions without justification
- Component architecture follows single responsibility principle
- CSS and styling is systematic – design tokens, consistent naming, no magic numbers
- Semantic HTML5 used correctly throughout
- File structure is predictable and navigable by any engineer
- No dead code, no commented-out blocks, no TODO debris

### Acceptable
- TypeScript is present but has minor type looseness
- Components are generally well-structured but some overreach their scope
- Styling is functional but not fully systematised
- No errors but room for architectural improvement

### Failing
- JavaScript instead of TypeScript, or TypeScript with widespread `any`
- Monolithic components that own too many concerns
- Inline styles, inconsistent naming, magic values
- Non-semantic HTML (div soup)
- Code that another engineer could not navigate without explanation

---

## 2. Performance

**The question:** Does the site load fast and feel fast?

### Excellent
- Lighthouse Performance score 95+
- Largest Contentful Paint under 2.0 seconds
- Cumulative Layout Shift under 0.05
- Interaction to Next Paint under 200 milliseconds
- Images optimised (WebP/AVIF, responsive srcset, lazy loading below fold, priority loading above fold)
- No render-blocking resources
- Bundle size appropriate for site complexity

### Acceptable
- Lighthouse Performance score 80 to 94
- Core Web Vitals within Google's "good" thresholds (LCP under 2.5 seconds, CLS under 0.1, INP under 200 milliseconds)
- Images optimised but may have minor sizing inefficiencies
- No catastrophic performance issues

### Failing
- Lighthouse Performance score below 80
- LCP exceeds 2.5 seconds
- Visible layout shift on page load
- Unoptimised images – full-resolution PNGs, missing width and height, no lazy loading
- JavaScript bundle exceeds reasonable size for site complexity

---

## 3. Accessibility

**The question:** Can everyone use this site?

### Excellent
- WCAG 2.1 AA compliance across all pages
- All interactive elements have visible focus states
- Colour contrast ratios meet AA minimums (4.5:1 normal text, 3:1 large text)
- Full keyboard navigation works logically through all interactive elements
- Screen reader announcement order matches visual layout
- All images have meaningful alt text – not "image" or a filename
- `prefers-reduced-motion` respected – animations degrade gracefully
- Form inputs have associated labels, error states are announced
- Skip navigation link present

### Acceptable
- WCAG AA compliance on primary user paths
- Focus states present on most interactive elements
- Colour contrast passes on primary content
- Basic keyboard navigation works
- Alt text present on most images

### Failing
- Colour contrast failures on primary content
- No focus states on interactive elements
- Images without alt text
- Forms without labels or error handling
- Keyboard traps or unreachable interactive elements
- Animations that cannot be disabled

---

## 4. SEO Completeness

**The question:** Will search engines and AI agents understand and surface this site?

### Excellent
- Dynamic `<title>` and `<meta description>` per page
- Complete OpenGraph and Twitter Card tags
- Canonical URLs on every page
- One `<h1>` per page with logical heading hierarchy
- JSON-LD structured data (LocalBusiness, Service, FAQPage, BreadcrumbList as applicable)
- Auto-generated XML sitemap
- Properly configured robots.txt
- Agentic Engine Optimisation: content structured for AI agent comprehension – FAQ schema, service area schema, comprehensive `knowsAbout` arrays

### Acceptable
- Title and meta description present on all pages
- Basic OpenGraph tags present
- Heading hierarchy is logical
- Sitemap and robots.txt present
- Some structured data

### Failing
- Missing or duplicate titles across pages
- No meta descriptions
- Multiple `<h1>` tags per page or illogical heading order
- No structured data
- No sitemap or robots.txt
- OpenGraph tags missing – social shares look broken

---

## 5. Security

**The question:** Is the site hardened against common threats?

### Excellent
- All security headers present (X-Frame-Options, X-Content-Type-Options, Referrer-Policy, Strict-Transport-Security) – matching the starter template's `next.config.ts` pattern
- No secrets in source code – all credentials in Vercel environment variables
- HTTPS enforced with HSTS
- Content Security Policy configured if applicable
- Input validation on all forms
- Rate limiting on form submissions if server-side
- No mixed content

### Acceptable
- Core security headers present (HSTS, X-Frame-Options)
- No secrets in source code
- HTTPS active
- Basic input validation

### Failing
- Missing security headers
- Secrets or API keys in source code or client-side bundles
- HTTP available without redirect
- No input validation on forms
- Mixed content warnings

---

## 6. Responsiveness

**The question:** Does the site work beautifully at every viewport?

### Excellent
- Flawless at mobile (375px), tablet (768px) and desktop (1280px+)
- Touch targets minimum 44 by 44 pixels on mobile (48 by 48 preferred)
- No horizontal scroll at any viewport
- Typography scales fluidly (clamp-based)
- Images swap to appropriate crops and sizes per viewport
- Navigation adapts appropriately – drawer or hamburger on mobile, full navigation on desktop
- Parallax and heavy animations disabled or simplified on mobile for performance

### Acceptable
- Functional at all three breakpoints
- Minor layout adjustments needed but nothing broken
- Touch targets mostly adequate
- No content is inaccessible on mobile

### Failing
- Broken layout at any standard viewport
- Horizontal scroll on mobile
- Touch targets too small to use
- Content that is hidden or inaccessible at mobile viewport
- Desktop-only features with no mobile fallback

---

## Applying the Rubric

### Scoring

Each criterion is evaluated as **Excellent**, **Acceptable** or **Failing**.

- **All Excellent:** Release with confidence.
- **Mix of Excellent and Acceptable:** Release if no criterion is Failing. Flag Acceptable areas for future improvement.
- **Any Failing:** Return to Execution. Specific revision notes required for each Failing criterion. Do not release.

### Context sensitivity

The bar adjusts by project tier, not by convenience:

- **Rapid Site Build (Silver):** Performance 80+ acceptable. Core structured data. Core accessibility.
- **Custom Website Build (Gold):** Performance 90+ target. Full structured data. WCAG AA complete.
- **Digital Platform Build (Platinum):** Performance 95+ target. Full AEO. WCAG AA with AAA aspirations on key paths.

### The QA Engineer's responsibility

The QA Engineer does not fix. The QA Engineer evaluates. When work is returned to Execution, the revision notes must be specific:

- **Not:** "Performance needs improvement."
- **Instead:** "LCP is 3.2 seconds on mobile – the hero image is 2.4 MB unoptimised. Serve WebP with width 1920 maximum, enable priority loading, add explicit width and height to prevent CLS."

Vague critique produces vague revision. Precise critique produces excellent work.
