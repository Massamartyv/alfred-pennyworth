# Document 2 of 7: Five Points Digital Presence Audit

**Document type:** Three part specification (client facing intake form + internal audit scoring template + tier scope notes)
**Location:** Client facing intake form lives on a dedicated page within the Five Points website. Internal scoring template and tier scope notes are internal operational documents used by the Five Points team.
**Purpose:** Provides the complete workflow for assessing a client's current digital footprint, from collecting the information Five Points needs, through evaluating what they find, to delivering a polished report.
**Tone:** Client facing sections are warm, confident, and partner oriented (consistent with Document 1). Internal sections are direct, systematic, and built for speed of execution.

**Used by:** Silver — Digital Marketing Strategy Session, Silver — Social Media Audit and Strategy, Gold — Fractional CMO (onboarding), Gold — Content Engine Retainer (onboarding), and as the pre session audit for any engagement where understanding the current digital state is required.

**Data dependency:** This form assumes the prospect has already completed the Discovery Intake Form (Document 1). Information captured in Document 1 (name, email, phone, role, business name, website URL, business description, business age, team size, services of interest, biggest challenge, desired outcome, timeline, previous agency experience, and referral source) is stored in the unified prospect profile and is never requested again.

---

## PART 1: CLIENT FACING INTAKE FORM (Website Hosted)

### Context

This form is the follow up that a prospect receives after selecting "Digital marketing strategy or execution" on the Discovery Intake Form (Document 1). It arrives via email as a link to a dedicated page on the Five Points website.

The prospect has already told Five Points who they are, what their business does, what their biggest challenge is, and what success looks like. This form goes deeper into their digital presence specifically, collecting the context and access that Five Points needs to conduct a thorough evaluation.

This form does not ask the prospect to evaluate themselves. It asks them to provide the raw information so Five Points can do the evaluation with full context.

### No Redundancy Rule

No field should appear on any follow up form if the data was already captured in a previous form within the Five Points intake system. Data collected once is stored in the unified prospect profile and accessed internally. The client never repeats themselves. When a field is close enough to debate, cut it. The discovery call exists to fill in the gaps that a form cannot capture with nuance.

### UX Architecture

Same multi step, one section per page layout as Document 1. Three steps, since the prospect has already provided foundational information in the Discovery Intake.

| Step | Section Title | Fields | Estimated Time | Emotional Weight |
|------|--------------|--------|----------------|-----------------|
| 1 | Your Digital Footprint | 5 fields | Two to three minutes | Low to medium (inventory, not reflection) |
| 2 | Your Goals and History | 3 fields | One to two minutes | Medium (requires some thought) |
| 3 | Access and Logistics | 3 fields | One to two minutes | Low (practical, quick) |

Total: 11 fields. Estimated completion time: five to seven minutes.

### Progress Indicator

Same format as Document 1. Three labeled dots connected by a thin line.

```
( Your Digital Footprint )----( Goals and History )----( Access )
            ●                          ○                    ○
```

### Button Copy

| Step | Button Text |
|------|------------|
| 1 | "Next: Your goals" |
| 2 | "Next: Access and logistics" |
| 3 | "Submit" |

### Transitions, Validation, and Mobile Behavior

All transition, validation, and mobile behavior follows the same specifications defined in Document 1. Subtle slide or fade animation between steps. Back link available on steps two and three. Validation on "Next" click with gentle inline messaging. Mobile progress indicator compresses to dots only. Next button fixed to bottom of viewport on mobile.

---

### Form Header (Visible on Step 1 Only)

**Headline:** Help us see what you see.

**Subheadline:** This questionnaire helps us understand your current digital presence so we can come to our conversation with specific observations and ideas, not generic advice. It takes about five to seven minutes.

---

### Step 1: Your Digital Footprint

**Section title displayed on page:** Where do you show up online?
**Visual note:** This step is mostly inventory. Checkboxes and short selections. It should feel quick and easy to move through.

**Field 1 — Which social media platforms are you currently active on?**
- Type: Multi select checkboxes
- Required: Yes (at least one, or a "none" option)
- Options:
  - Instagram
  - LinkedIn
  - Facebook
  - TikTok
  - X (formerly Twitter)
  - YouTube
  - Pinterest
  - We are not active on social media right now
