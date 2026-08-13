---
file_type: sop
sop_id: OPS-008
venture: Five Points Digital Studio
status: staged
last_updated: 2026-08-13
---

# Pre-Dial DNC Scrub

No cold outbound touch – voice or text – leaves Five Points without a current Do Not Call verdict on the number. This document is also the written do-not-call policy of the studio, available on request under 47 CFR 64.1200(d).

---

## Why this gate exists

- **Federal.** Calls to a number on the National DNC Registry carry a private right of action of $500 to $1,500 per call once a person receives more than one such call in 12 months by or on behalf of the same seller – 47 U.S.C. 227(c)(5); 47 CFR 64.1200(c)(2). Live human voice avoids the artificial-voice rules, not these.
- **Georgia.** O.C.G.A. 46-5-27 as amended by SB 73, effective 2024-07-01: $2,000 per violation, no knowledge requirement, uncapped class recovery with attorney fees and vicarious liability for calls placed on behalf of the studio. Same more-than-one-in-12-months trigger. The home state of the studio is among the most plaintiff-friendly in the country.
- **The B2B assumption does not hold.** The registry accepts personal numbers only, so a listed number is personal by declaration. Sole proprietors run businesses on registered cells; those numbers are the classic trap. Five Points never argues the point – a listed number is not touched. Separately, the 2024 TSR amendments extended the truthfulness rules to B2B calls, so clean B2B status is no longer a blanket federal pass.
- **The voicemail-plus-text beat is two solicitations.** On a listed number, the script's standard pair perfects both private actions in one afternoon. The gate therefore sits before the first touch, never the second.

## Trigger

Any cold outbound call or text under Five Points scope – every switchboard dial, every list import and every future vendor or agent dialing on behalf of the studio.

## Steps

0. **Subscribe – operator hand, once.** Register the studio at telemarketing.donotcall.gov for a Subscription Account Number covering the metro Atlanta area codes – 404, 470, 678 and 770, plus the 943 overlay. The first five codes are free; statewide coverage adds 229, 478, 706, 762 and 912 at $82 each per year at the FY2026 rate. Renew annually; the certification attests the data is used for scrubbing only.
1. **Snapshot – monthly, on the 1st.** Download the area-code files to `Growth/Prospecting/DNC Registry/` – gitignored, never committed – and record a ledger line: date, area codes, row counts. A snapshot older than 31 days is expired and blocks all dialing.
2. **Scrub – per card, at Brief.** Match the number on the card against the current snapshot. Write the verdict to the CRM card: `DNC Status` Clear or Listed, `Scrubbed` today. The monthly snapshot re-stamps every active Prospect card the same day.
3. **Gate – at Next and at the dial.** A number is served only when DNC Status is Clear and Scrubbed is within 31 days. Dial window 8:00 a.m. to 9:00 p.m. prospect local time. State first name, surname and the studio at the top of the call – Georgia requires prompt identification. Never block caller ID.
4. **Suppress – at Log.** The outcome word `remove` records a do-not-call request: quote it verbatim in the call log, set DNC Status to Do Not Call and Status to Lost. Suppression is same-day, permanent and portfolio-wide – it binds every future campaign, vendor and agent dialing for the studio.

## Decision points

- Listed number → no call, no text, no exception on cold outreach. Cold means cold: no established business relationship exists to invoke.
- An inbound inquiry opens a three-month contact window and a purchase an 18-month window – the federal established business relationship. Lifting a Listed verdict on that basis requires the evidence on the card and an operator ruling.
- A number the prospect gives during a live call, for a text they asked for, is solicited contact – clean. Log the ask in the call log line.
- Non-Georgia US numbers: 12 states run their own DNC lists – CO, FL, IN, LA, MA, MS, MO, OK, PA, TN, TX, WY – and roughly 32 require telemarketer registration. No cold dial into those states until that state clears at the outbound gate. International stays DM-first under the channel doctrine.

## Records – five years

Per the amended TSR recordkeeping rule – 16 CFR 310.5, effective 2024-10-15 – keep SAN receipts and certifications, the snapshot ledger, card verdict stamps and verbatim removal quotes for five years. The CRM card is the durable record; never delete a Lost card that carries a DNC request.

## Remediation – the blitz of 2026-08-13

The blitz began before this gate existed. On the first snapshot, scrub every number dialed or queued since 2026-08-13. Any listed number gets no second touch of any kind – both private actions perfect on the second solicitation, so stopping at one caps the exposure. Log each such card.

## Escalation

An attorney letter, AG contact or litigation threat stops the block immediately – operator and counsel before the next dial. An accidental dial to a listed number is logged the same hour and never redialed; the defense is the safe harbor, which this SOP exists to earn – written procedures, training, a scrub recorded within 31 days and the records above – 47 CFR 64.1200(c)(2)(i).

## Success criteria

Zero touches to listed or suppressed numbers. Every dialed card stamped Clear within 31 days. No snapshot older than 31 days on a dial day. Every removal request suppressed the day it is spoken.
