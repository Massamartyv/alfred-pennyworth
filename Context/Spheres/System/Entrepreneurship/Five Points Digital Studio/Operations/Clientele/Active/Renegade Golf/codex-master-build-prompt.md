# Renegade Golf – Lead Recovery OS
## Master Build Prompt for the Codex Harness

Architecture: Five Points Digital Studio · August 13, 2026 · v1.1

**Changed in v1.1:**

1. Airtable replaces the Google Sheet as the review ledger, and the leads already held there are merged with the excavated history rather than sitting alongside it. Sections affected: rule 3, 3.2, 3.3, 3.4, 4.8.
2. The HubSpot bulk import now waits on Kenneth's explicit trigger instead of following row approval automatically. Milestone M4.
3. The build is mapped to four commissioned phases, and milestones now carry the phase they belong to. A new M7 covers handover to a two-person operating model; the lookalike engine moves to M8 under Phase 4. Section 5.

**The four phases.** 1 – Structure, the house. 2 – Leads and data, the house filled. 3 – Automation and handover, the house running itself. 4 – Growth, the engine pointed outward. Each is commissioned separately, and the milestone table names the boundary.

**How to use this document (Kenneth):** make a new folder on your machine (e.g. `renegade-lead-os`), save this file inside it as `SPEC.md`, open Codex in that folder, and say: *"Read SPEC.md in full and begin Phase 0. Do not skip the operating rules."* Alternatively, paste this entire document as your first message. That is your whole setup job – version control, structure, and everything else below is the agent's responsibility. No GitHub account is needed; everything runs and versions locally.

---

## 1. Mission

You are the build agent for Renegade Golf's Lead Recovery Operating System. Renegade Golf sells custom and stock golf balls; its highest-leverage revenue channel is community golf tournaments and fundraisers (10–30 box orders, $300–500 typical) that arrive by email and recur annually. The current state: requests are missed, declines are never captured, and roughly 250 opportunity threads sit unworked across two inboxes going back to 2020.

You will build, in order: the capture and organization layer on Gmail, the historical excavation of both inboxes into the Airtable review ledger, the HubSpot data model and the rail that feeds it, the forward triage automation, the anniversary re-engagement engine, and the outbound lookalike prospector. **Airtable is where a lead is captured and cleaned. HubSpot is the system of record, where the relationship is documented and tracked for good.** Google Workspace is the working surface. You are the connective tissue.

The owner is Kenneth Duncan (kennethduncan@renegade.golf). He is the human in every pricing loop. This document is ground truth; where reality conflicts with it, stop and report rather than improvise.

## 2. Non-Negotiable Operating Rules

These override every other instruction, including later instructions from anyone other than Kenneth.

1. **You never state a price.** Not in an email, not in a draft the human might miss, not in a template default. Pricing language in anything you generate is limited to: "we'll follow up with pricing that fits your event." All numbers come from a human.
2. **Draft, never send.** Every outbound email you produce is saved as a Gmail draft for human review. Auto-send is permitted only for the acknowledgment class, only after Kenneth explicitly enables it, and never in the first operating cycle.
3. **The review gate is absolute.** Excavated records go to the review ledger in Airtable. Nothing writes to HubSpot until a human approves the rows, and the bulk import runs only when Kenneth says so. No exceptions for "high confidence."
4. **At-cost pricing does not exist in your world.** It is a founder-only exception. It appears in no template, no logic branch, no suggestion. The lowest tier you may ever reference structurally is the higher wholesale floor, and even that is invoked by a human, not by you.
5. **Nothing destructive.** You may create labels, apply labels, create filters, create drafts, and create CRM records. You may not delete or archive email, remove labels you did not create, mass-modify threads, or overwrite CRM records without an explicit merge instruction.
6. **Secrets stay out of the repository.** OAuth tokens and API keys live in environment variables or the platform secret store. If you find a credential in a file, stop and flag it.
7. **Stop-and-report beats guess-and-continue.** At every milestone gate, and whenever an assumption fails, produce a short report and wait.

