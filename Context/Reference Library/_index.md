---
file_type: reference_library_index
scope: personal
created: 2026-06-21
last_updated: 2026-06-21
---

# Reference Library

A curated corpus of the creators, brands, works and curators that inform research, inspiration and creative direction. Alfred draws on this library when a task needs a batch of grounded reference – what is working, what to extract, which canon to draw from – rather than reasoning from a blank page.

This is the personal library. Every venture holds its own isolated Reference Library inside its Knowledge Base. Personal and venture references never share a file.

## How Alfred uses it

1. A task calls for inspiration, creative direction or a research batch.
2. Alfred reads this index and matches the task to cards by type, domain and the Pull-for tags.
3. Alfred loads only the matched cards and returns a batch with the formula, the canon and the trend read already surfaced on each card.

Adding an entry is two motions: write the card in the right folder, then add one row to the registry.

## Structure

```
Reference Library/
├── _index.md      – this file: schema, vocabulary, registry
├── Creators/      – individuals: musicians, directors, designers, chefs, writers, photographers
├── Brands/        – companies, houses, labels, product brands
├── Works/         – specific pieces: albums, films, series, books, buildings, campaigns
├── Curators/      – tastemaker contexts: editorial buyers, galleries, movements, scenes
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
| André 3000 | creator | music, fashion, film | voice-and-tone, reinvention, restraint | canon | [Creators/andre-3000.md](Creators/andre-3000.md) |
| Anthony Bourdain | creator | food, travel, culture | narrative, taste-compass, hospitality, food-culture | canon | [Creators/anthony-bourdain.md](Creators/anthony-bourdain.md) |
| A$AP Rocky | creator | fashion, music | art-direction, high-low, layering direction, oversized-silhouette | canon | [Creators/asap-rocky.md](Creators/asap-rocky.md) |
| Bad Bunny | creator | fashion, music | materiality, color-and-light, colour-confidence, relaxed-silhouette | canon | [Creators/bad-bunny.md](Creators/bad-bunny.md) |
| Beyoncé | creator | music, performance | performance, precision-as-freedom, ancestral-tribute, cadence | canon | [Creators/beyonce.md](Creators/beyonce.md) |
| Colman Domingo | creator | fashion, acting | art-direction, restraint, materiality, statement-with-control | canon | [Creators/colman-domingo.md](Creators/colman-domingo.md) |
| Frank Ocean | creator | music, production, aesthetics | sound-design, voice-and-tone, restraint, nostalgia-as-texture | canon | [Creators/frank-ocean.md](Creators/frank-ocean.md) |
| Jean-Michel Basquiat | creator | visual art | visual-direction, art-direction, rawness, street-to-gallery | canon | [Creators/jean-michel-basquiat.md](Creators/jean-michel-basquiat.md) |
| Kanye West | creator | music, fashion, interior design, production | art-direction, visual-direction, color-and-light, materiality, maximalism | canon | [Creators/kanye-west.md](Creators/kanye-west.md) |
| Kurt Cobain | creator | fashion, music | anti-style, restraint, effortless-nonchalance, fashion | canon | [Creators/kurt-cobain.md](Creators/kurt-cobain.md) |
| Pharrell | creator | fashion, music | art-direction, high-low, playful-eclecticism, accessory direction | canon | [Creators/pharrell.md](Creators/pharrell.md) |
| Pierce and Ward | creator | interior design | spatial-direction, materiality, constrained-maximalism, maximalism | canon | [Creators/pierce-and-ward.md](Creators/pierce-and-ward.md) |
| Quentin Tarantino | creator | film, directing | cinematography, visual-direction, style-as-resistance, maximalism | canon | [Creators/quentin-tarantino.md](Creators/quentin-tarantino.md) |
| Ryan Coogler | creator | film, directing | world-building, art-direction, atmosphere, spatial-direction | canon | [Creators/ryan-coogler.md](Creators/ryan-coogler.md) |
| Travis Scott | creator | music, production, world-building | world-building, sound-design, immersive-atmosphere, narrative | canon | [Creators/travis-scott.md](Creators/travis-scott.md) |
| Tyler, the Creator | creator | music | taste-evolution, reinvention, creative-risk, craft-over-brand | canon | [Creators/tyler-the-creator.md](Creators/tyler-the-creator.md) |
| Virgil Abloh | creator | interior design, fashion, architecture | spatial-direction, art-direction, restraint, negative-space | canon | [Creators/virgil-abloh.md](Creators/virgil-abloh.md) |

### Brands

| Entity | Type | Domains | Pull for | Status | Card |
|---|---|---|---|---|---|
| Aesop | brand | grooming, interior design | design-conscious, ritual, restraint, interior-integration | canon | [Brands/aesop.md](Brands/aesop.md) |
| Aimé Leon Dore | brand | fashion, streetwear | streetwear, high-low, world-building, cultural-credibility | canon | [Brands/aime-leon-dore.md](Brands/aime-leon-dore.md) |
| Buly 1803 | brand | fragrance, grooming | heritage-craft, apothecary, world-building, ritual | canon | [Brands/buly-1803.md](Brands/buly-1803.md) |
| Hermès | brand | fashion, accessories, homeware | investment-luxury, craft-led, cross-category, accessories | canon | [Brands/hermes.md](Brands/hermes.md) |
| Lemaire | brand | fashion | materiality, anti-logo, restraint, quiet-luxury | canon | [Brands/lemaire.md](Brands/lemaire.md) |
| Liverpool FC | brand | sports, identity, culture | tribal-identity, unambiguous-loyalty, cultural-affiliation, world-building | canon | [Brands/liverpool-fc.md](Brands/liverpool-fc.md) |
| Loewe | brand | fashion, leather goods | investment-luxury, craft-led, materiality, artistic-direction | canon | [Brands/loewe.md](Brands/loewe.md) |
| Nayara Springs | brand | travel, hospitality, experiences | five-star-hospitality, pinnacle-standard, experience-design, ritual | canon | [Brands/nayara-springs.md](Brands/nayara-springs.md) |
| Nike | brand | fashion, footwear, athletics | selective-alignment, sub-line-curation, sneaker, high-low | canon | [Brands/nike.md](Brands/nike.md) |
| Ralph Lauren | brand | fashion | americana, quiet-luxury, tiered-curation, logo-avoidance | canon | [Brands/ralph-lauren.md](Brands/ralph-lauren.md) |
| Santa Maria Novella | brand | fragrance, grooming | heritage-craft, apothecary, cross-category, ritual | canon | [Brands/santa-maria-novella.md](Brands/santa-maria-novella.md) |
| Singita | brand | travel, hospitality, conservation | five-star-hospitality, conservation-luxury, sense-of-place, ritual | canon | [Brands/singita.md](Brands/singita.md) |
| Uniqlo | brand | fashion | foundation-fashion, quality-basics, anti-logo, restraint | canon | [Brands/uniqlo.md](Brands/uniqlo.md) |

### Works

| Entity | Type | Domains | Pull for | Status | Card |
|---|---|---|---|---|---|
| Astroworld | work | music | sound-design, world-building, immersive-atmosphere, ear-candy | canon | [Works/astroworld.md](Works/astroworld.md) |
| Breaking Bad | work | television | narrative, character-study, long-form-structure, pride-and-hubris | canon | [Works/breaking-bad.md](Works/breaking-bad.md) |
| Django Unchained | work | film | narrative, genre-inversion, style-as-resistance, power-and-identity | canon | [Works/django-unchained.md](Works/django-unchained.md) |
| Everything Everywhere All at Once | work | film | narrative, tonal-range, formal-experimentation, emotional-honesty | canon | [Works/everything-everywhere-all-at-once.md](Works/everything-everywhere-all-at-once.md) |
| Good Will Hunting | work | film | narrative, emotional-suppression, cost-of-greatness, mentor-dynamics | canon | [Works/good-will-hunting.md](Works/good-will-hunting.md) |
| Homegoing | work | literature | narrative, structure-as-argument, diaspora, historical-weight | canon | [Works/homegoing-yaa-gyasi.md](Works/homegoing-yaa-gyasi.md) |
| My Beautiful Dark Twisted Fantasy | work | music | sound-design, world-building, maximalism, ambition-as-form | canon | [Works/my-beautiful-dark-twisted-fantasy.md](Works/my-beautiful-dark-twisted-fantasy.md) |
| Naruto: Shippuden | work | animation, television | narrative, world-building, found-family, perseverance-and-identity | canon | [Works/naruto-shippuden.md](Works/naruto-shippuden.md) |
| One Piece | work | animation | narrative, world-building, long-form-structure, found-family | canon | [Works/one-piece.md](Works/one-piece.md) |
| Renaissance | work | music | sound-design, Black-joy, house-culture, precision-as-freedom | canon | [Works/renaissance-beyonce.md](Works/renaissance-beyonce.md) |
| Scarface | work | film | narrative, ambition-and-hubris, cost-of-the-climb, dramatic-inevitability | canon | [Works/scarface.md](Works/scarface.md) |
| Selena | work | film | narrative, cultural-identity, crossover-ambition, legacy | canon | [Works/selena-film.md](Works/selena-film.md) |
| Sex and the City | work | television | editorial, voice-and-tone, narrative, desire-and-identity | canon | [Works/sex-and-the-city.md](Works/sex-and-the-city.md) |
| Sex Education | work | television | voice-and-tone, vulnerability, community-dynamics, British-comedic-lens | canon | [Works/sex-education.md](Works/sex-education.md) |
| The Fresh Prince of Bel-Air | work | television | voice-and-tone, code-switching, cultural-identity, humor-as-armor | canon | [Works/fresh-prince-of-bel-air.md](Works/fresh-prince-of-bel-air.md) |
| Whiplash | work | film | narrative, pacing, cost-of-greatness | canon | [Works/whiplash.md](Works/whiplash.md) |

### Curators

| Entity | Type | Domains | Pull for | Status | Card |
|---|---|---|---|---|---|
| Dover Street Market | curator | fashion, retail | merchandising, spatial-direction, high-low, curation-strategy | canon | [Curators/dover-street-market.md](Curators/dover-street-market.md) |
| Mr Porter | curator | fashion, menswear | menswear-curation, editorial-filter, taste-proxy, secondary-storefront | canon | [Curators/mr-porter.md](Curators/mr-porter.md) |

## Card-pending references

Known references with no card yet.

**Creators:** Mike Dean, Noah "40" Shebib, Kendrick Lamar, Future, Young Thug, Gustavo Piers Milton, Alexander Nguyen, Tyrod Taylor, Dr. Michael Greger, Karen Page, Andrew Dornenburg, Andy Warhol, Salvador Dali, Pablo Picasso, Donald Glover, Steven Spielberg, Martin Scorsese, Dan Harmon, Michelangelo, Gus Van Sant, Brian De Palma, Damien Chazelle, Vince Gilligan, Masashi Kishimoto, Eiichiro Oda, Michael Singer, Myron Golden, Alex Hormozi

**Brands – fashion:** Acne Studios, Isabel Marant, Our Legacy, Ami Paris, Auralee, Common Projects, Blackstock and Weber, Goyard, Margaret Howell, Drake's, Paraboot, Alden, Brooklyn Circus, COS, Stüssy, Duke and Webster, Golden Goose, Rapha, Baserange, Vans, ARKET, Abercrombie, Lululemon

**Brands – fragrance:** Xerjoff, Creed, Byredo, Maison Francis Kurkdjian, Clive Christian, Maison Crivelli, Dolce and Gabbana, Bond No 9, Dior, Louis Vuitton, Bottega Veneta, Le Labo, Diptyque, Cire Trudon

**Brands – grooming:** Dr. Bronner's, Nubian Heritage, Kiehl's, Cecred, Salt and Stone, Innersense

**Brands – stationery and analog:** Leuchtturm1917, Midori, Kaweco, Stalogy, Rhodia, Blackwing, Smythson

**Brands – publishing:** Rizzoli, Taschen, Phaidon, Assouline

**Brands – homeware:** Hay, Iittala, Kinto, The Conran Shop, John Derian

**Brands – food and drink:** Maison Pierre Marcolini, La Maison du Chocolat, Mast Brothers, Dick Taylor, Olive and Sinclair, Jeni's Splendid Ice Creams, Burlap and Barrel, Diaspora Co, Levain Bakery, Kreation Organic, Erin McKenna's Bakery, Mariposa Baking Co, Blue Bottle Coffee, La Colombe, Kettl, Harney and Sons, Scribe Winery, Keplinger, Frog's Leap

**Brands – plants and flowers:** The Sill, Bloomscape, Terrain, Urban Stems, Farmgirl Flowers

**Brands – experiences and other:** Londolozi Game Reserve, Aire Ancient Baths, Bathhouse Brooklyn, Resy, MasterClass, Apple

**Curators:** Goodhood, SSENSE, END., Surrealism

**Works – albums:** Blonde, Coloring Book, Good Kid M.A.A.D City, Swimming, The Miseducation of Lauryn Hill

**Works – restaurants:** Roka Akor, Bonhomia

**Works – film:** Forrest Gump

**Works – fragrances:** Millesime Imperial, Bal d'Afrique, Baccarat Rouge 540 Extrait, Oud Ispahan, The One, Young Rose, Lafayette Street, L'Homme a la Rose

---

*Personal Reference Library. Created 2026-06-21 under the Manor Protocol. Venture libraries live in each venture Knowledge Base, isolated.*
