# Document 1 of 7: Five Points Discovery Intake Form

**Document type:** Website contact form (front door of the ecosystem)
**Location:** Primary contact page of the Five Points Digital Studio website
**Purpose:** First point of contact with every prospect. Captures enough information to route the prospect to the correct follow up form, qualify them for the appropriate tier, and give Five Points substantive context before any human conversation happens.
**Tone:** Warm, confident, partner oriented. This form should feel like the beginning of a conversation with someone who genuinely wants to understand your business, not like a corporate intake process.

---

## UX Architecture: Multi Step Form Design

### Design Philosophy

This form uses a multi step, one section per page layout inspired by the Soho House membership application. The principle is that each step feels like a single, manageable conversation topic rather than a wall of fields. The prospect is only ever thinking about one thing at a time, which reduces cognitive load and increases completion rates.

A 15 field form presented on a single page feels like work. The same 15 fields broken into four themed steps feel like a conversation.

### Step Structure Overview

| Step | Section Title | Fields | Estimated Time | Emotional Weight |
|------|--------------|--------|----------------|-----------------|
| 1 | About You | 4 fields | 30 seconds | Low (easy, personal, familiar) |
| 2 | About Your Business | 5 fields | Two to three minutes | Medium (requires thought but not vulnerability) |
| 3 | What Brought You Here | 3 fields | Two to three minutes | High (substantive, reflective, highest signal) |
| 4 | Logistics and Fit | 3 fields | 30 seconds | Low (simple selections, easy close) |

The arc is intentional. Start easy, build to the substantive middle, and close light. The prospect should never feel like the hardest question is the last one.

### Progress Indicator

Use a minimal horizontal progress bar or step indicator at the top of each page. Four dots or segments, with the current step highlighted. The indicator should be visually subtle but always visible so the prospect knows where they are and how much remains.

Recommended format: four labeled dots connected by a thin line.

```
( About You )----( Your Business )----( What Brought You Here )----( Almost Done )
     ●                  ○                        ○                       ○
```

The labels should be warm and conversational, not clinical. "About You" instead of "Step 1." "Almost Done" instead of "Step 4."

### Transitions Between Steps

When the prospect clicks "Next," the transition should feel smooth and intentional. Recommended approach:

- A subtle slide or fade animation (left to right) when advancing to the next step. Nothing dramatic. The movement should feel like turning a page, not loading a new screen.
- The progress indicator updates immediately so the prospect sees forward momentum.
- A "Back" link (not a button, a text link) should be available on steps two through four so the prospect can revisit previous answers without losing their work. Position it below the "Next" button or in the top left near the progress indicator.
- Field validation happens on "Next" click, not on each keystroke. If a required field is empty, a gentle inline message appears below the field ("This one helps us prepare for our conversation" rather than "This field is required").

### Button Copy

Do not use generic button text. Each step's button should feel like it is moving the conversation forward.

| Step | Button Text |
|------|------------|
| 1 | "Next: Tell us about your business" |
| 2 | "Next: What can we help with?" |
| 3 | "Next: One last thing" |
| 4 | "Submit" |

### Mobile Considerations

On mobile, each step should occupy the full viewport with generous spacing between fields. The progress indicator should compress to dots only (no labels) to preserve screen real estate. The "Next" button should be large, thumb friendly, and fixed to the bottom of the viewport so it is always accessible without scrolling.

---

## Form Header (Visible on Step 1 Only)

**Headline:** Let us learn about your business.

**Subheadline:** Before we talk, we want to understand where you are now and where you want to go. The more you share here, the more valuable our first conversation will be. This takes about five to seven minutes.

The headline and subheadline appear only on step one. On subsequent steps, the section title and progress indicator are sufficient context. Repeating the header on every step wastes space and creates visual noise.

---

## Step 1: About You

**Section title displayed on page:** About You
**Visual note:** This step should feel light and welcoming. Four simple fields, generous spacing, clean layout. The goal is to get the prospect typing immediately with zero friction.

**Field 1 — Full Name**
- Type: Text input
- Required: Yes
- Placeholder: "Your full name"

**Field 2 — Email Address**
- Type: Email input
- Required: Yes
- Placeholder: "your@email.com"

