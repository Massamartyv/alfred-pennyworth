# Renegade Golf — Lead Recovery and Inbox System

Working specification. Five Points Digital Studio. July 22, 2026.
Companion to commissioning statement FP-2026-001. Commercial terms live in commissioning documents, not here.

---

## 1. Problem Statement

Evidence from the July 22 inbox walkthrough with Kenneth Duncan.

- Two inboxes hold the history: **info@renegadegolf.com** (customer service, ~2022–present, Google Workspace) and **golfrenegade@gmail.com** (legacy, ~2020–2023).
- Inbound tournament, fundraiser, and donation requests arrive roughly weekly. Kenneth estimates **~250 threads over 4–5 years**. A closed order runs 10–30 boxes, **$300–500 typical**.
- Many arrive unread or unanswered. Donation-only asks are declined and never captured, though the standing conversion play — no to free, yes to discounted — works when it is actually run.
- **Tournaments are annual.** Every captured event has a predictable re-order window ~3–4 months before its anniversary. Owning that calendar is the system's core job.
- Critical detail (venue, exact date) often lives only in **flyer attachments**, not the email body.
- Known noise: The Golf Wire, The New York Sun, similar newsletters in the same inbox. A prior contractor's "Tournaments & Golf Outings" label exists and is partially applied — usable as a seed corpus, not ground truth.
- Recurring segments: Divine Nine chapters (Alpha Phi Alpha and Omega Psi Phi events observed; Kenneth is an Alpha Phi Alpha member), veterans organizations (Tuskegee Airmen chapters, Montfort Marines), women's golf associations, booster clubs, church and community foundations. Community-anniversary events, already warm to the brand.

### Observed examples (one 15-minute pass, one keyword pair)

| Org / contact | Event | Status |
|---|---|---|
| Colorado Tuskegee Airmen | Upcoming | Free-ball ask May 28, missed; they followed up 2 days ago |
| Kay Nelson — Alpha Golf / Alpha Xi Lambda, Toledo | Aug 10 | Worked from Apr 19; ~30 boxes closed. The model win |
| Lee Stovall | Aug tournament | Inbound Nov 29 last year; closed ~30 boxes |
| Unnamed (email Feb 19) | Mar 20 | Unread, missed entirely |
| JJ Jones | Apr 17 | Missed |
| Mark Anthony celebrity tournament | Jan 19 ask | No response |
| Brian | Nov 21 ask | Responded, declined |
| Rosalyn — women's golf | Sept 26–28 | Possible prior event together; unresolved |
| Que's Friendship Foundation | Oct 10 — Henry/Clayton Co, GA | Donation declined, never captured; likely recurring |
| Savannah tournament | Nov 6 | Donation declined, never captured |
| Montfort Marines | May 5 — Stockbridge, GA | Missed entirely (wrong inbox) |
| Football booster club | 2023 | Declined; recurring candidate |

---

## 2. Answer-Now List (this week, by hand — no system required)

