---
file_type: reference_library_index
scope: personal
created: 2026-06-21
last_updated: 2026-07-10
---

# Reference Library

A curated corpus of the creators, brands, works and curators that inform research, inspiration and creative direction. Alfred draws on this library when a task needs a batch of grounded reference – what is working, what to extract, which canon to draw from – rather than reasoning from a blank page.

This is the personal library. Every venture holds its own isolated Reference Library inside its Knowledge Base. Personal and venture references never share a file.

## How Alfred uses it

1. A task calls for inspiration, creative direction or a research batch.
2. Alfred reads this index and matches the task to cards by type, domain and the Pull-for tags.
3. Alfred loads only the matched cards and returns a batch with the formula and the canon already surfaced on each card.

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
| Adele | creator | music, vocal performance | restraint, voice-and-tone, anti-trend, era-pacing | canon | [Creators/adele.md](Creators/adele.md) |
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
| Caroline Shaw | creator | music, composition, vocal music | high-low, voice-as-instrument, form-invention, cultural-bridge | canon | [Creators/caroline-shaw.md](Creators/caroline-shaw.md) |
| Claude Monet | creator | visual art | light, atmosphere, color-and-light, biophilic | canon | [Creators/claude-monet.md](Creators/claude-monet.md) |
| Colman Domingo | creator | fashion, acting | art-direction, restraint, materiality, statement-with-control | canon | [Creators/colman-domingo.md](Creators/colman-domingo.md) |
| Damien Chazelle | creator | film, directing | obsession, cost-of-greatness, music-and-rhythm, kinetic | canon | [Creators/damien-chazelle.md](Creators/damien-chazelle.md) |
| Dan Harmon | creator | television, writing | narrative-structure, story-circle, world-building, voice-and-tone | canon | [Creators/dan-harmon.md](Creators/dan-harmon.md) |
| Do Ho Suh | creator | installation, sculpture, architecture | spatial-memory, fabric-architecture, displacement, home | canon | [Creators/do-ho-suh.md](Creators/do-ho-suh.md) |
| Dries Van Noten | creator | fashion | print, textile, antwerp-six, fabric-first | canon | [Creators/dries-van-noten.md](Creators/dries-van-noten.md) |
| Eddie Jackson | creator | culinary, restaurants | athlete-to-chef, southern, bbq, discipline | canon | [Creators/eddie-jackson.md](Creators/eddie-jackson.md) |
| Eric Adjepong | creator | culinary, restaurants | west-african, diaspora, forward-looking-heritage, cultural-bridge | canon | [Creators/eric-adjepong.md](Creators/eric-adjepong.md) |
| Frank Lloyd Wright | creator | architecture, interior design, furniture | spatial-direction, materiality, nature-integration, total-design | canon | [Creators/frank-lloyd-wright.md](Creators/frank-lloyd-wright.md) |
| Frank Ocean | creator | music, production, aesthetics | sound-design, voice-and-tone, restraint, nostalgia-as-texture | canon | [Creators/frank-ocean.md](Creators/frank-ocean.md) |
| Gunna | creator | music, hip-hop, atlanta | melodic-trap, slang-as-brand, cadence, resilience | canon | [Creators/gunna.md](Creators/gunna.md) |
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
| Lil Uzi Vert | creator | music, hip-hop, rage | genre-blur, persona-as-asset, high-low, world-building | canon | [Creators/lil-uzi-vert.md](Creators/lil-uzi-vert.md) |
| Logan Sylve | creator | visual art, illustration | street-to-gallery, high-low, surreal-expressionism, emerging-artist | active | [Creators/logan-sylve.md](Creators/logan-sylve.md) |
| Marcus Samuelsson | creator | culinary, restaurants | diaspora, three-continent-fusion, hospitality, cultural-bridge | canon | [Creators/marcus-samuelsson.md](Creators/marcus-samuelsson.md) |
| Martin Scorsese | creator | film, directing | kinetic-camera, music-as-structure, moral-weight, auteur | canon | [Creators/martin-scorsese.md](Creators/martin-scorsese.md) |
| Michael Greger | creator | nutrition, food science, medicine | evidence-based-nutrition, health-as-foundation, plant-forward, longevity | canon | [Creators/michael-greger.md](Creators/michael-greger.md) |
| Miguel | creator | music, r&b | auteur, texture, sound-design, reinvention | canon | [Creators/miguel.md](Creators/miguel.md) |
| Mötley Crüe | creator | music, rock, spectacle | maximalism, spectacle, image-first, conviction | canon | [Creators/motley-crue.md](Creators/motley-crue.md) |
| Pablo Picasso | creator | visual art | reinvention, multiple-perspective, creative-risk, art-direction | canon | [Creators/pablo-picasso.md](Creators/pablo-picasso.md) |
| Page and Dornenburg | creator | food writing, flavor theory | flavor-pairing, culinary-reference, creative-engine, technique | canon | [Creators/page-and-dornenburg.md](Creators/page-and-dornenburg.md) |
| Pharrell | creator | fashion, music | art-direction, high-low, playful-eclecticism, accessory direction | canon | [Creators/pharrell.md](Creators/pharrell.md) |
| Pierce and Ward | creator | interior design | spatial-direction, materiality, constrained-maximalism, maximalism | canon | [Creators/pierce-and-ward.md](Creators/pierce-and-ward.md) |
| Quentin Tarantino | creator | film, directing | cinematography, visual-direction, style-as-resistance, maximalism | canon | [Creators/quentin-tarantino.md](Creators/quentin-tarantino.md) |
| Quincy Jones | creator | music, production, film, arranging | polymath, producer-as-architect, ego-management, breadth | canon | [Creators/quincy-jones.md](Creators/quincy-jones.md) |
| Rebecca Maria | creator | visual art, sculpture | hip-hop-iconography, nostalgia, album-cover-art, emerging-artist | watch | [Creators/rebecca-maria.md](Creators/rebecca-maria.md) |
| Rihanna | creator | music, beauty, fashion, business | empire-pivot, catalog-longevity, scarcity, reinvention | canon | [Creators/rihanna.md](Creators/rihanna.md) |
| Ryan Coogler | creator | film, directing | world-building, art-direction, atmosphere, spatial-direction | canon | [Creators/ryan-coogler.md](Creators/ryan-coogler.md) |
| Salvador Dalí | creator | visual art, film | surrealism, dream-logic, conviction, theatrical | canon | [Creators/salvador-dali.md](Creators/salvador-dali.md) |
| Steven Spielberg | creator | film, directing | wonder, populist-craft, world-building, spectacle | canon | [Creators/steven-spielberg.md](Creators/steven-spielberg.md) |
| Takashi Murakami | creator | visual art, fashion | high-low, art-fashion, collaboration, anime-iconography | canon | [Creators/takashi-murakami.md](Creators/takashi-murakami.md) |
| Tems | creator | music, r&b, afrobeats | restraint, negative-space, self-production, cultural-bridge | canon | [Creators/tems.md](Creators/tems.md) |
| Travis Scott | creator | music, production, world-building | world-building, sound-design, immersive-atmosphere, narrative | canon | [Creators/travis-scott.md](Creators/travis-scott.md) |
| Tyler Durden | creator | fashion | anti-style, maximalist, high-low, statement | canon | [Creators/tyler-durden.md](Creators/tyler-durden.md) |
| Tyler, the Creator | creator | music | taste-evolution, reinvention, creative-risk, craft-over-brand | canon | [Creators/tyler-the-creator.md](Creators/tyler-the-creator.md) |
| Tyrod Taylor | creator | fashion | athletic-tailoring, fitted-silhouette, americana, fashion | canon | [Creators/tyrod-taylor.md](Creators/tyrod-taylor.md) |
| Vince Gilligan | creator | television, writing | long-form-structure, moral-transformation, slow-burn, consequence | canon | [Creators/vince-gilligan.md](Creators/vince-gilligan.md) |
| Virgil Abloh | creator | interior design, fashion, architecture | spatial-direction, art-direction, restraint, negative-space | canon | [Creators/virgil-abloh.md](Creators/virgil-abloh.md) |
| Wu-Tang Clan | creator | music, hip-hop, business strategy | brand-architecture, world-building, collective-and-sovereign, scarcity | canon | [Creators/wu-tang-clan.md](Creators/wu-tang-clan.md) |
| Yayoi Kusama | creator | visual art | repetition, visual-system, immersive-atmosphere, world-building | canon | [Creators/yayoi-kusama.md](Creators/yayoi-kusama.md) |
| Yeat | creator | music, hip-hop, rage | world-building, sonic-signature, lexicon-as-brand, sound-design | canon | [Creators/yeat.md](Creators/yeat.md) |

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
| Bond No. 9 | brand | fragrance | niche, new-york, place-as-concept, collectible | canon | [Brands/bond-no-9.md](Brands/bond-no-9.md) |
| Bottega Veneta | brand | fragrance | designer-fragrance, quiet-luxury, leather, restraint | canon | [Brands/bottega-veneta.md](Brands/bottega-veneta.md) |
| Brooklyn Circus | brand | fashion | americana, heritage, storytelling, high-low | canon | [Brands/brooklyn-circus.md](Brands/brooklyn-circus.md) |
| Buly 1803 | brand | fragrance, grooming | heritage-craft, apothecary, world-building, ritual | canon | [Brands/buly-1803.md](Brands/buly-1803.md) |
| Burlap and Barrel | brand | spices, pantry | single-origin, provenance, direct-trade, ethics | canon | [Brands/burlap-and-barrel.md](Brands/burlap-and-barrel.md) |
| Byredo | brand | fragrance | niche, memory-and-mood, art-direction, abstract | canon | [Brands/byredo.md](Brands/byredo.md) |
| Cécred | brand | haircare, personal care | haircare, prestige, ownership-as-strategy | canon | [Brands/cecred.md](Brands/cecred.md) |
| Celine | brand | fashion, leather goods | quiet-luxury, restraint, parisian, minimalism | canon | [Brands/celine.md](Brands/celine.md) |
| Cire Trudon | brand | fragrance | heritage, candle-house, lineage, restraint | canon | [Brands/cire-trudon.md](Brands/cire-trudon.md) |
| Clare Paint | brand | paint, interior design | curated-palette, color-and-light, decision-design, restraint | canon | [Brands/clare-paint.md](Brands/clare-paint.md) |
| Clive Christian | brand | fragrance | ultra-luxury, rare-ingredient, opulence, british-heritage | canon | [Brands/clive-christian.md](Brands/clive-christian.md) |
| Common Projects | brand | footwear, fashion | minimalism, sneaker, gold-stamp, restraint | canon | [Brands/common-projects.md](Brands/common-projects.md) |
| COS | brand | fashion | minimalism, architectural, accessible, restraint | canon | [Brands/cos.md](Brands/cos.md) |
| Crate and Barrel | brand | home goods, furniture, retail | merchandising, design-democratization, heritage, accessible | canon | [Brands/crate-and-barrel.md](Brands/crate-and-barrel.md) |
| Creed | brand | fragrance | niche, heritage-coded, status-scent, masculine | canon | [Brands/creed.md](Brands/creed.md) |
| Def Jam Recordings | brand | music, record labels, hip-hop | culture-making, artist-development, institution-building, reinvention | canon | [Brands/def-jam.md](Brands/def-jam.md) |
| Diaspora Co. | brand | spices, pantry | single-origin, equity, anti-colonial, brand-identity | canon | [Brands/diaspora-co.md](Brands/diaspora-co.md) |
| Dick Taylor | brand | chocolate | single-origin, maker-craft, materiality, two-ingredient | canon | [Brands/dick-taylor.md](Brands/dick-taylor.md) |
| Dior | brand | fragrance | prestige-niche, collection-privee, couture, maison | canon | [Brands/dior.md](Brands/dior.md) |
| Diptyque | brand | fragrance | heritage, candle-and-scent, botanical, restraint | canon | [Brands/diptyque.md](Brands/diptyque.md) |
| Dolce and Gabbana | brand | fragrance | designer-fragrance, mediterranean, italian, accessible-luxury | canon | [Brands/dolce-and-gabbana.md](Brands/dolce-and-gabbana.md) |
| Dr. Bronner's | brand | personal care, soap | castile-soap, values-led, heritage | canon | [Brands/dr-bronners.md](Brands/dr-bronners.md) |
| Drake's | brand | fashion | british, tailoring, sprezzatura, menswear | canon | [Brands/drakes.md](Brands/drakes.md) |
| Duke and Dexter | brand | footwear, fashion | loafer, velvet, british, statement | canon | [Brands/duke-and-dexter.md](Brands/duke-and-dexter.md) |
| Erin McKenna's Bakery | brand | bakery | vegan, gluten-free, allergen-free, no-compromise | canon | [Brands/erin-mckennas-bakery.md](Brands/erin-mckennas-bakery.md) |
| FanDuel | brand | gaming, sports betting, fantasy sports | positioning, product-pivot, conversion, category-leadership | canon | [Brands/fanduel.md](Brands/fanduel.md) |
| Frog's Leap | brand | wine | organic, dry-farmed, sustainability, new-world | canon | [Brands/frogs-leap.md](Brands/frogs-leap.md) |
| Golden Goose | brand | footwear, fashion | sneaker, distressed, italian, statement | canon | [Brands/golden-goose.md](Brands/golden-goose.md) |
| Goyard | brand | fashion, accessories, travel | heritage, discreet-luxury, accessories, travel | canon | [Brands/goyard.md](Brands/goyard.md) |
| Harney and Sons | brand | tea | fine-tea, blending, family-craft, accessible-luxury | canon | [Brands/harney-and-sons.md](Brands/harney-and-sons.md) |
| Hermès | brand | fashion, accessories, homeware | investment-luxury, craft-led, cross-category, accessories | canon | [Brands/hermes.md](Brands/hermes.md) |
| House of Nangman | brand | fashion, accessories | naming, narrative, headwear, sentiment-led | active | [Brands/house-of-nangman.md](Brands/house-of-nangman.md) |
| Innersense | brand | haircare, personal care | clean-haircare, salon-led, professional-grade | canon | [Brands/innersense.md](Brands/innersense.md) |
| Isabel Marant | brand | fashion | parisian, effortless, bohemian, sprezzatura | canon | [Brands/isabel-marant.md](Brands/isabel-marant.md) |
| Italic | brand | home goods, marketplace, fashion | anti-logo, quality-over-brand, materiality, merchandising | canon | [Brands/italic.md](Brands/italic.md) |
| Jeni's Splendid Ice Creams | brand | ice cream, dessert | flavor-invention, technique, artisan, craft | canon | [Brands/jenis-splendid-ice-creams.md](Brands/jenis-splendid-ice-creams.md) |
| Keplinger | brand | wine | cult-wine, rhone-varietals, small-production, terroir | canon | [Brands/keplinger.md](Brands/keplinger.md) |
| Kettl | brand | tea | japanese-tea, single-origin, provenance, seasonality | canon | [Brands/kettl.md](Brands/kettl.md) |
| Kiehl's | brand | skincare, personal care | apothecary, heritage, formulation | canon | [Brands/kiehls.md](Brands/kiehls.md) |
| Kreation Organic | brand | juice, cafe, wellness | organic, cold-pressed, wellness, ritual | canon | [Brands/kreation-organic.md](Brands/kreation-organic.md) |
| La Colombe | brand | coffee | specialty-coffee, product-innovation, sourcing, scale | canon | [Brands/la-colombe.md](Brands/la-colombe.md) |
| La Maison du Chocolat | brand | chocolate | ganache, french-luxury, restraint, heritage | canon | [Brands/la-maison-du-chocolat.md](Brands/la-maison-du-chocolat.md) |
| Le Labo | brand | fragrance | niche, ritual, anti-luxury-luxury, experiential | canon | [Brands/le-labo.md](Brands/le-labo.md) |
| Lemaire | brand | fashion | materiality, anti-logo, restraint, quiet-luxury | canon | [Brands/lemaire.md](Brands/lemaire.md) |
| Levain Bakery | brand | bakery, dessert | signature-product, cult-object, indulgence, craft | canon | [Brands/levain-bakery.md](Brands/levain-bakery.md) |
| Liverpool FC | brand | sports, identity, culture | tribal-identity, unambiguous-loyalty, cultural-affiliation, world-building | canon | [Brands/liverpool-fc.md](Brands/liverpool-fc.md) |
| Loewe | brand | fashion, leather goods | investment-luxury, craft-led, materiality, artistic-direction | canon | [Brands/loewe.md](Brands/loewe.md) |
| Louis Vuitton | brand | fashion, leather goods, fragrance | investment-luxury, high-low, world-building, craft-led | canon | [Brands/louis-vuitton.md](Brands/louis-vuitton.md) |
| Lulu and Georgia | brand | home decor, furniture | curated-decor, lineage, designer-collaboration, merchandising | canon | [Brands/lulu-and-georgia.md](Brands/lulu-and-georgia.md) |
| Lululemon | brand | activewear, fashion | activewear, technical, performance, repositioned | canon | [Brands/lululemon.md](Brands/lululemon.md) |
| Maison Crivelli | brand | fragrance | niche, olfactive-shock, nature-forward, concept-led | canon | [Brands/maison-crivelli.md](Brands/maison-crivelli.md) |
| Maison d'Etto | brand | fragrance, home fragrance | narrative, world-building, ritual, niche | canon | [Brands/maison-detto.md](Brands/maison-detto.md) |
| Maison Francis Kurkdjian | brand | fragrance | haute-parfumerie, technical-precision, signature-scent, parisian | canon | [Brands/maison-francis-kurkdjian.md](Brands/maison-francis-kurkdjian.md) |
| Maison Pierre Marcolini | brand | chocolate | haute-chocolate, craft-led, seasonality, provenance | canon | [Brands/maison-pierre-marcolini.md](Brands/maison-pierre-marcolini.md) |
| Mango | brand | fashion | high-street, mediterranean, accessible, foundation-fashion | canon | [Brands/mango.md](Brands/mango.md) |
| Margaret Howell | brand | fashion | british, utility, restraint, fabric-first | canon | [Brands/margaret-howell.md](Brands/margaret-howell.md) |
| Mariposa Baking Co. | brand | bakery | gluten-free, no-compromise, artisan, dedicated-facility | canon | [Brands/mariposa-baking-co.md](Brands/mariposa-baking-co.md) |
| Mast Brothers | brand | chocolate | packaging-design, craft-aesthetics, brand-storytelling, cautionary | watch | [Brands/mast-brothers.md](Brands/mast-brothers.md) |
| Moscot | brand | eyewear, accessories | eyewear, heritage, new-york, craft | canon | [Brands/moscot.md](Brands/moscot.md) |
| Motown | brand | music, record labels | systems-as-creativity, hit-factory, artist-development, institution-building | canon | [Brands/motown.md](Brands/motown.md) |
| Nayara Springs | brand | travel, hospitality, experiences | five-star-hospitality, pinnacle-standard, experience-design, ritual | canon | [Brands/nayara-springs.md](Brands/nayara-springs.md) |
| Nike | brand | fashion, footwear, athletics | selective-alignment, sub-line-curation, sneaker, high-low | canon | [Brands/nike.md](Brands/nike.md) |
| Nubian Heritage | brand | bath and body, personal care | heritage, african-black-soap, diaspora | canon | [Brands/nubian-heritage.md](Brands/nubian-heritage.md) |
| Olive and Sinclair | brand | chocolate | southern, place-rooted, craft, bean-to-bar | canon | [Brands/olive-and-sinclair.md](Brands/olive-and-sinclair.md) |
| Our Legacy | brand | fashion | scandinavian, fabric-first, textured, restraint | canon | [Brands/our-legacy.md](Brands/our-legacy.md) |
| Paraboot | brand | footwear, fashion | french, heritage, footwear, craft | canon | [Brands/paraboot.md](Brands/paraboot.md) |
| PlayStation | brand | gaming, hardware, entertainment | world-building, platform-ecosystem, brand-identity, immersive-atmosphere | canon | [Brands/playstation.md](Brands/playstation.md) |
| Prada | brand | fashion, leather goods | intellectual-fashion, restraint, materiality, anti-pretty | canon | [Brands/prada.md](Brands/prada.md) |
| Puebco | brand | home goods, interior design | found-materials, patina, imperfection-as-design, high-low | canon | [Brands/puebco.md](Brands/puebco.md) |
| Ralph Lauren | brand | fashion | americana, quiet-luxury, tiered-curation, logo-avoidance | canon | [Brands/ralph-lauren.md](Brands/ralph-lauren.md) |
| Rapha | brand | cycling, fashion | cycling, performance, premium, community | canon | [Brands/rapha.md](Brands/rapha.md) |
| Rieti | brand | eyewear, accessories | eyewear, korean, accessible-cool, detail | active | [Brands/rieti.md](Brands/rieti.md) |
| Salt and Stone | brand | deodorant, skincare | deodorant, elevated-design, fragrance-led | canon | [Brands/salt-and-stone.md](Brands/salt-and-stone.md) |
| Santa Maria Novella | brand | fragrance, grooming | heritage-craft, apothecary, cross-category, ritual | canon | [Brands/santa-maria-novella.md](Brands/santa-maria-novella.md) |
| Scribe Winery | brand | wine | natural-wine, place-as-experience, minimal-intervention, new-world | canon | [Brands/scribe-winery.md](Brands/scribe-winery.md) |
| Seasons | brand | home fragrance, diffusers, interior design | diffuser-as-object, design-conscious, ritual, scent | active | [Brands/seasons.md](Brands/seasons.md) |
| Singita | brand | travel, hospitality, conservation | five-star-hospitality, conservation-luxury, sense-of-place, ritual | canon | [Brands/singita.md](Brands/singita.md) |
| Steam | brand | gaming, software, digital distribution | platform-ecosystem, distribution, community, merchandising | canon | [Brands/steam.md](Brands/steam.md) |
| Stüssy | brand | fashion, streetwear | streetwear, surf, heritage, high-low | canon | [Brands/stussy.md](Brands/stussy.md) |
| Uniqlo | brand | fashion | foundation-fashion, quality-basics, anti-logo, restraint | canon | [Brands/uniqlo.md](Brands/uniqlo.md) |
| Vans | brand | footwear, fashion | skate, heritage, foundation-fashion, high-low | canon | [Brands/vans.md](Brands/vans.md) |
| West Elm | brand | furniture, home goods, retail | certified-sourcing, artisan-collaboration, accessible-modern, positioning | canon | [Brands/west-elm.md](Brands/west-elm.md) |
| Yves Saint Laurent | brand | fashion | tailoring, androgyny, parisian, statement | canon | [Brands/yves-saint-laurent.md](Brands/yves-saint-laurent.md) |

