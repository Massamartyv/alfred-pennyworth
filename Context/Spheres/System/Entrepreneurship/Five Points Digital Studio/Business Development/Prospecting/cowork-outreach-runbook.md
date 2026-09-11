# Five Points — Cowork Outreach Runbook

**Purpose:** A self-contained runbook for a Claude Cowork (computer-use) agent to send a set of pre-written outreach messages from the operator's own accounts.
**Operator:** Martavious Spicer — founder, Five Points Digital Studio.
**Authorized:** 2026-06-24. The operator has authorized sending every message in sections 3 and 4 from his accounts.
**Scope:** 11 Craigslist replies, plus 4 companies contacted on two channels each (LinkedIn note + job application) = 19 send tasks.

> These are real messages sent to real people from the operator's real accounts. Once sent, they cannot be recalled. Read sections 0–2 fully before acting.

---

## 0. Mode and non-negotiables

**SEND MODE: FULL AUTONOMOUS.** Do not pause for per-message confirmation. Work through the task list and send.

The following are not optional pauses — they protect the operator's outcome and must hold even in autonomous mode:

1. **Verbatim only.** Send each message exactly as written in the fenced block. Do not rewrite, embellish, summarize, translate, or add. Do not invent facts, names, results, prices, or links. The only substitutions permitted are the bracketed `[TOKENS]` filled from the Assets block in section 1.
2. **LinkedIn identity check.** Before any LinkedIn send, confirm the open profile matches BOTH the name AND the role/company named in the task. If it does not match, SKIP and log "identity unverified." This applies especially to Blue State (two people of that name exist — the target is "SVP, Platform Partnerships, Blue State").
3. **Missing-asset rule.** If a task needs an asset not present in section 1, send the asset-free version where one is noted; where the task is marked "requires assets," SKIP and log "missing assets."
4. **Account-survival pacing.** LinkedIn restricts accounts that send many cold touches quickly. Honour the pacing in section 2. This is what keeps the messages landing instead of getting the account locked partway through.
5. **Stop conditions.** If LinkedIn shows a checkpoint, captcha-wall, or "unusual activity" warning, STOP all LinkedIn sends and log. If any platform demands a login or 2FA you cannot complete, STOP that channel and log.

---

## 1. Assets — operator fills this in before the run

Cowork reads these values. Leave a line blank only if you accept the skips it causes.

```
OPERATOR_NAME:        Martavious Spicer
OPERATOR_EMAIL:       martavious.spicer@icloud.com
OPERATOR_PHONE:       +1 470-556-3989
OPERATOR_LOCATION:    Atlanta, GA — remote
CAL_LINK:             https://cal.com/martavious-spicer/30min
LINKEDIN_URL:         (not on file — not required; LinkedIn notes send from your logged-in account)
PORTFOLIO_URL:        https://fivepoints.studio
SAMPLE_BUILD_URLS:    https://strong-tower-christian-ministry.vercel.app, https://fountain-christian-center-mu.vercel.app
STANDARD_RATE:        (blank — no clean hourly/project rate on file; only $5,000–$8,000+/mo retainers, which do not fit the acupuncture hourly gig)
RESUME_FILE_PATH:     (not applicable — job applications dropped per operator instruction 2026-06-24)
WORK_AUTH:            US citizen
RELOCATE:             No — remote
```

---

## 2. Execution rules

**Pre-flight.** Confirm the operator is logged into: LinkedIn, the email account named in `OPERATOR_EMAIL`, and a working browser. Confirm section 1 is filled. If `RESUME_FILE_PATH` or `PORTFOLIO_URL` is blank, the four job-application tasks in section 4 will be skipped — proceed with the LinkedIn and Craigslist tasks regardless.

**Channel mechanics.**