**Field 3 — Phone Number**
- Type: Phone input
- Required: No
- Placeholder: "(555) 555-5555"
- Helper text: "Optional. We will never call without scheduling first."

**Field 4 — Your Role**
- Type: Text input
- Required: Yes
- Placeholder: "e.g. Founder, CEO, Marketing Director"
- Logic note: This field helps Five Points understand whether the person filling out the form is the decision maker or an internal champion who will need to involve others. This informs discovery call preparation.

---

## Step 2: About Your Business

**Section title displayed on page:** Tell us about your business.
**Visual note:** This step introduces the first long text field (Field 7). Give it visual prominence. The textarea should be tall enough to invite a real response, not a one liner. The dropdown fields should feel quick by contrast.

**Field 5 — Business Name**
- Type: Text input
- Required: Yes
- Placeholder: "Your business or organization name"

**Field 6 — Website URL**
- Type: URL input
- Required: No
- Placeholder: "https://yourbusiness.com"
- Helper text: "If you have one. If not, no worries."

**Field 7 — Tell us about your business.**
- Type: Long text (textarea)
- Required: Yes
- Placeholder: "Who do you serve, what do you do, and what makes your work meaningful? Write as much or as little as feels right."
- Character limit: 1,000 characters
- Visual note: This textarea should be at least four to five lines tall by default. The size of the field communicates how much you value the response. A small box says "give us a sentence." A generous box says "we actually want to hear this."
- Logic note: This is intentionally open ended. The way a prospect describes their business reveals their level of self awareness, their values, and how they think about what they do. It also provides language that Five Points can mirror back in the discovery call, which builds rapport.

**Field 8 — How long has your business been operating?**
- Type: Single select dropdown
- Required: Yes
- Options:
  - Less than one year
  - One to three years
  - Three to five years
  - Five to 10 years
  - More than 10 years
- Logic note: This is a soft firmographic filter. Businesses under one year may not yet be ready for Gold or Platinum level investment, but could be strong Bronze or Silver candidates. This does not disqualify anyone. It informs the routing and discovery preparation.

**Field 9 — Team Size**
- Type: Single select dropdown
- Required: Yes
- Options:
  - Just me
  - Two to five people
  - Six to 15 people
  - 16 to 50 people
  - More than 50 people
- Logic note: Aligns with the ICP firmographic filter (sweet spot: 10 to 50). Also informs which offers are appropriate. A solo founder is unlikely to need a Platinum AI Operations Overhaul, but a 30 person team might.

---

## Step 3: What Brought You Here

**Section title displayed on page:** What can we help with?
**Visual note:** This is the most important step and the one that requires the most from the prospect. The two long text fields (Fields 11 and 12) should each have generous height and clear, inviting placeholder text. Consider adding a brief sentence of context above each textarea to frame why the question matters, so the prospect does not feel like they are filling out a form but rather being asked a thoughtful question.

**Field 10 — What are you looking for help with?**
- Type: Multi select checkboxes
- Required: Yes (at least one selection)
- Options:
  - Understanding how AI can help my business (Education)
  - Automating repetitive tasks and workflows (Automation and Consulting)
  - Digital marketing strategy or execution (Marketing)
  - Brand identity, logo, or visual design (Design)
  - Website or application design and development (Development)
  - I am not sure yet. I just know something needs to change.
- Visual note: Display as a vertical list of checkboxes with generous tap targets on mobile. Each option should be selectable independently. The last option ("I am not sure yet") should be visually distinct, perhaps slightly separated from the others or styled as an alternative, so it reads as a valid and welcomed choice rather than a fallback.
- Logic note: This is the primary routing field. Selections here determine which follow up form the prospect receives. The last option routes to a general discovery call without a secondary form, because this prospect needs a conversation before they need a questionnaire.

**Field 11 — What is the single biggest challenge your business is facing right now?**
- Type: Long text (textarea)
- Required: Yes
- Context line above field: "Be as specific as you can. There are no wrong answers here."
- Placeholder: "What is not working the way you want it to?"
- Character limit: 1,000 characters
- Visual note: Same generous textarea height as Field 7. Minimum four to five visible lines.
- Logic note: This is the most important field on the form. The answer here gives Five Points the initial pain signal that the discovery call will deepen and quantify. When the prospect writes their challenge in their own words, they begin the psychological process of articulating the problem, which primes them for the anchoring conversation later.

