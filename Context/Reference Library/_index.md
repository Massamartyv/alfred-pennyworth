---
file_type: reference_library_index
scope: personal
created: 2026-06-21
last_updated: 2026-08-04
---

# Reference Library

A curated corpus of the creators, brands, works and curators that inform research, inspiration and creative direction. Alfred draws on this library when a task needs a batch of grounded reference – what is working, what to extract, which canon to draw from – rather than reasoning from a blank page.

This is the personal library. Every venture holds its own isolated Reference Library inside its Knowledge Base. Personal and venture references never share a file.

**This corpus is canonical.** A mirror lives in the Notion personal workspace for reading and capture away from the Mac, inside the Resources row named Reference Library, beside the References capture inbox. The mirror is written from here and never hand-edited into disagreement: anything added on the phone lands at status **Card pending** and is harvested back into a card here. When the two disagree, the markdown wins.

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
tags: [restraint, genre-defiance]  # legacy, free-form, not a retrieval surface
pull_for: [restraint, craft]       # controlled vocabulary, the retrieval surface
themes: [legacy, transformation]   # optional, the reflective axis
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

A controlled tag set keeps retrieval consistent. Rebuilt 2026-09-14 from all 255 cards, replacing
a set that had drifted to 698 terms, 557 of them used exactly once. The field carries retrieval
handles only: what kind of task should summon this card. Subject descriptors belong in `domains`,
thematic content in `themes`.

Cards carry the controlled vocabulary in the `pull_for` frontmatter field, which is the machine-readable
source for both this registry and the Notion mirror. The prose **Pull for** line in each card body is
the original authored wording and is left untouched, as is the legacy `tags` field. Neither is a
retrieval surface; `pull_for` is.

- **Posture** – restraint, maximalism, high-low, subversion, reinvention, conviction, anti-logo
- **Voice and story** – voice-and-tone, narrative, world-building, editorial, cadence, long-form-structure
- **Visual and space** – art-direction, spatial-direction, materiality, color-and-light, typography, scale
- **Atmosphere** – immersive-atmosphere, warmth, texture
- **Sound** – sound-design
- **Craft** – craft, fabric-first, precision, provenance, structural-honesty
- **Strategy and offer** – positioning, offer-design, merchandising, hospitality, ritual, institution-building, ownership-as-strategy, curation-strategy, taste-authority
- **Argument and rhetoric** – rhetoric, moral-clarity, essay-as-form, self-authorship, proof-as-argument, evidence, self-education
- **Nature and place** – biophilic, nature-integration, indoor-outdoor, sense-of-place, wellbeing
- **Heritage** – heritage, diaspora, cultural-bridge
- **Register** – quiet-luxury, investment-luxury, accessible-luxury

Extend the set deliberately. A handle earns its place by serving retrieval across more than one card;
anything that describes a single entity is a domain, not a handle.

## Themes vocabulary

The reflective axis, carried in the `themes` frontmatter field. What a reference is about rather than
how it works. Mostly Works, and the axis that serves the Personal Development, Social Development and
Education spheres.

