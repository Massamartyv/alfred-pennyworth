---
file_type: reference_library_index
scope: venture
venture: Martywood
created: 2026-06-21
last_updated: 2026-06-21
---

# Reference Library – Martywood

A curated corpus of the creators, brands, works and curators that informs research, inspiration and creative direction for Martywood. Alfred draws on this library when a task needs a batch of grounded reference – what is working, what to extract, which canon to draw from – rather than reasoning from a blank page.

This library is isolated to Martywood. It never holds personal references or another venture's references.

## How Alfred uses it

1. A Martywood task calls for inspiration, creative direction or a research batch.
2. Alfred reads this index and matches the task to cards by type, domain and the Pull-for tags.
3. Alfred loads only the matched cards and returns a batch with the formula, the canon and the trend read already surfaced on each card.

Adding an entry is two motions: write the card in the right folder, then add one row to the registry.

## Structure

```
Reference Library/
├── _index.md      – this file: schema, vocabulary, registry
├── Creators/      – individuals: podcasters, newsletter writers, cultural commentators, media founders, photographers, directors
├── Brands/        – media companies, editorial brands, newsletters, podcasts, analogues and competitors
├── Works/         – specific pieces: episodes, editions, albums, films, essays, campaigns, cultural moments
├── Curators/      – tastemaker contexts: editorial communities, scenes, festivals, movements
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
| Lenny Kravitz | creator | music, lifestyle, interior-design, fashion | world-building, materiality, spatial-direction, hospitality, ritual, artist-as-life | canon | [Creators/lenny-kravitz.md](Creators/lenny-kravitz.md) |
| Kanye West | creator | music, fashion, architecture, world-building | world-building, positioning, cross-domain direction, creative-risk framing, single-vision | canon | [Creators/kanye-west.md](Creators/kanye-west.md) |
| Frank Ocean | creator | music, release-strategy, scarcity, long-form-storytelling | proposition, ritual, offer-design, scarcity, cadence, canonical-drop, restraint | canon | [Creators/frank-ocean.md](Creators/frank-ocean.md) |
| Jean-Michel Basquiat | creator | visual-art, street-art, blue-chip-art, cultural-bridge | narrative, high-low, art-direction, cultural-bridge, raw-and-composed, reinvention | canon | [Creators/basquiat.md](Creators/basquiat.md) |
| Bad Bunny | creator | music, cultural-sovereignty, language-refusal, global-scale | positioning, narrative, cultural-sovereignty, refusal-to-translate, restraint, world-building | canon | [Creators/bad-bunny.md](Creators/bad-bunny.md) |

## Card-pending references

Known references with no card yet.

**Creators:** Skylar Marshai, Temi Ibisanmi, Daniel Dalen, Justin Tse, Shema Love, Duke Dennis, Stucci Gus, Alex Nguyen, Cassie Yeung, Giveon

**Brands:** Lust Text (Positype)

---

*Martywood Reference Library. Created 2026-06-21 under the Manor Protocol. Isolated from personal and from other ventures.*