- Helper text: "Active means you have posted within the last 90 days."
- Logic note: This determines which platforms Five Points evaluates. If a prospect checks Instagram and LinkedIn only, the audit does not waste time on platforms they are not using. The "not active" option is valuable signal. It tells Five Points this client needs a ground up social strategy, not an optimization of what exists.

**Field 2 — Please share the links to your active social profiles.**
- Type: Long text (textarea)
- Required: No
- Placeholder: "Paste the URLs to your social profiles here, one per line."
- Character limit: 1,000 characters
- Conditional display: Only appears if the prospect selected at least one platform in Field 1. Hidden if they selected "We are not active on social media right now."
- Logic note: Having direct links saves the Five Points team from hunting for the right profiles, especially for businesses with common names.

**Field 3 — Are you currently running any paid advertising?**
- Type: Single select radio buttons
- Required: Yes
- Options:
  - Yes, on one or more platforms
  - No, but we have in the past
  - No, we have never run paid ads
- Logic note: This determines whether the paid advertising section of the audit is active or dormant. "No, but we have in the past" is useful because it means there may be historical data and learnings Five Points can reference.

**Field 4 — Which advertising platforms are you using or have used?**
- Type: Multi select checkboxes
- Required: No
- Conditional display: Only appears if the prospect selected "Yes" or "No, but we have in the past" in Field 3.
- Options:
  - Meta (Facebook and Instagram Ads)
  - Google Ads (Search, Display, or YouTube)
  - LinkedIn Ads
  - TikTok Ads
  - Other (please specify)
- Logic note: Tells Five Points exactly which ad accounts to evaluate or ask about.

**Field 5 — Do you currently send email marketing (newsletters, campaigns, automated sequences)?**
- Type: Single select radio buttons
- Required: Yes
- Options:
  - Yes, regularly (at least monthly)
  - Occasionally (a few times per year)
  - No, but we have a list we are not using
  - No, we do not have an email list
- Logic note: Email is often the most overlooked channel for businesses at the ICP stage. "No, but we have a list" is a strong signal that there is low hanging fruit Five Points can identify quickly.

---

### Step 2: Your Goals and History

**Section title displayed on page:** What is working and what is not?
**Visual note:** This step has one long text field and two selection fields. It should feel balanced and move quickly.

**Field 6 — What is your digital presence doing well right now?**
- Type: Long text (textarea)
- Required: No
- Context line above field: "Even if it does not feel like much, tell us what you think is working."
- Placeholder: "This could be a social platform that gets good engagement, a website that converts well, or just something you feel good about."
- Character limit: 1,000 characters
- Visual note: Textarea should be at least four to five lines tall by default.
- Logic note: This question is not about validating what the client thinks. It is about understanding their perception. If a prospect says "our Instagram is doing great" and Five Points finds 12 followers and no engagement, that gap between perception and reality is a coaching moment in the discovery call. If they say "nothing is working," that tells you they are frustrated and ready for change.

**Field 7 — How would you describe your brand's visual consistency across platforms?**
- Type: Single select radio buttons
- Required: Yes
- Options:
  - Very consistent. We have brand guidelines and follow them.
  - Somewhat consistent. We try, but it is not always cohesive.
  - Not consistent at all. Every platform looks different.
  - We do not really have a defined brand identity yet.
- Logic note: This is a self assessment that Five Points will verify independently during the audit. The gap between what the client believes and what Five Points observes is one of the most valuable data points in the report. It also helps route prospects toward design services if they indicate low consistency or no brand identity.

**Field 8 — What tools or platforms do you use to manage your digital presence?**
- Type: Long text (textarea)
- Required: No
- Placeholder: "e.g. Squarespace for website, Mailchimp for email, Canva for graphics, Hootsuite for scheduling. List whatever you use."
- Character limit: 500 characters
- Logic note: Understanding the tech stack tells Five Points what they are working with and reveals integration opportunities. A prospect using Mailchimp, Squarespace, and Canva is in a very different position than one using HubSpot, Webflow, and Adobe Creative Suite.

---

### Step 3: Access and Logistics

**Section title displayed on page:** A few practical details.
**Visual note:** This step is short and logistical. Three fields, all simple. The prospect should feel the relief of being almost done.

**Field 9 — Can you provide Five Points with temporary access to your analytics?**
- Type: Single select radio buttons
- Required: Yes
- Options:
  - Yes, I can share access to Google Analytics, social insights, and ad dashboards
  - I can share some but not all
  - I am not sure what I have access to
  - I would prefer not to share access at this time
