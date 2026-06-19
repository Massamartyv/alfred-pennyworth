# Document 4 of 7: Five Points Brand Strategy Intake Questionnaire

**Document type:** Three part specification (client facing intake form + internal brand assessment checklist + tier scope notes)
**Location:** Client facing intake form lives on a dedicated page within the Five Points website. Internal assessment checklist and tier scope notes are internal operational documents used by the Five Points team.
**Purpose:** Captures the foundational inputs Five Points needs for any brand or design engagement. The intake form collects the client's vision, values, audience, and aesthetic preferences. The internal checklist guides the Five Points team through what to evaluate and explore during discovery and brand strategy sessions. The tier scope notes control depth.
**Tone:** Client facing sections are warm, creative, and inviting. Brand work is personal for clients. They are sharing how they want to be perceived by the world. The form should feel like the beginning of a creative partnership, not a procurement process.

**Used by:** Bronze — Brand Foundations Kit, Silver — Brand Identity Sprint, Gold — Comprehensive Brand Identity, Platinum — Brand Ecosystem Design, Silver — Content Strategy and Launch (brand voice section).

**Data dependency:** This form assumes the prospect has already completed the Discovery Intake Form (Document 1). Information captured in Document 1 (name, email, phone, role, business name, website URL, business description, business age, team size, services of interest, biggest challenge, desired outcome, timeline, previous agency experience, and referral source) is stored in the unified prospect profile and is never requested again.

**No Redundancy Rule:** No field should appear on any follow up form if the data was already captured in a previous form within the Five Points intake system. Data collected once is stored in the unified prospect profile and accessed internally. The client never repeats themselves. When a field is close enough to debate, cut it.

---

## PART 1: CLIENT FACING INTAKE FORM (Website Hosted)

### Context

This form is the follow up that a prospect receives after selecting "Brand identity, logo, or visual design" on the Discovery Intake Form (Document 1). It arrives via email as a link to a dedicated page on the Five Points website.

The prospect has already told Five Points who they are, what their business does, what their biggest challenge is, and what success looks like. This form goes deeper into how they want their brand to look, feel, and communicate, collecting the creative context Five Points needs to develop informed brand solutions.

### UX Architecture

Same multi step, one section per page layout as Documents 1 through 3. Three steps.

| Step | Section Title | Fields | Estimated Time | Emotional Weight |
|------|--------------|--------|----------------|-----------------|
| 1 | Your Brand Today | 4 fields | Two to three minutes | Medium (honest assessment of where they are) |
| 2 | Your Brand Tomorrow | 4 fields | Three to four minutes | High (aspirational, creative, personal) |
| 3 | Inspiration and Assets | 3 fields | Two to three minutes | Low to medium (fun, visual, closing) |

Total: 11 fields. Estimated completion time: seven to 10 minutes.

### Progress Indicator

```
( Your Brand Today )----( Your Brand Tomorrow )----( Inspiration )
          ●                        ○                      ○
```

### Button Copy

| Step | Button Text |
|------|------------|
| 1 | "Next: Where you want to go" |
| 2 | "Next: Inspiration and assets" |
| 3 | "Submit" |

### Transitions, Validation, and Mobile Behavior

All transition, validation, and mobile behavior follows the same specifications defined in Document 1.

---

### Form Header (Visible on Step 1 Only)

**Headline:** Let us get to know your brand.

**Subheadline:** Great brand work starts with understanding, not assumptions. The more we know about how you see your brand today and how you want it to feel tomorrow, the better our work will be. This takes about seven to 10 minutes.

---

### Step 1: Your Brand Today

**Section title displayed on page:** Where your brand is right now.
**Visual note:** This step asks the client to be honest about the current state of their brand. The tone should be encouraging, not judgmental. Many prospects are embarrassed about their current brand. The form should make it safe to be candid.

**Field 1 — Do you have existing brand assets (logo, color palette, fonts, brand guidelines)?**
- Type: Single select radio buttons
- Required: Yes
- Options:
  - Yes, we have a full set of brand guidelines
  - We have a logo and some basics, but no formal guidelines
  - We have a logo but it needs to be updated or replaced
  - We are starting from scratch
- Logic note: This determines whether Five Points is building on an existing foundation or creating from zero. "We have a logo but it needs to be updated" is the most common response at the ICP stage. It signals a business that has outgrown its original identity and is ready to invest in something more intentional.

