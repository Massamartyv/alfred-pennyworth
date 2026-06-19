# Benchmark Ledger

Provenance and refresh runbook for the figures in `wealth-trajectory.md`. Every benchmark here is sourced, dated and confidence-tagged. Both net-worth and income percentiles were computed directly from federal microdata; DQYDJ is retained only as a transparent cross-check. The standard is national (America). The target rung is the top 1%. Personal scope.

**Definition of "live."** Demographic income and wealth distributions are annual and triennial statistics, not a real-time feed. "Live" here means a living benchmark refreshed on the cadence the source publishes, with full provenance and an as-of date. Anything claiming real-time would be false precision.

Last full pull: **2026-06-13.**

---

## Methodology and validation

Both bars use the same weighted-percentile method: sort by the value, take the cumulative survey weight, read the value where cumulative weight crosses the target share of total weight. Applied to two federal microdata sources.

**Net worth — 2022 SCF.** The Federal Reserve Survey of Consumer Finances is the authoritative source for US wealth distribution by race. Aggregated tables publish medians and the racial gap but not the upper percentiles by race, so they were computed from the public microdata extract (`rscfp2022.dta`) using weight `wgt` across all five implicates. The SCF oversamples wealthy households, so its upper tail — including the 99th percentile — is well estimated.

**Income — CPS ASEC.** The Census Bureau Current Population Survey Annual Social and Economic Supplement is the authoritative annual income source and publishes a fresh wave every September. Percentiles were computed from the March 2025 person file (`pppub25.csv`, income year 2024) using the supplement weight `MARSUPWT`. Caveat: CPS topcodes the highest incomes, so the 99th percentile is conservative — understated versus reality — and thin for small subgroups.

**Validation.** The net-worth method applied to all families returned a 95th percentile of $3,795,600 against DQYDJ's published $3,779,600 from the same survey — a 0.4% difference. The income method returned an overall 95th percentile of $182,510 (all adults) and $190,000 (earners), bracketing DQYDJ's published individual 95th of $187,506. Both methods are sound; confidence per cell follows from sample size and, for income, topcoding.

---

## Net worth benchmarks (2022 SCF, computed 2026-06-13)

| Cell | Median | Top 10% | Top 5% | Top 1% | Sample (families) | Confidence |
|---|---|---|---|---|---|---|
| Overall US | $192,700 | $1,936,900 | $3,795,600 | $13,615,400 | ~4,595 | HIGH (validated) |
| Black, national | $49,590 | $507,000 | $822,500 | $2,023,440 | ~698 | HIGH (p99 MEDIUM) |
| Black, under 35 | $6,810 | $128,250 | $301,300 | $536,800 | ~125 | LOW — thin tail |
| Age 30–34, all races | $89,801 | $537,800 | $777,170 | $2,777,400 | ~291 | MEDIUM |

Source: Federal Reserve, Survey of Consumer Finances 2022, Summary Extract Public Data (`rscfp2022`). https://www.federalreserve.gov/econres/scfindex.htm — race code 2 = Black/African-American non-Hispanic.
Cross-check (overall US, DQYDJ on 2022 SCF): median $192,084, 90th $1,920,758, 95th $3,779,600. https://dqydj.com/net-worth-percentiles/

---

## Income benchmarks (income year 2024, computed from CPS ASEC 2025)

Total personal income (PTOTVAL) unless the row says earners, which uses positive earnings (PEARNVAL). Person file, weighted by MARSUPWT.

| Cell | Median | Top 10% | Top 5% | Top 1% | Basis | Sample (persons) | Confidence |
|---|---|---|---|---|---|---|---|
| Overall US, all adults 15+ | $38,000 | $130,722 | $182,510 | $370,067 | Total income | ~114,446 | HIGH (p99 topcode-affected) |
| Overall US, earners | $50,000 | $140,000 | $190,000 | $410,000 | Earnings | ~72,286 | HIGH (p99 topcode-affected) |
| Black, national 15+ | $30,000 | $99,160 | $132,402 | $250,250 | Total income | ~13,306 | HIGH (p99 MEDIUM) |
| Black, earners | $45,000 | $108,000 | $147,500 | $270,000 | Earnings | ~7,790 | HIGH (p99 MEDIUM) |
| Age 30–34, all races | $50,000 | $133,011 | $176,000 | $324,648 | Total income | ~9,349 | HIGH (p99 MEDIUM) |
| Black, age 30–34 | $39,000 | $91,070 | $137,000 | $203,850 | Total income | ~1,013 | p99 LOW — thin and topcoded |