- Helper text: "We will never make changes to your accounts. View only access helps us give you a much more accurate assessment."
- Logic note: Access to analytics transforms the audit from an outside in observation to a data driven evaluation. "I am not sure what I have access to" is common and tells Five Points they may need to walk the client through granting access during onboarding. "I would prefer not to share" is respected without question, and Five Points conducts the audit using publicly available information only.

**Field 10 — Is there a competitor or business you admire online?**
- Type: Long text (textarea)
- Required: No
- Placeholder: "Share one to three websites or social profiles you think do a great job. These do not need to be in your industry."
- Character limit: 500 characters
- Logic note: This is a taste and aspiration signal. It tells Five Points what the client considers excellent, which calibrates the recommendations. If they admire a minimalist luxury brand, the audit recommendations should not push them toward a loud, content heavy approach. It also gives Five Points ready made competitive benchmarks to reference in the report.

**Field 11 — Anything else we should know before we start?**
- Type: Long text (textarea)
- Required: No
- Placeholder: "Context, history, concerns, things you have tried before. Anything that helps us understand the full picture."
- Character limit: 1,000 characters
- Logic note: The open catch all. Some of the most valuable information comes from fields like this, things the prospect wanted to say but did not have a specific place to say it.

---

### Form Submission Experience

**Confirmation page headline:** "We have everything we need to get started."

**Confirmation page body:**
"Thank you for taking the time to share this. Our team will begin reviewing your digital presence within the next few business days. We will reach out to schedule a conversation once our initial review is complete.

If we need access to any accounts or have follow up questions, we will be in touch. In the meantime, you do not need to do anything else.

Talk soon.

Five Points Digital Studio"

---

### What Happens on the Five Points Side After Submission

1. Form submission triggers a Make automation
2. The automation compiles the intake responses into the internal lead record alongside the Discovery Intake data (Document 1), creating a unified prospect profile
3. Five Points receives an internal notification with the compiled Digital Presence Audit intake summary
4. The notification includes a checklist of what Five Points has access to and what still needs to be requested
5. The audit is assigned to the appropriate team member based on engagement tier (see Part 3: Tier Scope Notes)

---

## PART 2: INTERNAL AUDIT SCORING TEMPLATE

### Purpose

This is the evaluation framework Five Points uses to assess a client's digital presence. It is not client facing. It is the internal tool that ensures every audit, regardless of which team member conducts it, produces consistent, thorough, and actionable findings.

The scoring template is organized into six sections. Each section contains specific evaluation criteria, a scoring rubric, and space for qualitative notes. The completed template feeds into the branded PDF report that the client receives.

### Scoring Scale

All criteria are scored on a one to five scale:

| Score | Label | Definition |
|-------|-------|------------|
| 1 | Critical | Significant issues that are actively harming the business or creating negative perception. Immediate attention required. |
| 2 | Weak | Below standard. Noticeable gaps that are limiting performance or credibility. |
| 3 | Functional | Meets basic expectations but has clear room for improvement. Not a differentiator. |
| 4 | Strong | Above average. Performing well with minor opportunities for optimization. |
| 5 | Excellent | Best in class for the client's market and size. A genuine competitive advantage. |

---

### Section A: Website Performance and UX

**What Five Points evaluates:** The client's website from the perspective of a first time visitor, a returning customer, and a search engine.

**Data source:** Website URL from the unified prospect profile (captured in Document 1, Field 6).

| Criteria | What to Assess | Score (1-5) | Notes |
|----------|---------------|-------------|-------|
| A1. First impression and visual quality | Does the site look professional, current, and trustworthy within five seconds of landing? | | |
| A2. Mobile responsiveness | Does the site function well on mobile devices? Test on at least two screen sizes. | | |
| A3. Page load speed | Run through Google PageSpeed Insights. Note scores for mobile and desktop. | | |
| A4. Navigation and information architecture | Can a visitor find what they need within two clicks? Is the menu structure logical? | | |
| A5. Calls to action | Are CTAs clear, visible, and strategically placed? Is there a logical conversion path? | | |
| A6. Content quality | Is the copy well written, on brand, and speaking to the target audience? Is it current? | | |
| A7. SEO foundation | Check meta titles, descriptions, header structure, alt text, sitemap, and robots.txt. | | |
| A8. Trust signals | Are there testimonials, case studies, certifications, or social proof visible? | | |
| A9. Contact and conversion | How easy is it to contact the business or take the next step? Are forms functional? | | |
| A10. Accessibility basics | Check color contrast, alt text, keyboard navigation, and font readability. | | |