**Field 2 — If you have existing brand assets, please share them here.**
- Type: File upload (multiple files allowed)
- Required: No
- Conditional display: Hidden if the prospect selected "We are starting from scratch" in Field 1.
- Accepted file types: PDF, PNG, JPG, SVG, AI, EPS, ZIP
- Helper text: "Upload your logo files, brand guidelines, style guides, or anything else that represents your current brand. A ZIP file works great if you have multiple files."
- Logic note: Having the existing assets before the discovery call allows Five Points to evaluate the current brand independently and come to the conversation with informed observations rather than starting cold.

**Field 3 — How do you feel about your current brand?**
- Type: Single select radio buttons
- Required: Yes
- Options:
  - I am proud of it. It represents us well.
  - It is okay, but it does not fully capture who we are.
  - I am not happy with it. It feels outdated or misaligned.
  - We do not really have a defined brand yet.
- Logic note: This is an emotional baseline. The client's relationship with their current brand tells Five Points how much of the engagement will be about evolution versus revolution. A prospect who is "not happy" may need more reassurance and collaboration during the creative process. A prospect who is "proud" but seeking refinement may need Five Points to challenge their assumptions diplomatically.

**Field 4 — Who is your primary audience? Describe the people you serve.**
- Type: Long text (textarea)
- Required: Yes
- Context line above field: "Think about your best clients or customers. Who are they, what do they care about, and what motivates them?"
- Placeholder: "e.g. Small business owners in their 30s and 40s who are growing quickly and want to look as professional as they are. They care about quality and do not want to look like every other company in their space."
- Character limit: 1,000 characters
- Visual note: Textarea should be at least four to five lines tall.
- Logic note: Document 1, Field 7 captured a general business description. This field goes deeper into the audience specifically, because brand decisions are made for the audience, not for the founder. The way a prospect describes their audience reveals how well they understand the people they serve, which directly informs the brand strategy.

---

### Step 2: Your Brand Tomorrow

**Section title displayed on page:** How you want to be seen.
**Visual note:** This is the aspirational step. The questions are creative and personal. Give the long text fields generous height and use placeholder text that sparks imagination rather than constraining it.

**Field 5 — If your brand were a person, how would you describe their personality?**
- Type: Long text (textarea)
- Required: Yes
- Context line above field: "This is not about your logo. It is about how your brand feels to the people who experience it."
- Placeholder: "e.g. Confident but approachable. Knowledgeable without being condescending. Modern but warm. Think of a trusted advisor who also happens to have great taste."
- Character limit: 1,000 characters
- Logic note: Brand personality is the foundation of every visual and verbal decision. This question forces the prospect to think beyond aesthetics and into the emotional experience of their brand. The language they use here becomes the seed of the brand voice and visual direction.

**Field 6 — What three to five words do you want people to associate with your brand?**
- Type: Long text (textarea)
- Required: Yes
- Placeholder: "e.g. Trustworthy, innovative, warm, premium, bold."
- Character limit: 300 characters
- Visual note: This field can be shorter than the others. Three to five words do not need a large textarea. Two to three lines is sufficient.
- Logic note: These words become the brand attributes that guide the creative direction. They are also a gut check throughout the engagement. Every design decision, color choice, and copy direction should be testable against these words.

**Field 7 — Is there anything your brand should never feel like?**
- Type: Long text (textarea)
- Required: No
- Context line above field: "Sometimes knowing what you do not want is as useful as knowing what you do."
- Placeholder: "e.g. We never want to feel corporate or cold. We never want to look cheap. We never want to come across as exclusive or unapproachable."
- Character limit: 500 characters
- Logic note: The negative space of brand identity. This field prevents Five Points from exploring directions that would make the client uncomfortable and saves revision cycles. It is also a strong signal of self awareness. Prospects who can clearly articulate what they do not want tend to be more decisive and easier to collaborate with.

**Field 8 — Who do you compete with, and how do you want to stand apart from them?**
- Type: Long text (textarea)
- Required: Yes
- Context line above field: "Name a few competitors or businesses in your space. Then tell us what makes you different."
- Placeholder: "e.g. Our main competitors are [Company A] and [Company B]. They both feel very corporate and impersonal. We want to stand apart by feeling more human, more creative, and more accessible."
- Character limit: 1,000 characters
- Logic note: This is the competitive positioning field. It gives Five Points both the competitive set to research and the client's own framing of their differentiation. The competitors named here feed into the competitive analysis during the brand strategy phase.

