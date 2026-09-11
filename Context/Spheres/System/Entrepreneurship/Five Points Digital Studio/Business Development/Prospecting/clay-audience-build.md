# Clay Audience Build – High-Ticket Home Services

**Instrument:** sourcing and enrichment recipe for the first Clay prospect table.
**Thesis:** jobs-to-ROI – target trades where one closed job repays any rung of the ladder ($1,970 Commission through $19,700 Build). The buyer needs very few sales for our fee to be a rounding error.
**Approved scope (operator ruling, 2026-07-27):** design-build remodelers, pool builders and solar across the 23 US metros of the approved 32; about 500 fully enriched rows; solar is a test cell, not the lead.
**Companion instruments:** `cold-call-home-services.pdf` (The Dial Sheet), `affluent-neighborhoods-seed-list.md` (service-area overlap), switchboard skill (call blocks).

---

## Allocation

| Trade | Rows | Metros | Rationale |
|---|---|---|---|
| Design-build remodelers | 250 | All 23 US metros | $50K–$150K jobs; universal demand; Dial Sheet beat exists |
| Pool builders | 150 | Sun Belt band only – GA, FL, TX, AZ and southern CA | $80K+ builds; no meaningful inground market in the Pacific Northwest |
| Solar installers | 100 | CA, AZ, TX, FL, NY | $25K–$35K tickets; distressed and over-pitched niche – prove response before scaling |

Source wide, enrich narrow: pull roughly 2,000 raw rows, score them all with cheap columns, then spend premium enrichments on the ~500 that clear the tier line.

## Metro roster (23 US)

Atlanta · Savannah · New York City · Albany – Capital Region · Miami – Fort Lauderdale – Palm Beach · Naples – Marco Island – Bonita Springs · Orlando – Winter Park – Lake Nona · Tampa – Sarasota · Los Angeles · San Francisco Bay Area · San Diego · Palm Springs – Coachella Valley · Orange County – Newport Beach · Dallas – Fort Worth · Houston · Austin · San Antonio · Seattle – Bellevue · Spokane · Portland · Bend – Central Oregon · Phoenix – Scottsdale · Tucson

Pool cells run in: Atlanta, Savannah, all four Florida metros, all four Texas metros, Phoenix – Scottsdale, Tucson, Palm Springs, San Diego, Orange County, Los Angeles.
Solar cells run in: the five California metros, both Arizona metros, all four Texas metros, all four Florida metros, New York City, Albany.

## Search strings – Google Maps source

One search per trade × metro cell. Limit 100 results per cell on the probe run; raise only if a cell proves thin.

- **Remodelers:** `design build remodeling` primary; `kitchen and bath remodeling` secondary where the primary runs thin. The phrase "design build" is the high-ticket qualifier – plain "handyman" and "remodeling" pulls low-ticket volume.
- **Pools:** `custom pool builder` primary; `swimming pool construction` secondary. Exclude service and retail: any name or category containing pool cleaning, pool service, pool supply.
- **Solar:** `residential solar installer` primary; `solar installation company` secondary.

## Filters – before any paid enrichment

1. **Review band:** 20 to 600 Google reviews. Under 20 cannot afford us; over 600 has a marketing department.
2. **Rating floor:** 4.0 and above for v1.
3. **Franchise and roll-up exclusion** (name match, case-insensitive):
   - Remodel: Re-Bath, Bath Fitter, West Shore Home, Power Home Remodeling, Renewal by Andersen, Kitchen Tune-Up, Dreamstyle, Statewide Remodeling, Leaf Home
   - Pools: Premier Pools & Spas, Anthony & Sylvan, Blue Haven (franchise locations)
   - Solar: Sunrun, Tesla Energy, Freedom Forever, Momentum Solar, ADT Solar, Palmetto, Trinity Solar, plus any publicly listed operator
4. **Dedupe** on website domain, then on place ID.

## Enrichment columns, in build order