**Section A score:** Sum of criteria divided by 10. Record the average.

**Tools to use:** Google PageSpeed Insights, GTmetrix, Lighthouse (Chrome DevTools), WAVE accessibility checker, Screaming Frog (for SEO crawl if applicable).

---

### Section B: Social Media Platform Analysis

**What Five Points evaluates:** Each active platform the client identified in the intake form (Field 1). Repeat this section for each platform.

**Data source:** Platform selections and profile links from Document 2, Fields 1 and 2.

**Platform being evaluated:** _______________

| Criteria | What to Assess | Score (1-5) | Notes |
|----------|---------------|-------------|-------|
| B1. Profile completeness | Is the bio filled out, profile and cover photos current, and contact info accurate? | | |
| B2. Visual consistency | Do posts have a cohesive visual identity? Is there a recognizable brand aesthetic? | | |
| B3. Content quality | Is the content valuable, original, and relevant to the target audience? | | |
| B4. Posting frequency | How often are they posting? Is it consistent or sporadic? Note the average cadence. | | |
| B5. Engagement rate | Calculate engagement rate (likes + comments + shares divided by followers). Note the number. | | |
| B6. Audience relevance | Based on available data, does the follower base appear to match the target audience? | | |
| B7. Content mix | Is there variety (educational, promotional, behind the scenes, community) or is it one note? | | |
| B8. Response and community management | Does the business respond to comments and messages? How quickly? | | |
| B9. Use of platform features | Are they using Stories, Reels, Lives, LinkedIn articles, etc. beyond static posts? | | |
| B10. Bio and link optimization | Does the bio clearly communicate what they do and include a functional link? | | |

**Platform score:** Sum of criteria divided by 10. Record the average.

**Repeat for each active platform.** If the client is on three platforms, this section produces three platform scores.

**Tools to use:** Native platform analytics (if access granted), Social Blade, manual review.

---

### Section C: Content Audit

**What Five Points evaluates:** The quality, consistency, and strategic alignment of the client's content across blog, email, and video.

**Data source:** Email marketing status from Document 2, Field 5. Tech stack from Document 2, Field 8. Business description and goals from Document 1, Fields 7 and 12.

| Criteria | What to Assess | Score (1-5) | Notes |
|----------|---------------|-------------|-------|
| C1. Blog or long form content | Does the client produce blog posts, articles, or other long form content? Assess quality, frequency, and relevance. If none exists, score as 1 and note the gap. | | |
| C2. Email marketing | If the client sends emails, assess the quality of subject lines, content, design, and frequency. If no email marketing exists, score as 1 and note the gap. | | |
| C3. Video content | Does the client produce video? Assess quality, platform fit, and consistency. If none exists, score as 1 and note the gap. | | |
| C4. Content strategy alignment | Is there a visible content strategy, or does the content feel random and reactive? | | |
| C5. Brand voice consistency | Does the content sound like the same brand across channels? Or does the blog sound different from social, which sounds different from email? | | |

**Section C score:** Sum of criteria divided by five. Record the average.

**Note:** If the client has no blog, no email, and no video, this entire section scores low and becomes a primary recommendation area. That is not a failure of the client. It is an opportunity Five Points identifies.

---

### Section D: Paid Advertising Review

**What Five Points evaluates:** Current or historical paid advertising efforts. Only applicable if the client indicated they are running or have run paid ads in the intake form.

**Data source:** Paid advertising status and platform selections from Document 2, Fields 3 and 4.

**If no paid advertising exists, skip this section and note in the report that paid advertising was not evaluated because the client has no current or historical campaigns.**

| Criteria | What to Assess | Score (1-5) | Notes |
|----------|---------------|-------------|-------|
| D1. Campaign structure | Are campaigns organized logically with clear objectives, audiences, and ad groups? | | |
| D2. Targeting quality | Are the audiences well defined and aligned with the client's ICP? | | |
| D3. Creative quality | Are the ad creatives (images, video, copy) compelling and on brand? | | |
| D4. Landing page alignment | Do ads link to relevant, optimized landing pages, or to the homepage? | | |
| D5. Budget efficiency | Based on available data, is the spend producing reasonable cost per result? | | |
| D6. Tracking and attribution | Is conversion tracking properly set up? Are they measuring what matters? | | |