- **Craigslist (section 3).** Open the post URL. If it shows "this posting has expired/been deleted," log "expired" and skip. Otherwise click **reply**, choose the email/webform option, paste the message verbatim, solve any captcha, send.
- **LinkedIn note (section 4).** Open the profile URL. Run the identity check (rule 0.2). If already connected, open **Message** and send the FULL message. If not connected, send a **connection request with note** using the SHORT note (LinkedIn caps the note near 300 characters); log "invite sent — full message on accept," and once accepted on a later pass, send the full message. Do not use InMail unless the account has Premium.
- **Job application / ATS (section 4).** Open the apply URL. Fill fields from section 1. Upload `RESUME_FILE_PATH`. Paste the FULL message into the cover-letter or "anything else" field. Submit. If any required field cannot be filled from section 1, SKIP and log "form incomplete." Note: these forms expect an individual applicant and a resume; if that does not fit, the LinkedIn note for the same company is the primary touch.

**LinkedIn pacing (account safety).**

```
LINKEDIN_MAX_PER_DAY:   5
LINKEDIN_GAP_MINUTES:   10–30 (vary naturally)
```

Send Craigslist, the job applications, and any email today. Drip the LinkedIn notes across as many days as the cap requires. Raising these values risks an account restriction that stops every remaining send — change them only deliberately.

**Logging.** After each task, update the Results Log in section 5 with status, timestamp, and any note.

---

## 3. Tier 1 — Craigslist replies (11)

For each: open the URL, reply, paste the message verbatim, send. Sign-off is part of the message.

### TASK 1 — San Diego, counselling platform
URL: https://sandiego.craigslist.org/csd/cpg/d/san-diego-website-payment-system-and/7942697404.html
```
Saw your post about adding the payment and video pieces to the counselling site, with the end-of-July date on it. That timeline is the part most developers underestimate, so I will be straight: it is doable, and doing it properly matters more here than almost anywhere, because you are handling client payments and live sessions on the same platform. We build exactly this kind of system – secure payment, integrated video, a booking flow your clients move through without friction. I can send two relevant builds and a short plan for hitting end of July. What is the best email for you? Or if it is easier, twenty minutes this week: [CAL_LINK]

Martavious
Five Points Digital Studio
```

### TASK 2 — Phoenix, real estate site rebuild
URL: https://phoenix.craigslist.org/nph/cpg/d/phoenix-create-new-website-from/7942091692.html
```
Read your post on rebuilding the GoDaddy site into something more robust, and the line about not wanting a cookie-cutter build is the right instinct. In a market like the Biltmore corridor, the site is the one place you control the whole impression before a buyer ever calls, and most agents there look identical online. We build property-led sites with real interactivity, and where it earns its place, the AI layer you mentioned – search, qualification, the follow-up that usually slips. I can show you a couple of builds and map what yours would take. Worth a short call this week? [CAL_LINK]

Martavious
Five Points Digital Studio
```

### TASK 3 — Dallas / Rockwall, premium Framer brand site
URL: https://dallas.craigslist.org/dal/cpg/d/rockwall-framer-web-developer-needed/7939930671.html
```
Saw the brief for the Framer build – premium, minimal, the five product pages, launching 1 September. The Framer choice tells me you already know the look you are after, and that you are building a brand, not just a page. That is the work we like. We build creator and personal-brand sites that hold that premium feel and still turn a visitor into a buyer of the offer, and 1 September is comfortable from where the brief sits. I can send two relevant builds and a fixed scope mapped to the launch date. Best email for you?

Martavious
Five Points Digital Studio
```