coming-of-age, cost-of-greatness, ambition-and-hubris, moral-decay, class-and-identity, cultural-identity,
belonging-and-exclusion, found-family, mentor-dynamics, legacy, transformation, perseverance, vulnerability,
emotional-honesty, nostalgia, fatalism, dreams-and-ambition, self-invention

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
| Adele | creator | music, vocal performance | restraint, voice-and-tone, subversion, positioning, conviction | canon | [Creators/adele.md](Creators/adele.md) |
| Alberto Kalach | creator | architecture, urbanism, landscape | biophilic, materiality, spatial-direction, nature-integration, world-building | canon | [Creators/alberto-kalach.md](Creators/alberto-kalach.md) |
| Alex Guarnaschelli | creator | culinary, restaurants | craft, precision, hospitality, warmth | canon | [Creators/alex-guarnaschelli.md](Creators/alex-guarnaschelli.md) |
| Alexander Nguyen | creator | fashion | restraint, texture, quiet-luxury | watch | [Creators/alexander-nguyen.md](Creators/alexander-nguyen.md) |
| André 3000 | creator | music, fashion, film | voice-and-tone, reinvention, restraint, conviction, subversion | canon | [Creators/andre-3000.md](Creators/andre-3000.md) |
| André Leon Talley | creator | fashion, editorial, media | editorial, taste-authority, voice-and-tone, cultural-bridge | canon | [Creators/andre-leon-talley.md](Creators/andre-leon-talley.md) |
| Andy Warhol | creator | visual art, film, pop culture | high-low, positioning, art-direction | canon | [Creators/andy-warhol.md](Creators/andy-warhol.md) |
| Anthony Bourdain | creator | food, travel, culture | narrative, taste-authority, hospitality, cultural-bridge | canon | [Creators/anthony-bourdain.md](Creators/anthony-bourdain.md) |
| A$AP Rocky | creator | fashion, music | art-direction, high-low | canon | [Creators/asap-rocky.md](Creators/asap-rocky.md) |
| Bad Bunny | creator | fashion, music | materiality, color-and-light | canon | [Creators/bad-bunny.md](Creators/bad-bunny.md) |
| Banksy | creator | visual art, street art | subversion | canon | [Creators/banksy.md](Creators/banksy.md) |
| Ben Taylor | creator | fashion, accessories, luxury, interior design | investment-luxury, positioning, merchandising | active | [Creators/ben-taylor.md](Creators/ben-taylor.md) |
| Benjamin Banneker | creator | mathematics, astronomy, surveying, publishing | proof-as-argument, self-education, precision, high-low | canon | [Creators/benjamin-banneker.md](Creators/benjamin-banneker.md) |
| Beyoncé | creator | music, performance | precision, heritage, cadence | canon | [Creators/beyonce.md](Creators/beyonce.md) |
| Bobby Flay | creator | culinary, restaurants | institution-building, hospitality | canon | [Creators/bobby-flay.md](Creators/bobby-flay.md) |
| Brian De Palma | creator | film, directing | art-direction, long-form-structure, maximalism | canon | [Creators/brian-de-palma.md](Creators/brian-de-palma.md) |
| Brooke Williamson | creator | culinary, restaurants | provenance, craft, hospitality | canon | [Creators/brooke-williamson.md](Creators/brooke-williamson.md) |
| Cal Cologne | creator | fragrance | curation-strategy | watch | [Creators/cal-cologne.md](Creators/cal-cologne.md) |
| Caroline Shaw | creator | music, composition, vocal music | high-low, sound-design, reinvention, craft, cultural-bridge | canon | [Creators/caroline-shaw.md](Creators/caroline-shaw.md) |
| Claude Monet | creator | visual art | color-and-light, immersive-atmosphere, biophilic | canon | [Creators/claude-monet.md](Creators/claude-monet.md) |
| Colman Domingo | creator | fashion, acting | art-direction, restraint, materiality, conviction | canon | [Creators/colman-domingo.md](Creators/colman-domingo.md) |
| Damien Chazelle | creator | film, directing | sound-design, art-direction, narrative | canon | [Creators/damien-chazelle.md](Creators/damien-chazelle.md) |
| Dan Harmon | creator | television, writing | narrative, long-form-structure, world-building, voice-and-tone | canon | [Creators/dan-harmon.md](Creators/dan-harmon.md) |
| Do Ho Suh | creator | installation, sculpture, architecture | spatial-direction, materiality | canon | [Creators/do-ho-suh.md](Creators/do-ho-suh.md) |
| Dries Van Noten | creator | fashion | materiality, fabric-first, restraint | canon | [Creators/dries-van-noten.md](Creators/dries-van-noten.md) |
| Eddie Jackson | creator | culinary, restaurants | precision | canon | [Creators/eddie-jackson.md](Creators/eddie-jackson.md) |
| Edward Tufte | creator | data visualisation, information design, statistics | structural-honesty, evidence, restraint | watch | [Creators/edward-tufte.md](Creators/edward-tufte.md) |
| Eric Adjepong | creator | culinary, restaurants | diaspora, heritage, cultural-bridge | canon | [Creators/eric-adjepong.md](Creators/eric-adjepong.md) |
| Frank Lloyd Wright | creator | architecture, interior design, furniture | spatial-direction, materiality, nature-integration, art-direction | canon | [Creators/frank-lloyd-wright.md](Creators/frank-lloyd-wright.md) |
| Frank Ocean | creator | music, production, aesthetics | sound-design, voice-and-tone, restraint, immersive-atmosphere | canon | [Creators/frank-ocean.md](Creators/frank-ocean.md) |
| Frederick Douglass | creator | oratory, autobiography, publishing, photography | rhetoric, self-authorship, ownership-as-strategy, art-direction | canon | [Creators/frederick-douglass.md](Creators/frederick-douglass.md) |
| Gunna | creator | music, hip-hop, atlanta | voice-and-tone, cadence | canon | [Creators/gunna.md](Creators/gunna.md) |
| Gus Van Sant | creator | film, directing | restraint, narrative | canon | [Creators/gus-van-sant.md](Creators/gus-van-sant.md) |
| Gustavo Piers Milton | creator | fashion | editorial, subversion, art-direction | watch | [Creators/gustavo-piers-milton.md](Creators/gustavo-piers-milton.md) |
| James Baldwin | creator | literature, essay, cultural criticism | voice-and-tone, moral-clarity, essay-as-form, cadence, self-authorship | canon | [Creators/james-baldwin.md](Creators/james-baldwin.md) |
| James Cameron | creator | film, directing, technology | world-building, immersive-atmosphere, maximalism, precision, scale | canon | [Creators/james-cameron.md](Creators/james-cameron.md) |
| Jean-Michel Basquiat | creator | visual art | art-direction, texture, high-low, materiality | canon | [Creators/jean-michel-basquiat.md](Creators/jean-michel-basquiat.md) |
| Jet Tila | creator | culinary, restaurants | heritage, cultural-bridge | canon | [Creators/jet-tila.md](Creators/jet-tila.md) |
| Kanye West | creator | music, fashion, interior design, production | art-direction, color-and-light, materiality, reinvention, maximalism | canon | [Creators/kanye-west.md](Creators/kanye-west.md) |
| Kardea Brown | creator | culinary, restaurants, television | heritage, hospitality, cultural-bridge | canon | [Creators/kardea-brown.md](Creators/kardea-brown.md) |
| Kehinde Wiley | creator | visual art | subversion, art-direction, maximalism | canon | [Creators/kehinde-wiley.md](Creators/kehinde-wiley.md) |
| Kim Chong Hak | creator | visual art | color-and-light, nature-integration, restraint, materiality, subversion | canon | [Creators/kim-chong-hak.md](Creators/kim-chong-hak.md) |
| Kurt Cobain | creator | fashion, music | subversion, restraint | canon | [Creators/kurt-cobain.md](Creators/kurt-cobain.md) |
| Leonardo da Vinci | creator | visual art, science, engineering | reinvention, craft, precision | canon | [Creators/leonardo-da-vinci.md](Creators/leonardo-da-vinci.md) |
| Lil Uzi Vert | creator | music, hip-hop, rage | reinvention, positioning, high-low, world-building, conviction | canon | [Creators/lil-uzi-vert.md](Creators/lil-uzi-vert.md) |
| Logan Sylve | creator | visual art, illustration | high-low, art-direction | active | [Creators/logan-sylve.md](Creators/logan-sylve.md) |
| Malcolm X | creator | oratory, political thought, autobiography | rhetoric, reinvention, self-education, conviction | canon | [Creators/malcolm-x.md](Creators/malcolm-x.md) |
| Marcus Samuelsson | creator | culinary, restaurants | diaspora, cultural-bridge, hospitality, self-authorship | canon | [Creators/marcus-samuelsson.md](Creators/marcus-samuelsson.md) |
| Martin Scorsese | creator | film, directing | art-direction, sound-design, moral-clarity, narrative | canon | [Creators/martin-scorsese.md](Creators/martin-scorsese.md) |
| Michael Greger | creator | nutrition, food science, medicine | evidence, wellbeing | canon | [Creators/michael-greger.md](Creators/michael-greger.md) |
| Miguel | creator | music, r&b | art-direction, texture, sound-design, positioning, reinvention | canon | [Creators/miguel.md](Creators/miguel.md) |
| Mötley Crüe | creator | music, rock, spectacle | maximalism, art-direction, world-building, conviction | canon | [Creators/motley-crue.md](Creators/motley-crue.md) |
| Pablo Picasso | creator | visual art | reinvention, art-direction, conviction | canon | [Creators/pablo-picasso.md](Creators/pablo-picasso.md) |
| Page and Dornenburg | creator | food writing, flavor theory | craft | canon | [Creators/page-and-dornenburg.md](Creators/page-and-dornenburg.md) |
| Paula Scher | creator | graphic design, typography, identity, environmental graphics | typography, art-direction, high-low, maximalism, spatial-direction | canon | [Creators/paula-scher.md](Creators/paula-scher.md) |
| Pharrell | creator | fashion, music | art-direction, high-low | canon | [Creators/pharrell.md](Creators/pharrell.md) |
| Pierce and Ward | creator | interior design | spatial-direction, materiality, maximalism, restraint | canon | [Creators/pierce-and-ward.md](Creators/pierce-and-ward.md) |
| Quentin Tarantino | creator | film, directing | art-direction, subversion, maximalism | canon | [Creators/quentin-tarantino.md](Creators/quentin-tarantino.md) |
| Quincy Jones | creator | music, production, film, arranging | reinvention, craft, curation-strategy, cadence | canon | [Creators/quincy-jones.md](Creators/quincy-jones.md) |
| Rebecca Maria | creator | visual art, sculpture | art-direction, high-low | watch | [Creators/rebecca-maria.md](Creators/rebecca-maria.md) |
| Rihanna | creator | music, beauty, fashion, business | ownership-as-strategy, positioning, reinvention | canon | [Creators/rihanna.md](Creators/rihanna.md) |
| Ryan Coogler | creator | film, directing | world-building, art-direction, immersive-atmosphere, spatial-direction | canon | [Creators/ryan-coogler.md](Creators/ryan-coogler.md) |
| Salvador Dalí | creator | visual art, film | immersive-atmosphere, conviction, art-direction, maximalism | canon | [Creators/salvador-dali.md](Creators/salvador-dali.md) |
| Steven Spielberg | creator | film, directing | accessible-luxury, world-building, maximalism, narrative | canon | [Creators/steven-spielberg.md](Creators/steven-spielberg.md) |
| Takashi Murakami | creator | visual art, fashion | high-low, art-direction | canon | [Creators/takashi-murakami.md](Creators/takashi-murakami.md) |
| Tems | creator | music, r&b, afrobeats | restraint, ownership-as-strategy, voice-and-tone, cultural-bridge | canon | [Creators/tems.md](Creators/tems.md) |
| Travis Scott | creator | music, production, world-building | world-building, sound-design, immersive-atmosphere, narrative | canon | [Creators/travis-scott.md](Creators/travis-scott.md) |
| Tyler Durden | creator | fashion | subversion, maximalism, high-low, conviction | canon | [Creators/tyler-durden.md](Creators/tyler-durden.md) |
| Tyler, the Creator | creator | music | taste-authority, reinvention, conviction, craft, anti-logo | canon | [Creators/tyler-the-creator.md](Creators/tyler-the-creator.md) |
| Tyrod Taylor | creator | fashion | restraint, conviction | canon | [Creators/tyrod-taylor.md](Creators/tyrod-taylor.md) |
| Vince Gilligan | creator | television, writing | long-form-structure, narrative | canon | [Creators/vince-gilligan.md](Creators/vince-gilligan.md) |
| Virgil Abloh | creator | interior design, fashion, architecture | spatial-direction, art-direction, restraint, reinvention | canon | [Creators/virgil-abloh.md](Creators/virgil-abloh.md) |
| Wisdom Kaye | creator | fashion, styling, modelling | high-low, art-direction, curation-strategy | canon | [Creators/wisdom-kaye.md](Creators/wisdom-kaye.md) |
| Wu-Tang Clan | creator | music, hip-hop, business strategy | institution-building, world-building, ownership-as-strategy, positioning | canon | [Creators/wu-tang-clan.md](Creators/wu-tang-clan.md) |
| Yayoi Kusama | creator | visual art | art-direction, immersive-atmosphere, world-building, high-low | canon | [Creators/yayoi-kusama.md](Creators/yayoi-kusama.md) |
| Yeat | creator | music, hip-hop, rage | world-building, sound-design, voice-and-tone, ownership-as-strategy | canon | [Creators/yeat.md](Creators/yeat.md) |
### Brands