1. **Colorado Tuskegee Airmen** — reply today: apology for the miss, thanks for their service, discounted-ball offer for the upcoming event.
2. **Rosalyn (women's Sept 26–28 event)** — reach out now; August is her order window. First resolve "did we work together last year" from thread history.
3. **Que's Friendship Foundation** — get-ahead-of-it note: October 10 is close; discounted balls this year.
4. **Savannah November 6 tournament** — capture, then convert the declined donation into a paid offer.
5. **Montfort Marines** — contrition note now; capture for next year's cycle.

---

## 3. System Phases

| Phase | Work | Commercial boundary |
|---|---|---|
| **1 — Structure** | HubSpot records and pipeline, forward capture, Gmail organization layer (§4), integration, calibration | FP-2026-001 (current commission) |
| **2 — Excavation** | Both inboxes 2020–present → opportunity ledger → human review → HubSpot import (§5) | Separate commission |
| **3 — Automation** | Anniversary engine, inbox triage agent, no-email-unanswered acknowledgment, weekly digest (§7) | Separate commission |
| **Human layer** | CEO win-back notes (~50, drafted for Kenneth's personal send), final pricing and closing | Kenneth, always |

---

## 4. Gmail Organization Layer (Phase 1)

Applied in a working session on Kenneth's account (~45 minutes). Five Points has no direct access to Renegade Golf's Google accounts; §4 is applied by screen-share session. Phases 2–3 require delegated OAuth access for the automation harness.

### 4.1 Consolidate the accounts

- Set auto-forward: golfrenegade@gmail.com → info@renegadegolf.com. Add send-as alias on info@ if replies from the old identity still matter.
- Legacy box stays untouched for excavation. One working surface going forward: **info@**.

### 4.2 Label tree

```
RG/Action                      <- needs a human reply
RG/Opportunity/Tournament
RG/Opportunity/Fundraiser
RG/Opportunity/Donation-ask
RG/Opportunity/Wholesale
RG/Captured                    <- pushed to HubSpot; done
RG/Noise                       <- newsletters, spam-adjacent
```

### 4.3 Filters (Settings → Filters; exact strings)

1. **Noise** — Matches: `from:(thegolfwire.com OR nysun.com)` → Skip inbox · Apply `RG/Noise` · Never mark important. Extend the from-list during the session; run an unsubscribe pass on the worst offenders.
2. **Opportunity, coarse cut** — Matches: `{tournament outing scramble "golf classic" "golf day" fundraiser booster charity} {sponsor sponsorship donation donate "golf balls" raffle prizes "tee gift"}` → Apply `RG/Opportunity/Tournament` · Always mark important · Star. (Braces are Gmail OR-groups; the two groups together require one hit from each.)
3. **Wholesale** — Matches: `{wholesale bulk "boxes of" cases}` → Apply `RG/Opportunity/Wholesale`.

Fine classification (tournament vs fundraiser vs donation-ask) belongs to the Phase 3 triage agent. Filters only make the coarse catch so nothing slips past the eye.

### 4.4 At-a-glance inbox (Settings → Inbox type → Multiple inboxes)

- Section 1 — "Needs reply": `label:rg-action`
- Section 2 — "Opportunities not yet captured": `label:rg-opportunity -label:rg-captured`
- Section 3 — "Captured, last 30 days": `label:rg-captured newer_than:30d`

This is the fallback view: even mail that never reaches HubSpot stays organized and visible, which is the explicit requirement.

---

## 5. Excavation Spec (Phase 2)

### 5.1 Corpus and query bank

Run each family across **both accounts**, per year window `after:YYYY/01/01 before:YYYY+1/01/01`, 2020 → present:

- `{tournament outing scramble "golf classic" "golf day"}`
- `{fundraiser charity foundation booster benefit} golf`
- `{sponsor sponsorship donation donate} {golf "golf balls"}`
- `{raffle prizes "tee gift" "goodie bag"}`
- Seed set: the prior contractor's label — `label:tournaments-golf-outings` (verify exact label name in session).

### 5.2 Extraction (agentic pass, thread level)

Ledger fields per opportunity: Organization · Contact name · Email · Phone · Event name · Event date · Venue · City/State · Ask type (donation / discounted / purchase / wholesale) · Outcome (won + qty / declined / no response / unknown) · Last touch · Thread link(s) · Prior customer (y/n/unknown) · Next outreach date (event date − 120 days) · Confidence · Notes.

Attachments: flyers run through OCR/vision extraction for venue and date when the body lacks them. Expect ~85–90% clean automatic extraction; the remainder queue for manual review. No magic promised — a ledger Kenneth approves.

### 5.3 Dedupe and the prior-customer join

- Normalize organization names; match on contact email and domain.
- Cross-reference sent mail and order history to resolve prior-customer status (the Rosalyn problem). **Open: where do order records live (Shopify?) and can we export them.**

### 5.4 Review gate

Ledger lands in a Google Sheet. Kenneth or Marty approves rows before any HubSpot import. Nothing writes to the CRM unreviewed.

---

## 6. HubSpot Spec (Phase 1 tie-in)

- Custom Deal properties: Event Name, Event Date, Venue, Ask Type, Outcome, Boxes, Next Outreach Date (Event Date − 120 days), Source Thread.
- Pipeline "Tournament & Event Sales": Captured → Qualified → Outreach Sent → In Conversation → Quoted → Closed Won / Declined (donation-only) / No Response.
- Wholesale accounts keep their separate structure per FP-2026-001.

---

## 7. Automation Spec (Phase 3)

- **Anniversary engine** — workflow fires at Next Outreach Date (T−120): planning-season email; follow-up at T−90. Draft-only mode for the first cycle; Kenneth approves every send until trust is earned.
- **Triage agent on info@** — classify → label → HubSpot upsert → draft acknowledgment (catalog attached; "we don't do donations, here's what we do" variant). Drafts only at first; auto-send limited to the acknowledgment class after a review period.
- **SLA** — nothing sits unanswered past 48 hours without surfacing in the digest.
- **Weekly digest to Kenneth** — new opportunities, anniversaries inside 120 days, threads aging past SLA.

---

## 8. CEO Win-Back Note (skeleton — Kenneth's voice, his personal send)

> **Subject: We owe you a better answer**
>
> Hi {First name},
>
> Kenneth here, founder of Renegade Golf. Going back through our inbox I found your note about {event} — and I hate that it never got the answer it deserved. We were growing faster than our systems, and your email paid the price. That's on me.
>
> We can't always do donations, but for community events like yours we do custom Renegade balls at a price that makes sense for fundraisers — they make great prizes and tee gifts. If {event} is running again this year, I'd love to actually be useful this time.
>
> Either way — thank you for thinking of us the first time. Hoping to earn the second.
>
> — Kenneth

---

## 9. The Workflow — Start to End (discovery round 2, July 22)

### 9.1 Entry

- **Primary:** website contact form → info@renegadegolf.com. One watch surface covers both.
- **Stragglers:** social DMs and occasional phone/text — manually forwarded into info@ for now; formal DM capture deferred until volume justifies it.
- **Outbound:** the discovery engine (§9.6) files prospects directly into HubSpot on the same calendar.

### 9.2 Triage (agentic — runs on Kenneth's Codex harness)

Classify every inbound on two axes: **ask type** and **budget signal**.

| Ask | Budget signal | Auto-response | Price posture |
|---|---|---|---|
| Donation / free balls | — | Tactful pivot: no donations, but discounted community pricing for events like yours | No numbers in the auto-reply; the tier is named by a human |
| Purchase intent | None stated | Acknowledge + qualify (date, quantity, logo) | Standard wholesale; no discount volunteered |
| Purchase intent | Low budget stated | Acknowledge + qualify; flag for discount discretion | Discount floored at the **higher wholesale tier** — never below without Kenneth |
| Any | — | — | **At-cost is a Kenneth-only exception** (the Colorado case); never offered by the system |

Every classified thread: label per §4.2 → HubSpot upsert → draft reply for human review. **The machine never states a price.**

### 9.3 Qualify

One pass captures: event name, event date, venue, quantity range, logo/custom need, budget signal, recurrence. Flyer OCR when the body lacks the detail.

### 9.4 Price and close (human lane)

- All pricing and closing is human — confirmed as the firm line.
- Big orders (threshold TBD, roughly 20+ boxes or wholesale accounts): Kenneth personally.
- Small orders: Kenneth for now; a future hire's lane once one exists.

### 9.5 Fulfill

Two branches:

- **Stock:** Shopify/store link or manual invoice → ship. Fast, minimal touch.
- **Custom logo:** artwork in → proof approved → production → ship. **Lead time unknown** — this number sets the true anniversary offset. T−120 stands until measured.

### 9.6 Outbound discovery engine (the lookalike play)

Seed from wins and warm history: Alpha Xi Lambda, Toledo (Alpha Phi Alpha Fraternity, Inc. alumni chapter), Tuskegee Airmen chapters, Lee Stovall's event, 100 Black Men of Atlanta (prior relationship).

Lenses to enumerate the marketplace:

- **Alpha Phi Alpha Fraternity, Inc. chapters first** — Kenneth's own fraternity; native credibility. Undergraduate and alumni chapters with annual golf outings, scholarship classics and founders'-day events
- The wider Divine Nine after the Alpha pass — Omega Psi Phi, Kappa Alpha Psi and the rest, each with its own golf-event tradition
- 100 Black Men chapters nationally
- Veterans organizations (Tuskegee Airmen chapters and lineage orgs)
- Women-in-golf associations
- Booster clubs, church and community foundations — Georgia first
- Further lenses extracted from the excavation corpus as patterns emerge

Each lens → org list → contact + next event date → HubSpot as outbound prospects on the same anniversary calendar. The architecture is defined in Phase 1 (statement stream 04); the engine runs at scale in Phase 3.

### 9.7 Re-engage

Anniversary engine per §7, offset validated against the real custom-logo lead time.

### 9.8 Harness note

Kenneth is building his agentic layer on **Codex**. Everything in this document is delivered harness-ready: plain-language agent instructions, the triage table above, the ledger schema (§5.2) as JSON-shaped fields, and explicit API scopes (Gmail read/label/draft, HubSpot CRM objects, Google Sheets). Nothing platform-locked.

---

## 10. Open Questions

1. **Custom-logo lead time in days** (proof + production + ship) — sets the anniversary offset.
2. **The wholesale ladder in numbers** — standard wholesale, higher-wholesale floor, at-cost. Kenneth defines; the system enforces the floor.
3. **Big-order threshold** for Kenneth's personal lane (boxes or dollars).
4. Order history location (Shopify?) and export access — the prior-customer join.
5. 100 Black Men of Atlanta history — where does that relationship record live?
6. Current catalog / price sheet for the acknowledgment.
7. Exact name of the prior contractor's label.
8. Access route for Phases 2–3: delegated OAuth to the harness.

---

*Last updated: 2026-07-22 — workflow defined end to end from discovery round 2; Codex named as the harness.*
