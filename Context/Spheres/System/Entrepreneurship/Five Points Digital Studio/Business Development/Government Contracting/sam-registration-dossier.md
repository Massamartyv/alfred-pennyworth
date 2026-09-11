---
file_type: registration_dossier
department: Business Development
venture: Five Points Digital Studio
status: reference
last_updated: 2026-07-14
---

# SAM.gov Entity Registration — Pre-Flight Dossier

Reference document. Every field required by the SAM.gov entity registration, with the answer determined in advance. Registration typically stalls not on difficulty but on encountering an unanswerable field mid-form. This removes that.

Live registration status lives in Notion, not here.

**Registration is free.** Every stage. Any service charging a fee to register an entity in SAM.gov is a scam. There is no exception to this.

---

## Entity of record

| Field | Value |
|---|---|
| Legal business name | **Five Points Digital Studio LLC** — operator-confirmed 2026-07-14 |
| State of formation | **Wyoming** |
| EIN | On file. IRS letter at `Administration/Legal/Employer Identification Number/` in the Five Points Google Drive. **Never transcribe the number into this repository.** |
| Articles of Organization | Same Drive path, `Administration/Legal/Articals of Organization/` |
| Wyoming standing | **Unverified.** The Wyoming registry is CAPTCHA-gated. Operator to confirm status and formation date at `wyobiz.wyo.gov`. Wyoming LLCs fall delinquent on a missed annual report and can be administratively dissolved. |
| Georgia registration | **None found.** No Certificate of Authority on the Georgia Corporations Division register. |

Verify the legal name against the IRS letter character for character before entering it into SAM. SAM validates the entity name against IRS records and a mismatch — a comma, a period, a missing "LLC" — is the most common cause of a stalled registration.

---

## The structural problem, and it precedes registration

Five Points is a **Wyoming LLC operating entirely in Georgia**, with no Georgia Certificate of Authority. This is not a filing detail. It is working against every lane of the strategy.

**A Wyoming LLC is an anonymity vehicle.** Wyoming does not publicly disclose members or managers. That is what it is purchased for. Every lane in this strategy is anonymity-destroying by design — SAM registration requires full ownership disclosure, and minority-business certification *is* the act of proving who owns and controls the company. The privacy the charter buys must be surrendered to execute the plan.

Three concrete costs:

1. **Contracts are currently unenforceable in Georgia courts.** A foreign LLC transacting business in Georgia without a Certificate of Authority may not maintain an action in a Georgia court until it registers. This does not void contracts — it bars enforcement until the registration is cured and back fees paid. The exposure is live today, across every retainer, and is independent of government contracting.
2. **Local-business tests fail on their face.** City of Atlanta EBO, DeKalb County and GMSDC all require an entity authorised to do business in Georgia with a genuine Georgia place of business. These are the three highest-value near-term lanes.
3. **The tax advantage does not travel.** Income earned by a business operating in Georgia is generally Georgia-source and taxable in Georgia regardless of the state of charter. Two states of annual fees and two registered agents, for a benefit that does not apply.

**Recommended direction: domesticate the LLC to Georgia.** Conversion preserves the EIN and the formation date, and therefore the past-performance clock — which matters, because GSA MAS requires two years of demonstrated history and every capability statement rests on the founding year. Foreign qualification is the cheaper half-measure: it cures the litigation exposure but leaves a Wyoming charter that serves no purpose.

**This is a strategic read, not legal advice.** Domestication carries tax consequences and the mechanics vary by state. Route the execution to a Georgia business attorney or the CPA.

### SAM address consequence

SAM requires a **physical business address where the entity actually operates**, and no PO boxes. That is the Georgia address, not the Wyoming registered-agent address on the Articles. The same is true for HUBZone, where the principal office is defined as where the greatest number of employees perform their work. Wyoming is a charter, not a place of business, and SAM validates against reality.

---

## Prerequisites

Complete all of these before opening the registration form.

| Prerequisite | Status | Notes |
|---|---|---|
| Login.gov account, identity verified | Operator action | Requires government photo ID and SSN. Operator only. |
| Legal entity in existence | Confirmed — LLC, out of state | State TBD |
| EIN from the IRS | Confirmed | Exact name on record TBD |
| Physical business address | Required | **No PO boxes.** Must be a physical location. |
| Business bank account | Confirmed | Routing number, account number, account type needed for EFT |
| Entity Administrator | Operator | A named human who carries legal accountability for the registration |
| Notarised Entity Administrator letter | Pending | Remote online notarisation is accepted |

---

## Core entity data

| Field | Value |
|---|---|
| Legal Business Name | Five Points Digital Studio LLC — verify character for character against the IRS letter |
| Doing Business As | Five Points Digital Studio |
| Entity Structure | Limited Liability Company |
| Profit Structure | For Profit Organization |
| Country of Incorporation | United States |
| State of Incorporation | Wyoming — see the structural problem above. This answer may change if the entity is domesticated to Georgia before registration. |
| Physical Address | The **Georgia** operating address. Not the Wyoming registered-agent address. No PO box. |
| Mailing Address | May differ from physical |
| Fiscal Year End Close Date | Typically 12/31 |
| CAGE Code | Auto-assigned during registration by the DLA. No separate application. |
| UEI | Issued on registration |

---

## NAICS codes