| Entity | Type | Domains | Pull for | Status | Card |
|---|---|---|---|---|---|
| Abercrombie | brand | fashion | positioning, accessible-luxury | canon | [Brands/abercrombie.md](Brands/abercrombie.md) |
| Acne Studios | brand | fashion | restraint, subversion | canon | [Brands/acne-studios.md](Brands/acne-studios.md) |
| Aesop | brand | grooming, interior design | art-direction, ritual, restraint, spatial-direction | canon | [Brands/aesop.md](Brands/aesop.md) |
| Aimé Leon Dore | brand | fashion, streetwear | high-low, world-building, cultural-bridge | canon | [Brands/aime-leon-dore.md](Brands/aime-leon-dore.md) |
| Alden | brand | footwear, fashion | heritage, craft | canon | [Brands/alden.md](Brands/alden.md) |
| Ami Paris | brand | fashion | accessible-luxury, restraint | canon | [Brands/ami-paris.md](Brands/ami-paris.md) |
| ARKET | brand | fashion, homeware | merchandising, accessible-luxury | canon | [Brands/arket.md](Brands/arket.md) |
| Auralee | brand | fashion | fabric-first, quiet-luxury, materiality | canon | [Brands/auralee.md](Brands/auralee.md) |
| Baserange | brand | fashion | materiality, nature-integration, restraint | canon | [Brands/baserange.md](Brands/baserange.md) |
| Blackstock and Weber | brand | footwear, fashion | conviction | canon | [Brands/blackstock-and-weber.md](Brands/blackstock-and-weber.md) |
| Blue Bottle Coffee | brand | coffee | provenance, restraint, craft, ritual | canon | [Brands/blue-bottle-coffee.md](Brands/blue-bottle-coffee.md) |
| Bond No. 9 | brand | fragrance | sense-of-place, investment-luxury | canon | [Brands/bond-no-9.md](Brands/bond-no-9.md) |
| Bottega Veneta | brand | fragrance | quiet-luxury, restraint | canon | [Brands/bottega-veneta.md](Brands/bottega-veneta.md) |
| Brooklyn Circus | brand | fashion | heritage, narrative, high-low | canon | [Brands/brooklyn-circus.md](Brands/brooklyn-circus.md) |
| Buly 1803 | brand | fragrance, grooming | heritage, craft, world-building, ritual | canon | [Brands/buly-1803.md](Brands/buly-1803.md) |
| Burlap and Barrel | brand | spices, pantry | provenance | canon | [Brands/burlap-and-barrel.md](Brands/burlap-and-barrel.md) |
| Byredo | brand | fragrance | art-direction | canon | [Brands/byredo.md](Brands/byredo.md) |
| Cécred | brand | haircare, personal care | investment-luxury, ownership-as-strategy | canon | [Brands/cecred.md](Brands/cecred.md) |
| Celine | brand | fashion, leather goods | quiet-luxury, restraint | canon | [Brands/celine.md](Brands/celine.md) |
| Cire Trudon | brand | fragrance | heritage, restraint | canon | [Brands/cire-trudon.md](Brands/cire-trudon.md) |
| Clare Paint | brand | paint, interior design | curation-strategy, color-and-light, offer-design, restraint, positioning | canon | [Brands/clare-paint.md](Brands/clare-paint.md) |
| Clive Christian | brand | fragrance | investment-luxury, maximalism, heritage | canon | [Brands/clive-christian.md](Brands/clive-christian.md) |
| Common Projects | brand | footwear, fashion | restraint, precision | canon | [Brands/common-projects.md](Brands/common-projects.md) |
| COS | brand | fashion | restraint, accessible-luxury | canon | [Brands/cos.md](Brands/cos.md) |
| Crate and Barrel | brand | home goods, furniture, retail | merchandising, accessible-luxury, heritage | canon | [Brands/crate-and-barrel.md](Brands/crate-and-barrel.md) |
| Creed | brand | fragrance | heritage, investment-luxury | canon | [Brands/creed.md](Brands/creed.md) |
| Def Jam Recordings | brand | music, record labels, hip-hop | institution-building, reinvention, positioning | canon | [Brands/def-jam.md](Brands/def-jam.md) |
| Diaspora Co. | brand | spices, pantry | provenance, subversion, positioning | canon | [Brands/diaspora-co.md](Brands/diaspora-co.md) |
| Dick Taylor | brand | chocolate | provenance, craft, materiality, restraint | canon | [Brands/dick-taylor.md](Brands/dick-taylor.md) |
| Dior | brand | fragrance | investment-luxury, heritage | canon | [Brands/dior.md](Brands/dior.md) |
| Diptyque | brand | fragrance | heritage, restraint | canon | [Brands/diptyque.md](Brands/diptyque.md) |
| Dolce and Gabbana | brand | fragrance | accessible-luxury | canon | [Brands/dolce-and-gabbana.md](Brands/dolce-and-gabbana.md) |
| Dr. Bronner's | brand | personal care, soap | moral-clarity, heritage, ritual | canon | [Brands/dr-bronners.md](Brands/dr-bronners.md) |
| Drake's | brand | fashion | restraint | canon | [Brands/drakes.md](Brands/drakes.md) |
| Duke and Dexter | brand | footwear, fashion | conviction | canon | [Brands/duke-and-dexter.md](Brands/duke-and-dexter.md) |
| Erin McKenna's Bakery | brand | bakery | precision, craft | canon | [Brands/erin-mckennas-bakery.md](Brands/erin-mckennas-bakery.md) |
| FanDuel | brand | gaming, sports betting, fantasy sports | positioning, offer-design | canon | [Brands/fanduel.md](Brands/fanduel.md) |
| Frog's Leap | brand | wine | nature-integration, craft | canon | [Brands/frogs-leap.md](Brands/frogs-leap.md) |
| Golden Goose | brand | footwear, fashion | texture, conviction, high-low | canon | [Brands/golden-goose.md](Brands/golden-goose.md) |
| Goyard | brand | fashion, accessories, travel | heritage, quiet-luxury | canon | [Brands/goyard.md](Brands/goyard.md) |
| Harney and Sons | brand | tea | craft, art-direction, accessible-luxury | canon | [Brands/harney-and-sons.md](Brands/harney-and-sons.md) |
| Hermès | brand | fashion, accessories, homeware | investment-luxury, craft, positioning | canon | [Brands/hermes.md](Brands/hermes.md) |
| House of Nangman | brand | fashion, accessories | positioning, narrative | active | [Brands/house-of-nangman.md](Brands/house-of-nangman.md) |
| Innersense | brand | haircare, personal care | precision | canon | [Brands/innersense.md](Brands/innersense.md) |
| Isabel Marant | brand | fashion | restraint | canon | [Brands/isabel-marant.md](Brands/isabel-marant.md) |
| Italic | brand | home goods, marketplace, fashion | anti-logo, materiality, positioning, merchandising | canon | [Brands/italic.md](Brands/italic.md) |
| Jeni's Splendid Ice Creams | brand | ice cream, dessert | craft | canon | [Brands/jenis-splendid-ice-creams.md](Brands/jenis-splendid-ice-creams.md) |
| Keplinger | brand | wine | provenance | canon | [Brands/keplinger.md](Brands/keplinger.md) |
| Kettl | brand | tea | provenance, taste-authority | canon | [Brands/kettl.md](Brands/kettl.md) |
| Kiehl's | brand | skincare, personal care | heritage, craft | canon | [Brands/kiehls.md](Brands/kiehls.md) |
| Kreation Organic | brand | juice, cafe, wellness | wellbeing, ritual | canon | [Brands/kreation-organic.md](Brands/kreation-organic.md) |
| La Colombe | brand | coffee | offer-design, provenance, scale, craft | canon | [Brands/la-colombe.md](Brands/la-colombe.md) |
| La Maison du Chocolat | brand | chocolate | investment-luxury, restraint, heritage, craft | canon | [Brands/la-maison-du-chocolat.md](Brands/la-maison-du-chocolat.md) |
| Le Labo | brand | fragrance | ritual, anti-logo, hospitality | canon | [Brands/le-labo.md](Brands/le-labo.md) |
| Lemaire | brand | fashion | materiality, anti-logo, restraint, quiet-luxury | canon | [Brands/lemaire.md](Brands/lemaire.md) |
| Levain Bakery | brand | bakery, dessert | positioning, craft, restraint | canon | [Brands/levain-bakery.md](Brands/levain-bakery.md) |
| Liverpool FC | brand | sports, identity, culture | world-building | canon | [Brands/liverpool-fc.md](Brands/liverpool-fc.md) |
| Loewe | brand | fashion, leather goods | investment-luxury, craft, materiality, art-direction | canon | [Brands/loewe.md](Brands/loewe.md) |
| Louis Vuitton | brand | fashion, leather goods, fragrance | investment-luxury, high-low, world-building, craft | canon | [Brands/louis-vuitton.md](Brands/louis-vuitton.md) |
| Lulu and Georgia | brand | home decor, furniture | curation-strategy, heritage, merchandising, warmth | canon | [Brands/lulu-and-georgia.md](Brands/lulu-and-georgia.md) |
| Lululemon | brand | activewear, fashion | positioning | canon | [Brands/lululemon.md](Brands/lululemon.md) |
| Maison Crivelli | brand | fragrance | subversion, nature-integration, art-direction | canon | [Brands/maison-crivelli.md](Brands/maison-crivelli.md) |
| Maison d'Etto | brand | fragrance, home fragrance | narrative, world-building, ritual, materiality | canon | [Brands/maison-detto.md](Brands/maison-detto.md) |
| Maison Francis Kurkdjian | brand | fragrance | craft, precision, positioning | canon | [Brands/maison-francis-kurkdjian.md](Brands/maison-francis-kurkdjian.md) |
| Maison Pierre Marcolini | brand | chocolate | craft, provenance, restraint | canon | [Brands/maison-pierre-marcolini.md](Brands/maison-pierre-marcolini.md) |
| Mango | brand | fashion | accessible-luxury | canon | [Brands/mango.md](Brands/mango.md) |
| Margaret Howell | brand | fashion | structural-honesty, restraint, fabric-first | canon | [Brands/margaret-howell.md](Brands/margaret-howell.md) |
| Mariposa Baking Co. | brand | bakery | precision, craft | canon | [Brands/mariposa-baking-co.md](Brands/mariposa-baking-co.md) |
| Mast Brothers | brand | chocolate | art-direction, craft, narrative | watch | [Brands/mast-brothers.md](Brands/mast-brothers.md) |
| Moscot | brand | eyewear, accessories | heritage, precision, craft | canon | [Brands/moscot.md](Brands/moscot.md) |
| Motown | brand | music, record labels | institution-building, positioning | canon | [Brands/motown.md](Brands/motown.md) |
| Nayara Springs | brand | travel, hospitality, experiences | hospitality, precision, ritual | canon | [Brands/nayara-springs.md](Brands/nayara-springs.md) |
| Nike | brand | fashion, footwear, athletics | curation-strategy, high-low | canon | [Brands/nike.md](Brands/nike.md) |
| Nubian Heritage | brand | bath and body, personal care | heritage, diaspora | canon | [Brands/nubian-heritage.md](Brands/nubian-heritage.md) |
| Olive and Sinclair | brand | chocolate | sense-of-place, craft, heritage, provenance | canon | [Brands/olive-and-sinclair.md](Brands/olive-and-sinclair.md) |
| Our Legacy | brand | fashion | fabric-first, texture, restraint | canon | [Brands/our-legacy.md](Brands/our-legacy.md) |
| Paraboot | brand | footwear, fashion | heritage, craft | canon | [Brands/paraboot.md](Brands/paraboot.md) |
| PlayStation | brand | gaming, hardware, entertainment | world-building, institution-building, positioning, immersive-atmosphere, high-low | canon | [Brands/playstation.md](Brands/playstation.md) |
| Prada | brand | fashion, leather goods | restraint, materiality, subversion | canon | [Brands/prada.md](Brands/prada.md) |
| Puebco | brand | home goods, interior design | materiality, texture, high-low | canon | [Brands/puebco.md](Brands/puebco.md) |
| Ralph Lauren | brand | fashion | quiet-luxury, curation-strategy, anti-logo | canon | [Brands/ralph-lauren.md](Brands/ralph-lauren.md) |
| Rapha | brand | cycling, fashion | investment-luxury | canon | [Brands/rapha.md](Brands/rapha.md) |
| Rieti | brand | eyewear, accessories | accessible-luxury, precision | active | [Brands/rieti.md](Brands/rieti.md) |
| Salt and Stone | brand | deodorant, skincare | art-direction | canon | [Brands/salt-and-stone.md](Brands/salt-and-stone.md) |
| Santa Maria Novella | brand | fragrance, grooming | heritage, craft, positioning, ritual | canon | [Brands/santa-maria-novella.md](Brands/santa-maria-novella.md) |
| Scribe Winery | brand | wine | sense-of-place, restraint, world-building | canon | [Brands/scribe-winery.md](Brands/scribe-winery.md) |
| Seasons | brand | home fragrance, diffusers, interior design | art-direction, ritual, wellbeing | active | [Brands/seasons.md](Brands/seasons.md) |
| Singita | brand | travel, hospitality, conservation | hospitality, ritual, sense-of-place, world-building, positioning, nature-integration, spatial-direction | canon | [Brands/singita.md](Brands/singita.md) |
| Steam | brand | gaming, software, digital distribution | institution-building, ownership-as-strategy, merchandising, positioning | canon | [Brands/steam.md](Brands/steam.md) |
| Stüssy | brand | fashion, streetwear | heritage, high-low | canon | [Brands/stussy.md](Brands/stussy.md) |
| Uniqlo | brand | fashion | accessible-luxury, anti-logo | canon | [Brands/uniqlo.md](Brands/uniqlo.md) |
| Vans | brand | footwear, fashion | heritage, high-low | canon | [Brands/vans.md](Brands/vans.md) |
| West Elm | brand | furniture, home goods, retail | provenance, craft, accessible-luxury, positioning | canon | [Brands/west-elm.md](Brands/west-elm.md) |
| Yves Saint Laurent | brand | fashion | conviction | canon | [Brands/yves-saint-laurent.md](Brands/yves-saint-laurent.md) |
### Works