### Works

| Entity | Type | Domains | Pull for | Status | Card |
|---|---|---|---|---|---|
| Albert Einstein Education and Research Center | work | architecture, institutional, landscape | biophilic, spatial-direction, color-and-light, atrium | canon | [Works/albert-einstein-education-research-center.md](Works/albert-einstein-education-research-center.md) |
| Astroworld | work | music | sound-design, world-building, immersive-atmosphere, ear-candy | canon | [Works/astroworld.md](Works/astroworld.md) |
| Baccarat Rouge 540 Extrait | work | fragrance | oriental-floral, status-scent, amber, cultural-reach | canon | [Works/baccarat-rouge-540-extrait.md](Works/baccarat-rouge-540-extrait.md) |
| Bal d'Afrique | work | fragrance | woody-floral-musk, modern-classic, warm, gateway-niche | canon | [Works/bal-dafrique.md](Works/bal-dafrique.md) |
| Bonhomía | work | restaurant, salumeria | salumeria, convivial, indoor-outdoor, hospitality | canon | [Works/bonhomia.md](Works/bonhomia.md) |
| Breaking Bad | work | television | narrative, character-study, long-form-structure, pride-and-hubris | canon | [Works/breaking-bad.md](Works/breaking-bad.md) |
| Building Frame of the House | work | architecture, residential | materiality, spatial-direction, structural-honesty, small-space-ingenuity | canon | [Works/building-frame-of-the-house.md](Works/building-frame-of-the-house.md) |
| Chess | work | gaming, strategy | strategy, constraint-as-depth, timeless-system, mastery | canon | [Works/chess.md](Works/chess.md) |
| Dallas Buyers Club | work | film | transformation, defiance, total-commitment, against-the-system | canon | [Works/dallas-buyers-club.md](Works/dallas-buyers-club.md) |
| Django Unchained | work | film | narrative, genre-inversion, style-as-resistance, power-and-identity | canon | [Works/django-unchained.md](Works/django-unchained.md) |
| Dromeas (The Runner) | work | sculpture, public art | glass, motion, materiality, public-sculpture | canon | [Works/dromeas.md](Works/dromeas.md) |
| Dune | work | furniture, design | furniture-as-topography, modular, status-object, world-building | canon | [Works/dune-pierre-paulin.md](Works/dune-pierre-paulin.md) |
| Everything Everywhere All at Once | work | film | narrative, tonal-range, formal-experimentation, emotional-honesty | canon | [Works/everything-everywhere-all-at-once.md](Works/everything-everywhere-all-at-once.md) |
| Fallingwater | work | architecture, residential | nature-integration, materiality, spatial-direction, restraint | canon | [Works/fallingwater.md](Works/fallingwater.md) |
| Forrest Gump | work | film | innocence-as-wisdom, americana, sentiment, history | canon | [Works/forrest-gump.md](Works/forrest-gump.md) |
| Good Will Hunting | work | film | narrative, emotional-suppression, cost-of-greatness, mentor-dynamics | canon | [Works/good-will-hunting.md](Works/good-will-hunting.md) |
| Holocaust Memorial Miami Beach | work | architecture, memorial, sculpture | memorial, monumental, emotional-weight, spatial-direction | canon | [Works/holocaust-memorial-miami-beach.md](Works/holocaust-memorial-miami-beach.md) |
| Homegoing | work | literature | narrative, structure-as-argument, diaspora, historical-weight | canon | [Works/homegoing-yaa-gyasi.md](Works/homegoing-yaa-gyasi.md) |
| Lafayette Street | work | fragrance | fresh-woody-musk, versatile, new-york, easy-wear | canon | [Works/lafayette-street.md](Works/lafayette-street.md) |
| L'Homme à la Rose | work | fragrance | masculine-floral, rose, elegant, prestige | canon | [Works/lhomme-a-la-rose.md](Works/lhomme-a-la-rose.md) |
| Menace II Society | work | film | hood-realism, coming-of-age, fatalism, black-cinema | canon | [Works/menace-ii-society.md](Works/menace-ii-society.md) |
| Millésime Impérial | work | fragrance | marine, aquatic-citrus, warm-weather, fresh-luxury | canon | [Works/millesime-imperial.md](Works/millesime-imperial.md) |
| My Beautiful Dark Twisted Fantasy | work | music | sound-design, world-building, maximalism, ambition-as-form | canon | [Works/my-beautiful-dark-twisted-fantasy.md](Works/my-beautiful-dark-twisted-fantasy.md) |
| Naruto: Shippuden | work | animation, television | narrative, world-building, found-family, perseverance-and-identity | canon | [Works/naruto-shippuden.md](Works/naruto-shippuden.md) |
| One Piece | work | animation | narrative, world-building, long-form-structure, found-family | canon | [Works/one-piece.md](Works/one-piece.md) |
| Oud Ispahan | work | fragrance | oud, rose-oud, refined, collection-privee | canon | [Works/oud-ispahan.md](Works/oud-ispahan.md) |
| Pulp Fiction | work | film | nonlinear-structure, dialogue-as-set-piece, high-low, needle-drop | canon | [Works/pulp-fiction.md](Works/pulp-fiction.md) |
| Ready Player One | work | literature, film, gaming | world-building, immersive-atmosphere, virtual-world, nostalgia | canon | [Works/ready-player-one.md](Works/ready-player-one.md) |
| Renaissance | work | music | sound-design, Black-joy, house-culture, precision-as-freedom | canon | [Works/renaissance-beyonce.md](Works/renaissance-beyonce.md) |
| Reservoir Dogs | work | film | nonlinear-structure, dialogue-as-suspense, restraint-of-means, debut-grammar | canon | [Works/reservoir-dogs.md](Works/reservoir-dogs.md) |
| Roka Akor | work | restaurant, japanese | robatayaki, japanese, moody-dining, hospitality | canon | [Works/roka-akor.md](Works/roka-akor.md) |
| Scarface | work | film | narrative, ambition-and-hubris, cost-of-the-climb, dramatic-inevitability | canon | [Works/scarface.md](Works/scarface.md) |
| Selena | work | film | narrative, cultural-identity, crossover-ambition, legacy | canon | [Works/selena-film.md](Works/selena-film.md) |
| Sex and the City | work | television | editorial, voice-and-tone, narrative, desire-and-identity | canon | [Works/sex-and-the-city.md](Works/sex-and-the-city.md) |
| Sex Education | work | television | voice-and-tone, vulnerability, community-dynamics, British-comedic-lens | canon | [Works/sex-education.md](Works/sex-education.md) |
| The Fresh Prince of Bel-Air | work | television | voice-and-tone, code-switching, cultural-identity, humor-as-armor | canon | [Works/fresh-prince-of-bel-air.md](Works/fresh-prince-of-bel-air.md) |
| The One | work | fragrance | oriental-spicy, tobacco-amber, masculine-benchmark, accessible | canon | [Works/the-one.md](Works/the-one.md) |
| Ushiku Daibutsu | work | architecture, monument, sculpture | monumental, inhabitable-sculpture, scale, spatial-direction | canon | [Works/ushiku-daibutsu.md](Works/ushiku-daibutsu.md) |
| Whiplash | work | film | narrative, pacing, cost-of-greatness | canon | [Works/whiplash.md](Works/whiplash.md) |
| Young Rose | work | fragrance | floral-woody-musk, modern-rose, unisex, restrained | canon | [Works/young-rose.md](Works/young-rose.md) |

