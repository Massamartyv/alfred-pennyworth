---
file_type: reference_library_index
scope: personal
created: 2026-06-21
last_updated: 2026-06-27
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
| Alberto Kalach | creator | architecture, urbanism, landscape | biophilic, materiality, spatial-direction, nature-integration | canon | [Creators/alberto-kalach.md](Creators/alberto-kalach.md) |
| Alex Guarnaschelli | creator | culinary, restaurants | french-technique, comfort-food, precision, hospitality | canon | [Creators/alex-guarnaschelli.md](Creators/alex-guarnaschelli.md) |
| Alexander Nguyen | creator | fashion | minimalism, texture, quiet-luxury, fashion | watch | [Creators/alexander-nguyen.md](Creators/alexander-nguyen.md) |
| André 3000 | creator | music, fashion, film | voice-and-tone, reinvention, restraint | canon | [Creators/andre-3000.md](Creators/andre-3000.md) |
| André Leon Talley | creator | fashion, editorial, media | editorial, taste-authority, voice-and-tone, fashion-as-culture | canon | [Creators/andre-leon-talley.md](Creators/andre-leon-talley.md) |
| Andy Warhol | creator | visual art, film, pop culture | high-low, icon-making, repetition, art-direction | canon | [Creators/andy-warhol.md](Creators/andy-warhol.md) |
| Anthony Bourdain | creator | food, travel, culture | narrative, taste-compass, hospitality, food-culture | canon | [Creators/anthony-bourdain.md](Creators/anthony-bourdain.md) |
| A$AP Rocky | creator | fashion, music | art-direction, high-low, layering direction, oversized-silhouette | canon | [Creators/asap-rocky.md](Creators/asap-rocky.md) |
| Bad Bunny | creator | fashion, music | materiality, color-and-light, colour-confidence, relaxed-silhouette | canon | [Creators/bad-bunny.md](Creators/bad-bunny.md) |
| Banksy | creator | visual art, street art | subversion, context-as-content, wit, anti-establishment | canon | [Creators/banksy.md](Creators/banksy.md) |
| Beyoncé | creator | music, performance | performance, precision-as-freedom, ancestral-tribute, cadence | canon | [Creators/beyonce.md](Creators/beyonce.md) |
| Bobby Flay | creator | culinary, restaurants | bold-flavor, grilling, competition, brand-building | canon | [Creators/bobby-flay.md](Creators/bobby-flay.md) |
| Brian De Palma | creator | film, directing | visual-bravura, suspense, operatic-excess, cinematography | canon | [Creators/brian-de-palma.md](Creators/brian-de-palma.md) |
| Brooke Williamson | creator | culinary, restaurants | vegetable-forward, california-cuisine, produce-first, hospitality | canon | [Creators/brooke-williamson.md](Creators/brooke-williamson.md) |
| Claude Monet | creator | visual art | light, atmosphere, color-and-light, biophilic | canon | [Creators/claude-monet.md](Creators/claude-monet.md) |
| Colman Domingo | creator | fashion, acting | art-direction, restraint, materiality, statement-with-control | canon | [Creators/colman-domingo.md](Creators/colman-domingo.md) |
| Damien Chazelle | creator | film, directing | obsession, cost-of-greatness, music-and-rhythm, kinetic | canon | [Creators/damien-chazelle.md](Creators/damien-chazelle.md) |
| Dan Harmon | creator | television, writing | narrative-structure, story-circle, world-building, voice-and-tone | canon | [Creators/dan-harmon.md](Creators/dan-harmon.md) |
| Dries Van Noten | creator | fashion | print, textile, antwerp-six, fabric-first | canon | [Creators/dries-van-noten.md](Creators/dries-van-noten.md) |
| Eddie Jackson | creator | culinary, restaurants | athlete-to-chef, southern, bbq, discipline | canon | [Creators/eddie-jackson.md](Creators/eddie-jackson.md) |
| Eric Adjepong | creator | culinary, restaurants | west-african, diaspora, forward-looking-heritage, cultural-bridge | canon | [Creators/eric-adjepong.md](Creators/eric-adjepong.md) |
| Frank Lloyd Wright | creator | architecture, interior design, furniture | spatial-direction, materiality, nature-integration, total-design | canon | [Creators/frank-lloyd-wright.md](Creators/frank-lloyd-wright.md) |
| Frank Ocean | creator | music, production, aesthetics | sound-design, voice-and-tone, restraint, nostalgia-as-texture | canon | [Creators/frank-ocean.md](Creators/frank-ocean.md) |
| Gus Van Sant | creator | film, directing | emotional-restraint, outsiders, naturalism, character-study | canon | [Creators/gus-van-sant.md](Creators/gus-van-sant.md) |
| Gustavo Piers Milton | creator | fashion | editorial-risk, avant-garde, proportion-play, fashion | watch | [Creators/gustavo-piers-milton.md](Creators/gustavo-piers-milton.md) |
| James Cameron | creator | film, directing, technology | world-building, immersive-atmosphere, spectacle, technical-innovation | canon | [Creators/james-cameron.md](Creators/james-cameron.md) |
| Jean-Michel Basquiat | creator | visual art | visual-direction, art-direction, rawness, street-to-gallery | canon | [Creators/jean-michel-basquiat.md](Creators/jean-michel-basquiat.md) |
| Jet Tila | creator | culinary, restaurants | thai-cuisine, pan-asian, heritage, cultural-custodian | canon | [Creators/jet-tila.md](Creators/jet-tila.md) |
| Kanye West | creator | music, fashion, interior design, production | art-direction, visual-direction, color-and-light, materiality, maximalism | canon | [Creators/kanye-west.md](Creators/kanye-west.md) |
| Kardea Brown | creator | culinary, restaurants, television | gullah-geechee, heritage-preservation, southern, hospitality | canon | [Creators/kardea-brown.md](Creators/kardea-brown.md) |
| Kehinde Wiley | creator | visual art | portraiture, reclaiming-the-canon, heroic-posture, ornament | canon | [Creators/kehinde-wiley.md](Creators/kehinde-wiley.md) |
| Kim Chong Hak | creator | visual art | color-and-light, nature, depth-of-attention, anti-trend | canon | [Creators/kim-chong-hak.md](Creators/kim-chong-hak.md) |
| Kurt Cobain | creator | fashion, music | anti-style, restraint, effortless-nonchalance, fashion | canon | [Creators/kurt-cobain.md](Creators/kurt-cobain.md) |
| Leonardo da Vinci | creator | visual art, science, engineering | polymath, art-and-science, mastery, curiosity | canon | [Creators/leonardo-da-vinci.md](Creators/leonardo-da-vinci.md) |
| Logan Sylve | creator | visual art, illustration | street-to-gallery, high-low, surreal-expressionism, emerging-artist | active | [Creators/logan-sylve.md](Creators/logan-sylve.md) |
| Marcus Samuelsson | creator | culinary, restaurants | diaspora, three-continent-fusion, hospitality, cultural-bridge | canon | [Creators/marcus-samuelsson.md](Creators/marcus-samuelsson.md) |
| Martin Scorsese | creator | film, directing | kinetic-camera, music-as-structure, moral-weight, auteur | canon | [Creators/martin-scorsese.md](Creators/martin-scorsese.md) |
| Michael Greger | creator | nutrition, food science, medicine | evidence-based-nutrition, health-as-foundation, plant-forward, longevity | canon | [Creators/michael-greger.md](Creators/michael-greger.md) |
| Pablo Picasso | creator | visual art | reinvention, multiple-perspective, creative-risk, art-direction | canon | [Creators/pablo-picasso.md](Creators/pablo-picasso.md) |
| Page and Dornenburg | creator | food writing, flavor theory | flavor-pairing, culinary-reference, creative-engine, technique | canon | [Creators/page-and-dornenburg.md](Creators/page-and-dornenburg.md) |
| Pharrell | creator | fashion, music | art-direction, high-low, playful-eclecticism, accessory direction | canon | [Creators/pharrell.md](Creators/pharrell.md) |
| Pierce and Ward | creator | interior design | spatial-direction, materiality, constrained-maximalism, maximalism | canon | [Creators/pierce-and-ward.md](Creators/pierce-and-ward.md) |
| Quentin Tarantino | creator | film, directing | cinematography, visual-direction, style-as-resistance, maximalism | canon | [Creators/quentin-tarantino.md](Creators/quentin-tarantino.md) |
| Rebecca Maria | creator | visual art, sculpture | hip-hop-iconography, nostalgia, album-cover-art, emerging-artist | watch | [Creators/rebecca-maria.md](Creators/rebecca-maria.md) |
| Ryan Coogler | creator | film, directing | world-building, art-direction, atmosphere, spatial-direction | canon | [Creators/ryan-coogler.md](Creators/ryan-coogler.md) |
| Salvador Dalí | creator | visual art, film | surrealism, dream-logic, conviction, theatrical | canon | [Creators/salvador-dali.md](Creators/salvador-dali.md) |
| Steven Spielberg | creator | film, directing | wonder, populist-craft, world-building, spectacle | canon | [Creators/steven-spielberg.md](Creators/steven-spielberg.md) |
| Takashi Murakami | creator | visual art, fashion | high-low, art-fashion, collaboration, anime-iconography | canon | [Creators/takashi-murakami.md](Creators/takashi-murakami.md) |
| Travis Scott | creator | music, production, world-building | world-building, sound-design, immersive-atmosphere, narrative | canon | [Creators/travis-scott.md](Creators/travis-scott.md) |
| Tyler Durden | creator | fashion | anti-style, maximalist, high-low, statement | canon | [Creators/tyler-durden.md](Creators/tyler-durden.md) |
| Tyler, the Creator | creator | music | taste-evolution, reinvention, creative-risk, craft-over-brand | canon | [Creators/tyler-the-creator.md](Creators/tyler-the-creator.md) |
| Tyrod Taylor | creator | fashion | athletic-tailoring, fitted-silhouette, americana, fashion | canon | [Creators/tyrod-taylor.md](Creators/tyrod-taylor.md) |
| Vince Gilligan | creator | television, writing | long-form-structure, moral-transformation, slow-burn, consequence | canon | [Creators/vince-gilligan.md](Creators/vince-gilligan.md) |
| Virgil Abloh | creator | interior design, fashion, architecture | spatial-direction, art-direction, restraint, negative-space | canon | [Creators/virgil-abloh.md](Creators/virgil-abloh.md) |
| Yayoi Kusama | creator | visual art | repetition, visual-system, immersive-atmosphere, world-building | canon | [Creators/yayoi-kusama.md](Creators/yayoi-kusama.md) |

