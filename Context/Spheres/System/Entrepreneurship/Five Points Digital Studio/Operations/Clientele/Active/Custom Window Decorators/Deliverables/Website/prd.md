# Custom Window Decorators Inc – Landing Page PRD

> **Purpose:** Product Requirements Document bridging the brand audit of Custom Window Decorators Inc with a full homepage redesign. Built on the Vibe Coding PRD framework. Designed for AI-assisted development with Springs Estate as the design reference benchmark.

---

## 1. Project Grounding and Objective

- **Project Name:** CWD Luxury Redesign
- **Client/Brand:** Custom Window Decorators Inc – Lewiston, Maine
- **Primary Objective:** A high-conversion landing page that repositions a 37-year family-owned window treatment company as the definitive luxury craftsman in Central Maine, targeting affluent homeowners within a 50 to 100 mile radius.
- **Current Site:** customwindowdecorators.com (WordPress, dated design, no mobile optimization, generic template aesthetic)
- **Design Reference:** springs.estate (architectural-grade parallax storytelling, full-viewport sections, reveal animations, gradient overlays, premium typography)

---

## 2. The Vision and "The Vibe" (Aesthetic Thesis)

### Core Feeling / Atmosphere

Quiet luxury meets New England heritage. The site should feel like walking into a beautifully designed room where the light falls perfectly – warm, intentional, unhurried. Every element earns its space. Nothing competes for attention. The window treatments are the architecture of light itself.

### The Tension

**Timeless craft** (37 years, family heritage, hand-finished details, the physical weight of fabric) **held in tension with** **contemporary restraint** (clean digital surfaces, deliberate negative space, modern typography, smooth scroll-driven reveals). The site should feel like a heritage brand that never stopped evolving – not a legacy business that finally "got a website."

### Animation and Interaction Philosophy

Borrowed directly from the Springs Estate playbook: smooth, parallax-driven, scroll-triggered. Animations are gravitational – elements drift into view with the weight and patience of heavy drapery falling into place. No bouncing, no snapping, no eagerness. Interactions reward scrolling with new visual layers. Hover states are subtle shifts in opacity or position, never color explosions. Page transitions dissolve rather than cut. The scroll itself is the primary interaction – the user reveals the story by moving through it.

Specific patterns from Springs Estate to adapt:
- Full-viewport sticky sections that layer over each other via clip-path reveals
- Parallax image scaling (1.2 to 1.0) as elements enter the viewport
- Gradient overlay animations on dark sections (multi-layer blur-fix divs)
- Scroll-snap points for section-level pacing
- Reveal animations with vertical distance (data-reveal="title" pattern)
- Split-screen compositions: image on one half, content on the other, with independent parallax

### Visual References

- **springs.estate/about** – What we are taking: the full-viewport parallax architecture, sticky section layering, clip-path reveal transitions, gradient overlays, split-screen compositions, typographic scale, and the scroll-as-narrative pacing. The way sections dissolve into each other rather than stack.
- **springs.estate (home)** – What we are taking: the hero treatment (background image with overlay text and scroll indicator), the stats/credibility section pattern, the panoramic image section breaks, the contact modal pattern.
- **customwindowdecorators.com** – What we are keeping: the brand identity essence (navy/teal), the family heritage story, the service-area authority, the product breadth. Everything else is being elevated.
- **mcs.maranacook.org** – Palette contribution: the purple-to-plum range provides depth and unexpected sophistication when refined for a luxury context.

---

## 3. Consolidated Color Palette

Two source palettes (CWD and Maranacook) merged through the lens of the Springs Estate warm-neutral luxury energy.

### Design Tokens