| Entity | Type | Domains | Pull for | Status | Card |
|---|---|---|---|---|---|
| Albert Einstein Education and Research Center | work | architecture, institutional, landscape | biophilic, spatial-direction, color-and-light, warmth | canon | [Works/albert-einstein-education-research-center.md](Works/albert-einstein-education-research-center.md) |
| Astroworld | work | music | sound-design, world-building, immersive-atmosphere, sense-of-place | canon | [Works/astroworld.md](Works/astroworld.md) |
| Baccarat Rouge 540 Extrait | work | fragrance | investment-luxury, positioning | canon | [Works/baccarat-rouge-540-extrait.md](Works/baccarat-rouge-540-extrait.md) |
| Bal d'Afrique | work | fragrance | warmth | canon | [Works/bal-dafrique.md](Works/bal-dafrique.md) |
| Bonhomía | work | restaurant, salumeria | hospitality, indoor-outdoor | canon | [Works/bonhomia.md](Works/bonhomia.md) |
| Breaking Bad | work | television | narrative, long-form-structure | canon | [Works/breaking-bad.md](Works/breaking-bad.md) |
| Building Frame of the House | work | architecture, residential | materiality, spatial-direction, structural-honesty, restraint | canon | [Works/building-frame-of-the-house.md](Works/building-frame-of-the-house.md) |
| Chess | work | gaming, strategy | positioning, restraint, structural-honesty, precision | canon | [Works/chess.md](Works/chess.md) |
| Dallas Buyers Club | work | film | subversion | canon | [Works/dallas-buyers-club.md](Works/dallas-buyers-club.md) |
| Django Unchained | work | film | narrative, subversion, long-form-structure | canon | [Works/django-unchained.md](Works/django-unchained.md) |
| Dromeas (The Runner) | work | sculpture, public art | materiality, scale | canon | [Works/dromeas.md](Works/dromeas.md) |
| Dune | work | furniture, design | spatial-direction, structural-honesty, immersive-atmosphere, investment-luxury, world-building | canon | [Works/dune-pierre-paulin.md](Works/dune-pierre-paulin.md) |
| Everything Everywhere All at Once | work | film | narrative, reinvention | canon | [Works/everything-everywhere-all-at-once.md](Works/everything-everywhere-all-at-once.md) |
| Fallingwater | work | architecture, residential | nature-integration, materiality, spatial-direction, sense-of-place, restraint | canon | [Works/fallingwater.md](Works/fallingwater.md) |
| Forrest Gump | work | film | narrative | canon | [Works/forrest-gump.md](Works/forrest-gump.md) |
| Good Will Hunting | work | film | narrative, long-form-structure | canon | [Works/good-will-hunting.md](Works/good-will-hunting.md) |
| Holocaust Memorial Miami Beach | work | architecture, memorial, sculpture | scale, spatial-direction | canon | [Works/holocaust-memorial-miami-beach.md](Works/holocaust-memorial-miami-beach.md) |
| Homegoing | work | literature | narrative, long-form-structure, diaspora, heritage | canon | [Works/homegoing-yaa-gyasi.md](Works/homegoing-yaa-gyasi.md) |
| Lafayette Street | work | fragrance | accessible-luxury, sense-of-place | canon | [Works/lafayette-street.md](Works/lafayette-street.md) |
| L'Homme à la Rose | work | fragrance | restraint, investment-luxury | canon | [Works/lhomme-a-la-rose.md](Works/lhomme-a-la-rose.md) |
| Menace II Society | work | film | immersive-atmosphere | canon | [Works/menace-ii-society.md](Works/menace-ii-society.md) |
| Millésime Impérial | work | fragrance | investment-luxury, heritage | canon | [Works/millesime-imperial.md](Works/millesime-imperial.md) |
| My Beautiful Dark Twisted Fantasy | work | music | sound-design, world-building, maximalism, high-low | canon | [Works/my-beautiful-dark-twisted-fantasy.md](Works/my-beautiful-dark-twisted-fantasy.md) |
| Naruto: Shippuden | work | animation, television | narrative, world-building, long-form-structure | canon | [Works/naruto-shippuden.md](Works/naruto-shippuden.md) |
| One Piece | work | animation | narrative, world-building, long-form-structure | canon | [Works/one-piece.md](Works/one-piece.md) |
| Oud Ispahan | work | fragrance | restraint | canon | [Works/oud-ispahan.md](Works/oud-ispahan.md) |
| Pulp Fiction | work | film | long-form-structure, voice-and-tone, high-low, sound-design, narrative | canon | [Works/pulp-fiction.md](Works/pulp-fiction.md) |
| Ready Player One | work | literature, film, gaming | world-building, immersive-atmosphere, narrative | canon | [Works/ready-player-one.md](Works/ready-player-one.md) |
| Renaissance | work | music | sound-design, precision, heritage | canon | [Works/renaissance-beyonce.md](Works/renaissance-beyonce.md) |
| Reservoir Dogs | work | film | long-form-structure, voice-and-tone, restraint, art-direction, narrative | canon | [Works/reservoir-dogs.md](Works/reservoir-dogs.md) |
| Roka Akor | work | restaurant, japanese | immersive-atmosphere, hospitality | canon | [Works/roka-akor.md](Works/roka-akor.md) |
| Scarface | work | film | narrative, long-form-structure | canon | [Works/scarface.md](Works/scarface.md) |
| Selena | work | film | narrative | canon | [Works/selena-film.md](Works/selena-film.md) |
| Sex and the City | work | television | editorial, voice-and-tone, narrative, world-building, sense-of-place | canon | [Works/sex-and-the-city.md](Works/sex-and-the-city.md) |
| Sex Education | work | television | voice-and-tone, long-form-structure | canon | [Works/sex-education.md](Works/sex-education.md) |
| The Fresh Prince of Bel-Air | work | television | voice-and-tone | canon | [Works/fresh-prince-of-bel-air.md](Works/fresh-prince-of-bel-air.md) |
| The One | work | fragrance | accessible-luxury | canon | [Works/the-one.md](Works/the-one.md) |
| Ushiku Daibutsu | work | architecture, monument, sculpture | scale, spatial-direction | canon | [Works/ushiku-daibutsu.md](Works/ushiku-daibutsu.md) |
| Whiplash | work | film | narrative, long-form-structure | canon | [Works/whiplash.md](Works/whiplash.md) |
| Young Rose | work | fragrance | restraint | canon | [Works/young-rose.md](Works/young-rose.md) |
### Curators