### Brands

| Entity | Type | Domains | Pull for | Status | Card |
|---|---|---|---|---|---|
| Abercrombie | brand | fashion | rebrand, elevated-basics, americana, foundation-fashion | canon | [Brands/abercrombie.md](Brands/abercrombie.md) |
| Acne Studios | brand | fashion | scandinavian, minimalism, denim, subversive | canon | [Brands/acne-studios.md](Brands/acne-studios.md) |
| Aesop | brand | grooming, interior design | design-conscious, ritual, restraint, interior-integration | canon | [Brands/aesop.md](Brands/aesop.md) |
| Aimé Leon Dore | brand | fashion, streetwear | streetwear, high-low, world-building, cultural-credibility | canon | [Brands/aime-leon-dore.md](Brands/aime-leon-dore.md) |
| Alden | brand | footwear, fashion | american, heritage, shell-cordovan, footwear | canon | [Brands/alden.md](Brands/alden.md) |
| Ami Paris | brand | fashion | parisian, accessible-luxury, everyday-chic, restraint | canon | [Brands/ami-paris.md](Brands/ami-paris.md) |
| ARKET | brand | fashion, homeware | scandinavian, basics, market-hall, accessible | canon | [Brands/arket.md](Brands/arket.md) |
| Auralee | brand | fashion | japanese, fabric-first, quiet-luxury, materiality | canon | [Brands/auralee.md](Brands/auralee.md) |
| Baserange | brand | fashion | natural-fibre, sustainability, basics, restraint | canon | [Brands/baserange.md](Brands/baserange.md) |
| Blackstock and Weber | brand | footwear, fashion | loafer, americana-reimagined, statement, footwear | canon | [Brands/blackstock-and-weber.md](Brands/blackstock-and-weber.md) |
| Blue Bottle Coffee | brand | coffee | third-wave, freshness-first, minimalism, craft | canon | [Brands/blue-bottle-coffee.md](Brands/blue-bottle-coffee.md) |
| Brooklyn Circus | brand | fashion | americana, heritage, storytelling, high-low | canon | [Brands/brooklyn-circus.md](Brands/brooklyn-circus.md) |
| Buly 1803 | brand | fragrance, grooming | heritage-craft, apothecary, world-building, ritual | canon | [Brands/buly-1803.md](Brands/buly-1803.md) |
| Burlap and Barrel | brand | spices, pantry | single-origin, provenance, direct-trade, ethics | canon | [Brands/burlap-and-barrel.md](Brands/burlap-and-barrel.md) |
| Celine | brand | fashion, leather goods | quiet-luxury, restraint, parisian, minimalism | canon | [Brands/celine.md](Brands/celine.md) |
| Common Projects | brand | footwear, fashion | minimalism, sneaker, gold-stamp, restraint | canon | [Brands/common-projects.md](Brands/common-projects.md) |
| COS | brand | fashion | minimalism, architectural, accessible, restraint | canon | [Brands/cos.md](Brands/cos.md) |
| Diaspora Co. | brand | spices, pantry | single-origin, equity, anti-colonial, brand-identity | canon | [Brands/diaspora-co.md](Brands/diaspora-co.md) |
| Dick Taylor | brand | chocolate | single-origin, maker-craft, materiality, two-ingredient | canon | [Brands/dick-taylor.md](Brands/dick-taylor.md) |
| Drake's | brand | fashion | british, tailoring, sprezzatura, menswear | canon | [Brands/drakes.md](Brands/drakes.md) |
| Duke and Dexter | brand | footwear, fashion | loafer, velvet, british, statement | canon | [Brands/duke-and-dexter.md](Brands/duke-and-dexter.md) |
| Erin McKenna's Bakery | brand | bakery | vegan, gluten-free, allergen-free, no-compromise | canon | [Brands/erin-mckennas-bakery.md](Brands/erin-mckennas-bakery.md) |
| Frog's Leap | brand | wine | organic, dry-farmed, sustainability, new-world | canon | [Brands/frogs-leap.md](Brands/frogs-leap.md) |
| Golden Goose | brand | footwear, fashion | sneaker, distressed, italian, statement | canon | [Brands/golden-goose.md](Brands/golden-goose.md) |
| Goyard | brand | fashion, accessories, travel | heritage, discreet-luxury, accessories, travel | canon | [Brands/goyard.md](Brands/goyard.md) |
| Harney and Sons | brand | tea | fine-tea, blending, family-craft, accessible-luxury | canon | [Brands/harney-and-sons.md](Brands/harney-and-sons.md) |
| Hermès | brand | fashion, accessories, homeware | investment-luxury, craft-led, cross-category, accessories | canon | [Brands/hermes.md](Brands/hermes.md) |
| House of Nangman | brand | fashion, accessories | naming, narrative, headwear, sentiment-led | active | [Brands/house-of-nangman.md](Brands/house-of-nangman.md) |
| Isabel Marant | brand | fashion | parisian, effortless, bohemian, sprezzatura | canon | [Brands/isabel-marant.md](Brands/isabel-marant.md) |
| Jeni's Splendid Ice Creams | brand | ice cream, dessert | flavor-invention, technique, artisan, craft | canon | [Brands/jenis-splendid-ice-creams.md](Brands/jenis-splendid-ice-creams.md) |
| Keplinger | brand | wine | cult-wine, rhone-varietals, small-production, terroir | canon | [Brands/keplinger.md](Brands/keplinger.md) |
| Kettl | brand | tea | japanese-tea, single-origin, provenance, seasonality | canon | [Brands/kettl.md](Brands/kettl.md) |
| Kreation Organic | brand | juice, cafe, wellness | organic, cold-pressed, wellness, ritual | canon | [Brands/kreation-organic.md](Brands/kreation-organic.md) |
| La Colombe | brand | coffee | specialty-coffee, product-innovation, sourcing, scale | canon | [Brands/la-colombe.md](Brands/la-colombe.md) |
| La Maison du Chocolat | brand | chocolate | ganache, french-luxury, restraint, heritage | canon | [Brands/la-maison-du-chocolat.md](Brands/la-maison-du-chocolat.md) |
| Lemaire | brand | fashion | materiality, anti-logo, restraint, quiet-luxury | canon | [Brands/lemaire.md](Brands/lemaire.md) |
| Levain Bakery | brand | bakery, dessert | signature-product, cult-object, indulgence, craft | canon | [Brands/levain-bakery.md](Brands/levain-bakery.md) |
| Liverpool FC | brand | sports, identity, culture | tribal-identity, unambiguous-loyalty, cultural-affiliation, world-building | canon | [Brands/liverpool-fc.md](Brands/liverpool-fc.md) |
| Loewe | brand | fashion, leather goods | investment-luxury, craft-led, materiality, artistic-direction | canon | [Brands/loewe.md](Brands/loewe.md) |
| Louis Vuitton | brand | fashion, leather goods, fragrance | investment-luxury, high-low, world-building, craft-led | canon | [Brands/louis-vuitton.md](Brands/louis-vuitton.md) |
| Lululemon | brand | activewear, fashion | activewear, technical, performance, repositioned | canon | [Brands/lululemon.md](Brands/lululemon.md) |
| Maison Pierre Marcolini | brand | chocolate | haute-chocolate, craft-led, seasonality, provenance | canon | [Brands/maison-pierre-marcolini.md](Brands/maison-pierre-marcolini.md) |
| Mango | brand | fashion | high-street, mediterranean, accessible, foundation-fashion | canon | [Brands/mango.md](Brands/mango.md) |
| Margaret Howell | brand | fashion | british, utility, restraint, fabric-first | canon | [Brands/margaret-howell.md](Brands/margaret-howell.md) |
| Mariposa Baking Co. | brand | bakery | gluten-free, no-compromise, artisan, dedicated-facility | canon | [Brands/mariposa-baking-co.md](Brands/mariposa-baking-co.md) |
| Mast Brothers | brand | chocolate | packaging-design, craft-aesthetics, brand-storytelling, cautionary | watch | [Brands/mast-brothers.md](Brands/mast-brothers.md) |
| Moscot | brand | eyewear, accessories | eyewear, heritage, new-york, craft | canon | [Brands/moscot.md](Brands/moscot.md) |
| Nayara Springs | brand | travel, hospitality, experiences | five-star-hospitality, pinnacle-standard, experience-design, ritual | canon | [Brands/nayara-springs.md](Brands/nayara-springs.md) |
| Nike | brand | fashion, footwear, athletics | selective-alignment, sub-line-curation, sneaker, high-low | canon | [Brands/nike.md](Brands/nike.md) |
| Olive and Sinclair | brand | chocolate | southern, place-rooted, craft, bean-to-bar | canon | [Brands/olive-and-sinclair.md](Brands/olive-and-sinclair.md) |
| Our Legacy | brand | fashion | scandinavian, fabric-first, textured, restraint | canon | [Brands/our-legacy.md](Brands/our-legacy.md) |
| Paraboot | brand | footwear, fashion | french, heritage, footwear, craft | canon | [Brands/paraboot.md](Brands/paraboot.md) |
| Prada | brand | fashion, leather goods | intellectual-fashion, restraint, materiality, anti-pretty | canon | [Brands/prada.md](Brands/prada.md) |
| Ralph Lauren | brand | fashion | americana, quiet-luxury, tiered-curation, logo-avoidance | canon | [Brands/ralph-lauren.md](Brands/ralph-lauren.md) |
| Rapha | brand | cycling, fashion | cycling, performance, premium, community | canon | [Brands/rapha.md](Brands/rapha.md) |
| Rieti | brand | eyewear, accessories | eyewear, korean, accessible-cool, detail | active | [Brands/rieti.md](Brands/rieti.md) |
| Santa Maria Novella | brand | fragrance, grooming | heritage-craft, apothecary, cross-category, ritual | canon | [Brands/santa-maria-novella.md](Brands/santa-maria-novella.md) |
| Scribe Winery | brand | wine | natural-wine, place-as-experience, minimal-intervention, new-world | canon | [Brands/scribe-winery.md](Brands/scribe-winery.md) |
| Singita | brand | travel, hospitality, conservation | five-star-hospitality, conservation-luxury, sense-of-place, ritual | canon | [Brands/singita.md](Brands/singita.md) |
| Stüssy | brand | fashion, streetwear | streetwear, surf, heritage, high-low | canon | [Brands/stussy.md](Brands/stussy.md) |
| Uniqlo | brand | fashion | foundation-fashion, quality-basics, anti-logo, restraint | canon | [Brands/uniqlo.md](Brands/uniqlo.md) |
| Vans | brand | footwear, fashion | skate, heritage, foundation-fashion, high-low | canon | [Brands/vans.md](Brands/vans.md) |
| Yves Saint Laurent | brand | fashion | tailoring, androgyny, parisian, statement | canon | [Brands/yves-saint-laurent.md](Brands/yves-saint-laurent.md) |