**Field 12 — What does success look like for you in the next 12 months?**
- Type: Long text (textarea)
- Required: Yes
- Context line above field: "If everything went exactly the way you wanted, what would be different?"
- Placeholder: "Paint the picture for us."
- Character limit: 1,000 characters
- Visual note: Same generous textarea height as Fields 7 and 11.
- Logic note: This mirrors Phase 2 of the Discovery and Anchoring Framework (understanding the desired state). Having this answer in advance means the discovery call can move faster and go deeper. It also reveals whether the prospect thinks in terms of outcomes (ICP aligned) or tactics ("I need more social media posts"), which helps with qualification.

---

## Step 4: Almost Done

**Section title displayed on page:** A few last details.
**Visual note:** This step should feel fast and easy. Three simple selection fields, no long text. The prospect should feel the momentum of being almost finished. Keep the layout clean and uncluttered. This is the exhale after the substantive middle steps.

**Field 13 — What is your timeline?**
- Type: Single select dropdown
- Required: Yes
- Options:
  - I need help as soon as possible
  - Within the next 30 days
  - Within the next one to three months
  - I am planning ahead. No immediate rush.
- Logic note: Urgency signals both qualification and routing. "As soon as possible" prospects with strong pain signals may be fast tracked to a discovery call. "Planning ahead" prospects may be better served with a follow up form and a scheduled call two weeks out.

**Field 14 — Have you worked with a digital agency, studio, or freelancer before?**
- Type: Single select radio buttons
- Required: Yes
- Options:
  - Yes, and it went well
  - Yes, but it did not meet expectations
  - No, this would be our first time
- Logic note: This field is deceptively useful. "Yes, but it did not meet expectations" signals a prospect who has experienced the pain of bad execution. They are often the strongest Gold and Platinum candidates because they understand what low quality costs and are willing to invest in getting it right. It also gives Five Points a conversation thread for the discovery call. "No, this would be our first time" signals a prospect who may need more education and anchoring during discovery.

**Field 15 — How did you hear about Five Points?**
- Type: Single select dropdown with "Other" text field
- Required: Yes
- Options:
  - Referral from someone I know
  - Social media (Instagram, LinkedIn, etc.)
  - Google search
  - Attended a workshop or event
  - Podcast or article
  - Other (please specify)
- Logic note: Attribution tracking. This is the field that tells you which lead generation channels are actually working so you can double down on what converts and cut what does not.

---

## Form Submission Experience

### What the prospect sees after submitting:

This should be a dedicated confirmation page, not a modal or toast notification. The prospect just invested five to seven minutes. Honor that with a real page that confirms their effort mattered.

**Confirmation page headline:** "Thank you. We are already thinking about your business."

**Confirmation page body:**
"Here is what happens next. Within one business day, you will hear from us. Depending on what you shared, we may send you a short follow up questionnaire to help us prepare for our conversation. It lives right here on our site and takes about 10 minutes. The more context you give us upfront, the more valuable our first call will be.

If you have any questions before then, reach out to [email]. We are glad you are here."

**Design note:** The confirmation page should feel warm and unhurried. Consider including a subtle visual element (the Five Points brand mark, a simple illustration, or a photograph) that reinforces the brand and makes the page feel intentional rather than like a default "form submitted" screen.

---

## Routing Logic

### Follow up form routing based on Field 10 selections:

| Selection(s) | Follow up form sent | Notes |
|---|---|---|
| Education only | No secondary form | Route to Bronze workshop funnel or discovery call |
| Automation and Consulting (with or without Education) | Workflow and Operations Intake Questionnaire | Page link within the website |
| Design (with or without others) | Brand Strategy Intake Questionnaire | Page link within the website |
| Marketing (without Design or Development) | Digital Presence Audit intake section | Page link within the website |
| Development (with or without Marketing) | Workflow and Operations Intake Questionnaire + brief project scope questions | Development projects need operational context |
| Multiple pillars selected (Automation + Design, Marketing + Development, etc.) | Both relevant forms sent | Prospect receives links to all applicable follow up pages |
| "I am not sure yet" | No secondary form | Route directly to discovery call scheduling |