**Section D score:** Sum of criteria divided by six. Record the average.

**Tools to use:** Platform ad libraries (Meta Ad Library, Google Ads Transparency Center), client provided dashboard access if available.

---

### Section E: Brand Consistency Assessment

**What Five Points evaluates:** How consistently the brand shows up across all digital touchpoints.

**Data source:** Brand consistency self assessment from Document 2, Field 7. Website URL from Document 1, Field 6. Social profile links from Document 2, Field 2.

| Criteria | What to Assess | Score (1-5) | Notes |
|----------|---------------|-------------|-------|
| E1. Visual identity consistency | Are colors, fonts, logo usage, and imagery consistent across website, social, and any other digital touchpoints? | | |
| E2. Messaging consistency | Does the brand communicate the same positioning, values, and tone across all channels? | | |
| E3. Experience consistency | Does interacting with the brand feel cohesive whether you find them on Google, Instagram, or their website? | | |
| E4. Brand differentiation | Does the brand stand out from competitors, or could you swap the logo and not notice? | | |

**Section E score:** Sum of criteria divided by four. Record the average.

**Cross reference note:** Compare the Five Points evaluation with the client's self assessment from Field 7. If the client said "Very consistent" and Five Points scores Section E at 2.0, that perception gap is a key finding to surface in the report and discuss during the discovery call.

---

### Section F: Competitive Landscape Snapshot

**What Five Points evaluates:** Three to five competitors identified through industry research and any competitors the client mentioned in the intake form.

**Data source:** Admired competitors from Document 2, Field 10. Business description from Document 1, Field 7.

This section does not produce a numerical score. It produces a qualitative comparison that gives the client context for where they stand relative to their market.

**For each competitor, note:**

| Competitor | Website Quality (1-5) | Social Presence (1-5) | Content Activity (1-5) | Key Strength | Key Weakness | What Client Can Learn |
|-----------|----------------------|----------------------|----------------------|-------------|-------------|---------------------|
| [Competitor 1] | | | | | | |
| [Competitor 2] | | | | | | |
| [Competitor 3] | | | | | | |

**Selection criteria for competitors:** Choose three to five businesses that are either direct competitors (same market, same audience) or aspirational competitors (where the client wants to be). Prioritize businesses the client mentioned in their intake form, then supplement with Five Points research.

---

### Audit Summary Dashboard

After completing all sections, compile the scores into a summary view. This becomes the first page of the branded PDF report.

```
FIVE POINTS DIGITAL PRESENCE AUDIT — [Client Name]
Date: [Date]
Conducted by: [Team Member]
Engagement tier: [Silver / Gold / Platinum]

OVERALL SCORE: [Average of all section scores] / 5

Section Scores:
  A. Website Performance and UX:     [Score] / 5
  B. Social Media (Platform avg):    [Score] / 5
  C. Content:                        [Score] / 5
  D. Paid Advertising:               [Score] / 5  (or "Not applicable")
  E. Brand Consistency:              [Score] / 5
  F. Competitive Landscape:          Qualitative (see report)

TOP THREE STRENGTHS:
  1. [Strength]
  2. [Strength]
  3. [Strength]

TOP THREE PRIORITIES FOR IMPROVEMENT:
  1. [Priority]
  2. [Priority]
  3. [Priority]

RECOMMENDED FIVE POINTS SERVICES:
  [Based on findings, recommend specific offers from the Five Points suite]
```

---

## PART 3: TIER SCOPE NOTES

### Purpose

Not every engagement requires the full audit. These notes tell the Five Points team how deep to go based on the tier of the engagement. The intake form (Part 1) is the same regardless of tier. The depth of evaluation (Part 2) scales with the investment.

---

### Silver — Digital Marketing Strategy Session ($1,500)

**Scope:** Focused audit. Prioritize the areas most relevant to the client's stated challenge.

**Required sections:**
- Section A: Website Performance and UX (full evaluation)
- Section B: Social Media (evaluate top two platforms only, based on client activity)
- Section E: Brand Consistency (full evaluation)