Editorial and retail tastemakers.

| Entity | Type | Domains | Pull for | Status | Card |
|---|---|---|---|---|---|
| Architectural Digest | curator | architecture, interior design, media | editorial, taste-authority, art-direction | canon | [Curators/architectural-digest.md](Curators/architectural-digest.md) |
| Dover Street Market | curator | fashion, retail | merchandising, spatial-direction, high-low, curation-strategy | canon | [Curators/dover-street-market.md](Curators/dover-street-market.md) |
| Mr Porter | curator | fashion, menswear | curation-strategy, taste-authority, merchandising | canon | [Curators/mr-porter.md](Curators/mr-porter.md) |
| Sylvia Rhone | curator | music, record labels, a&r | taste-authority, curation-strategy, institution-building, positioning | canon | [Curators/sylvia-rhone.md](Curators/sylvia-rhone.md) |
Aesthetic styles and movements – filed as curators, with the movement or vernacular standing as the tastemaking context.

| Entity | Type | Domains | Pull for | Status | Card |
|---|---|---|---|---|---|
| Biophilic | curator | architecture, interior design, landscape | biophilic, nature-integration, color-and-light, wellbeing | canon | [Curators/biophilic.md](Curators/biophilic.md) |
| Brownstone | curator | architecture, interior design, urbanism | heritage, sense-of-place, materiality, warmth | canon | [Curators/brownstone.md](Curators/brownstone.md) |
| Brutalist | curator | architecture, interior design | materiality, texture, warmth, scale, structural-honesty | canon | [Curators/brutalist.md](Curators/brutalist.md) |
| California Bungalow | curator | architecture, interior design, residential | craft, spatial-direction, indoor-outdoor, materiality | canon | [Curators/california-bungalow.md](Curators/california-bungalow.md) |
| Feng Shui | curator | interior design, spatial philosophy | spatial-direction, ritual, restraint, wellbeing | canon | [Curators/feng-shui.md](Curators/feng-shui.md) |
| French Provincial | curator | architecture, interior design | materiality, warmth, texture, craft | active | [Curators/french-provincial.md](Curators/french-provincial.md) |
| Industrial | curator | architecture, interior design | materiality, structural-honesty, texture, warmth, spatial-direction | canon | [Curators/industrial.md](Curators/industrial.md) |
| Japandi | curator | interior design | materiality, restraint, warmth, texture | canon | [Curators/japandi.md](Curators/japandi.md) |
| Mediterranean | curator | architecture, interior design | materiality, indoor-outdoor, warmth, color-and-light, spatial-direction | canon | [Curators/mediterranean.md](Curators/mediterranean.md) |
| Midcentury Modern | curator | architecture, interior design, furniture | restraint, materiality, warmth | canon | [Curators/midcentury-modern.md](Curators/midcentury-modern.md) |
| Modern | curator | architecture, interior design | restraint, spatial-direction, structural-honesty | canon | [Curators/modern.md](Curators/modern.md) |
| Native Plant Gardens | curator | landscape, gardening, ecology | nature-integration, biophilic | canon | [Curators/native-plant-gardens.md](Curators/native-plant-gardens.md) |
| Organic Modern | curator | interior design | warmth, restraint, materiality, color-and-light, texture | canon | [Curators/organic-modern.md](Curators/organic-modern.md) |
| Speakeasy | curator | interior design, hospitality | restraint, immersive-atmosphere, ritual, world-building, hospitality | canon | [Curators/speakeasy.md](Curators/speakeasy.md) |
| Surrealism | curator | visual art, literature, film | immersive-atmosphere, high-low, conviction, art-direction | canon | [Curators/surrealism.md](Curators/surrealism.md) |
| Tropical Modernism | curator | architecture, interior design | indoor-outdoor, nature-integration, materiality | canon | [Curators/tropical-modernism.md](Curators/tropical-modernism.md) |
| Verdant | curator | interior design | biophilic, indoor-outdoor, color-and-light | active | [Curators/verdant.md](Curators/verdant.md) |
| West African Modern | curator | architecture, interior design | heritage, materiality, diaspora, world-building, cultural-bridge | active | [Curators/west-african-modern.md](Curators/west-african-modern.md) |
Mediums and formats – immersive mediums and game, social and betting formats held as creative contexts.