### Curators

Editorial and retail tastemakers.

| Entity | Type | Domains | Pull for | Status | Card |
|---|---|---|---|---|---|
| Architectural Digest | curator | architecture, interior design, media | editorial, interiors, taste-proxy, luxury-homes | canon | [Curators/architectural-digest.md](Curators/architectural-digest.md) |
| Dover Street Market | curator | fashion, retail | merchandising, spatial-direction, high-low, curation-strategy | canon | [Curators/dover-street-market.md](Curators/dover-street-market.md) |
| Mr Porter | curator | fashion, menswear | menswear-curation, editorial-filter, taste-proxy, secondary-storefront | canon | [Curators/mr-porter.md](Curators/mr-porter.md) |
| Sylvia Rhone | curator | music, record labels, a&r | taste-authority, curation-strategy, anti-silo, artist-development | canon | [Curators/sylvia-rhone.md](Curators/sylvia-rhone.md) |

Aesthetic styles and movements – filed as curators, with the movement or vernacular standing as the tastemaking context.

| Entity | Type | Domains | Pull for | Status | Card |
|---|---|---|---|---|---|
| Biophilic | curator | architecture, interior design, landscape | biophilic, nature-integration, greenery, wellbeing | canon | [Curators/biophilic.md](Curators/biophilic.md) |
| Brownstone | curator | architecture, interior design, urbanism | historical-fabric, urban-vernacular, materiality, warmth | canon | [Curators/brownstone.md](Curators/brownstone.md) |
| Brutalist | curator | architecture, interior design | materiality, raw-and-warm, sculptural-mass, monumental | canon | [Curators/brutalist.md](Curators/brutalist.md) |
| California Bungalow | curator | architecture, interior design, residential | craftsman, joinery, horizontal-massing, indoor-outdoor | canon | [Curators/california-bungalow.md](Curators/california-bungalow.md) |
| Feng Shui | curator | interior design, spatial philosophy | spatial-arrangement, energy-flow, ritual, wellbeing | canon | [Curators/feng-shui.md](Curators/feng-shui.md) |
| French Provincial | curator | architecture, interior design | materiality, warmth, rustic-refinement, craftsmanship | active | [Curators/french-provincial.md](Curators/french-provincial.md) |
| Industrial | curator | architecture, interior design | materiality, loft, exposed-structure, raw-and-warm | canon | [Curators/industrial.md](Curators/industrial.md) |
| Japandi | curator | interior design | natural-materials, pared-palette, quiet-warmth, restraint | canon | [Curators/japandi.md](Curators/japandi.md) |
| Mediterranean | curator | architecture, interior design | materiality, indoor-outdoor, warmth, color-and-light | canon | [Curators/mediterranean.md](Curators/mediterranean.md) |
| Midcentury Modern | curator | architecture, interior design, furniture | clean-line, organic-shape, warm-modernism, furniture-as-icon | canon | [Curators/midcentury-modern.md](Curators/midcentury-modern.md) |
| Modern | curator | architecture, interior design | clean-line, open-plan, form-follows-function, restraint | canon | [Curators/modern.md](Curators/modern.md) |
| Native Plant Gardens | curator | landscape, gardening, ecology | habitat-gardening, native-species, nature-integration, biophilic | canon | [Curators/native-plant-gardens.md](Curators/native-plant-gardens.md) |
| Organic Modern | curator | interior design | warm-minimalism, sculptural-silhouette, earthy-palette, tactile | canon | [Curators/organic-modern.md](Curators/organic-modern.md) |
| Speakeasy | curator | interior design, hospitality | concealment, moody-intimacy, ritual, world-building | canon | [Curators/speakeasy.md](Curators/speakeasy.md) |
| Surrealism | curator | visual art, literature, film | dream-logic, the-uncanny, juxtaposition, conviction | canon | [Curators/surrealism.md](Curators/surrealism.md) |
| Tropical Modernism | curator | architecture, interior design | indoor-outdoor, climate-responsive, passive-cooling, materiality | canon | [Curators/tropical-modernism.md](Curators/tropical-modernism.md) |
| Verdant | curator | interior design | green-saturation, plant-density, garden-room, biophilic | active | [Curators/verdant.md](Curators/verdant.md) |
| West African Modern | curator | architecture, interior design | heritage-forward, textile-and-symbol, diaspora, cultural-bridge | active | [Curators/west-african-modern.md](Curators/west-african-modern.md) |