### Works

| Entity | Type | Domains | Pull for | Status | Card |
|---|---|---|---|---|---|
| Albert Einstein Education and Research Center | work | architecture, institutional, landscape | biophilic, spatial-direction, color-and-light, atrium | canon | [Works/albert-einstein-education-research-center.md](Works/albert-einstein-education-research-center.md) |
| Astroworld | work | music | sound-design, world-building, immersive-atmosphere, ear-candy | canon | [Works/astroworld.md](Works/astroworld.md) |
| Bonhomía | work | restaurant, salumeria | salumeria, convivial, indoor-outdoor, hospitality | canon | [Works/bonhomia.md](Works/bonhomia.md) |
| Breaking Bad | work | television | narrative, character-study, long-form-structure, pride-and-hubris | canon | [Works/breaking-bad.md](Works/breaking-bad.md) |
| Building Frame of the House | work | architecture, residential | materiality, spatial-direction, structural-honesty, small-space-ingenuity | canon | [Works/building-frame-of-the-house.md](Works/building-frame-of-the-house.md) |
| Dallas Buyers Club | work | film | transformation, defiance, total-commitment, against-the-system | canon | [Works/dallas-buyers-club.md](Works/dallas-buyers-club.md) |
| Django Unchained | work | film | narrative, genre-inversion, style-as-resistance, power-and-identity | canon | [Works/django-unchained.md](Works/django-unchained.md) |
| Everything Everywhere All at Once | work | film | narrative, tonal-range, formal-experimentation, emotional-honesty | canon | [Works/everything-everywhere-all-at-once.md](Works/everything-everywhere-all-at-once.md) |
| Fallingwater | work | architecture, residential | nature-integration, materiality, spatial-direction, restraint | canon | [Works/fallingwater.md](Works/fallingwater.md) |
| Forrest Gump | work | film | innocence-as-wisdom, americana, sentiment, history | canon | [Works/forrest-gump.md](Works/forrest-gump.md) |
| Good Will Hunting | work | film | narrative, emotional-suppression, cost-of-greatness, mentor-dynamics | canon | [Works/good-will-hunting.md](Works/good-will-hunting.md) |
| Homegoing | work | literature | narrative, structure-as-argument, diaspora, historical-weight | canon | [Works/homegoing-yaa-gyasi.md](Works/homegoing-yaa-gyasi.md) |
| Menace II Society | work | film | hood-realism, coming-of-age, fatalism, black-cinema | canon | [Works/menace-ii-society.md](Works/menace-ii-society.md) |
| My Beautiful Dark Twisted Fantasy | work | music | sound-design, world-building, maximalism, ambition-as-form | canon | [Works/my-beautiful-dark-twisted-fantasy.md](Works/my-beautiful-dark-twisted-fantasy.md) |
| Naruto: Shippuden | work | animation, television | narrative, world-building, found-family, perseverance-and-identity | canon | [Works/naruto-shippuden.md](Works/naruto-shippuden.md) |
| One Piece | work | animation | narrative, world-building, long-form-structure, found-family | canon | [Works/one-piece.md](Works/one-piece.md) |
| Renaissance | work | music | sound-design, Black-joy, house-culture, precision-as-freedom | canon | [Works/renaissance-beyonce.md](Works/renaissance-beyonce.md) |
| Roka Akor | work | restaurant, japanese | robatayaki, japanese, moody-dining, hospitality | canon | [Works/roka-akor.md](Works/roka-akor.md) |
| Scarface | work | film | narrative, ambition-and-hubris, cost-of-the-climb, dramatic-inevitability | canon | [Works/scarface.md](Works/scarface.md) |
| Selena | work | film | narrative, cultural-identity, crossover-ambition, legacy | canon | [Works/selena-film.md](Works/selena-film.md) |
| Sex and the City | work | television | editorial, voice-and-tone, narrative, desire-and-identity | canon | [Works/sex-and-the-city.md](Works/sex-and-the-city.md) |
| Sex Education | work | television | voice-and-tone, vulnerability, community-dynamics, British-comedic-lens | canon | [Works/sex-education.md](Works/sex-education.md) |
| The Fresh Prince of Bel-Air | work | television | voice-and-tone, code-switching, cultural-identity, humor-as-armor | canon | [Works/fresh-prince-of-bel-air.md](Works/fresh-prince-of-bel-air.md) |
| Whiplash | work | film | narrative, pacing, cost-of-greatness | canon | [Works/whiplash.md](Works/whiplash.md) |