| Entity | Type | Domains | Pull for | Status | Card |
|---|---|---|---|---|---|
| Augmented Reality | curator | gaming, technology, immersive media | immersive-atmosphere, subversion, spatial-direction | canon | [Curators/augmented-reality.md](Curators/augmented-reality.md) |
| Murder Mystery Parties | curator | gaming, social games, hospitality | hospitality, ritual, narrative | canon | [Curators/murder-mystery-parties.md](Curators/murder-mystery-parties.md) |
| Sportsbooks | curator | gaming, sports betting, finance | offer-design, positioning | canon | [Curators/sportsbooks.md](Curators/sportsbooks.md) |
| Virtual Reality | curator | gaming, technology, immersive media | immersive-atmosphere, world-building, spatial-direction | canon | [Curators/virtual-reality.md](Curators/virtual-reality.md) |
Typologies and features – dwelling typologies, home features and design techniques held as creative contexts.

| Entity | Type | Domains | Pull for | Status | Card |
|---|---|---|---|---|---|
| Ambient Lighting | curator | interior design, lighting | color-and-light, warmth, immersive-atmosphere | canon | [Curators/ambient-lighting.md](Curators/ambient-lighting.md) |
| The Dream Home | curator | architecture, interior design, residential | biophilic, structural-honesty, immersive-atmosphere, taste-authority | active | [Curators/the-dream-home.md](Curators/the-dream-home.md) |
| Homestead | curator | land, lifestyle, sustainability | ownership-as-strategy, nature-integration, ritual | canon | [Curators/homestead.md](Curators/homestead.md) |
| Houseboats | curator | architecture, dwelling, travel | sense-of-place, spatial-direction | canon | [Curators/houseboats.md](Curators/houseboats.md) |
| Outdoor Showers | curator | architecture, residential | indoor-outdoor, ritual | canon | [Curators/outdoor-showers.md](Curators/outdoor-showers.md) |
| Smart Home | curator | interior design, technology | restraint, structural-honesty | canon | [Curators/smart-home.md](Curators/smart-home.md) |
| Solariums | curator | architecture, interior design | color-and-light, indoor-outdoor, wellbeing | canon | [Curators/solariums.md](Curators/solariums.md) |
| Sunroofs | curator | architecture, residential | indoor-outdoor, color-and-light, structural-honesty | canon | [Curators/sunroofs.md](Curators/sunroofs.md) |
| Treehouses | curator | architecture, hospitality, travel | nature-integration, hospitality, world-building | canon | [Curators/treehouses.md](Curators/treehouses.md) |
Museums and institutions – galleries and museums held as tastemaking contexts.