```css
:root {
  /* -- Foundation Darks -- */
  --obsidian: #0D1A1C;         /* Primary dark. Deepened from CWD navy #112124. Hero overlays, footer, dark sections. */
  --dusk: #1A2F2A;             /* Secondary dark. Forest-green undertone from Springs Estate #162D24. Navigation, secondary backgrounds. */

  /* -- Signature Brand -- */
  --heirloom-teal: #257885;    /* The bridge. CWD's existing hover teal, promoted to primary brand color. CTAs, links, key accents. */
  --patina: #36ADBF;           /* CWD's original accent teal. Secondary interactive states, highlights, data points. */
  --twilight-plum: #4A2D5E;    /* Maranacook purple, darkened and desaturated. Section accents, gradient endpoints, typographic flourishes. */

  /* -- Warm Neutrals (the Springs Estate energy) -- */
  --linen: #F5EDE0;            /* Primary light background. Warm white derived from Springs #F5E8D1. */
  --sandstone: #E8DFD0;        /* Card backgrounds, alternate sections, subtle separation. */
  --driftwood: #C5B9A8;        /* Borders, dividers, muted elements. */

  /* -- Luxury Accents -- */
  --aged-gold: #B8976A;        /* Premium accent. Badges, highlights, hover states on dark backgrounds. */
  --soft-copper: #C49A6C;      /* Warm metallic complement. Subtle gradients, icon fills. */

  /* -- Functional -- */
  --white: #FFFFFF;
  --rich-black: #0A0A0A;
  --stone: #6B6560;            /* Body text on light backgrounds. Warm gray, never cold. */
  --error: #C44B4B;
  --success: #3B8A7A;

  /* -- Gradients -- */
  --gradient-hero: linear-gradient(180deg, rgba(13, 26, 28, 0.85) 0%, rgba(26, 47, 42, 0.6) 50%, rgba(13, 26, 28, 0.9) 100%);
  --gradient-section: linear-gradient(135deg, var(--obsidian) 0%, var(--twilight-plum) 100%);
  --gradient-warm: linear-gradient(180deg, var(--linen) 0%, var(--sandstone) 100%);
  --gradient-cta: linear-gradient(135deg, var(--heirloom-teal) 0%, var(--patina) 100%);
}
```

### Palette Rationale

| Source | Contributed | Transformed Into | Role |
|---|---|---|---|
| CWD #112124 (navy) | Brand anchor dark | Obsidian #0D1A1C | Deepened 15% for richer contrast against warm neutrals |
| CWD #36adbf (teal) | Brand accent | Patina #36ADBF | Retained as-is – recognizable equity |
| CWD #257885 (hover teal) | Interactive state | Heirloom Teal #257885 | Promoted from hover to primary brand color – more sophisticated than the brighter teal |
| Maranacook #662e80 (purple) | Institutional purple | Twilight Plum #4A2D5E | Darkened 30%, desaturated 20% – kills the "school" read, introduces depth |
| Maranacook #3bb5b5 (teal) | Secondary accent | Merged into Patina | Confirmed the teal as shared DNA between both palettes |
| Springs Estate #F5E8D1 | Warm cream | Linen #F5EDE0 | Slightly cooled to prevent yellowing on screens while keeping warmth |
| Springs Estate #162D24 | Forest green | Dusk #1A2F2A | Lightened marginally – used as secondary dark to prevent monotone |
| New addition | – | Aged Gold #B8976A | Luxury signifier. Bridges warm neutrals and cool teals. The "premium" tell. |

### Color Usage Rules