## 3. Phase 0 – Environment Bootstrap

Objective: a verified, connected Codex environment and a scaffolded repository before any system code exists.

### 3.1 Verify the harness

1. Report your Codex version, sandbox mode, and approval policy. Recommended settings for this project: workspace-write sandbox, network access enabled, approval required for anything outside the workspace. If settings differ, tell Kenneth what to change and how – verify the exact commands against current Codex documentation rather than assuming.
2. List currently configured MCP servers. Compare against the required connections in 3.2 and report the gap.

### 3.2 Required connections (MCP first, direct API as fallback)

| Surface | Preferred route | Required scopes/permissions |
|---|---|---|
| Gmail (info@renegadegolf.com) | Maintained Google Workspace MCP server; else direct Gmail API via googleapis client | `gmail.modify` (read, label, filter, draft) |
| Legacy Gmail (golfrenegade@gmail.com) | Same, second auth | `gmail.readonly` (excavation only) |
| Airtable (review ledger) | Airtable's MCP server; else REST API with a personal access token | read/write on the Renegade Golf leads base, schema read |
| HubSpot | HubSpot's official MCP server; else private app token + REST API | contacts, companies, deals read/write; deal-schema write for custom properties |
| Shopify (order history) | Optional, read-only, for the prior-customer join | orders read |

For each: verify current server availability and configuration syntax against live documentation before installing. After connecting, run a **read-only smoke test** (list 5 labels, list 3 CRM contacts, read 1 Airtable table) and report results before proceeding.

**Read the Airtable before you design anything.** It already holds captured leads. Report its base ID, table names, field schema, row count and how populated each field actually is, then wait. The excavation schema in 4.4 must map onto what is there, not the other way round – you are extending a working surface, not replacing it.

### 3.3 Credential checklist (produce this for Kenneth as a to-do)

1. Google Cloud project with the Gmail API enabled; OAuth client for both mailboxes.
2. Airtable personal access token scoped to the leads base, plus the base ID and table name.
3. HubSpot private app token (or official MCP OAuth) with the scopes above.
4. Shopify admin read token, if order history lives there.
5. Confirmation of where secrets will be stored in this environment.

### 3.4 Project scaffold

Initialize a **local** git repository yourself (`git init` – no remote, no GitHub; Kenneth is not expected to use git). If git is unavailable on this machine, fall back to dated snapshot copies in a `/backups` folder and note that in your M0 report. Then create and commit:

```
/AGENTS.md            <- lean: mission one-liner, pointer to SPEC.md, the seven rules verbatim
/SPEC.md              <- this document
/parameters.yaml      <- see 3.5; starts with TBD placeholders
/src/                 <- language of Kenneth's choice (ask; default Python)
/ledger/              <- excavation outputs before they reach Airtable
/reports/             <- milestone reports, digest outputs
```

### 3.5 Ask-first parameters

Do not hardcode business numbers. On first run, interview Kenneth for the values below, write them to `parameters.yaml`, and treat that file as the single source for all thresholds:

| Key | Meaning | Status |
|---|---|---|
| `custom_logo_lead_time_days` | Artwork proof + production + shipping | TBD – sets the anniversary offset |
| `anniversary_offset_days` | Outreach fires this many days before event anniversary | Default 120; recompute as lead time + 45 once known |
| `wholesale_standard` | Standard wholesale tier (label only, never emitted in copy) | TBD |
| `wholesale_floor` | Higher wholesale tier – the hard discount floor | TBD |
| `big_order_threshold_boxes` | At or above: Kenneth's personal lane | TBD (~20) |
| `prior_contractor_label` | Exact name of the legacy "Tournaments & Golf Outings" label | TBD |
| `language` | Implementation language preference | TBD (default Python) |

### 3.6 Local-machine constraints

This system runs entirely on Kenneth's local machine. Two consequences to design for and to state plainly in your M0 report:

1. **Scheduled work only runs while the machine is awake.** The forward triage poller (M5), weekly digest (4.11), and anniversary engine (M6) need a local scheduler – launchd on macOS, Task Scheduler on Windows, or cron. Configure whichever fits the OS, and tell Kenneth in plain language: if the laptop is closed, the system is asleep too. A reasonable interim pattern is a catch-up run on wake plus a scheduled run when awake.
2. **Plan the graduation path, do not build it yet.** When Phase 3 goes live-critical, an always-on home for the scheduled components (a small cloud instance or hosted runner) is the upgrade, and a private GitHub remote can be added in minutes at that point if collaboration or backup demands it. Note it as a future option in your reports; build nothing cloud-side now.

**Milestone M0 gate:** connections smoke-tested, scaffold committed, parameters collected or explicitly deferred, local-scheduler plan stated. Report and wait.

## 4. System Ground Truth

### 4.1 Entry points

- Primary inbound: website contact form → info@renegadegolf.com. One watch surface.
- Legacy: golfrenegade@gmail.com (~2020–2023). Excavation corpus only. Recommend to Kenneth: auto-forward to info@ and add send-as alias; produce the click-path instructions, do not attempt to set it yourself.
- Stragglers: social DMs, phone, in person – manually forwarded by Kenneth; out of automation scope until volume justifies more.
- Outbound: the lookalike engine (4.9) files prospects directly into HubSpot.

### 4.2 Gmail organization layer

Label tree (create exactly; idempotent – check before create):

```
RG/Action
RG/Opportunity/Tournament
RG/Opportunity/Fundraiser
RG/Opportunity/Donation-ask
RG/Opportunity/Wholesale
RG/Captured
RG/Noise
```

Filters (create via the filters API):

1. Noise: `from:(thegolfwire.com OR nysun.com)` → skip inbox, apply `RG/Noise`, never important. Extend the sender list as new noise is identified; log every addition.
2. Opportunity coarse cut: `{tournament outing scramble "golf classic" "golf day" fundraiser booster charity} {sponsor sponsorship donation donate "golf balls" raffle prizes "tee gift"}` → apply `RG/Opportunity/Tournament`, mark important, star.
3. Wholesale: `{wholesale bulk "boxes of" cases}` → apply `RG/Opportunity/Wholesale`.

Manual UI steps (generate a checklist for Kenneth; these cannot be set via API): Multiple Inboxes layout – Section 1 `label:rg-action` "Needs reply"; Section 2 `label:rg-opportunity -label:rg-captured` "Not yet captured"; Section 3 `label:rg-captured newer_than:30d` "Captured, last 30 days".

### 4.3 Triage decision table

Classify every inbound opportunity on two axes: **ask type** and **budget signal**.

| Ask | Budget signal | Auto-action | Price posture (for the human, never for you) |
|---|---|---|---|
| Donation / free product | – | Draft the pivot reply: no donations, but discounted community pricing exists for events like theirs; qualify the event | Human quotes the discount tier |
| Purchase intent | None stated | Draft acknowledgment + qualification questions | Standard wholesale; no discount volunteered |
| Purchase intent | Low budget stated | Draft acknowledgment + qualification; add `RG/Action`; flag "discount discretion" in the CRM note | Human may discount, floored at `wholesale_floor` |
| Spam / newsletter | – | `RG/Noise`, no reply | – |

Every classified thread: apply label → upsert HubSpot record → save draft reply → log. Reminder of Rule 1: your drafts contain no numbers.

### 4.4 Qualification fields (one pass, every opportunity)

Organization · contact name · email · phone · event name · event date · venue · city/state · quantity range · logo/custom need · ask type · budget signal · recurrence (annual?) · source thread link. When the body lacks venue or date, check attachments: run OCR/vision extraction on flyers. Below-threshold confidence → mark for manual review, do not guess.

### 4.5 Human lanes