| Entity | Type | Domains | Pull for | Status | Card |
|---|---|---|---|---|---|
| The Guggenheim | curator | art, museum, architecture | spatial-direction, art-direction, world-building | canon | [Curators/guggenheim.md](Curators/guggenheim.md) |
| The Hermitage Museum | curator | art, museum | scale, maximalism, spatial-direction, art-direction | canon | [Curators/hermitage-museum.md](Curators/hermitage-museum.md) |
| High Museum of Art | curator | art, museum, architecture | spatial-direction, art-direction | canon | [Curators/high-museum-of-art.md](Curators/high-museum-of-art.md) |
| The Louvre | curator | art, museum | taste-authority, spatial-direction, art-direction | canon | [Curators/the-louvre.md](Curators/the-louvre.md) |
| The Metropolitan Museum of Art | curator | art, museum, fashion | curation-strategy, high-low, editorial, art-direction | canon | [Curators/metropolitan-museum-of-art.md](Curators/metropolitan-museum-of-art.md) |
| Musée d'Orsay | curator | art, museum | color-and-light, art-direction | canon | [Curators/musee-dorsay.md](Curators/musee-dorsay.md) |
| Museo del Prado | curator | art, museum | art-direction | canon | [Curators/museo-del-prado.md](Curators/museo-del-prado.md) |
| Museum of Modern Art (MoMA) | curator | art, museum | taste-authority, art-direction | canon | [Curators/museum-of-modern-art.md](Curators/museum-of-modern-art.md) |
| Tate Modern | curator | art, museum | structural-honesty, spatial-direction | canon | [Curators/tate-modern.md](Curators/tate-modern.md) |
| Vatican Museums | curator | art, museum | spatial-direction, art-direction | canon | [Curators/vatican-museums.md](Curators/vatican-museums.md) |
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