### Curators

Editorial and retail tastemakers.

| Entity | Type | Domains | Pull for | Status | Card |
|---|---|---|---|---|---|
| Architectural Digest | curator | architecture, interior design, media | editorial, interiors, taste-proxy, luxury-homes | canon | [Curators/architectural-digest.md](Curators/architectural-digest.md) |
| Dover Street Market | curator | fashion, retail | merchandising, spatial-direction, high-low, curation-strategy | canon | [Curators/dover-street-market.md](Curators/dover-street-market.md) |
| Mr Porter | curator | fashion, menswear | menswear-curation, editorial-filter, taste-proxy, secondary-storefront | canon | [Curators/mr-porter.md](Curators/mr-porter.md) |

Aesthetic styles and movements – filed as curators, with the movement or vernacular standing as the tastemaking context.

| Entity | Type | Domains | Pull for | Status | Card |
|---|---|---|---|---|---|
| Biophilic | curator | architecture, interior design, landscape | biophilic, nature-integration, greenery, wellbeing | canon | [Curators/biophilic.md](Curators/biophilic.md) |
| Brownstone | curator | architecture, interior design, urbanism | historical-fabric, urban-vernacular, materiality, warmth | canon | [Curators/brownstone.md](Curators/brownstone.md) |
| Brutalist | curator | architecture, interior design | materiality, raw-and-warm, sculptural-mass, monumental | canon | [Curators/brutalist.md](Curators/brutalist.md) |
| French Provincial | curator | architecture, interior design | materiality, warmth, rustic-refinement, craftsmanship | active | [Curators/french-provincial.md](Curators/french-provincial.md) |
| Industrial | curator | architecture, interior design | materiality, loft, exposed-structure, raw-and-warm | canon | [Curators/industrial.md](Curators/industrial.md) |
| Mediterranean | curator | architecture, interior design | materiality, indoor-outdoor, warmth, color-and-light | canon | [Curators/mediterranean.md](Curators/mediterranean.md) |
| Modern | curator | architecture, interior design | clean-line, open-plan, form-follows-function, restraint | canon | [Curators/modern.md](Curators/modern.md) |
| Surrealism | curator | visual art, literature, film | dream-logic, the-uncanny, juxtaposition, conviction | canon | [Curators/surrealism.md](Curators/surrealism.md) |