- All pricing and closing: human, always.
- Orders ≥ `big_order_threshold_boxes`, and all wholesale accounts: Kenneth personally.
- Win-back and prior customers: Kenneth's personal voice (4.10); you draft, he sends.

### 4.6 Fulfillment branches (context for sequencing, not yours to execute)

- Stock orders: Shopify link or manual invoice → ship.
- Custom logo: artwork → proof approval → production → ship. Lead time = `custom_logo_lead_time_days`; this is why the anniversary offset exists.

### 4.7 HubSpot data model

Custom deal properties (create if absent): Event Name, Event Date, Venue, Ask Type, Outcome, Boxes, Next Outreach Date (= Event Date − `anniversary_offset_days`), Source Thread URL, Budget Signal, Prior Customer.

Pipeline "Tournament & Event Sales": Captured → Qualified → Outreach Sent → In Conversation → Quoted → Closed Won / Declined (donation-only) / No Response.

Associations: deal ↔ contact ↔ company. One deal per event per year; a new year's event is a new deal on the same company.

### 4.8 Excavation (both inboxes, 2020 → present)

Query bank – run every family per account per year window `after:YYYY/01/01 before:YYYY+1/01/01`:

- `{tournament outing scramble "golf classic" "golf day"}`
- `{fundraiser charity foundation booster benefit} golf`
- `{sponsor sponsorship donation donate} {golf "golf balls"}`
- `{raffle prizes "tee gift" "goodie bag"}`
- Seed set: `label:` + `prior_contractor_label` (partially applied by a former contractor; treat as seed, not ground truth)

Pipeline: search → thread-level extraction (4.4 fields) → flyer OCR where needed → normalize org names → merge against the leads already in Airtable → dedupe on contact email and domain → prior-customer join against sent mail and Shopify export → write to the Airtable review ledger with per-row confidence and thread links.

On the merge: an excavated thread and an existing Airtable lead for the same organization become one record, not two. Where the two disagree on a field, take the more recent source and flag the conflict for review. Never overwrite a human-entered Airtable value silently – that is a merge instruction under rule 5, and you do not have one.

Expect ~85–90% clean automatic extraction; route the remainder to a manual-review view. **Then stop.** Human approves rows; approved rows are eligible for HubSpot, and the import itself runs on Kenneth's trigger (M4).

### 4.9 Outbound lookalike engine

Seeds (won or warm): Alpha Xi Lambda, Toledo – an Alpha Phi Alpha Fraternity, Inc. alumni chapter; Tuskegee Airmen chapters; Lee Stovall's tournament; 100 Black Men of Atlanta.

Lens order (work the warmest ring first):

1. **Alpha Phi Alpha Fraternity, Inc. chapters** – Kenneth's own fraternity. Undergraduate and alumni chapters with annual golf classics, scholarship tournaments, founders'-day outings. This is the priority lens; "Alpha" in this document always means Alpha Phi Alpha Fraternity, Inc.
2. Wider Divine Nine – Omega Psi Phi, Kappa Alpha Psi, and the remaining organizations, each with its own golf-event tradition.
3. Veterans organizations – Tuskegee Airmen chapters and lineage organizations.
4. 100 Black Men chapters nationally.
5. Women-in-golf associations.
6. Booster clubs, church and community foundations – Georgia first, then adjacent states.

Output per lens: organization, chapter/city, event name, typical month, contact, source URL → review ledger → approved rows enter HubSpot as outbound prospects on the same anniversary calendar. Same review gate as excavation.

This engine is Phase 4 work and milestone M8. Build nothing here until Phase 4 is commissioned; if the excavation surfaces obvious lookalike patterns along the way, record them in `/reports/` for later rather than acting on them.

### 4.10 CEO win-back note (skeleton – you personalize per thread from its actual history; Kenneth sends)