Mediums and formats – immersive mediums and game, social and betting formats held as creative contexts.

| Entity | Type | Domains | Pull for | Status | Card |
|---|---|---|---|---|---|
| Augmented Reality | curator | gaming, technology, immersive media | layered-reality, context-as-content, spatial-direction, overlay | canon | [Curators/augmented-reality.md](Curators/augmented-reality.md) |
| Murder Mystery Parties | curator | gaming, social games, hospitality | participation, role-play, ritual, hospitality | canon | [Curators/murder-mystery-parties.md](Curators/murder-mystery-parties.md) |
| Sportsbooks | curator | gaming, sports betting, finance | odds-as-product, engagement-loop, positioning, conversion | canon | [Curators/sportsbooks.md](Curators/sportsbooks.md) |
| Virtual Reality | curator | gaming, technology, immersive media | immersive-atmosphere, presence, world-building, spatial-direction | canon | [Curators/virtual-reality.md](Curators/virtual-reality.md) |

Typologies and features – dwelling typologies, home features and design techniques held as creative contexts.

| Entity | Type | Domains | Pull for | Status | Card |
|---|---|---|---|---|---|
| Ambient Lighting | curator | interior design, lighting | color-and-light, light-as-material, warmth, atmosphere | canon | [Curators/ambient-lighting.md](Curators/ambient-lighting.md) |
| The Dream Home | curator | architecture, interior design, residential | dream-home-standard, nature-inside, engineering-of-ease, personal-canon | active | [Curators/the-dream-home.md](Curators/the-dream-home.md) |
| Homestead | curator | land, lifestyle, sustainability | self-sufficiency, land-as-system, food-production, sustainability | canon | [Curators/homestead.md](Curators/homestead.md) |
| Houseboats | curator | architecture, dwelling, travel | floating-dwelling, water-living, regional-vernacular, adaptive-reuse | canon | [Curators/houseboats.md](Curators/houseboats.md) |
| Outdoor Showers | curator | architecture, residential | open-air-bathing, ritual, coastal, elemental | canon | [Curators/outdoor-showers.md](Curators/outdoor-showers.md) |
| Smart Home | curator | interior design, technology | concealed-technology, integration, intelligent-comfort, restraint | canon | [Curators/smart-home.md](Curators/smart-home.md) |
| Solariums | curator | architecture, interior design | light-capture, glass-room, color-and-light, indoor-outdoor | canon | [Curators/solariums.md](Curators/solariums.md) |
| Sunroofs | curator | architecture, residential | open-sky, transformation, light-capture, indoor-outdoor | canon | [Curators/sunroofs.md](Curators/sunroofs.md) |
| Treehouses | curator | architecture, hospitality, travel | nature-immersion, elevated-perspective, hospitality, world-building | canon | [Curators/treehouses.md](Curators/treehouses.md) |

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

**Creators:** Mike Dean, Noah "40" Shebib, Kendrick Lamar, Future, Young Thug, Donald Glover, Michelangelo, Masashi Kishimoto, Eiichiro Oda, Michael Singer, Myron Golden, Alex Hormozi**Brands – stationery and analog:** Leuchtturm1917, Midori, Kaweco, Stalogy, Rhodia, Blackwing, Smythson

**Brands – publishing:** Rizzoli, Taschen, Phaidon, Assouline

**Brands – homeware:** Hay, Iittala, Kinto, The Conran Shop, John Derian
**Brands – plants and flowers:** The Sill, Bloomscape, Terrain, Urban Stems, Farmgirl Flowers

**Brands – experiences and other:** Londolozi Game Reserve, Aire Ancient Baths, Bathhouse Brooklyn, Resy, MasterClass, Apple

**Curators:** Goodhood, SSENSE, END.

**Works – albums:** Blonde, Coloring Book, Good Kid M.A.A.D City, Swimming, The Miseducation of Lauryn Hill

---

*Personal Reference Library. Created 2026-06-21 under the Manor Protocol. Venture libraries live in each venture Knowledge Base, isolated.*