Museums and institutions – galleries and museums held as tastemaking contexts.

| Entity | Type | Domains | Pull for | Status | Card |
|---|---|---|---|---|---|
| The Guggenheim | curator | art, museum, architecture | architecture-as-destination, spatial-direction, modern-art | canon | [Curators/guggenheim.md](Curators/guggenheim.md) |
| The Hermitage Museum | curator | art, museum | scale, opulence, imperial, spatial-direction | canon | [Curators/hermitage-museum.md](Curators/hermitage-museum.md) |
| High Museum of Art | curator | art, museum, architecture | atlanta, architecture, home-institution, art-direction | canon | [Curators/high-museum-of-art.md](Curators/high-museum-of-art.md) |
| The Louvre | curator | art, museum | the-canon, masterpiece, antiquity, art-direction | canon | [Curators/the-louvre.md](Curators/the-louvre.md) |
| The Metropolitan Museum of Art | curator | art, museum, fashion | breadth, juxtaposition, costume-institute, editorial | canon | [Curators/metropolitan-museum-of-art.md](Curators/metropolitan-museum-of-art.md) |
| Musée d'Orsay | curator | art, museum | impressionism, color-and-light, adaptive-reuse, paris | canon | [Curators/musee-dorsay.md](Curators/musee-dorsay.md) |
| Museo del Prado | curator | art, museum | old-master, spanish-masters, drama, portraiture | canon | [Curators/museo-del-prado.md](Curators/museo-del-prado.md) |
| Museum of Modern Art (MoMA) | curator | art, museum | modern-art, canon-setting, institutional-authority | canon | [Curators/museum-of-modern-art.md](Curators/museum-of-modern-art.md) |
| Tate Modern | curator | art, museum | contemporary, adaptive-reuse, exposed-structure, london | canon | [Curators/tate-modern.md](Curators/tate-modern.md) |
| Vatican Museums | curator | art, museum | renaissance, sacred-art, michelangelo, spatial-direction | canon | [Curators/vatican-museums.md](Curators/vatican-museums.md) |