### TASK 4 — Los Angeles, acupuncture education platform — REQUIRES ASSETS (`SAMPLE_BUILD_URLS` and `STANDARD_RATE`)
URL: https://losangeles.craigslist.org/wst/cpg/d/los-angeles-web-designer-word-press/7940411932.html
Note: the post states "NO RESPONSE WITHOUT THIS INFO." If `SAMPLE_BUILD_URLS` or `STANDARD_RATE` is blank, SKIP and log "missing assets."
```
Saw your post – WordPress and WooCommerce, the social side, and the Mailchimp programme, for a platform serving several thousand practitioners. The thing I would want to protect for you is the path a licensee takes from email to enrolled, especially around the renewal cycle when demand spikes. That is where most education stores quietly lose people. We run all of it as one system – store, email, social – so it works together instead of in pieces. A few relevant builds: [SAMPLE_BUILD_URLS]. My rate: [STANDARD_RATE]. Happy to walk the platform on a call: [CAL_LINK]

Martavious
Five Points Digital Studio
```

### TASK 5 — Miami / Fort Lauderdale, The Invest Coach
URL: https://www.craigslist.org/view/d/miami-part-time-web-developer-needed/jwnVCXaN7iYxgwqpmg1iqX
```
Saw your post for ongoing help with the presence at TheInvestCoach.com. The timing reads right – the .com is still on a holding page, so this is the moment to build the coaching side properly rather than patch it later. What we do well is exactly this: stand up the site, then steward it month to month as the offer grows, so you are not rehiring every time something needs to change. I can send a couple of relevant builds and how a long-term engagement tends to run. Best email, or twenty minutes this week: [CAL_LINK]

Martavious
Five Points Digital Studio
```

### TASK 6 — San Diego (Kearny Mesa), ongoing site and SEO
URL: https://sandiego.craigslist.org/csd/cpg/d/san-diego-seeking-website-pro/7942026223.html
```
Saw you are after ongoing help with the site and the SEO – someone steady rather than a one-off. For a newer business that is the right call, because the early months are when the site and the search footing actually compound, if they are set up correctly. We do this as a standing engagement: the site maintained, the SEO worked properly, no scramble every time something needs to change. Happy to start by text per your note – what is the best number? Or a quick call here: [CAL_LINK]

Martavious
Five Points Digital Studio
```

### TASK 7 — San Francisco, lead-gen pipeline (Drop Cowboy)
URL: https://sfbay.craigslist.org/sfc/cpg/d/san-francisco-python-aws-contractor/7937110304.html
```
Saw the post on extending the follow-up pipeline – the Day 1/3/7/14/21 cadence across SMS and ringless voicemail, with the Drop Cowboy API and the suppression handling. That is a specific build, and the suppression and opt-out logic is the part that has to be exactly right, not the cadence. We build and maintain these pipelines – Python and AWS, clean webhook handling into Drop Cowboy, a dashboard if you want eyes on it. Send me the current setup and I will come back with a scope and a quote. Best email for that?

Martavious
Five Points Digital Studio
```

### TASK 8 — Santa Rosa (SF Bay), EHR to HIPAA-compliant app
URL: https://sfbay.craigslist.org/nby/cpg/d/santa-rosa-ruby-on-rails-web-developer/7936439581.html
```
Saw your post on taking the EHR from where it is to HIPAA-compliant. That is a specific kind of build – the compliance work sits underneath everything, so it is best approached in phases rather than one leap, which also lets you see progress and cost as it goes. We can map the compliance architecture, then build to it. Before I say more, two quick questions so I do not waste your time: is this a paid contract, or are you weighing the CTO route? And is Rails fixed, or open if there is a cleaner path? Happy to talk it through: [CAL_LINK]

Martavious
Five Points Digital Studio
```

### TASK 9 — Beverly Hills / LA, AI companion app
URL: https://losangeles.craigslist.org/wst/cpg/d/los-angeles-ai-companionship-app/7941344496.html
```
Saw the post – an AI companion with a real subscriber base, looking to make the persona feel more alive and less like the competitors. That problem is rarely a model swap. It is persona design, memory, and the small interaction details that make someone feel known. That is the interesting part, and the part we build for. I would want to understand your current stack and where it falls short before saying how we would approach it. Worth a conversation – [CAL_LINK], or send me the best email.

Martavious
Five Points Digital Studio
```