| # | Column | Tool in Clay | Runs on | Est. credits/row |
|---|---|---|---|---|
| 1 | Source: Find Local Businesses (Google Maps) | Native source | All cells | Low – verify rate in-app before the full run |
| 2 | Website scrape | Scrape Website | All rows passing filters (~800) | 1 |
| 3 | Leak classification | AI column over the scrape: booking widget present? chat present? form-only contact? online estimate path? | Same ~800 | 1 |
| 4 | Service-area read | AI column: which neighbourhoods and suburbs does the site claim? | Same ~800 | included in 3 if combined |
| 5 | Owner name | Claygent: owner or principal from the site's about page, state contractor licence records (GA SoS, FL DBPR, CA CSLB, TX TDLR) or LinkedIn | Top ~500 by provisional score | 1–3 |
| 6 | Owner email | Waterfall: Prospeo → Hunter → Dropcontact | Top ~500 | 2–3 on hit |
| 7 | Owner mobile | Phone waterfall | Tier 1 only (~150) | 3–10 – the expensive one |

Business phone arrives free with the Maps source – the dial block never waits on enrichment.

## Scoring formula

Plain-English spec for the Clay formula column:

- Trade AOV index: remodel +3, pool +3, solar +2
- No online booking detected: +2
- No chat widget: +1
- Contact is form-only with no phone prominence: +1
- Review count inside 40–300 (volume sweet spot): +1
- Service area names any seed-list affluent neighbourhood: +2
- Independent (passed franchise filter): +1

**Tier 1: score ≥ 8. Tier 2: 5–7. Tier 3: below 5.** Tier 1 receives mobile enrichment and enters the switchboard call queue. Tier 2 receives email only and enters the DM or email lane. Tier 3 stays in the master table unenriched.

## Output

v1 keeps the integration surface at zero: export Tier 1 and Tier 2 as CSV, import to the Five Points Notion CRM through the existing import path, master table remains in Clay. A native Clay → Notion HTTP push is a v2 decision once the recipe is proven.

**Import runs through Alfred, never the native Notion CSV importer.** Native import forks duplicates and bypasses both the contacts protocol – dedupe before create, oldest page canonical – and the metadata completeness rule. The Next invocation of Switchboard reads directly off CRM hygiene, so a polluted import degrades the call queue on arrival.

**Tier lands on the card.** Operator ruling 2026-07-27: a `Tier` select property on the Five Points Contacts database, property id `%3AIRj`, options Tier 1, Tier 2 and Tier 3. Written once at import and never updated. It orders the queue only while a card is un-appraised; the prospect-appraiser star rating supersedes it the moment stars land. Retained so the scoring formula above can be calibrated against real call outcomes rather than held on faith. Registered read-only in both skill CRM references.

**Company to person.** The Maps source returns businesses; the CRM is person-titled, so a card needs a human name. Column 5 owner resolution is the conversion step and it will not clear every row. Rows with no resolved owner stay in Clay – a nameless card violates the metadata completeness rule. Unruled: whether a persistently unresolvable Tier 1 row earns a company-titled exception.

**Three scores, three axes.** The Clay tier measures business shape, the appraisal star measures buying capacity, the Next ordering measures timing. They are not interchangeable and must never be collapsed into one number.

## Build order in Clay

1. New table → source **Find Local Businesses**.
2. **Probe cell first:** `design build remodeling` × Atlanta, limit 100. Verify returned fields – name, domain, phone, review count, rating, address – and the actual credit rate charged.
3. Add remaining remodeler cells, then pool cells, then solar cells.
4. Apply filters 1–4. Confirm surviving row count before enrichment (~800 target).
5. Columns 2–4, run on survivors. Provisional score with what exists at this point.
6. Column 5 on the top ~500. Final score and tier.
7. Columns 6–7 per tier rules.
8. Export and import to CRM.

Credit checkpoint before steps 5, 6 and 7 – each is a spend gate requiring live balance read and operator nod.

---

## Probe run – 2026-07-27, Atlanta remodelers

