---
file_type: technical_recon
client: Strong Tower Christian Ministry
venture: Five Points Digital Studio
workflow: Website Development
phase: Reconnaissance
date: 2026-06-22
status: active
---

# Technical Reconnaissance – Strong Tower Christian Ministry

Audit of the existing live site at `http://strongtowercm.org` and the client intelligence gathered from it. This is a rebuild, not a refactor: the current site is a dated Wix property with stale content and unused features.

---

## Current Site Audit

| Layer | Finding |
|---|---|
| Platform | Wix (static.wixstatic.com assets throughout) |
| Protocol | Serves over HTTP, no enforced HTTPS |
| Domain | `strongtowercm.org` (registrar to be confirmed) |
| Freshness | Newest sermon videos date to 2022; Groups area empty; Members area unused |
| Streaming | Facebook and YouTube |

### Existing navigation

Home · Tithes & Offering · Leadership · Sermons · Sonship · What's Happening @ The Tower · Groups · Members · More

### Page-by-page

| Page | Status | Notes |
|---|---|---|
| Home | Live | Mission, vision, taglines, an audio player, service times |
| Tithes & Offering | Live | Giving page; current processor not yet confirmed |
| Leadership | Live | Pastor Kelsey M. Goodson and Prophetess Angela Goodson only |
| Sermons | Live | YouTube embeds, newest from 2022 (stale) |
| Sonship | Live | Teaching/discipleship concept; no usable body copy captured |
| What's Happening @ The Tower | Live | Events |
| Groups | Live (empty) | Wix Groups app installed but "No Groups at the Moment" |
| Members | Live (unused) | Wix Members login area, no active use |

---

## Client Intelligence

### Identity

- **Name:** Strong Tower Christian Ministry
- **Taglines (verbatim):** "He Loves You to Life, So We Love You to Life" and "It's All About Him"
- **Scriptural anchor (inferred):** Proverbs 18:10 – "The name of the LORD is a strong tower; the righteous run to it and are safe." To confirm with the pastor.

### Leadership

| Name | Title | Details (verbatim from site) |
|---|---|---|
| Kelsey M. Goodson | Pastor | "born and raised in Darlington, SC to Argie M. Goodson. He is a graduate of Mayo High School c/o 1989." |
| Angela Goodson | Prophetess | "wife of Kelsey Goodson… parents of two beautiful young ladies Chelsea and Naudia." |

No other leaders, elders or ministers are named on the current site. Confirm the full roster.

### Service schedule

| Service | Day | Time | Mode |
|---|---|---|---|
| Sunday Worship | Sunday | 10:30 AM | In-person, Facebook, YouTube |
| Mid-Week Service | Wednesday | 7:00 PM | In-person, Facebook, YouTube |
| Prophetic Impartation | Saturday | 10:00 AM | In-house only |

### Mission and vision (verbatim, usable as-is)

- **Mission:** "We the Strong Tower Christian Ministries strive to be ambassadors for Christ. This is accomplished in harmonious phases. We are a church body that is dependent on the Word of God through preaching, teaching, and displaying the Word of God in all we do."
- **Vision:** "To provide an environment for each person to grow in the knowledge of Jesus Christ and demonstrate that same love He has shown to all creations."

### Contact

- **Address:** 320 E National Cemetery Rd, Florence, SC 29506
- **Phone:** 843-468-0964
- **Email:** strongtowercm@yahoo.com

### Social and media

- Facebook: facebook.com/StrongTowerCm
- YouTube: @strongtowerchristianminist4397

---

## Content Gaps (to fill before or during the one-shot build)

1. **Confession of Faith / What We Believe** – referenced but no usable text. Five Points to draft from the church's tradition for pastoral approval.
2. **Sonship** – a teaching distinctive with no captured copy. Five Points to draft for approval.
3. **Leadership roster** – only the two Goodsons are named. Confirm whether elders, ministers or armour-bearers should appear.
4. **Brand kit** – logo files, exact hex colours and font names. Client has a brand; assets not yet supplied. Lift-and-confirm authorised as a fallback.
5. **Giving processor** – placeholder approved by the operator; provider to be selected by the church.
6. **Photography** – current site imagery is low-resolution Wix stock. Source or commission service and leadership photography.

---

## Infrastructure Requirements for Production

- Vercel project under the Five Points team (`studio-fivepoints`, `team_WYO4svCJKeaeKO6f00PpUg2y`)
- YouTube Data API v3 key and channel ID as environment variables (live status and sermon auto-pull)
- Resend API key and verified sending domain for the contact and prayer-request forms
- Newsletter provider key (provider-agnostic; default to a swappable env-configured endpoint)
- Giving destination URL as a single environment-configured value (swap-slot)
- Domain cutover from Wix to Vercel at handover (`dns-cutover.md` to be produced at the Release phase)

---

## Strengths to Preserve

- Strong, memorable taglines that already carry the brand voice
- Clear, usable mission and vision statements
- An active streaming habit on two platforms – the congregation already watches online
- A distinctive ministry identity (prophetic impartation, Sonship) worth foregrounding rather than burying in a "More" menu
