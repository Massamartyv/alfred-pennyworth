---
file_type: reference_library_index
scope: venture
venture: Five Points Digital Studio
created: 2026-06-21
last_updated: 2026-06-21
---

# Reference Library – Five Points Digital Studio

A curated corpus of the creators, brands, works and curators that informs research, inspiration and creative direction for Five Points Digital Studio. Alfred draws on this library when a task needs a batch of grounded reference – what is working, what to extract, which canon to draw from – rather than reasoning from a blank page.

This library is isolated to Five Points Digital Studio. It never holds personal references or another venture's references.

## How Alfred uses it

1. A Five Points task calls for inspiration, creative direction or a research batch.
2. Alfred reads this index and matches the task to cards by type, domain and the Pull-for tags.
3. Alfred loads only the matched cards and returns a batch with the formula, the canon and the trend read already surfaced on each card.

Adding an entry is two motions: write the card in the right folder, then add one row to the registry.

## Structure

```
Reference Library/
├── _index.md      – this file: schema, vocabulary, registry
├── Creators/      – individuals: designers, strategists, copywriters, agency founders, digital practitioners
├── Brands/        – agencies, studios, competitors, analogues and client-category brands worth tracking
├── Works/         – specific pieces: campaigns, case studies, product launches, digital experiences, decks
├── Curators/      – tastemaker contexts: industry publications, award bodies, editorial communities, scenes
└── Anti-References/ – references held up as boundaries, what to define against
```

## Card schema

One markdown file per entity. Frontmatter is the queryable layer. The body carries the judgement.

```
---
name: <kebab-slug>                 # matches the filename
type: creator | brand | work | curator
domains: [music, film, fashion]    # free taxonomy, lowercase
spheres: [Music Production]           # the spheres this relates to
tags: [restraint, genre-defiance]  # retrieval handles, lowercase kebab
status: canon | active | watch | defunct | card-pending
links: []                          # optional URLs
added: YYYY-MM-DD
---
```

Libraries may add optional lowercase frontmatter fields for venture-specific retrieval, documented in that index – Lillie and Lynette uses `constellation` to tag a card to a pillar.

Body sections, in order:

- **Who** or **What** – one line that identifies the entity and its place in the canon. Use **Who** for a person or house, **What** for a work or place.
- **Why aligned** – the thesis. Why it earns a place. For an anti-reference, why it marks the boundary.
- **The extraction** – what to take and reuse. The section label adapts to the type:

  | Type | Section label |
  |---|---|
  | creator | The formula |
  | brand | The proposition |
  | work | Why it lands |
  | curator | The filter |

- **Canon** – the landmark works, moments or products that anchor the reference.
- **Pull for** – the task tags that should summon this card.
- **Trend read** – how it relates to what is working now. Dated when time-sensitive. Marked "pending enrichment" when the source carries no current signal – never invented.

## Pull-for vocabulary

A controlled tag set keeps retrieval consistent. Extend it deliberately, not casually.

- **Voice and story** – voice-and-tone, narrative, naming, world-building, editorial
- **Visual and space** – visual-direction, art-direction, typography, photography, color-and-light, materiality, spatial-direction
- **Sound** – sound-design, cadence
- **Strategy and offer** – positioning, proposition, offer-design, merchandising, hospitality, ritual
- **Posture** – restraint, maximalism, reinvention, high-low, anti-logo

## Status values

- **canon** – a locked, load-bearing reference
- **active** – in current use
- **watch** – tracking; identity or currency unconfirmed
- **defunct** – no longer operating; retained as a historical filter
- **card-pending** – a known reference held as a registry row until it earns a full card

## Registry

Full cards, grouped by type. A card link means a file exists.

### Creators

| Entity | Type | Domains | Pull for | Status | Card |
|---|---|---|---|---|---|
| Alex Hormozi | creator | entrepreneurship, offer design, sales methodology, pricing philosophy | offer-design, positioning, pricing decisions, sales-page copy, Human Construct tier positioning | canon | [Creators/alex-hormozi.md](Creators/alex-hormozi.md) |

### Brands

| Entity | Type | Domains | Pull for | Status | Card |
|---|---|---|---|---|---|
| Pentagram | brand | graphic design, branding, architecture, editorial design | positioning, photography, art-direction, partnership-model, editorial-register | canon | [Brands/pentagram.md](Brands/pentagram.md) |
| Rolls-Royce | brand | luxury automotive, bespoke manufacturing, commissioning culture | positioning, offer-design, commissioning-document language, photography, video-grading, Marque Principle | canon | [Brands/rolls-royce.md](Brands/rolls-royce.md) |
| Ferrari | brand | luxury automotive, artisanal manufacturing, archival photography, video grading | positioning, offer-design, photography, video-grading, Marque Principle, style-arbiter | canon | [Brands/ferrari.md](Brands/ferrari.md) |
| Kinfolk | brand | editorial photography, lifestyle publishing, slow design | photography, art-direction, negative-space composition, editorial layout | canon | [Brands/kinfolk.md](Brands/kinfolk.md) |
| Cereal Magazine | brand | editorial photography, travel publishing, material photography | photography, art-direction, collateral-photography, material-documentation | canon | [Brands/cereal-magazine.md](Brands/cereal-magazine.md) |
| Monocle | brand | editorial photography, journalism, people-at-work imagery | photography, art-direction, people-photography, thought-leadership-content | canon | [Brands/monocle.md](Brands/monocle.md) |
| Aman | brand | ultra-luxury hospitality, editorial photography, monogram design | photography, warmth-register decisions, mark-creative-brief, brand-altitude | canon | [Brands/aman.md](Brands/aman.md) |
| Aesop | brand | luxury skincare, minimalist retail, editorial design, wordmark design | editorial-register decisions, wordmark design, copy tone, quality-gate, restraint decisions | canon | [Brands/aesop.md](Brands/aesop.md) |
| A Friend Of Mine | brand | graphic design, brand identity, collateral production, editorial design | collateral-production, document-standards, physical-craft, colour-application, editorial-spreads | canon | [Brands/a-friend-of-mine.md](Brands/a-friend-of-mine.md) |
| Pangram Pangram | brand | type foundry, graphic design, editorial typography | typography, brand-system, typographic-hierarchy, font-licensing, web-implementation | canon | [Brands/pangram-pangram.md](Brands/pangram-pangram.md) |

## Card-pending references

Known references with no card yet.

**Creators:** Daniel Priestley, Michael Singer

**Brands:** Bottega Veneta, Hermès, Vitsoe, Road and Track, Automobile Quarterly, Car Magazine

**Curators:** Concours d'Elegance

---

*Five Points Digital Studio Reference Library. Created 2026-06-21 under the Manor Protocol. Isolated from personal and from other ventures.*