---

### Step 3: Inspiration and Assets

**Section title displayed on page:** Show us what inspires you.
**Visual note:** This step should feel lighter and more fun than the previous two. Sharing inspiration is enjoyable for most people. The file upload field should be prominent and easy to use.

**Field 9 — Share brands, websites, or visual styles you admire.**
- Type: Long text (textarea)
- Required: No
- Context line above field: "These do not need to be in your industry. We are looking for the feeling, not the category."
- Placeholder: "e.g. I love the clean, modern feel of Apple. The warmth and earthiness of Patagonia. The playfulness of Mailchimp. Here are some links: [paste URLs]."
- Character limit: 1,000 characters
- Logic note: Inspiration references are the fastest way to calibrate aesthetic taste. When a prospect references Apple, Patagonia, and Mailchimp, Five Points immediately understands the design universe they are drawn to. This saves significant time during moodboarding and concept development.

**Field 10 — Do you have any specific deliverables or outcomes you are hoping for?**
- Type: Multi select checkboxes
- Required: No
- Options:
  - Logo design or refresh
  - Color palette and typography
  - Brand guidelines document
  - Business cards and stationery
  - Social media visual kit
  - Website design direction
  - Brand voice and messaging framework
  - I am not sure. I trust your recommendation.
- Helper text: "Select as many as apply. We will refine the scope during our conversation."
- Logic note: This is a scope signal, not a commitment. It helps Five Points understand the client's expectations and prepare appropriate tier recommendations for the discovery call. "I trust your recommendation" is a strong ICP indicator. It signals a client who respects expertise and will be collaborative rather than prescriptive.

**Field 11 — Anything else about your brand vision that would help us understand what you are looking for?**
- Type: Long text (textarea)
- Required: No
- Placeholder: "Context, preferences, concerns, things you have seen that you loved or hated. Anything that helps us understand your taste and vision."
- Character limit: 1,000 characters
- Logic note: The open catch all. Consistent with Documents 2 and 3.

---

### Form Submission Experience

**Confirmation page headline:** "We cannot wait to see what we create together."

**Confirmation page body:**
"Thank you for sharing your vision with us. This gives us a real foundation to start thinking about your brand. Our team will review what you shared and reach out within one business day to schedule a conversation.

When we talk, we will come with initial observations and ideas, not a blank slate.

Talk soon.

Five Points Digital Studio"

---

### What Happens on the Five Points Side After Submission

1. Form submission triggers a Make automation
2. The automation compiles the intake responses (including any uploaded files) into the unified prospect profile alongside data from Document 1 (and Documents 2 or 3 if applicable)
3. Five Points receives an internal notification with the compiled Brand Strategy intake summary
4. The notification flags key signals: brand maturity (Field 1), emotional relationship with current brand (Field 3), brand personality descriptors (Fields 5 and 6), and desired deliverables (Field 10)
5. Uploaded brand assets are stored in the prospect's project folder in Google Drive for team review
6. The engagement is assigned to the appropriate team member based on the recommended tier and the creative complexity revealed in this intake

---

## PART 2: INTERNAL BRAND ASSESSMENT CHECKLIST

### Purpose

This is a structured checklist and conversation guide that ensures the Five Points team evaluates the right things during brand discovery calls and strategy sessions. It is not a numerical scoring rubric. Brand work is subjective and contextual, and forcing it into a one to five scale would produce misleading precision.

The checklist is organized by assessment area. Each area includes what to look for, what questions to ask during discovery, and what to document.

### How to Use This Checklist

Before the discovery call or brand strategy session, review the client's intake responses from Document 1 and Document 4. Review any uploaded brand assets. Use this checklist to guide the conversation. After the session, complete the documentation column for each area. The completed checklist becomes the foundation for the Brand Foundations Kit (Bronze), the brand strategy session (Silver), or the comprehensive brand engagement scope (Gold and Platinum).

---

### Area 1: Brand Foundation

**What to look for:** Whether the client has a clear sense of purpose, positioning, and values, or whether these need to be established.

