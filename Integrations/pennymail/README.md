# Pennymail

Owned email infrastructure. Campaigns, contacts, templates, tracking and analytics held in our own database, dispatched through rented delivery.

Pennymail replaces the email marketing platforms – Mailchimp, Klaviyo, Beehiiv and their peers – across every venture and the personal brand. It does not replace Google Workspace or iCloud. Human mailboxes stay where they are.

Sibling to [Pennyone](../pennyone/README.md), which does the same job for social syndication. Same shape: a thin control layer over a rented backend, routed per pipeline, operated by Alfred through MCP.

---

## What this is not

Pennymail is **not** a mail server. It runs no MTA, no Postfix, no Dovecot, no IMAP. The decision is deliberate and it is the single most important one in the design.

Running an outbound MTA on a fresh IP means earning reputation from zero. Gmail and Microsoft bulk-sender rules require SPF, DKIM, DMARC alignment, RFC 8058 one-click unsubscribe and complaint rates below 0.3%. A new IP arrives with none of that, warming takes weeks of disciplined volume ramps, and a single poisoned list damages every brand sharing the address space.

So Pennymail owns the application layer and rents the delivery layer. Lists, consent, templates, campaigns, sequences, tracking and analytics are ours, in our database, queryable by Alfred, portable to any provider. Only the last mile is bought.

---

## Provenance