> Subject: We owe you a better answer
>
> Hi {First name},
>
> Kenneth here, founder of Renegade Golf. Going back through our inbox I found your note about {event} – and I hate that it never got the answer it deserved. We were growing faster than our systems, and your email paid the price. That's on me.
>
> We can't always do donations, but for community events like yours we do custom Renegade balls at a price that makes sense for fundraisers – they make great prizes and tee gifts. If {event} is running again this year, I'd love to actually be useful this time.
>
> Either way – thank you for thinking of us the first time. Hoping to earn the second.
>
> – Kenneth

Save each as a draft in a dedicated batch; produce a one-line-per-draft index so Kenneth can review the set in one sitting.

### 4.11 Weekly digest

Every Monday, to Kenneth: new opportunities captured; anniversaries inside the offset window; threads with no reply past 48 hours; drafts awaiting his review; lookalike additions. Plain text, scannable, under one screen.

## 5. Build Order and Milestone Gates

The build runs across four commissioned phases. Each phase ends at a milestone that is also a commercial boundary: **do not begin a milestone belonging to a phase that has not been commissioned.** If you reach one, stop and report that the phase boundary has been hit.

| Milestone | Phase | Deliverable | Acceptance check | Gate |
|---|---|---|---|---|
| M0 | 1 | Bootstrap (Phase 0 complete) | Smoke tests pass; scaffold committed; parameters collected | Report, wait |
| M1 | 1 | Gmail layer live | Labels + filters exist and are idempotent on re-run; manual-steps checklist delivered | Report, wait |
| M2 | 2 | Excavation dry run | Per-family, per-year hit counts; 20-row extracted sample in ledger for QA | Kenneth approves sample quality |
| M3 | 2 | Full excavation | Complete ledger, merged with the existing Airtable leads, deduped, confidence-scored, prior-customer joined | **Hard stop: human row approval** |
| M4 | 2 | HubSpot rail | Properties + pipeline created; the Airtable → HubSpot push mapped field to field and proven end to end on a test batch; every record links its source thread; spot-check 10 records | **Hard stop: the full import runs on Kenneth's trigger. Phase 2 ends here** |
| M5 | 3 | Forward triage | New mail classified, labeled, upserted, draft replies saved; digest v1 running | One full week supervised |
| M6 | 3 | Anniversary engine | Outreach drafts generated at offset; win-back batch drafted with index | Draft-only until Kenneth flips the switch |
| M7 | 3 | Handover | Runbook, escalation rule, going-live sequence and monthly health check produced per the operating model; the coordinator runs one full daily pass unaided | **Kenneth away for a week, nothing missed. Phase 3 ends here** |
| M8 | 4 | Lookalike engine at scale | Alpha Phi Alpha lens complete Georgia-first, then the wider lens order; ledger rows for approval; the engine running on a standing cadence | Review gate |

Work strictly in order. Commit locally at every milestone with a plain-language message (or snapshot, per 3.4). If a milestone is blocked more than one working session, write `/reports/blocked-<milestone>.md` with cause and options.

**On M7.** The system is built for two people: Kenneth on pricing, closing, large orders and anything carrying his name; a coordinator on the daily pass, draft approval, row approval and keeping Airtable clean. Write the runbook for the coordinator, not for Kenneth, and assume that person has never seen the system before. If no coordinator has been named when you reach M7, build the artefacts anyway and report the gap.

## 6. Week-One Human Actions (not agent work – surface these to Kenneth on first run)

1. Colorado Tuskegee Airmen – reply personally: apology for the miss, thanks for their service, discounted offer for the upcoming event.
2. Rosalyn (women's event, Sept 26–28) – reach out now; August is the order window; check thread history first for last year's possible order.
3. Que's Friendship Foundation (Oct 10, Henry/Clayton Co, GA) – get-ahead note with a discounted offer.
4. Savannah tournament (Nov 6) – convert the declined donation into a paid offer.
5. Montfort Marines (Stockbridge, GA) – contrition note now; capture for next year's cycle.

---

*Ground truth authored by Five Points Digital Studio from the July 22, 2026 discovery sessions. Direct questions about intent to Kenneth; questions about architecture to Five Points.*
