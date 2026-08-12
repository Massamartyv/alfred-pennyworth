# Van Westendorp Pricing Study – Custom Website Build (5.2-G)

Method: Van Westendorp Price Sensitivity Meter, house standard per the `van-westendorp-analysis` skill. Design-phase deliverable – fielding-ready instrument and fielding plan. Analysis begins when `responses.csv` lands.

Offer under study: 5.2-G Custom Website Build, Gold tier, one-time commissioned project currently priced $7,500 to $12,000. A study objective is to replace the range with one defensible number, or a justified two-tier structure if the market turns out to be two markets.

Sales motion on record: sales-led – discovery calls and proposals. At analysis time the recommendation prices toward the revenue-maximising point and PME, not the volume plateau.

---

## 1. Study decisions

| Decision | Ruling |
|---|---|
| Billing unit | One-time project fee, USD. Held constant across every question. |
| Anchor discipline | No respondent sees any price. The $7,500–$12,000 band, the Stripe listing and the proposal history stay invisible to the sample. Do not field to past proposal recipients who saw a quoted number. |
| Primary segment | Annual revenue band – under $1M, $1M to $5M, over $5M. |
| Secondary segments | Vertical, current site status, annual marketing spend band, channel. Sliced opportunistically. |
| NMS purchase-intent extension | Omitted. This is range-finding for a launch-firm price, not a revenue forecast. Add later only if a demand forecast becomes the goal. |
| Sample floor | 30 consistent responses per revenue band = 90 minimum; field 110–120 to absorb the typical 10–20% consistency loss. |

## 2. Instrument – ready to field

### Intro – no price appears anywhere above the four questions

> A few minutes of your judgment, if you will lend it. We build websites for owner-run businesses and we are setting the price of a new engagement before it opens. There are no right answers and nothing to buy here – we want your honest read on what this work is worth. Four minutes, anonymous.

### Screener – disqualify early, politely

**S1. Which best describes your role?**
- Owner or co-owner
- Managing partner or general manager with budget authority
- Manager without budget authority – *disqualify*
- Employee or contractor – *disqualify*

**S2. What was your business's approximate revenue over the last 12 months?**
- Under $250,000 – *disqualify*
- $250,000 to $999,999 *(band: under_1m)*
- $1,000,000 to $4,999,999 *(band: 1m_5m)*
- $5,000,000 or more *(band: over_5m)*

**S3. In the last 24 months, have you purchased, commissioned or seriously evaluated a professional website project for your business?**
- Yes, purchased or commissioned one
- Yes, evaluated seriously but did not proceed
- No, but it is on the horizon within the next year *(pass – active intenders are valid buyers)*
- No, and it is not something we would pay for – *disqualify*

### Offering description – shown once, before the four questions

> **The Custom Website Build**
>
> A commissioned website, built for your business by a studio – not assembled from a template.
>
> What the engagement includes:
> - Custom development to a design created for you, or to designs you already own
> - Up to 15 pages or page templates
> - A content management system you control – edit anything without a developer
> - Intelligent features where they serve the business: chat, smart forms, dynamic content
> - Performance engineering, with a guarantee: if the site does not score 80 or better on Google PageSpeed at launch, we optimise until it does at no charge
> - Search engine foundation built in from the first line of code
> - Two full rounds of revisions
> - Thirty days of post-launch support, a training session on managing your own site and your first three months of hosting and maintenance included
>
> The engagement runs four to eight weeks. You own everything at handover – the site, the system and the keys.
>
> For the next four questions, answer with a specific one-time dollar amount for this entire engagement. There is no wrong number – your honest read is the value.

### The four price questions – free-entry dollar amounts, fixed order within this wave

**Q1.** At what price would this website engagement be so expensive that you would not consider it, regardless of how much you wanted it?
`$________`

**Q2.** At what price would this engagement feel like a bargain – excellent work for the money?
`$________`

**Q3.** At what price would this engagement start to feel expensive – you would have to think hard, but you would still consider it?
`$________`

**Q4.** At what price would this engagement be so inexpensive that you would doubt the quality and not trust it?
`$________`

### Customer-stats block – banded, for segment slicing

**C1. Which best describes your business?**
- Home services and trades
- Food, hospitality and events
- Health and wellness
- Professional services
- Faith and community organisations
- Retail and e-commerce
- Other

**C2. What best describes your current website?**
- No website
- A template or DIY site we have outgrown
- A professionally built site more than three years old
- A professionally built site less than three years old

**C3. Roughly what does your business spend per year on marketing in total – advertising, design, agencies and software combined?**
- Under $10,000
- $10,000 to $30,000
- $30,000 to $75,000
- Over $75,000

### Open text

**O1.** What would have to be true about this engagement for it to be an easy yes at the right price?
`[open text]`

## 3. Sample and fielding plan

Three revenue bands sliced, 30 consistent responses per band minimum: **90 consistent, field 110–120**. Over-recruit the over-$5M band deliberately – it is the scarcest and the most strategically interesting, given the upmarket thesis.

Channels, in order of answer quality:

1. **Live prospects and discovery calls** – the four questions asked verbatim at the end of switchboard calls and discovery calls, logged to the response sheet with `channel=call`. Exclude anyone who has already received a quoted price.
2. **Clay prospect universe** – the enriched outbound lists, invited by email to the anonymous survey. Strict screener enforcement; `channel=clay`.
3. **Owner communities** – trade and owner groups in the live verticals: home services, food and events, church administration networks. Modest neutral incentive, never the build itself; `channel=community`.
4. **Screened panel** – Respondent, Prolific or similar with S1–S3 enforced, to fill under-represented bands; `channel=panel`.

Bias controls per the house standard: anonymous where the channel allows, one response per person, channel tagged on every row, no fielding to anyone who has seen a Five Points price.

## 4. Response file

CSV header, matched to the analysis script's auto-detected columns:

```
respondent_id,too_cheap,bargain,expensive,too_expensive,revenue_band,vertical,site_status,marketing_spend_band,channel
```

When the file lands, the analysis runs:

```bash
python3 ~/.claude/skills/van-westendorp-analysis/scripts/psm_analysis.py responses.csv --segment revenue_band --style fivepoints-theme.json
```

Analysis will report the four intersection points, the acceptable range, revenue-optimal pricing for the sales-led motion, segment slices by revenue band and vertical, and the chart set – themed to the Five Points palette.

## 5. What this study settles

1. **The single number.** Whether the Gold build carries one price – and what it is – in place of the $7,500–$12,000 range.
2. **The band question.** Whether the market under this offer is one population or two. If the over-$5M band's acceptable range separates cleanly, the finding feeds the ladder architecture rather than one compromise price.
3. **The upmarket signal.** Where PME sits for the strongest band – the empirical ceiling for the deliberate upmarket move the studio intends.