## Card-pending references

Known references with no card yet.

**Creators:** Mike Dean, Noah "40" Shebib, Kendrick Lamar, Future, Young Thug, Donald Glover, Michelangelo, Masashi Kishimoto, Eiichiro Oda, Michael Singer, Myron Golden, Alex Hormozi
**Brands – fragrance:** Xerjoff, Creed, Byredo, Maison Francis Kurkdjian, Clive Christian, Maison Crivelli, Dolce and Gabbana, Bond No 9, Dior, Bottega Veneta, Le Labo, Diptyque, Cire Trudon

**Brands – grooming:** Dr. Bronner's, Nubian Heritage, Kiehl's, Cecred, Salt and Stone, Innersense

**Brands – stationery and analog:** Leuchtturm1917, Midori, Kaweco, Stalogy, Rhodia, Blackwing, Smythson

**Brands – publishing:** Rizzoli, Taschen, Phaidon, Assouline

**Brands – homeware:** Hay, Iittala, Kinto, The Conran Shop, John Derian
**Brands – plants and flowers:** The Sill, Bloomscape, Terrain, Urban Stems, Farmgirl Flowers

**Brands – experiences and other:** Londolozi Game Reserve, Aire Ancient Baths, Bathhouse Brooklyn, Resy, MasterClass, Apple

**Curators:** Goodhood, SSENSE, END.

**Works – albums:** Blonde, Coloring Book, Good Kid M.A.A.D City, Swimming, The Miseducation of Lauryn Hill**Works – fragrances:** Millesime Imperial, Bal d'Afrique, Baccarat Rouge 540 Extrait, Oud Ispahan, The One, Young Rose, Lafayette Street, L'Homme a la Rose

---

*Personal Reference Library. Created 2026-06-21 under the Manor Protocol. Venture libraries live in each venture Knowledge Base, isolated.*