### TASK 10 — New York City, site re-setup and maintenance
URL: https://newyork.craigslist.org/mnh/cpg/d/new-york-web-site-set-up/7941830147.html
```
Saw your post about re-setting up the site and keeping it maintained. The word "simple" usually hides a few decisions worth getting right once, so the upkeep stays light afterwards rather than constant. The way I would approach it: a clean rebuild of what you have, then a small standing arrangement to keep it current. I can scope both quickly so you know the shape before committing to anything. Best email, or a short call: [CAL_LINK]

Martavious
Five Points Digital Studio
```

### TASK 11 — New Rochelle (NYC), virtual wellness studio
URL: https://newyork.craigslist.org/wch/cpg/d/new-rochelle-set-up-virtual-wellness/7938369149.html
```
Saw your post on setting up the virtual studio – the streaming, the booking, the look of the space. Most of that is a one-time build done right, not an ongoing hourly job, and you will feel the difference the moment students can find and book a class in two taps. I would put it together as one package – booking, streaming, a simple landing page – so it is live and working rather than half-assembled. Happy to sketch what that looks like for you. Best email, or twenty minutes: [CAL_LINK]

Martavious
Five Points Digital Studio
```

---

## 4. Tier 2 — LinkedIn note + job application, per company (4)

Each company gets two tasks: a LinkedIn note to the named person, and a job-application submission. Honour LinkedIn pacing (section 2).

### Zip — procurement SaaS, San Francisco

**TASK 12 — LinkedIn.** Profile: https://www.linkedin.com/in/aleenewebber  · Verify: "Aleene Webber, VP Corporate Marketing, Zip."
SHORT note (connection request):
```
Aleene – saw Zip is bringing on contract Webflow help for the marketing site, and that you already work with agency partners on it. After the Series D, that site has to carry far more weight, fast. I run a studio that builds exactly this. Worth a short connect?
```
FULL message (if connected, or after accept):
```
Aleene – saw Zip is bringing on contract Webflow help to build and grow the marketing site, and that you already work with agency partners on it. After the Series D and the pace of the EMEA push, that site has to carry far more weight, far faster. That is the work Five Points does – we build and run marketing sites in Webflow as one system, with Marketo, GA and GTM wired in properly, so the site keeps pace with the demand rather than lagging it. Rather than another hourly contractor, we can sit in as the studio partner on it. I can send a couple of relevant builds – worth a short call?

Martavious
Five Points Digital Studio
```
**TASK 13 — Application.** URL: https://jobs.ashbyhq.com/zip/25da2141-ede2-4294-909f-55b04b54f1bf — fill from section 1, upload resume, paste the FULL message above into the cover field, submit.

### Homebase — small-business SaaS, San Francisco and Toronto

**TASK 14 — LinkedIn.** Profile: https://www.linkedin.com/in/katie-daire-4899602  · Verify: "Katie Daire, CMO, Homebase."
SHORT note:
```
Katie – saw Homebase is bringing on senior Webflow help for the marketing site. With the team building out under you, that is the moment to treat the site as a system, not one-off pages. That is what my studio builds. Open to a quick connect?
```
FULL message:
```
Katie – saw Homebase is bringing on senior Webflow help for the marketing site: the performance work, the landing pages, the testing. With the team building out under you, that is the right moment to treat the site as a system rather than a backlog of one-off pages. That is what Five Points builds – a Webflow foundation tuned for Core Web Vitals, and a landing-page and experiment setup your team can run without a developer needed for every change. Rather than a single contractor, we can plug in as the studio partner behind it. Happy to send relevant builds and a short scope – open to a quick call?

Martavious
Five Points Digital Studio
```
**TASK 15 — Application.** URL: https://jobs.ashbyhq.com/homebase — locate "Senior Marketing Web Developer (contract)"; if not listed, log "role closed" and skip. Otherwise fill from section 1, upload resume, paste the FULL message, submit.

