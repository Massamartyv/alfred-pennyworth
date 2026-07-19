---
file_type: fill_sheet
department: Growth
venture: Five Points Digital Studio
status: reference
last_updated: 2026-07-14
---

# SAM.gov Registration — Fill Sheet

Work down this sheet with the registration open in the other window. Pre-answered fields are marked **[SET]**. Fields only the operator can supply are marked **[YOURS]**. Fields requiring a decision are marked **[DECIDE]** with a recommendation attached.

Companion document: `sam-registration-dossier.md` — the reasoning behind these answers. This sheet is the answers only.

**Before starting, confirm no registration already exists:** sam.gov → sign in → Workspace → Entity Management. A SAM.gov user account is not an entity registration. If a UEI is already sitting there, stop and tell Alfred.

The form structure below is reconstructed, not read from the live wizard. Section names and ordering may differ. Correct anything that does not match and the sheet gets updated.

---

## 0 · Prerequisites

| Item | Value |
|---|---|
| Login.gov account, identity verified | **[YOURS]** — requires government photo ID and SSN |
| Entity Administrator | **[YOURS]** — the named human carrying legal accountability |
| Notarised Entity Administrator letter | **[YOURS]** — remote online notarisation accepted |
| IRS EIN letter to hand | **[YOURS]** — for exact-name verification |
| Business bank details to hand | **[YOURS]** — routing, account number, account type |

**Registration is free at every stage.** Any service charging for it is a scam.

---

## 1 · Entity Validation

The hardest gate. SAM validates the legal name and physical address against authoritative records. A mismatch of one character stalls the registration for weeks.

| Field | Value |
|---|---|
| Legal Business Name | **FIVE POINTS DIGITAL STUDIO LIMITED LIABILITY CO.** — corrected 2026-07-14. This is the name SAM returned from entity validation, spelled out in full rather than abbreviated to "LLC". Validated and passed. |
| Taxpayer Name | **[VERIFY AGAINST THE IRS EIN LETTER]** — a **separate field**, checked against IRS records, not entity records. It may legitimately differ from the legal business name above. The IRS may hold "LLC" where Wyoming holds "LIMITED LIABILITY CO." Type what the letter says, character for character. A mismatch sends the registration into manual review and costs weeks. |
| Doing Business As | Five Points Digital Studio **[SET]** |
| Physical Address | **[YOURS]** — the **Georgia** operating address. **Not** the Wyoming registered-agent address on the Articles. **No PO boxes.** SAM validates this against reality. |
| Mailing Address | **[YOURS]** — may be the same |
| Start Date / Date of Incorporation | **[YOURS]** — from the Wyoming Articles |

---

## 2 · Core Data

| Field | Value |
|---|---|
| TIN / EIN | **[YOURS]** — from the IRS letter. Never transcribed into this repository. |
| Taxpayer Name | **[YOURS]** — must match the IRS record exactly. Usually identical to legal name. |
| Fiscal Year End Close Date | **12/31** **[SET]** — confirm if the LLC uses a non-calendar year |
| Entity Structure | **Limited Liability Company** **[SET]** |
| Profit Structure | **For Profit Organization** **[SET]** |
| Country of Incorporation | **United States** **[SET]** |
| State of Incorporation | **Wyoming** **[SET]** — correct for today. Update to Georgia after domestication. Do not pre-empt it. |
| CAGE Code | Leave blank. Auto-assigned by the DLA during registration. **[SET]** |
| Registration Purpose | **All Awards** **[SET]** — covers contracts and grants. Costs nothing to include both. |

### Financial Information — EFT

| Field | Value |
|---|---|
| Routing / Account / Type | **[YOURS]** — business account, in the legal name of the entity |
| Remittance Address | **[YOURS]** — usually the same as physical |
| Accounts Receivable POC | `finance@fivepoints.studio` **[SET]** |

### Executive Compensation

| Field | Value |
|---|---|
| Did the entity receive ≥80% and ≥$25M of annual gross revenue from federal awards in the preceding fiscal year? | **No** **[SET]** |
| Consequence | The compensation disclosure section does not apply. |

### Proceedings

| Field | Value |
|---|---|
| Criminal, civil or administrative proceedings in the last five years | **[YOURS]** — expected **No**. Answer honestly. |

---

## 3 · Assertions

### NAICS codes

Settled against USASpending award data, FY2024 to date, contract awards only. Raw volume is a trap — the largest pools are largest because they contain work Five Points does not do.

| Code | Description | Awards | ≤$350K | Verdict |
|---|---|---|---|---|
| **541511** | Custom Computer Programming | 12,013 | 5,231 | **PRIMARY** — real application-development work under PSC DA01/DA10 |
| 541512 | Computer Systems Design | 30,020 | 18,864 | Include |
| 541611 | Administrative and General Management Consulting | 28,984 | 13,959 | Include, with eyes open — see below |
| 541810 | Advertising Agencies | 1,043 | 561 | Include — small, but exactly our work |
| 541613 | Marketing Consulting | 854 | 473 | Include |
| 541820 | Public Relations Agencies | 485 | 308 | Include |
| 541430 | Graphic Design | 462 | 385 | Include |
| 541990 | All Other Professional, Scientific and Technical | 19,526 | 11,632 | Include — catch-all |
| ~~541519~~ | ~~Other Computer Related Services~~ | 88,186 | 67,206 | **DROP** |