The architecture is informed by [BillionMail](https://github.com/aaPanel/BillionMail), an open-source mail server and marketing platform. BillionMail bundles two products – an MTA stack and a marketing application – and Pennymail takes the shape of the second while discarding the first.

**No BillionMail code is used.** BillionMail is AGPLv3, and the network clause of that licence triggers on serving the software over a network. A fork would bind every future client-facing deployment to source disclosure. Functionality is not copyrightable; the implementation is. Pennymail is written from scratch.

---

## Architecture

```
Clay ──────────────┐
                   ▼
             pm-clay-intake ──┐
                              ▼
Alfred ──► Pennymail MCP ──► Supabase (pm schema) ──► pm-dispatch ──► provider ──► inbox
                              ▲                                          │
Console (Next.js) ────────────┤                                          │
                              │                                          ▼
                        pm-track / pm-unsub ◄──── recipient       pm-webhook
                              │                                          │
                              └──────────► pm.events ◄───────────────────┘
```

Six components:

| Component | Where | Job |
|---|---|---|
| **Schema** | Supabase Postgres, `pm` schema | The record. Contacts, consent, lists, templates, campaigns, sequences, messages, events, suppressions. |
| **Edge functions** | Supabase | Ingest from Clay, open and click tracking, unsubscribe, provider webhooks, the dispatch worker. |
| **MCP server** | `Integrations/pennymail/`, Python and FastMCP | Alfred's hands. Read the state, draft the work, send behind confirmation. |
| **Console** | `Apps/pennymail-console/`, Next.js on Vercel | Template preview, campaign analytics, deliverability. Eyes only where eyes are needed. |
| **Providers** | Amazon SES, Postmark | The rented last mile. Swappable per lane. |
| **Clay** | External | List building and enrichment. Feeds contacts in; sends nothing. |

---

## The three lanes

Pennymail carries three classes of traffic. They share a codebase and a database. They share **no** reputation whatsoever, and the schema enforces the separation rather than trusting a convention.

| Lane | Traffic | Sending domain | Provider | Risk |
|---|---|---|---|---|
| `transactional` | Stripe receipts, Camp Pennyworth enrolment, form confirmations, proposal delivery | `mail.{brand}` subdomain | Postmark | Low. A lost message costs money, so this lane buys the best inbox placement available. |
| `marketing` | Newsletters, campaigns, announcements to opted-in lists | `news.{brand}` subdomain | SES, dedicated configuration set | Medium. Real people who asked for it, but volume and complaint exposure. |
| `cold` | Outbound prospecting sequences | **Separate burner domains.** Never a brand domain. | SES, isolated configuration set and identities | High. Quarantined by design. |

Three rules make the separation real:

1. **The root domain never sends automated mail.** `fivepoints.studio` and its peers are reserved for human Workspace correspondence. Subdomain isolation means a marketing reputation hit cannot stop a client email reaching its recipient.
2. **Cold outbound lives on domains we are willing to lose.** Registered separately, DNS separate, reputation separate, and if one burns it is replaced without touching the brand. The schema enforces this with a bidirectional constraint – a cold-lane identity must be flagged as a burner, and a burner may not be used for any other lane.
3. **Lane mismatch is impossible, not merely discouraged.** Campaigns, sequences and messages carry a composite foreign key against `(sending_identity_id, lane)`. A marketing campaign cannot be dispatched from a cold identity at the database level.

### On Clay and cold outbound

Clay retains enrichment and list building for every venture and the personal brand. It no longer sends.

That transfer brings the hard part of cold outbound in-house: burner domain rotation, per-mailbox daily caps, reply detection, and the discipline of stopping a sequence the moment a human responds. Phase 6 exists to build exactly that, and it is sequenced last because it should not be attempted until the tracking, suppression and deliverability instrumentation are proven on lower-risk traffic.

---

## Pipelines

Every operation declares a pipeline, which resolves to a tenant. Same routing key as Pennyone.

| Pipeline | Tenant kind | Notion workspace |
|---|---|---|
| `personal` | personal | Personal |
| `marty_gras` | venture | Personal – the standing exception |
| `five_points` | venture | Five Points |
| `paradigm` | venture | Own |
| `lillie_and_lynette` | venture | Own |
| `atlas` | venture | Own |

Tenancy is single-tenant in practice and multi-tenant in structure. Every table carries `tenant_id`, row-level security is enabled from the first migration, and policies key off `app.tenant_id`. Retrofitting tenancy into a live email system is brutal; carrying the column from the start costs nothing.

A pipeline with no verified sending identity returns a clean "not provisioned" error. No provider call is made.

---

## Privacy and compliance

Non-negotiable, and built into the schema rather than added later.

- **Opaque tracking tokens.** The open pixel and click redirect carry a random per-message token, never an email address or contact identifier. No personal data ever appears in a URL.
- **Hashed IPs.** Event rows store a salted hash. The raw address is never persisted.
- **One-click unsubscribe.** RFC 8058 headers on every marketing and cold message – `List-Unsubscribe` plus `List-Unsubscribe-Post`, with a POST endpoint that honours the request without a confirmation step.
- **Consent as provenance, not a flag.** The `consent` table records the basis, the evidence and the timestamp for every contact on every lane. An import and a double opt-in are not the same thing and are not stored as though they were.
- **Suppression outranks everything.** A suppression entry blocks a send regardless of list membership, campaign configuration or manual override. Hard bounces and complaints write one automatically. Global scope blocks across all tenants.

---

## MCP surface

Read tools are free. Write tools that dispatch mail require explicit confirmation in chat per Navigation Rule 3, and `send_campaign` is the hard gate.

**Read**

| Tool | Returns |
|---|---|
| `health_check` | Provider connectivity, identity verification state, queue depth, per-lane sending status |
| `list_pipelines` | Configured pipelines and their provisioning state |
| `list_identities` | Sending identities with DKIM, SPF and DMARC verification |
| `list_audiences` | Lists and segments with live counts |
| `search_contacts` | Contact lookup across a tenant |
| `get_contact` | Full record – attributes, consent per lane, message history, event trail |
| `list_campaigns` | Campaigns filtered by status |
| `campaign_report` | Sends, delivered, opens, clicks, bounces, complaints, unsubscribes |
| `deliverability_report` | Per-identity complaint and bounce rates against the 0.3% threshold. The one that matters. |

**Write**

| Tool | Gate |
|---|---|
| `upsert_contact`, `create_list`, `add_to_list`, `remove_from_list` | Standard |
| `suppress` | Standard. Suppression is always safe. |
| `create_template`, `update_template` | Standard |
| `create_campaign` | Standard. Drafts only – creation never sends. |
| `preview_campaign` | Standard. Renders against sample contacts and runs a pre-flight check. |
| `schedule_campaign` | **Confirmation required** |
| `send_campaign` | **Confirmation required** |
| `pause_campaign`, `cancel_campaign` | Standard. Stopping is always safe. |
| `enroll_sequence` | **Confirmation required** |
| `stop_enrollment` | Standard |

---

## Build sequence

| Phase | Delivers | Gate |
|---|---|---|
| **0. Foundation** | Schema, migrations, tenant seed, provider and identity registration. No sending. | Migration applied, RLS verified |
| **1. Spine** | MCP server, Clay intake function, suppression import from the outgoing platforms | Alfred can read and write contacts |
| **2. Transactional** | Postmark wired, identities verified, dispatch worker, delivery webhooks | First real send – a Stripe receipt |
| **3. Instrumentation** | Open pixel, click redirect, RFC 8058 unsubscribe, event pipeline | Tracking verified end to end on transactional traffic |
| **4. Marketing** | SES wired, warm-up ramp, first list migration, first broadcast | A campaign sent from `news.` with clean metrics |
| **5. Console** | Next.js surface for template preview and analytics | Deployed on Vercel |
| **6. Cold** | Burner domains, sequences, mailbox rotation, reply detection | Sequence running with reply-stop proven |

Phases 2 and 4 each require provider production access and DNS work. Neither is instant, and both should be started early even though they gate later phases.

---

## Status

**Phase 0 in progress.** Schema authored. Nothing provisioned, nothing sending.

| Surface | State |
|---|---|
| Schema | Authored, not applied |
| Supabase project | Not selected |
| Postmark account | Not created |
| SES account | Not created |
| Burner domains | Not registered |
| MCP server | Not built |
| Console | Not built |

---

## Open decisions

Carried forward for a ruling rather than assumed:

1. **Supabase project.** A dedicated project, or the existing `fivepoints-site` instance. A dedicated project is cleaner given Pennymail serves all six brands and Five Points is only one of them – putting cross-venture infrastructure inside a venture project repeats the mistake that put Atlas state in the Five Points workspace.
2. **Epiphany and Substack.** Substack is partly a discovery network rather than a send button. Migrating the newsletter gains ownership and loses distribution. Leaving it there while everything else moves is defensible.
3. **Burner domain slate.** How many, on what registrar, and what naming. Needs deciding before Phase 6 and registering well before it, since aged domains outperform fresh ones.

---

*Last updated: 2026-08-08 – Phase 0. Architecture ratified, schema authored.*