Step 2 executed in-app. Query `design build remodeling contractor`, Atlanta GA, 31-mile radius, service-area businesses included, limit 100.

**Field schema returned (20 columns):** Name, Google Maps URL, Website, Phone, Address, Rating, Reviews, Primary Type, Types, Business Status, Search Location, Original Search Query, Id, Location, Opening Hours, Accessibility, Uses Preferred Google Api, Generative Summary, Payment Options.

Verified against the filter requirements:

- Filters 1 and 2 (review band, rating floor) – supported. `Reviews` returns a JSON object carrying `count` plus `topReviews` with full review text, so review mining comes free with the source.
- Filter 3 (franchise exclusion) – supported on `Name`.
- Filter 4 (dedupe) – supported on `Website` domain and on `Id`, which is the Google place ID.
- `Location` returns latitude and longitude, so the seed-list neighbourhood overlap can be computed geometrically rather than inferred from the site copy.

**No owner name and no email in the source.** Columns 5 and 6 are mandatory, not optional, exactly as the instrument assumed. Business phone does arrive free, so the dial block never waits on enrichment.

**Sample rows:** Innovative Design + Build (5.0, 138 reviews), MOSAIC Design + Build (4.9, 45), Glazer Design and Construction, Copper Sky Design + Remodel, Ponce Design Build. All independent, all inside the review band, none caught by the franchise filter.

**Cost:** the source charges ~1 action per row, as estimated.

**Account state – the binding constraint.** The Clay trial has expired and the workspace has dropped to the Free plan: 2,495 credits remaining, replenishing at 100 per month. The build as specified needs roughly 5,500 to 8,000 credits. It cannot run at full scope on this balance, and the free tier also appears to cap enrichment rows. Scope or plan must change before step 3; see the phone-first variant below.

## Phone-first variant – fits the current balance

Rationale: the closing motion is the call, not the email, and the Maps source supplies the business phone at no extra cost. Deferring columns 6 and 7 removes the majority of the spend without touching the part of the funnel that actually converts.

| Step | Rows | Est. credits |
|---|---|---|
| Source – remodelers, Atlanta plus three metros | ~400 | ~400 |
| Filters 1 to 4 | – | 0 |
| Website scrape plus combined leak and service-area AI column | ~150 survivors | ~300 |
| Owner name via Claygent, top tier only | ~75 | ~150 |
| **Total** | | **~850** |

Leaves roughly 1,600 credits in reserve. Produces about 150 dial-ready rows with business phone and about 75 carrying a named owner. Columns 6 and 7 stay parked until the recipe has proven itself on the phone or the plan is upgraded.

## Live table – built 2026-07-27

Workbook `wb_0tiueamAQTQDbBVDZUo`, table `t_0tiueanhpcpBXfHqKzn`. Personal Workspace, Clay Free plan.

**Configuration as run:** query `design build remodeling contractor`, multi-location across Atlanta Georgia, Miami Florida, Palm Springs California and Bend Oregon; 31-mile circle per metro; 100 results per location; service-area businesses included; location matching `Selected area only`.

**Metro selection.** Operator chose Atlanta, Miami and Palm Springs directly and delegated the fourth as an under-canvassed outlier. Bend – Central Oregon was selected on seed-list evidence: it is the only low-outreach metro on the roster carrying a **high** homebuilder vertical signal, where Savannah and Spokane are medium and Albany and Tucson are low. Its buyer profile is explicit in the seed list – remote-work wealth relocators and incoming equity migrants across Northwest Crossing, Broken Top, Tetherow, Awbrey Butte and Sunriver.

**Result at first read – 28 rows, all four metros live.** Approximate split: Miami 14, Bend 10, Atlanta 2, Palm Springs 1.

Bend validated the outlier thesis on first contact, returning ten genuine design-build firms – Life Design Build, Bend Craftsmen Company, Tumalo Construction, Lee Downing Building, Linnius Construction, WELBuilt Homes, K2 Design Remodel, Winsome Construction, C.O.R.R. Construction, Neil Kelly Bend. That is a denser independent-operator yield per capita than any other cell.