**Why 541511 is primary.** Not because it carries the most money — it does not. Because the work behind it is addressable: PSC DA01 and DA10, business application and application development, in the winnable band. It carries the most revenue headroom of the set, and it substantiates the digital-architecture and automation spine that is the actual claim. It is defensible in a room.

**Why 541519 is dropped despite being the largest pool by a factor of three.** Its top product codes are perpetual software licences, servers, network hardware and Tier 1–2 help desk. The awards in the winnable band are Cisco licence renewals and hardware resale. This is the value-added-reseller and help-desk market. Five Points cannot compete there and should not want to. Listing it invites the wrong inbound and dilutes a coherent identity.

**What 541611 actually contains.** Its top product codes are R499, R408 and R699 — professional support, programme management, administrative support. The winners are ICF, Cadmus and PAE selling programme-management staff by the hour. It is body-shop consulting, not automation strategy. Worth listing, not worth building a thesis on.

**Where the creative work actually lives.** 541810 is tiny — roughly 350 awards a year nationally — but its contents are precisely Five Points' work: public health campaigns, recruitment marketing, publication design. **HHS appears repeatedly as the buyer.** If a federal creative engagement ever lands here, it comes from Health and Human Services.

**The buyer flag.** DoD is the top awarding agency in nearly every code above. DoD work carries DFARS obligations and, for anything touching controlled unclassified information, CMMC certification. That is a real and unfunded compliance burden. Do not follow the volume there without pricing it in.

**The strategic read.** Across all four creative codes combined, the federal market for what Five Points actually does is roughly 950 awards a year nationally. Federal registration is a free option, not a plan. The near-term revenue is Georgia, DeKalb, City of Atlanta and GMSDC.

Small-business size standards are revenue-based and inflation-adjusted. Five Points sits well inside the threshold on every code. Verify current figures against the SBA size standards table rather than a remembered number.

### Size Metrics

| Field | Value |
|---|---|
| Annual receipts, 5-year average | **[YOURS]** |
| Number of employees, 12-month average | **[YOURS]** |

### Optional registries

| Field | Value |
|---|---|
| Disaster Response Registry | **[DECIDE]** — opt in. Free, and FEMA-adjacent communications and web work is real. |
| EDI Information | Skip **[SET]** |

---

## 4 · Representations and Certifications

**Legal attestations made under penalty of perjury.** Read them rather than clicking through. A false certification is False Claims Act exposure and the fastest route a small firm has to suspension or debarment.

| Certification | Answer |
|---|---|
| Small business, per NAICS | **Yes**, all listed codes **[SET]** |
| Small Disadvantaged Business | **Yes**, self-certified **[SET]** — no application required. Note the price evaluation adjustment that once made this a competitive edge has been suspended for over a decade. It is a reporting category now, not an advantage. |
| Woman-Owned Small Business | No **[SET]** |
| Veteran-Owned / Service-Disabled | No **[SET]** |
| HUBZone | **[YOURS]** — pending the map check at `maps.certify.sba.gov/hubzone/map`. Qualified tracts only; Redesignated expired 1 July 2026. |
| Debarred, suspended or proposed for debarment | No **[SET]** |
| Delinquent federal tax liability | No **[SET]** |
| **Section 889 — covered telecommunications** | **[VERIFY BEFORE ANSWERING]** |

**On 889.** You will certify that Five Points does not use covered telecommunications or video surveillance equipment — Huawei, ZTE, Hytera, Hikvision, Dahua — as a substantial component of any system. Most people tick this without looking. Before you do: check the router, check any security cameras, check anything network-attached with a brand you did not consciously choose. This is a perjury-exposed certification about physical objects in your building.

---

## 5 · Points of Contact

SAM requires a primary and an alternate for each. Routing follows the email directory and Navigation Rule 9.

| Role | Primary | Alternate |
|---|---|---|
| Electronic Business POC | `finance@fivepoints.studio` **[SET]** | **[YOURS]** |
| Government Business POC | `martavious@fivepoints.studio` **[SET]** | **[YOURS]** |
| Past Performance POC | `martavious@fivepoints.studio` **[SET]** | **[YOURS]** |

**The alternates are a genuine gap.** SAM wants a second named human per role. If Five Points has no second person, the alternate can be the same individual with a different address — `hello@fivepoints.studio` — but a real second contact is better, and a contracting officer who cannot reach anyone is a contracting officer who moves on.

---

## 6 · Submit

Submission is a legal act by the Entity Administrator. Operator only.

| Stage | Duration |
|---|---|
| Form, start to submit | 45 to 90 minutes with this sheet |
| Validation against IRS and state records | 2 to 4 weeks — the slow part, largely out of our hands |
| Outcome | Active registration, UEI, CAGE code, and the API rate limit rising from 10 requests per day to 1,000 |

---

## Open items

| Item | Owner |
|---|---|
| Confirm no existing registration — sam.gov Workspace → Entity Management | Operator |
| Wyoming standing and formation date — `wyobiz.wyo.gov`, CAPTCHA-gated | Operator |
| HUBZone map, Georgia address | Operator |
| Primary NAICS — 541511 or 541810 | Operator decision, recommendation above |
| POC alternates | Operator |
| Section 889 hardware audit | Operator |
| Georgia domestication — **by conversion, never by dissolve-and-reform** | Georgia business attorney |

---

*Reference document. Registration status is tracked in Notion, not here.*