1. Dark sections (hero, footer, feature blocks) use Obsidian as base with Dusk as gradient endpoint
2. Light sections use Linen as base with Sandstone for cards and alternate rows
3. Heirloom Teal is the only CTA color – never use Patina for primary actions
4. Twilight Plum appears sparingly: gradient accents, decorative borders, typographic details
5. Aged Gold is reserved for premium signifiers: badges, trust indicators, accent borders
6. Body text on Linen uses Stone (#6B6560). Body text on Obsidian uses Linen (#F5EDE0)
7. Never place Patina text on Linen – insufficient contrast. Use Heirloom Teal instead

---

## 4. Global Architecture and the Stack

- **Core Framework:** Next.js 14+ App Router (React 18)
- **Styling Architecture:** Vanilla CSS with structured design tokens in CSS custom properties. No Tailwind. No utility classes. Every class name is semantic and descriptive.
- **Animation/Interaction Engine:** GSAP (GreenSock) with ScrollTrigger for parallax, sticky sections, and reveal animations. Framer Motion for component-level transitions and page transitions. CSS transitions for hover states and micro-interactions.
- **Data and Content Architecture:** Static content hardcoded in JSX for v1. Structured for future Sanity CMS migration (content blocks as isolated components).
- **Image Handling:** Next.js Image component with WebP format, responsive srcset, priority loading for above-fold hero, lazy loading below the fold.
- **Deployment:** Vercel (matching Five Points infrastructure standard)

---

## 5. Universal Engineering Mandates

### Layout and Structure Rules

- Semantic HTML5 throughout: `<header>`, `<main>`, `<section>`, `<article>`, `<footer>`, `<nav>`, `<address>`
- CSS Grid for page-level layout. 12-column system. Max container width: 1440px. Content padding: clamp(1.5rem, 4vw, 6rem)
- 8pt spacing system globally. All margins, paddings, and gaps are multiples of 8px
- Fluid typography using clamp(): minimum at 320px viewport, maximum at 1440px
- Full-viewport sections (min-height: 100svh) for hero and feature blocks – matching Springs Estate's architectural pacing
- Every section gets a semantic ID for scroll-nav targeting and SEO anchor linking

### Typography Scale

```css
:root {
  /* Display -- hero headlines only */
  --text-display: clamp(3.5rem, 8vw, 8rem);

  /* H1 -- page title */
  --text-h1: clamp(2.75rem, 6vw, 5.5rem);

  /* H2 -- section headers */
  --text-h2: clamp(2rem, 4vw, 3.5rem);

  /* H3 -- sub-section headers */
  --text-h3: clamp(1.5rem, 2.5vw, 2rem);

  /* Body large -- feature text, pull quotes */
  --text-body-lg: clamp(1.125rem, 1.5vw, 1.375rem);

  /* Body -- standard paragraphs */
  --text-body: clamp(1rem, 1.2vw, 1.125rem);

  /* Caption -- labels, meta text */
  --text-caption: clamp(0.75rem, 0.9vw, 0.875rem);

  /* Font families */
  --font-display: 'Cormorant Garamond', 'Georgia', serif;
  --font-body: 'DM Sans', 'Helvetica Neue', sans-serif;
  --font-accent: 'Cormorant', serif;
}
```

**Font Rationale:**
- Cormorant Garamond for display/headlines: elegant, high-contrast serif with the refinement of a luxury brand. Not overused in web design. Reads as architectural and timeless.
- DM Sans for body: geometric sans-serif with warmth. Clean without being clinical. Better character than Inter or Roboto. Excellent readability at small sizes.
- Cormorant (without Garamond) for accent elements: italic pull quotes, decorative numbers, section labels.

### Responsive Strategy

- Mobile-first CSS with breakpoints at 640px (sm), 768px (md), 1024px (lg), 1440px (xl)
- Touch targets minimum 48x48px on mobile
- Parallax effects disabled below 768px (performance and usability)
- Full-viewport sticky sections collapse to standard scroll on mobile
- Images swap to portrait-oriented crops on mobile via `<picture>` srcset
- Navigation collapses to slide-in drawer on mobile with full-screen overlay

### Component Design

- Each section is a self-contained component with its own CSS module
- Props define content, not layout – layout is determined by the component
- No component depends on another component's internal structure
- All interactive components have visible focus states (2px solid var(–heirloom-teal) with 2px offset)
- Motion respects `prefers-reduced-motion: reduce` – all parallax and reveals fall back to static

---

## 6. Scope and Mechanics (The Map)

### Page: `/` (Home – Landing Page)

**Goal:** Convert affluent homeowners within 50 to 100 miles of Lewiston into consultation requests. Establish CWD as the premier window treatment authority in Maine.

**Scroll Narrative Arc:** Heritage and Craft > Transformation > Services > Trust > Action

---

### Section 1: Hero (Full Viewport, Sticky)

**Pattern:** Springs Estate intro section – full-bleed background image with gradient overlay, headline reveal, scroll indicator

**Content:**
- Pre-headline (caption): "Lewiston, Maine – Since 1987"
- Headline (display): "The Architecture of Light"
- Sub-headline (body-lg): "Custom window treatments crafted for homes that demand more than a covering"
- CTA: "Schedule Your Consultation" (scroll-link to contact section)
- Scroll indicator: Animated down-arrow with "Explore" label

**Technical:**
- Full-viewport min-height: 100svh
- Background: Hero image with `var(--gradient-hero)` overlay
- Headline reveals with GSAP SplitText, staggered character animation
- Parallax on background image: scale 1.15 to 1.0 on scroll
- Sticky positioning so next section scrolls over it (Springs pattern)

**Image Art Direction:**
- A wide, editorial shot of a luxury living room with floor-to-ceiling windows. Sheer linen drapery filters warm afternoon light across hardwood floors. The room has that quiet, lived-in affluence – not staged, not sterile. Think Architectural Digest editorial, Maine lake house energy. Color grading: warm, slightly desaturated, golden hour. No people. The drapery is the protagonist.

---

### Section 2: Brand Essence (Full Viewport, Split Screen)

**Pattern:** Springs Estate a-about section – clip-path reveal, image left / content right, independent parallax

**Content (right panel, dark background with gradient):**
- Section label (caption, aged-gold): "Our Craft"
- Headline (h2): "37 Years of Transforming Maine Homes"
- Body: "What began as a vertical blind workshop in 1987 has grown into Central Maine's most comprehensive window treatment studio. Founded by Mike Favreau, Custom Window Decorators serves homeowners who understand that the right window treatment does not just dress a room – it defines how light, privacy and atmosphere work together."
- Secondary body: "From motorized solar shades that respond to your phone to hand-sewn drapery that falls with the weight of real craft – every installation carries three decades of expertise."
- Small inset image (bottom right, parallax)

**Technical:**
- Two-column split: image left (50%), content right (50%)
- Left image reveals via clip-path animation (polygon bottom-to-top) on scroll
- Right panel slides in from top via clip-path (polygon top-to-bottom)
- Both panels have independent parallax scales (1.2 to 1.0)
- Dark gradient overlay on right panel: Obsidian to Twilight Plum at 135 degrees

**Image Art Direction – Large (Left Panel):**
- Close-up detail shot of hands adjusting a Roman shade mechanism – the craft moment. Shallow depth of field. The hands are weathered, capable. The fabric is rich, textured. Warm, natural light from the window being dressed. This is the "heritage" image – it says "people make this, not machines." Shot feels editorial, not stock.

**Image Art Direction – Small (Right Inset):**
- A tight crop of layered fabric samples fanning out on a wooden surface. Linen, silk, wool – tactile and warm. Natural light. The palette of the fabrics echoes the site palette: creams, teals, soft golds. Overhead or 45-degree angle. Think materials palette in an architect's studio.

---

### Section 3: Transformation Gallery (Full Viewport, Parallax Background)

**Pattern:** Springs Estate a-overview section – large background image with floating text overlay, scroll-driven opacity and position

**Content:**
- Headline (h2, over image): "Every window tells a different story. We listen to what yours is asking for."
- Body (bottom right, over image): "Your home in Lewiston is not the same as a coastal estate in Portland or a farmhouse in Augusta. We travel up to 100 miles to understand the light, the architecture and the life inside before we recommend a single product."

**Technical:**
- Full-bleed background image, fixed/parallax
- Text overlays animate in from off-screen via translateY with scroll progress
- Text fades out as user scrolls past (opacity tied to scroll position)
- Scroll-snap point at section start

**Image Art Direction:**
- Panoramic interior shot – a dramatic window wall with layered treatments visible: sheers underneath, heavier drapes pulled to the sides, a motorized shade tucked into the valance. The room is expansive. You can see Maine landscape through the windows – trees, maybe a glimpse of water. Late afternoon light creates long shadows. The mood is cinematic. Color grading: warm with deep shadows, almost chiaroscuro. This is the "transformation" image – the before is implied by how dramatic the after looks.

---

### Section 4: Services Grid (Standard Scroll, Light Background)

**Pattern:** Custom – editorial grid with staggered reveals, adapting Springs Estate's photo grid parallax for service cards

**Content:**
Six service cards, each with:

1. **Custom Drapery and Curtains**
   - Icon or small image
   - "Hand-measured, hand-sewn, installed with precision. From sheer linens to blackout silks."

2. **Motorized Window Treatments**
   - "Control light and privacy from your phone. Lutron, Somfy and Hunter Douglas integration."

3. **Shutters and Blinds**
   - "Wood, faux wood and vinyl shutters. Horizontal and vertical blinds for every window profile."

4. **Specialty Shades**
   - "Solar, cellular, Roman, roller and pleated shades. Energy-efficient options for Maine winters."

5. **Valances and Top Treatments**
   - "Swags, cornices and custom valances that frame and finish every window."

6. **Commercial and Stage Curtains**
   - "Auditorium curtains, commercial window treatments and institutional installations."

Each card:
- Staggered reveal animation (GSAP ScrollTrigger, 0.15s delay between cards)
- Parallax on card images (subtle, translateY 15% range)
- On hover: image scales 1.05, shadow deepens, Aged Gold border appears

**Technical:**
- 3-column grid on desktop, 2 on tablet, 1 on mobile
- Linen background with Sandstone cards
- Generous padding: 120px top/bottom on desktop
- Each card links to future service detail page (href defined, page not yet built)

**Image Art Direction (per card):**
1. Drapery – flowing curtain fabric caught in a gentle breeze from an open window. Ethereal, slow-motion feel.
2. Motorized – a shade descending smoothly in a modern kitchen. Clean lines. A phone visible on the counter with the shade app.
3. Shutters – plantation shutters in a sunlit bathroom. Slats partially open, light streaming through in sharp lines.
4. Shades – a cellular shade in a cozy reading nook. Winter light outside. The shade glows warmly from transmitted light.
5. Valances – an ornate swag valance over a dining room window. Formal, rich fabric, tassels. The table below is set for dinner.
6. Commercial – a dramatic stage curtain in deep burgundy, partially open, with stage lights visible. Scale and grandeur.

---

### Section 5: Trust and Authority (Full Viewport, Dark)

**Pattern:** Springs Estate stats/credibility section adapted – large numbers with supporting text, editorial layout

**Content:**
- Section label (caption, aged-gold): "By the Numbers"
- Stats row:
  - "37" – "Years of Continuous Operation"
  - "24+" – "Product Categories"
  - "100" – "Mile Service Radius"
  - "1987" – "Family-Owned Since"
- Testimonial block (if available, placeholder for now):
  - Pull quote in Cormorant italic
  - Attribution with location
- Brand partners / product lines: Hunter Douglas, Lutron, Somfy, Silhouette (logos in muted grayscale, Aged Gold on hover)

**Technical:**
- Obsidian background with subtle Twilight Plum gradient
- Stats animate with GSAP counter (0 to final number) triggered on scroll-in
- Large display numbers in Cormorant Garamond, Aged Gold color
- Supporting text in DM Sans, Linen color
- Partner logos in a single row, grayscale filter, hover reveals color

**Image Art Direction:**
- No primary image in this section. The typography and numbers are the visual. Optionally: a subtle, very low-opacity texture overlay – linen fabric weave pattern at 3 to 5% opacity over the dark background, adding tactile depth without competing.

---

### Section 6: Shop From Home (Split Screen, Light)

**Pattern:** Springs Estate split-screen adapted – image right, content left

**Content:**
- Section label (caption, aged-gold): "The Experience"
- Headline (h2): "Your Home Is Our Showroom"
- Body: "We bring the showroom to you – fabric samples, measurement tools and 37 years of expertise, all in your living room. No high-pressure sales. No guesswork. We use your natural light, your existing decor and your actual windows to recommend treatments that work in your space, not in a fluorescent-lit store."
- Process steps (numbered, minimal):
  1. "Call or request a consultation online"
  2. "We visit your home with curated samples"
  3. "Review options in your actual lighting"
  4. "Receive a no-obligation estimate"
  5. "Professional installation on your schedule"
- CTA: "Book Your Free Home Consultation" (links to contact section)

**Technical:**
- Two-column split: content left (50%), image right (50%)
- Linen background
- Process steps animate in sequentially on scroll (staggered by 0.2s)
- Image parallax: translateY range of 10%, scale 1.1 to 1.0
- CTA button: Heirloom Teal background, Linen text, subtle hover scale (1.02)

**Image Art Direction:**
- A consultant (or just their hands) spreading fabric samples across a homeowner's dining table. The home is clearly upscale – you see crown molding, a quality light fixture, a window in the background. The samples are fanned out beautifully. Two coffee cups visible. The mood is collaborative, intimate, unhurried. Natural light. Shallow depth of field on the fabrics. This is the "white-glove service" image.

---

### Section 7: Service Area (Minimal, Light)

**Pattern:** Custom – map-adjacent section with geographic authority content

**Content:**
- Headline (h3): "Serving Central Maine and Beyond"
- Body: "Based in Lewiston with a working radius of 100 miles, we serve homeowners across Androscoggin, Cumberland, Kennebec, Oxford, Sagadahoc and Lincoln counties. From Portland waterfront condos to Augusta Victorians to lakeside retreats in the Belgrade Lakes – if the project is right, we will be there."
- Cities list (for SEO and AEO): Lewiston, Auburn, Portland, South Portland, Brunswick, Augusta, Waterville, Bangor, Scarborough, Falmouth, Freeport, Bath, Topsham, Gardiner, Belgrade Lakes, Rangeley, Bethel, Norway, Bridgton, Windham, Gorham, Westbrook
- CTA: "Check If We Serve Your Area" (opens contact with pre-filled "service area inquiry")

**Technical:**
- Sandstone background
- Cities rendered as a flowing inline list with en-dash separators, Heirloom Teal color
- Optional: subtle CSS-only map outline of Maine with service radius indicator (decorative, not interactive – avoid Google Maps embed for performance)
- Section doubles as rich geo-content for search engines and AI agents

---

### Section 8: Contact / Consultation CTA (Full Viewport, Dark)

**Pattern:** Springs Estate callback-modal adapted into a full section rather than modal

**Content:**
- Headline (h2): "Let Us Transform Your Space"
- Sub-headline: "Schedule a free in-home consultation or visit our Lewiston showroom"
- Form fields:
  - Full name (required)
  - Email (required)
  - Phone (required)
  - Property type: dropdown (Single-family home, Condo/Apartment, Commercial, Vacation/Second home, Other)
  - Project scope: dropdown (1 to 3 windows, 4 to 10 windows, Full home, Commercial project)
  - Preferred contact method: radio (Phone, Email, Text)
  - Message (textarea, optional)
  - Photo upload (optional, labeled "Share a photo of your windows")
- Submit CTA: "Request My Consultation"
- Below form: direct contact info
  - Phone: (207) 784-4113
  - Email: info@customwindowdecorators.com
  - Address: 1478 Lisbon Street, Lewiston, ME 04240
  - Hours: Monday through Friday, 9 AM to 5 PM. Saturday by appointment.

**Technical:**
- Obsidian background with Dusk gradient
- Form card on Sandstone background (contrast against dark section) with generous padding
- Form validation: client-side with clear error states (var(–error) border + message)
- Submit triggers: email notification to info@customwindowdecorators.com (v1: Formspree or similar; v2: Supabase edge function)
- Contact details styled with `<address>` semantic tag
- Schema.org ContactPoint structured data embedded

---

### Section 9: Footer

**Content:**
- Logo (simplified mark)
- Tagline: "The Architecture of Light – Since 1987"
- Navigation links: Services, About, Gallery, Contact, Privacy Policy
- Social: Facebook link
- Address block with schema markup
- Copyright: 2026 Custom Window Decorators Inc. All rights reserved.
- "Website by Five Points Digital Studio" (linked)

**Technical:**
- Rich Black background
- Compact layout: logo left, links center, contact right on desktop; stacked on mobile
- Minimal animation: fade-in on scroll

---

## 7. Performance and SEO Requirements

### Technical SEO

- Dynamic `<title>` per page: "Custom Window Treatments in Lewiston, Maine | Custom Window Decorators"
- Comprehensive `<meta>` description: "Family-owned since 1987. Custom drapery, motorized shades, shutters and blinds for luxury homes in Central Maine. Free in-home consultations within 100 miles of Lewiston."
- Complete OpenGraph and Twitter Card tags with branded social image
- Strictly one `<h1>` per page
- Canonical URL on every page
- XML sitemap auto-generated
- robots.txt properly configured
- Structured data (JSON-LD): LocalBusiness, Service, FAQPage, BreadcrumbList

### Agentic Engine Optimization (AEO)

AEO ensures AI agents (ChatGPT, Claude, Perplexity, Google AI Overviews) can parse, understand and recommend this business when users ask natural-language questions about window treatments in Maine.

**Implementation:**

1. **Comprehensive JSON-LD Schema Markup:**
```json
{
  "@context": "https://schema.org",
  "@type": "LocalBusiness",
  "name": "Custom Window Decorators Inc",
  "description": "Premium custom window treatments for luxury homes in Central Maine. Family-owned since 1987. Offering custom drapery, motorized shades, shutters, blinds and professional installation within 100 miles of Lewiston, Maine.",
  "foundingDate": "1987",
  "founder": {
    "@type": "Person",
    "name": "Mike Favreau"
  },
  "address": {
    "@type": "PostalAddress",
    "streetAddress": "1478 Lisbon Street",
    "addressLocality": "Lewiston",
    "addressRegion": "ME",
    "postalCode": "04240",
    "addressCountry": "US"
  },
  "geo": {
    "@type": "GeoCoordinates",
    "latitude": "44.1003",
    "longitude": "-70.2148"
  },
  "telephone": "+12077844113",
  "email": "info@customwindowdecorators.com",
  "url": "https://customwindowdecorators.com",
  "openingHoursSpecification": [
    {
      "@type": "OpeningHoursSpecification",
      "dayOfWeek": ["Monday","Tuesday","Wednesday","Thursday","Friday"],
      "opens": "09:00",
      "closes": "17:00"
    },
    {
      "@type": "OpeningHoursSpecification",
      "dayOfWeek": "Saturday",
      "opens": "00:00",
      "closes": "00:00",
      "description": "By appointment only"
    }
  ],
  "areaServed": {
    "@type": "GeoCircle",
    "geoMidpoint": {
      "@type": "GeoCoordinates",
      "latitude": "44.1003",
      "longitude": "-70.2148"
    },
    "geoRadius": "160934"
  },
  "serviceArea": {
    "@type": "AdministrativeArea",
    "name": "Central Maine",
    "containsPlace": [
      {"@type": "City", "name": "Lewiston"},
      {"@type": "City", "name": "Auburn"},
      {"@type": "City", "name": "Portland"},
      {"@type": "City", "name": "Augusta"},
      {"@type": "City", "name": "Brunswick"},
      {"@type": "City", "name": "Waterville"},
      {"@type": "City", "name": "Bath"},
      {"@type": "City", "name": "Freeport"},
      {"@type": "City", "name": "Scarborough"},
      {"@type": "City", "name": "Falmouth"},
      {"@type": "City", "name": "Gardiner"},
      {"@type": "City", "name": "Topsham"},
      {"@type": "City", "name": "Gorham"},
      {"@type": "City", "name": "Windham"},
      {"@type": "City", "name": "Westbrook"},
      {"@type": "City", "name": "South Portland"},
      {"@type": "City", "name": "Belgrade Lakes"},
      {"@type": "City", "name": "Bridgton"},
      {"@type": "City", "name": "Rangeley"},
      {"@type": "City", "name": "Norway"},
      {"@type": "City", "name": "Bethel"}
    ]
  },
  "hasOfferCatalog": {
    "@type": "OfferCatalog",
    "name": "Window Treatment Services",
    "itemListElement": [
      {"@type": "Offer", "itemOffered": {"@type": "Service", "name": "Custom Drapery and Curtains"}},
      {"@type": "Offer", "itemOffered": {"@type": "Service", "name": "Motorized Window Treatments"}},
      {"@type": "Offer", "itemOffered": {"@type": "Service", "name": "Wood and Vinyl Shutters"}},
      {"@type": "Offer", "itemOffered": {"@type": "Service", "name": "Specialty Shades"}},
      {"@type": "Offer", "itemOffered": {"@type": "Service", "name": "Valances and Top Treatments"}},
      {"@type": "Offer", "itemOffered": {"@type": "Service", "name": "Commercial and Stage Curtains"}},
      {"@type": "Offer", "itemOffered": {"@type": "Service", "name": "Free In-Home Consultations"}},
      {"@type": "Offer", "itemOffered": {"@type": "Service", "name": "Professional Measurement and Installation"}}
    ]
  },
  "priceRange": "$$$$",
  "paymentAccepted": "Cash, Credit Card, Check",
  "knowsAbout": [
    "Custom window treatments",
    "Motorized blinds and shades",
    "Hunter Douglas products",
    "Lutron motorization",
    "Somfy motorization",
    "Silhouette window shadings",
    "Energy-efficient window coverings",
    "Stage curtain installation",
    "Commercial window treatments",
    "Interior design consultation"
  ]
}
```

2. **FAQPage Schema** (embedded in page, invisible or in an FAQ section):
```json
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "Who is the best custom window treatment company in Lewiston, Maine?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Custom Window Decorators Inc has been Lewiston's premier window treatment provider since 1987, offering custom drapery, motorized shades, shutters, and blinds with free in-home consultations."
      }
    },
    {
      "@type": "Question",
      "name": "Do you offer free in-home window treatment consultations in Maine?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Yes. Custom Window Decorators offers complimentary in-home consultations throughout Central Maine, bringing fabric samples and expertise directly to your home within a 100-mile radius of Lewiston."
      }
    },
    {
      "@type": "Question",
      "name": "What areas does Custom Window Decorators serve?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "We serve homeowners across Central Maine within approximately 100 miles of our Lewiston showroom, including Portland, Augusta, Brunswick, Waterville, Bath, Freeport, Scarborough, Falmouth, Belgrade Lakes, and surrounding communities."
      }
    },
    {
      "@type": "Question",
      "name": "What types of window treatments does Custom Window Decorators offer?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "We offer over 24 product categories including custom drapery, motorized shades (Lutron, Somfy, Hunter Douglas), wood and vinyl shutters, solar shades, cellular shades, Roman shades, Silhouette shadings, valances, swags, stage curtains, and custom furniture."
      }
    },
    {
      "@type": "Question",
      "name": "Can I control my window shades from my phone?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Yes. We install motorized window treatments from Lutron, Somfy, and Hunter Douglas that can be controlled via smartphone, remote control, or wireless switch, allowing you to adjust light and privacy from anywhere in your home."
      }
    }
  ]
}
```

3. **Content Strategy for AI Discoverability:**
   - Every section contains natural-language sentences that directly answer common queries (not keyword-stuffed, but query-shaped)
   - Service descriptions use the exact phrasing someone would ask an AI: "custom window treatments in Lewiston Maine," "motorized shades Maine," "free window treatment consultation"
   - Geographic content is explicit and comprehensive – AI agents need entity-rich text to make local recommendations
   - The service area section contains all city names in running prose, not hidden in metadata
   - FAQ content is both schema-marked and visible on the page

4. **Entity Optimization:**
   - Business name, address, phone (NAP) consistent across all structured data, visible content, and footer
   - Founder name explicitly mentioned (entity association)
   - Brand partner names (Hunter Douglas, Lutron, Somfy, Silhouette) mentioned in context – AI agents use brand associations for recommendation ranking
   - "Since 1987" and "37 years" appear in multiple contexts – longevity is a primary trust signal for AI recommendations

### Performance Budget

- Target: 95+ Lighthouse Performance score
- All images: WebP format, responsive srcset, explicit width/height to prevent CLS
- Hero image: priority loading. All others: lazy loaded via Next.js Image
- Total page weight target: under 2MB including all images
- First Contentful Paint: under 1.5s
- Largest Contentful Paint: under 2.5s
- Cumulative Layout Shift: under 0.1
- GSAP and ScrollTrigger: loaded asynchronously, non-blocking
- Fonts: self-hosted WOFF2, preloaded, with proper font-display: swap fallbacks

### Accessibility (A11y)

- WCAG AA compliance minimum
- All interactive elements have visible focus states
- Color contrast ratios meet AA standards (verified against the Obsidian/Linen and Linen/Stone combinations)
- All images have descriptive alt text
- Form fields have associated `<label>` elements
- Skip-to-content link at page top
- Reduced-motion media query disables all parallax and scroll animations
- Keyboard-navigable throughout
- Screen reader tested with VoiceOver

---

## 8. ICP Alignment Strategy

### Target Client Profile

- **Demographics:** Homeowner, 35 to 70, household income $150K+, owns property valued at $400K+ in Central Maine
- **Psychographics:** Values quality over price. Invests in their home as a reflection of personal taste. Has worked with contractors, designers, or architects before. Prefers working with established local businesses over big-box alternatives.
- **Behavioral:** Researches online but values in-person service. Will drive to a showroom or pay for a home consultation. Makes deliberate purchasing decisions. Appreciates expertise and guidance without pressure.
- **Geographic:** Primary: Lewiston/Auburn metro. Secondary: Portland metro, Augusta, Brunswick, Bath corridor. Tertiary: lakefront and seasonal properties (Belgrade Lakes, Rangeley, Bridgton)

### How the Design Serves the ICP

| ICP Signal | Design Response |
|---|---|
| Values quality over price | No pricing on the page. Emphasis on craft, materials, heritage. The site itself signals premium through its execution. |
| Invests in home as reflection of taste | Image art direction shows aspirational-but-attainable interiors. Not mansion-level, but clearly refined. |
| Prefers local, established businesses | "Since 1987" and founder story front and center. Service area content emphasizes local knowledge. |
| Researches online | Comprehensive service descriptions, FAQ content, schema markup ensure they find CWD whether searching Google, asking an AI, or browsing. |
| Appreciates expertise without pressure | "Shop From Home" section emphasizes no-obligation, consultative approach. Form is low-friction. |
| Makes deliberate decisions | The scroll narrative is unhurried. No popups, no countdown timers, no urgency tactics. The site respects the buyer's pace. |

---

## 9. AI Mega-Prompt Injection

> **SYSTEM PROMPT INJECTION:**
> "You are an elite, design-obsessed engineer building the CWD Luxury Redesign for Custom Window Decorators Inc of Lewiston, Maine. You will strictly use Next.js 14 App Router with vanilla CSS (structured design tokens in CSS custom properties – no Tailwind, no utility classes). Your output must feel like quiet luxury meets New England heritage – warm, intentional, unhurried. Every element earns its space. Prioritize premium vanilla CSS with semantic class names over any utility framework. Maintain the aesthetic tension between timeless craft (37 years of heritage, the physical weight of fabric, hand-finished details) and contemporary restraint (clean digital surfaces, deliberate negative space, smooth scroll-driven reveals). Use GSAP with ScrollTrigger for parallax, sticky sections, and scroll-triggered reveals. Use Framer Motion for component-level transitions. Animations feel gravitational – heavy, patient, like drapery falling into place. The consolidated color palette anchors on Obsidian (#0D1A1C), Heirloom Teal (#257885), Linen (#F5EDE0), and Aged Gold (#B8976A). Typography pairs Cormorant Garamond (display/headlines) with DM Sans (body). Adhere strictly to an 8pt spacing grid. Full-viewport sections (100svh) for hero and feature blocks. All images use Next.js Image with WebP, responsive srcset, and lazy loading below the fold. Every section must contain natural-language content optimized for both traditional SEO and agentic engine discoverability. Target Lighthouse 95+. WCAG AA minimum. The site should feel like springs.estate rebuilt for a window treatment craftsman in Maine."

---

*Last updated: April 2026*
*Five Points Digital Studio – Client: Custom Window Decorators Inc*