**Diagnosis – query breadth, not throttling.** An intermediate reading of this run attributed the low yield to free-plan queue throttling and predicted hours of background accumulation. That was wrong and is recorded here so it is not repeated. A 300-row fetch request returned a single row and the source reported `Businesses search completed. The number of results added may be less than requested, due to deduping or a limited number of actual results in your search area.` The search had simply exhausted the available matches. Total source cost held at 28 credits for 28 rows, confirming the 1 credit per row rate.

Two settings were suppressing the result set:

1. **Query narrowed in error.** The instrument specifies `design build remodeling`; the run used `design build remodeling contractor`. The trailing token suppressed matches severely. Atlanta returned five strong firms under the single-location probe – Innovative Design + Build, MOSAIC Design + Build, Glazer Design and Construction, Copper Sky Design + Remodel, Ponce Design Build – and none survived into the multi-location run.
2. **Location matching set to `Selected area only`.** The strict setting hard-excludes any business whose registered address falls outside the circle, even where it serves inside it. The alternative is `Selected area first`, which prioritises the metro without excluding. Because `Address` arrives free in the source schema, out-of-metro rows can be filtered afterward at zero credit cost, so the strict setting buys nothing.

**Corrected run – 98 rows.** Reverting to `design build remodeling` and switching to `Selected area first` took the table from 28 rows to **98**, a 3.5x lift for 70 additional credits. Balance after the corrected run: ~2,397 of 2,495. The search exhausts again at 98 under this query.

**Standing rule for this source.** Use the instrument query strings verbatim; do not append qualifying nouns such as `contractor`, `company` or `services`. Default `Location matching` to `Selected area first` and filter on `Address` post-hoc.

**To go beyond 98:** run the instrument secondary string `kitchen and bath remodeling` as a second pass over the same four metros, which the instrument already prescribes for thin cells. Additional metros are the other lever.

**State at handoff:** source complete at 98 rows. Filters 1 to 4 and the enrichment columns have not been applied and no premium enrichment has been spent.

## Filter pass – 2026-07-27, zero credits

Applied as view filters on the Default view of table `t_0tiueanhpcpBXfHqKzn`. Non-destructive and reversible; the master table stays at 98 rows.

| Filter | Rows after | Removed |
|---|---|---|
| Start | 98 | – |
| Review floor, Reviews Count ≥ 20 | 45 | 53 |
| Review ceiling, Reviews Count ≤ 600 | 45 | 0 |
| Rating floor, Rating ≥ 4.0 | 45 | 0 |

**The review floor is the whole filter.** It removed 53 of 98 on its own. The ceiling and the rating floor are both no-ops on this set – the largest review count is 343 and every row clearing 20 reviews already rates 4.5 or better. Independent design-build firms of this size do not carry weak ratings, so filter 2 buys nothing here and can be dropped from the recipe for this trade unless a future metro proves otherwise.

**Franchise exclusion – one hit, not on the list.** None of the nine named brands appear. **Alair Homes Decatur** – row 23, 4.6, 44 reviews – is a franchised design-build network and meets the exclusion rule the list was written to express. Add Alair Homes to the standing remodel exclusion list. Operator ruling pending on removing the row; count is 45 with it, 44 without.

**Dedupe – partially unavailable.** The table materialised 11 columns, not the 20 the source schema returns. There is no `Id` column, so a rigorous place-ID dedupe cannot be run here; the source deduped at fetch and no duplicate website domains are visible across the 45. If place-ID dedupe matters later, the source column has to be unpacked.

**Metro conformance – the fifth filter, still owed.** `Selected area first` did what it was chosen to do and pulled five rows outside the four metros: San Diego ×2 – Creative Design & Build, Sunset Design and Build – Carlsbad ×1 – TNT Design & Build – Los Angeles ×1 – DT Design & Build – and one Illinois number, D'Agostino Design. Filtering these on Address costs nothing and takes the set to 39. The instrument prescribes this pass; it should be written into the filter list as filter 5 rather than left as a footnote to the location setting.