---

## What Happens on the Five Points Side

1. Form submission triggers a Make automation
2. The automation evaluates Field 10 (services selected), Field 8 (business age), and Field 9 (team size)
3. Based on routing logic, the automation sends the prospect a personalized email with a link to the appropriate follow up form page(s) on the Five Points website
4. Simultaneously, Five Points receives an internal notification (email or Slack) with a pre qualified lead summary containing: prospect name, business name, website URL, services of interest, biggest challenge, desired outcome, timeline, previous agency experience, and referral source
5. The internal notification includes a recommended next step: send follow up form, schedule discovery call, or route to Bronze workshop funnel
6. If the prospect selected "I am not sure yet" for services, the automation skips the follow up form and sends a warm email inviting them to book a discovery call directly

---

## Automated Email Templates

### Email to prospect (follow up form routing):

**Subject line:** "One more step before we talk, [First Name]."

**Body:**
"Thank you for reaching out to Five Points. We read every submission carefully, and what you shared about [Business Name] already has our wheels turning.

Before we schedule a conversation, we put together a short follow up questionnaire that will help us come prepared with ideas specific to your business. It takes about 10 minutes and lives on our site:

[Link to follow up form page]

Once you complete it, we will reach out within one business day to find a time to talk.

Looking forward to learning more.

Five Points Digital Studio"

### Email to prospect (no follow up form, direct to call):

**Subject line:** "Let us find a time to talk, [First Name]."

**Body:**
"Thank you for reaching out to Five Points. We appreciate you sharing what is on your mind, and it sounds like the best next step is a conversation.

Here is a link to book a 30 minute discovery call at a time that works for you:

[Scheduling link]

No preparation needed on your end. We will come with questions and curiosity.

Looking forward to it.

Five Points Digital Studio"

---

## Internal Lead Summary Template (delivered to Five Points via automation)

```
NEW LEAD — [Business Name]

Contact: [Full Name] ([Role])
Email: [Email] | Phone: [Phone or "Not provided"]
Website: [URL or "No website provided"]

Business overview: [Field 7 response]
Operating: [Field 8 response] | Team: [Field 9 response]

Services of interest: [Field 10 selections]
Biggest challenge: [Field 11 response]
Desired outcome (12 months): [Field 12 response]

Timeline: [Field 13 response]
Previous agency experience: [Field 14 response]
Referral source: [Field 15 response]

RECOMMENDED NEXT STEP: [Auto generated based on routing logic]
FOLLOW UP FORM SENT: [Yes/No — which form(s)]
```

---

## Global Design and UX Notes

- The form should live on a dedicated page within the Five Points website, not in a modal or sidebar. It deserves its own space.
- Each step occupies its own view. The prospect should never see fields from another step. One conversation at a time.
- Background and styling should be consistent across all four steps, reinforcing that this is one continuous experience, not four separate pages.
- Long text fields should be visually generous. Do not compress them into small boxes. The size of the field communicates how much you value the response.
- Mobile optimization is critical. Every field should be easy to complete on a phone. On mobile, the progress indicator compresses to dots only. The "Next" button is fixed to the bottom of the viewport.
- The form should feel like a conversation, not a bureaucratic process. Warm copy, generous spacing, and a clean layout reinforce the Five Points brand.
- No CAPTCHA unless spam becomes an issue. Friction at the front door costs you more than a few junk submissions.
- Auto save progress if technically feasible, so a prospect who navigates away can return and pick up where they left off. This is especially valuable on mobile where interruptions are common.
- The form URL should be clean and memorable: something like fivepointsdigital.com/start or fivepointsdigital.com/connect.

---

## Dependencies

- Make automation for routing logic and email delivery
- Email templates for both routing paths (follow up form and direct to call)
- Scheduling tool integration (Calendly or similar) for the direct to call path
- Follow up form pages built on the website (Documents 2 through 4 in this series)
- Multi step form implementation on the website (native build or form tool that supports stepped layouts)

---

*Document 1 of 7 — Five Points Discovery Intake Form*
*Part of the Standardized Document Library for Five Points Digital Studio*