### Blue State — progressive digital agency, NYC / DC / Oakland

**TASK 16 — LinkedIn.** Profile: https://www.linkedin.com/in/samuel-zimmerman-2a462559  · **Verify carefully:** must read "SVP, Platform Partnerships, Blue State." Two people share this name — if the open profile is not that role at that company, SKIP and log "identity unverified."
SHORT note:
```
Sam – I run a studio on the same stack Blue State runs for client sites: WordPress, PHP, CRM and fundraising platforms. The standing contract web role usually means delivery capacity, not talent. We work white-label behind agencies. Open to a conversation?
```
FULL message:
```
Sam – I run a studio that builds on the same stack Blue State runs for client sites: WordPress and PHP, the CRM and CDP work, the fundraising platforms. I noticed you keep a standing contract web role open, which usually means delivery capacity is the constraint rather than talent. We work white-label behind agencies on exactly that – taking client builds off the bench cleanly, to your standard, under your name. With the senior bench you have added lately and the client load that follows it, it could be worth a conversation. I can send relevant builds and how we tend to run an overflow engagement. Open to it?

Martavious
Five Points Digital Studio
```
**TASK 17 — Application.** URL: https://www.bluestate.co/careers/job/?gh_jid=7241232 — fill from section 1, upload resume, paste the FULL message, submit.

### Intellibright — performance marketing agency, Austin

**TASK 18 — LinkedIn.** Profile: https://www.linkedin.com/in/ronrbrowning  · Verify: "Ron Browning, Founder/CEO, Intellibright."
SHORT note:
```
Ron – saw you are hiring WordPress and Elementor delivery, and that you just stood up the RevOps division off the RevRight deal. That kind of growth pulls build capacity tight. I run a studio that works white-label behind agencies on exactly that. Worth twenty minutes?
```
FULL message:
```
Ron – saw you are hiring WordPress and Elementor delivery, and that you have just stood up the new RevOps division off the RevRight acquisition. That kind of expansion usually pulls build capacity tight right as client work is climbing. I run a studio that works white-label behind agencies on exactly that – WordPress and Elementor, multi-client, to your spec and under your name. Rather than carrying the hiring and the overhead, you point overflow at us and it ships. Happy to send relevant builds and how an overflow partnership runs. Worth twenty minutes?

Martavious
Five Points Digital Studio
```
**TASK 19 — Application.** URL: https://apply.workable.com/intellibright/j/0FCF872419 — fill from section 1, upload resume, paste the FULL message, submit.

---

## 5. Results log — Cowork fills this in

| # | Task | Channel | Status | Time | Note |
|---|---|---|---|---|---|
| 1 | SD counselling | Craigslist | | | |
| 2 | Phoenix realtor | Craigslist | | | |
| 3 | Dallas Framer | Craigslist | | | |
| 4 | LA acupuncture | Craigslist | | | |
| 5 | Invest Coach | Craigslist | | | |
| 6 | SD Kearny Mesa | Craigslist | | | |
| 7 | SF lead-gen | Craigslist | | | |
| 8 | Santa Rosa EHR | Craigslist | | | |
| 9 | BH AI companion | Craigslist | | | |
| 10 | NYC site re-setup | Craigslist | | | |
| 11 | New Rochelle studio | Craigslist | | | |
| 12 | Zip / Aleene | LinkedIn | | | |
| 13 | Zip | Application | | | |
| 14 | Homebase / Katie | LinkedIn | | | |
| 15 | Homebase | Application | | | |
| 16 | Blue State / Sam | LinkedIn | | | |
| 17 | Blue State | Application | | | |
| 18 | Intellibright / Ron | LinkedIn | | | |
| 19 | Intellibright | Application | | | |

---

*Built 2026-06-24. Messages are final and in the operator's voice. Fill section 1, confirm logins, then run.*
</content>