Source: Census Bureau CPS ASEC March 2025, income year 2024. File: https://www2.census.gov/programs-surveys/cps/datasets/2025/march/asecpub25csv.zip — PRDTRACE==2 (Black alone), PTOTVAL total income, PEARNVAL earnings, MARSUPWT weight.
Household context: overall US household income median $83,592, 95th $335,575 (DQYDJ on CPS, income year 2024). https://dqydj.com/household-income-percentiles/

**Topcoding note.** The income 99th-percentile figures are floors. CPS ASEC replaces very high incomes through rank-proximity swapping and topcodes, which compresses the extreme tail. The true top-1% thresholds run somewhat higher. Net-worth 99th percentiles do not carry this caveat. Where a precise income top 1% matters, the IRS Statistics of Income is the authoritative source for the upper tail, though it does not break out by race.

---

## Racial wealth gap context

Substantiates why the demographic top 1% sits well below the overall top 1%, and why the instrument shows both frames rather than one.

- Median white household net worth (2022): $285,000. Median Black household net worth (2022): $44,900. Ratio 6.4×. Source: Federal Reserve FEDS Note, Oct 2023. https://federalreserve.gov/econres/notes/feds-notes/greater-wealth-greater-uncertainty-changes-in-racial-inequality-in-the-survey-of-consumer-finances-20231018.html
- The Black-national top 1% net worth ($2,023,440, computed) is below the overall US top 5% threshold of $3,795,600 — the frames are roughly a decade of compounding apart at the top of each distribution.

---

## Standard: national (America)

Per operator decision 2026-06-13, the benchmark standard is national. The earlier Atlanta metro cut is dropped: no source breaks a metro income distribution by race at the 99th percentile, and national sources update more reliably and annually. The demographic upper percentiles, previously unpublished, are computed directly from CPS ASEC and SCF microdata above.

Remaining limitation: Black income is computed at the person level, not the household level — household race is ambiguous for mixed households, and the person level is the right frame for a single earner regardless. Black household net worth uses the SCF family unit, which is the standard wealth frame.

---

## Refresh runbook

**Cadence.** Income refreshes annually when CPS ASEC publishes (September). Net worth refreshes when the SCF publishes (triennial).

| Data | Next release | Expected |
|---|---|---|
| CPS ASEC (income, national, by race and age) | income year 2025 | September 2026 |
| SCF (net worth by race) | 2025 wave | Late 2026 |

**Re-pull procedure** (reproducible — run from `.working/wealth-trajectory/`):

1. Income (CPS ASEC). Download the next March person file `pppub<YY>.csv` from `https://www2.census.gov/programs-surveys/cps/datasets/20<YY>/march/asecpub<YY>csv.zip`. Compute weighted percentiles (50/90/95/99) of PTOTVAL (total income) and PEARNVAL>0 (earners) using MARSUPWT, for: all adults 15+, Black (PRDTRACE==2), age 30–34, Black age 30–34. Validate the overall all-adults 95th against the DQYDJ individual figure before trusting the demographic cells.
2. Net worth (SCF). When the next wave publishes, download `scfp<year>s.zip` from federalreserve.gov/econres, unzip to `rscfp<year>.dta`, and compute weighted percentiles (50/90/95/99) of `networth` by `wgt` for: all families, Black (race==2), Black under 35, age 30–34. Validate the all-families 95th against the DQYDJ figure.
3. Update the marker tables in `wealth-trajectory.md`, update both "Last updated" dates, and note any percentile-position movement for the nudge.

**Environment note.** This Mac's system Python 3.9 has no pandas by default — the refresh installs it with `python3 -m pip install --user pandas`. Weighted percentiles are scale-invariant to the weight, so the weight need not be rescaled. The Census data API requires a free key; the microdata files used here need no key.

---

## Change log

- 2026-06-13 — Target rung set to top 1% (operator: top 5% read low). Income 99th percentiles computed from CPS ASEC 2025; topcoding caveat recorded. Net-worth 99th percentiles already present from the SCF computation.
- 2026-06-13 — Standard set to national. Atlanta metro cut removed. Demographic income percentiles computed from CPS ASEC 2025 microdata (income year 2024), replacing earlier published-only and metro figures. Income method validated against DQYDJ.
- 2026-06-13 — Ledger created. Net-worth percentiles computed from 2022 SCF microdata (method validated to 0.4% against DQYDJ).