**Questions to ask during discovery:**
- "Why does your business exist beyond making money? What problem were you put here to solve?"
- "If you had to describe what makes you different from everyone else in your space in one sentence, what would you say?"
- "What do your best clients say about you when you are not in the room?"
- "Are there values that your team lives by that your brand does not yet communicate?"

**What to document:**
- Mission clarity: Does the client have a clear, articulate mission, or is it vague?
- Positioning: How does the client position themselves relative to competitors? Is it defensible and distinct?
- Values: What values drive the business? Are they lived or aspirational?
- Founder story: Is there a compelling origin story that should inform the brand narrative?

---

### Area 2: Audience Understanding

**What to look for:** How deeply the client understands the people they serve and whether their current brand resonates with that audience.

**Questions to ask during discovery:**
- "You described your audience as [intake Field 4 response]. Tell me more about what motivates them to choose you over someone else."
- "What does your ideal client care about beyond your product or service? What are their values?"
- "Have you ever lost a client or customer to a competitor? What was the reason?"
- "If your audience could change one thing about how you present yourself, what do you think they would say?"

**What to document:**
- Audience profile depth: Is the client's understanding of their audience surface level (demographics only) or deep (psychographics, motivations, pain points)?
- Brand audience alignment: Does the current brand speak to the audience the client wants to attract, or is there a mismatch?
- Audience aspirations: What does the client's audience aspire to? This informs the emotional register of the brand.

---

### Area 3: Visual Identity Evaluation

**What to look for:** The current state of the client's visual identity and how well it communicates their positioning and values.

**Questions to ask during discovery:**
- "Walk me through the story of your current logo. Who designed it, when, and what was the brief?"
- "When you see your brand next to your competitors, what stands out? What blends in?"
- "Is there anything about your current visual identity that actively works against you?"
- "Do you have strong feelings about any specific colors, styles, or visual approaches?"

**What to document:**
- Current visual identity inventory: Logo, colors, fonts, imagery style, and any existing guidelines
- Visual identity strengths: What is working and worth preserving
- Visual identity gaps: What is missing, outdated, or misaligned with the brand foundation
- Client aesthetic preferences and aversions (cross reference with intake Fields 5, 6, 7, and 9)
- Competitive visual landscape: How the client's visual identity compares to competitors named in intake Field 8

---

### Area 4: Brand Voice and Messaging

**What to look for:** Whether the client has a defined brand voice and whether their current messaging effectively communicates their value to their audience.

**Questions to ask during discovery:**
- "If your brand could only say one thing to a new prospect, what should it be?"
- "How would you describe the way your brand speaks? Formal or casual? Authoritative or conversational? Serious or playful?"
- "Show me something you have written for your business that you think sounds exactly like you."
- "Show me something that does not sound like you at all."

**What to document:**
- Current brand voice characteristics: How the brand actually sounds across channels
- Desired brand voice characteristics: How the client wants the brand to sound (cross reference with intake Fields 5 and 6)
- Messaging gaps: Where the current messaging undersells, overcomplicates, or misrepresents the brand
- Key messages to develop: Primary value proposition, supporting messages, tagline direction

---

### Area 5: Brand Ecosystem and Touchpoints

**What to look for:** Every place the brand shows up and how consistent the experience is across touchpoints.

**Questions to ask during discovery:**
- "Walk me through every place a potential client encounters your brand, from the very first time they hear about you to the moment they become a customer."
- "Are there touchpoints where you feel especially strong? Where you feel weakest?"
- "Are there touchpoints that do not exist yet but should?"
- "Does your team have trouble staying on brand? If so, where does it break down?"

**What to document:**
- Complete touchpoint inventory: Website, social media, email, business cards, proposals, invoices, signage, packaging, events, etc.
- Consistency assessment: Where the brand is cohesive and where it fractures
- Priority touchpoints: Which touchpoints have the highest impact on perception and conversion
- Missing touchpoints: Where the brand should show up but does not yet

---

## PART 3: TIER SCOPE NOTES

### Purpose

The intake form (Part 1) is universal across all tiers. The depth of assessment (Part 2) and the deliverables scale with the engagement tier.

---

### Bronze — Brand Foundations Kit ($497)

**Scope:** Async assessment based on intake form responses and uploaded assets only. No live discovery call.

**Checklist areas to complete:**
- Area 1: Brand Foundation (based on intake responses only)
- Area 3: Visual Identity Evaluation (review of uploaded assets and public facing brand presence)