**Optional sections (include if relevant to the client's stated challenge):**
- Section C: Content Audit (light review, focus on whether content exists and its general quality)
- Section D: Paid Advertising (only if client indicated active or historical campaigns)

**Section F (Competitive Landscape):** Three competitors. Brief notes only, not full scoring.

**Deliverable depth:** Summary dashboard plus two to three pages of findings and recommendations. Delivered as branded PDF.

**Time budget for the audit:** Two to three Pomodoro sessions (50 to 75 minutes of focused work).

---

### Silver — Social Media Audit and Strategy ($2,000)

**Scope:** Deep dive on social media specifically. Website and brand consistency are evaluated at a lighter level for context.

**Required sections:**
- Section B: Social Media (full evaluation of all active platforms, not just top two)
- Section E: Brand Consistency (full evaluation, with emphasis on cross platform visual and messaging consistency)

**Supporting sections (lighter evaluation for context):**
- Section A: Website Performance and UX (evaluate criteria A1, A5, A6, and A9 only, to understand how social traffic converts)
- Section C: Content Audit (focus on C4 and C5, strategy alignment and voice consistency)

**Section F (Competitive Landscape):** Three to five competitors, with emphasis on their social media presence specifically.

**Deliverable depth:** Summary dashboard plus four to six pages focused on social media findings, with platform specific recommendations and a recommended content strategy framework. Delivered as branded PDF.

**Time budget for the audit:** Three to four Pomodoro sessions (75 to 100 minutes of focused work).

---

### Gold — Fractional CMO Onboarding ($5,000 per month)

**Scope:** Comprehensive audit. Every section, full depth. This is the baseline assessment that informs ongoing strategic leadership.

**Required sections:** All sections (A through F), full evaluation.

**Section F (Competitive Landscape):** Five competitors, full scoring and qualitative analysis.

**Deliverable depth:** Summary dashboard plus eight to 12 pages of detailed findings, organized by section, with prioritized recommendations and a 90 day action plan. Delivered as branded PDF.

**Time budget for the audit:** Five to seven Pomodoro sessions (125 to 175 minutes of focused work).

**Additional note:** For Fractional CMO engagements, the audit is not a standalone deliverable. It is the foundation of the ongoing relationship. The findings feed directly into the first monthly strategy session and inform the marketing calendar development. Store the raw scoring data for reference throughout the engagement so progress can be measured against the initial baseline.

---

### Gold — Content Engine Retainer Onboarding ($4,750 per month)

**Scope:** Comprehensive audit with extra depth on content and brand voice.

**Required sections:**
- Section A: Website Performance and UX (full evaluation, with emphasis on A6 content quality)
- Section B: Social Media (full evaluation of all active platforms)
- Section C: Content Audit (full evaluation, with extra depth on brand voice analysis and content gap identification)
- Section E: Brand Consistency (full evaluation)

**Optional sections:**
- Section D: Paid Advertising (include if the content strategy will support paid campaigns)

**Section F (Competitive Landscape):** Three to five competitors, with emphasis on their content approach, publishing cadence, and content quality.

**Deliverable depth:** Summary dashboard plus six to eight pages, with a dedicated section on content opportunities and a recommended content pillar framework. Delivered as branded PDF.

**Time budget for the audit:** Four to five Pomodoro sessions (100 to 125 minutes of focused work).

---

### Platinum Engagements

**Scope:** Full comprehensive audit as described in the Gold Fractional CMO scope, plus any additional depth required by the specific Platinum engagement. For Platinum clients, the audit may also include stakeholder interviews and a more extensive competitive landscape analysis.

**Deliverable depth:** 12 to 20 pages. Delivered as branded PDF with executive summary suitable for board or leadership presentation.

**Time budget for the audit:** Seven to 10 Pomodoro sessions (175 to 250 minutes of focused work).

---

## DEPENDENCIES

- Document 1 (Discovery Intake Form) must be live for the routing to work
- Unified prospect profile system must be in place so data from Document 1 is accessible when conducting the audit (no redundant data collection)
- Make automation to compile intake data from Documents 1 and 2 into the unified prospect profile
- Branded PDF report template (design deliverable, to be created during fulfillment system build in Next Step 5)
- Tool access: Google PageSpeed Insights, Lighthouse, WAVE, Social Blade, platform ad libraries, and any client granted analytics access
- Internal project management system to assign and track audit completion by tier

---

*Document 2 of 7 — Five Points Digital Presence Audit*
*Part of the Standardized Document Library for Five Points Digital Studio*
