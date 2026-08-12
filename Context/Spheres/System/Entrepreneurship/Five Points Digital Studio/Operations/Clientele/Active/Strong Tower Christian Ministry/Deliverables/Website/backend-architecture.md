# Backend Architecture — Strong Tower Christian Ministry

**Current ruling, 2026-07-29: there is no backend. Every form goes to the church inbox by email.** Supabase is shelved, not deleted. The content management layer is an open question, deliberately unanswered.

This supersedes the 2026-07-27 "Supabase all-in" ruling, which was planned and provisioned but never wired into the site.

## How the three intake paths work

All three use Resend, and none of them stores anything.

| Path | Route | Goes to |
|---|---|---|
| Contact form | `src/app/contact/actions.ts` | `CONTACT_TO_EMAIL` |
| Prayer requests — page and the site-wide Need-prayer panel | `src/app/prayer/actions.ts` | `PRAYER_TO_EMAIL`, falling back to `CONTACT_TO_EMAIL` |
| Newsletter sign-up | `src/app/api/newsletter/route.ts` | `NEWSLETTER_TO_EMAIL`, falling back to `CONTACT_TO_EMAIL` |

Each carries a honeypot field, validates the email, sets `replyTo` to the sender so the office can reply in one click, and returns a plain-spoken error when the keys are absent rather than pretending to succeed.

The newsletter route was rewritten on 2026-07-29. It previously tried to add the address to a Resend audience and, whenever `NEWSLETTER_LIST_ID` was unset, accepted the sign-up and silently discarded it. Sign-ups now arrive as email like everything else.

## What has to be set before launch

Five environment variables in Vercel. Until `RESEND_API_KEY` and a recipient exist, all three forms show an honest "not set up yet — please ring the church" message.

```
RESEND_API_KEY=            # Resend API key
RESEND_FROM=               # e.g. Strong Tower Website <noreply@strongtowercm.org>
CONTACT_TO_EMAIL=          # the church office inbox
PRAYER_TO_EMAIL=           # optional; defaults to CONTACT_TO_EMAIL
NEWSLETTER_TO_EMAIL=       # optional; defaults to CONTACT_TO_EMAIL
```

`.env.example` still lists the retired `NEWSLETTER_LIST_ID` and `NEWSLETTER_PROVIDER` and is missing `NEWSLETTER_TO_EMAIL`. The file is permission-blocked to the agent; the operator updates it by hand.

**Sending domain.** Resend will only send from a verified domain. `strongtowercm.org` is still on Wix, so either verify it there by adding Resend DNS records, or set `RESEND_FROM` to a verified Five Points domain in the interim. This is a launch blocker for all three forms and is independent of the DNS cutover.

## Known limits of the email-only model

Accepted deliberately in exchange for having no database to run.

- **No list management.** Newsletter sign-ups arrive one per email; somebody in the office keeps the actual list. No unsubscribe handling, no broadcast tool. If the church later wants to send a real newsletter, that is a mailing-list provider decision, not a backend one.
- **No record of prayer requests.** Once the email is read, that is the only copy. There is no inbox with statuses, no history, no follow-up tracking.
- **No admin panel.** Nothing for staff to log into.
- **Volume.** Fine at church scale. If sign-ups ever arrive in bulk, per-signup email stops being sensible.

## The shelved Supabase foundation

Provisioned 2026-07-27, never connected to the site, holding no data.

| Item | Value |
|---|---|
| Org | Five Points Digital Studio (`auenrodwupfdfrfdhbrf`) |
| Project | `strong-tower-christian-ministry`, ref `elwpogjctnrqhqjkabrx`, us-east-1, free tier, $0 |
| Migrations applied | `init_core` (tables, RLS), `harden_advisor_warnings` |
| Tables | `staff`, `prayer_requests`, `contact_messages`, `subscribers`, `events` — all empty |

Free-tier projects pause after about a week of inactivity, which is harmless while nothing depends on it. The schema lives in migrations, so it replays into any project on demand. **Operator decision outstanding: leave it dormant against a future need, or delete it and reclaim the slot.** Nothing in the codebase references it either way.

If the church later wants persistence — a prayer inbox with statuses, an events calendar staff can edit — the route back is the phased plan in the git history of this file, starting with server actions that write to the database and notify by email rather than only notifying.

## Content management — open

Unanswered on purpose. Today all content is typed in the repo: page copy in the page files, service times and contact details in `src/lib/site.ts`, ministries in `src/app/ministries/page.tsx`, events hardcoded on the events page.

The question is whether the church needs to edit content themselves, and which content. The honest starting position is that most of it — doctrine, leadership biographies, service times — changes once a year, and the studio editing it on request may be cheaper and better than any tool. The plausible exceptions are events and announcements. Decide what actually changes weekly before choosing anything.