**Areas to skip:**
- Area 2: Audience Understanding (requires live conversation for depth)
- Area 4: Brand Voice and Messaging (requires live conversation)
- Area 5: Brand Ecosystem and Touchpoints (more depth than this tier warrants)

**Deliverable:** Brand Foundations Kit — brand strategy workbook, mood board creation guide, typography and color theory guide, template pack, and a 15 minute Loom video with general feedback on the client's current brand.

**Time budget:** Two to three Pomodoro sessions (50 to 75 minutes of focused work).

---

### Silver — Brand Identity Sprint ($5,000)

**Scope:** Full assessment across all five checklist areas. The 90 minute brand strategy session (Week 1) provides the depth needed.

**Checklist areas to complete:** All five areas (1 through 5), full depth.

**Discovery format:** Areas 1 and 2 are the primary focus of the strategy session. Areas 3 and 4 are explored through review of uploaded assets and the strategy conversation. Area 5 is documented to inform the deliverable scope.

**Deliverable:** Primary logo, alternate mark, color palette, typography selection, basic brand guidelines (10 to 15 pages), and social media profile kit.

**Time budget for assessment (separate from design work):** Three to four Pomodoro sessions (75 to 100 minutes of focused work).

---

### Gold — Comprehensive Brand Identity ($10,000 to $15,000)

**Scope:** Full assessment across all five checklist areas, with additional depth on audience research and competitive visual analysis.

**Checklist areas to complete:** All five areas (1 through 5), full depth, with expanded competitor evaluation (five to seven competitors reviewed for visual identity, messaging, and brand positioning).

**Additional assessment work beyond the checklist:**
- Independent audience research to validate or challenge the client's audience description
- Visual audit of all existing brand touchpoints
- Brand voice analysis across all available content (website copy, social posts, emails, proposals)

**Deliverable:** Full logo system, complete color system, typography system, visual language (photography direction, illustration style, iconography), comprehensive brand guidelines (40+ pages), core collateral design, and AI Brand Voice Training.

**Time budget for assessment:** Five to seven Pomodoro sessions (125 to 175 minutes of focused work).

---

### Platinum — Brand Ecosystem Design ($25,000 to $40,000)

**Scope:** Comprehensive assessment across all five checklist areas, with enterprise level depth. The assessment may involve multiple stakeholder interviews and cross departmental brand perception analysis.

**Checklist areas to complete:** All five areas (1 through 5), with department or audience segment level depth where applicable.

**Additional assessment work beyond the checklist:**
- Stakeholder interviews (30 minutes each) with leadership and key team members to understand internal brand perception
- Customer or client interviews (if client provides introductions) to understand external brand perception
- Full brand architecture analysis for multi brand or multi product organizations
- Environmental and experiential touchpoint evaluation (signage, packaging, physical spaces)

**Deliverable:** Everything in Gold plus brand architecture strategy, environmental and experiential applications, digital brand system (design system for web and app), brand launch strategy, internal brand training, and 90 day post launch brand stewardship.

**Time budget for assessment:** Eight to 12 Pomodoro sessions (200 to 300 minutes of focused work).

---

### Silver — Content Strategy and Launch ($3,500)

**Scope:** Focused assessment on brand voice and messaging only. This engagement uses the Brand Strategy Intake for the brand voice section of the content strategy work.

**Checklist areas to complete:**
- Area 1: Brand Foundation (light review to establish context)
- Area 4: Brand Voice and Messaging (full depth, this is the primary focus)

**Deliverable:** Brand Voice Guide as part of the broader content strategy engagement.

**Time budget for assessment:** Two to three Pomodoro sessions (50 to 75 minutes of focused work).

---

## DEPENDENCIES

- Document 1 (Discovery Intake Form) must be live for the routing to work
- Unified prospect profile system must be in place so data from Document 1 is accessible (no redundant data collection)
- Make automation to compile intake data from Documents 1 and 4 into the unified prospect profile
- File upload handling: uploaded brand assets must be automatically stored in the prospect's project folder in Google Drive
- Internal project management system to assign and track assessment completion by tier

---

*Document 4 of 7 — Five Points Brand Strategy Intake Questionnaire*
*Part of the Standardized Document Library for Five Points Digital Studio*
