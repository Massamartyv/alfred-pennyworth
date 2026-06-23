---
file_type: reference_library_index
scope: venture
venture: Lillie and Lynette
created: 2026-06-21
last_updated: 2026-06-21
---

# Reference Library – Lillie and Lynette

A curated corpus of the creators, brands, works and curators that informs research, inspiration and creative direction for Lillie and Lynette. Alfred draws on this library when a task needs a batch of grounded reference – what is working, what to extract, which canon to draw from – rather than reasoning from a blank page.

This library is isolated to Lillie and Lynette. It never holds personal references or another venture's references.

## How Alfred uses it

1. A Lillie and Lynette task calls for inspiration, creative direction or a research batch.
2. Alfred reads this index and matches the task to cards by type, domain and the Pull-for tags.
3. Alfred loads only the matched cards and returns a batch with the formula, the canon and the trend read already surfaced on each card.

Adding an entry is two motions: write the card in the right folder, then add one row to the registry.

## Structure

```
Reference Library/
├── _index.md      – this file: schema, vocabulary, registry
├── Creators/      – individuals: hospitality founders, service designers, interior stylists, photographers, writers
├── Brands/        – hospitality brands, home-service companies, analogues, competitors and aspirational references to draw from or define against
├── Works/         – specific pieces: campaigns, products, editorial spreads, guest experience case studies, publications
├── Curators/      – tastemaker contexts: hospitality publications, editorial buyers, design communities, service movements
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

### Brands

| Entity | Type | Domains | Pull for | Status | Card |
|---|---|---|---|---|---|
| Aman | brand | ultra-luxury-hospitality, resort-design, serenity-led-luxury | positioning, visual-direction, spatial-direction, hospitality, restraint | canon | [Brands/aman.md](Brands/aman.md) |
| Belmond | brand | ultra-luxury-travel, heritage-properties, experiential-hospitality | positioning, narrative, world-building, spatial-direction, hospitality | canon | [Brands/belmond.md](Brands/belmond.md) |
| Flamingo Estate | brand | lifestyle, home-goods, garden-produce, amenity-to-retail | offer-design, merchandising, ritual, materiality, positioning | canon | [Brands/flamingo-estate.md](Brands/flamingo-estate.md) |
| Aesop | brand | luxury-skincare, retail-design, amenity-to-retail, editorial-design | offer-design, ritual, merchandising, materiality, positioning, restraint | canon | [Brands/aesop.md](Brands/aesop.md) |
| Soho Home | brand | hospitality-to-retail, home-goods, hotel-inspired-interiors | offer-design, merchandising, ritual, positioning, narrative | canon | [Brands/soho-home.md](Brands/soho-home.md) |
| The Laundress | brand | premium-home-care, cleaning-products, formulation | offer-design, positioning, merchandising, restraint | canon | [Brands/the-laundress.md](Brands/the-laundress.md) |
| Onefinestay | brand | luxury-home-rental, curated-property-management, premium-short-let | positioning, offer-design, hospitality, ritual | canon | [Brands/onefinestay.md](Brands/onefinestay.md) |
| Wander | brand | luxury-short-let, tech-enabled-hospitality, curated-property-management | offer-design, positioning, hospitality, restraint | canon | [Brands/wander.md](Brands/wander.md) |
| NEAT Method | brand | premium-home-organisation, branded-home-service, scalable-luxury-service | positioning, offer-design, proposition | canon | [Brands/neat-method.md](Brands/neat-method.md) |

### Anti-References

| Entity | Type | Domains | Pull for | Status | Card |
|---|---|---|---|---|---|
| Molly Maid | brand | home-services, residential-cleaning, franchise | positioning, proposition, offer-design, restraint | canon | [Anti-References/molly-maid.md](Anti-References/molly-maid.md) |
| The Cleaning Authority | brand | home-services, residential-cleaning, franchise | positioning, proposition, offer-design, restraint | canon | [Anti-References/the-cleaning-authority.md](Anti-References/the-cleaning-authority.md) |

## Card-pending references

Known references with no card yet.

**Brands:** Frette, Matouk, Koala Eco, Murchison-Hume, Nayara Springs, Rosewood Hotels and Resorts, Blackberry Farm, The Newt, Nines

---

*Lillie and Lynette Reference Library. Created 2026-06-21 under the Manor Protocol. Isolated from personal and from other ventures.*