**Metro split of the 45:** Bend 13, Atlanta 12, Miami 10, Palm Springs five, out of metro five. Bend continues to over-deliver against its size, holding the outlier thesis from the build run.

**One trade miss.** Central Oregon Painting – row 8 – is a painting contractor, not a design-build remodeler. The query string admits adjacent trades; the leak-classification AI column should be asked to confirm trade, not only read the booking surface.

**Surviving count for the enrichment gate: 39 clean, 44 including out-of-metro, 45 including Alair.** Against the instrument target of roughly 150 dial-ready rows this is about a quarter, because the source exhausted at 98 across four metros. Reaching instrument volume needs the secondary query string `kitchen and bath remodeling` and more metros, both at 1 credit per row.

Revised spend for the next stage at 39 rows: website scrape plus combined leak and service-area column ≈ 80 credits; Claygent owner name ≈ 40 to 120. Roughly 200 against the phone-first estimate of 850, which was sized for 150 rows.

## Secondary source pass – 2026-07-27, `kitchen and bath remodeling`

Operator ruling: source to volume before enriching, so the enrichment attention is paid once across the whole set rather than twice.

Run through the existing source column via Edit inputs, query string swapped to the instrument secondary `kitchen and bath remodeling`, same four metros, `Selected area first`, 100 per location. **Fetches append, they do not replace** – the run history shows the original 28 and the corrected 70 as separate additive runs, and this pass behaved the same way. That is the mechanism for adding a query string to an existing table.

**98 → 157 rows.** 59 added at 1 credit per row; the balance display moved from 2.4K to 2.3K.

Provenance caveat: the source column now stores the secondary query string, so the column configuration no longer describes the 98 rows sourced under `design build remodeling`. The run history preserves both. Anyone reading the column config alone will misread the provenance of the table.

## Filter state – four conditions, 77 of 157

| Condition | Field | Test |
|---|---|---|
| 1 | Reviews Count | ≥ 20 |
| 2 | Reviews Count | ≤ 600 |
| 3 | Rating | ≥ 4.0 |
| 4 | Name | does not contain any of – Renewal by Andersen, Re-Bath, Bath Fitter, Alair, West Shore Home, Power Home Remodeling, Kitchen Tune-Up, Dreamstyle, Statewide Remodeling, Leaf Home |

Clay supports `does not contain any of`, so the whole franchise list rides in one condition rather than nine. Use that operator; do not build one condition per brand.

**The franchise filter caught exactly one: Alair Homes Decatur.** Count moved 78 to 77 as the tag landed. None of the nine originally listed brands appear even after the kitchen-and-bath pass, which was expected to be franchise territory.

## The binding constraint – 200 rows per table on the Free plan

Clay warns at 157: `This table is nearing the 200 row limit`. This is a plan cap on table size, not a credit cap, and it was not known when the instrument was written. Consequences:

- This table has roughly 43 rows of headroom. A third query string or additional metros will hit the wall part-way through a fetch.
- The instrument target of about 500 fully enriched rows cannot be met in one table on the Free plan at all.
- The workaround inside the current plan is one table per batch, each capped at 200, with the CRM as the place they recombine. That makes the Notion import the join, which suits the architecture but multiplies the manual export step.

Credits are no longer the binding constraint on volume. Table size is.

---

*Last updated: 2026-07-27 – probe run recorded, field schema verified, free-plan credit constraint and phone-first variant added; live table built across Atlanta, Miami, Palm Springs and Bend, throttling and query-narrowing findings logged; Tier property ruled and created on the Contacts database, import-path and company-to-person rules recorded; filter pass run at zero credits, 98 to 45, metro-conformance filter and Alair franchise hit surfaced; secondary query string sourced to 157 rows, franchise list applied as one condition, 77 surviving, 200-row Free-plan table cap identified as the binding constraint on volume.*