The strategic thesis: *we make government communicate well, and we make its operations work.* Creative and communications as the front door, automation and digital architecture as the spine. The codes below express that. A firm that claims everything claims nothing, so this list is deliberately bounded.

**Primary NAICS is a decision, not a default.** It determines how the entity is discovered in searches. Recommendation and rationale below the table.

| Code | Description | Role |
|---|---|---|
| 541511 | Custom Computer Programming Services | Recommended primary |
| 541512 | Computer Systems Design Services | Core |
| 541611 | Administrative Management and General Management Consulting Services | Core — the automation and operations consulting lane |
| 541810 | Advertising Agencies | Core — the creative front door |
| 541613 | Marketing Consulting Services | Core |
| 541430 | Graphic Design Services | Secondary |
| 541519 | Other Computer Related Services | Secondary |
| 541820 | Public Relations Agencies | Secondary |
| 541910 | Marketing Research and Public Opinion Polling | Optional |
| 541990 | All Other Professional, Scientific, and Technical Services | Catch-all |

**On the primary.** 541511 is recommended because federal digital-modernisation money flows through it and it maps to the automation and digital-architecture spine that is the actual differentiator. The counter-argument is real and worth weighing: 541511 is the most crowded pool in federal small-business contracting, while 541810 is a materially thinner field where government genuinely struggles to buy good work. If the near-term strategy leads with creative and communications, 541810 is the better primary. This is an operator decision.

Size standards are revenue-based and inflation-adjusted periodically. Verify the current figures against the SBA size standards table at registration rather than relying on remembered numbers. Five Points sits comfortably inside the small-business threshold on every code listed.

---

## Product Service Codes

PSCs are not required at registration but govern opportunity search and should be settled at the same time. Verify each against the current PSC manual before relying on it — the IT codes were restructured and remembered codes are unreliable.

Candidate areas: IT systems development and IT strategy and architecture under the D series; advertising and marketing services under the R series. Confirm exact codes at build time.

---

## Representations and Certifications

These are legal attestations made under penalty of perjury. Read them. A false certification is exposure under the False Claims Act and is the fastest route a small firm has to suspension or debarment.

| Certification | Expected answer | Note |
|---|---|---|
| Small business size, per NAICS | Yes, on every listed code | Self-certified against the SBA size standard |
| Small Disadvantaged Business | Available, self-certified | No application required. Note: the price evaluation adjustment that once gave SDB a competitive edge has been suspended for over a decade. It is a reporting category, not an advantage. |
| Woman-Owned Small Business | No | |
| Veteran / Service-Disabled Veteran-Owned | No | |
| HUBZone | Pending map check | Runs on census-tract economics, not ownership demographics. The one federal programme currently untouched by the wider political turbulence. Redesignated areas expired 1 July 2026; the map does not refresh until 2028. |
| 8(a) Business Development | Parked, deliberately | See the strategy note in `_index.md`. SBA proposed a rule on 11 June 2026 removing the social-disadvantage narrative path; public comment closed 13 July 2026 and the standard for new applicants is currently unknown. Roughly a quarter of existing participants were suspended in January 2026. This is the worst entry moment in the programme's history. Revisit in two quarters. |
| Debarment / suspension | No | |
| Delinquent federal tax | No | |
| Section 889 — covered telecommunications equipment | **Verify before certifying** | Certifies that the entity does not use covered telecom or video surveillance equipment — Huawei, ZTE, Hytera, Hikvision, Dahua — in its operations. Audit the actual hardware and the router before answering. This one catches people out. |

---

## Points of contact

Per the email directory and Navigation Rule 9, business context routes to `@fivepoints.studio` with the purpose-specific address taking priority.

| Role | Address | Rationale |
|---|---|---|
| Electronic Business POC | `finance@fivepoints.studio` | Receives contract payment and EFT notices |
| Government Business POC | `martavious@fivepoints.studio` | The named, accountable representative |
| Past Performance POC | `martavious@fivepoints.studio` | |
| Alternates | To be assigned | SAM requires an alternate for each POC |

---

## Timeline

| Stage | Duration |
|---|---|
| Login.gov account and identity verification | Same day |
| Notarised Entity Administrator letter | Same day with remote online notarisation |
| Registration form, start to submit | 45 to 90 minutes with this dossier in hand |
| SAM validation against IRS and state records | 2 to 4 weeks — the slow part, and largely out of our hands |
| CAGE code assignment | Automatic, during registration |
| **Outcome** | Active registration, UEI, CAGE code |

---

## What registration unlocks

Beyond the obvious — the legal capacity to be awarded a federal dollar — registration lifts the SAM.gov API rate limit from **10 requests per day** to **1,000**, because the limit is set by whether the account holds a role on a registered entity. The intelligence engine is architected to not depend on this, but it stops being a constraint.

---

## Adjacent, and more urgent than it looks

The Georgia Corporations Division shows no registration for Five Points under any searched name. An out-of-state LLC transacting business in Georgia requires a Certificate of Authority. Without one, the entity generally **cannot bring suit in Georgia courts** — meaning an unpaid client contract may be unenforceable until the registration is cured and back fees paid.

This is a standing business risk independent of government contracting, and it is also a blocker for City of Atlanta, DeKalb County and State of Georgia vendor registration. It should be cured regardless of what happens with any of this.

---

*Reference document. Registration status is tracked in Notion, not here.*
