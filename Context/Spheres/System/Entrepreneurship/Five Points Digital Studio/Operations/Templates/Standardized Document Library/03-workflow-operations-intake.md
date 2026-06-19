# Document 3 of 7: Five Points Workflow and Operations Intake Questionnaire

**Document type:** Three part specification (client facing intake form + internal workflow assessment checklist + tier scope notes)
**Location:** Client facing intake form lives on a dedicated page within the Five Points website. Internal assessment checklist and tier scope notes are internal operational documents used by the Five Points team.
**Purpose:** Captures the operational context Five Points needs to identify automation opportunities, map workflows, and scope AI integration. The intake form collects what only the client can tell you. The internal checklist guides the Five Points team through what to evaluate and ask during discovery and strategy sessions. The tier scope notes control depth.
**Tone:** Client facing sections are warm, confident, and partner oriented. The language should make operational questions feel approachable, not technical or intimidating. Many prospects filling out this form are not technical people. They know their business is inefficient but may not have the vocabulary to describe why. The form should meet them where they are.

**Used by:** Bronze — Automation Audit, Silver — Automation Strategy Sprint, Gold — Automation Build Out, Gold — AI Transformation Day (pre session), Platinum — AI Operations Overhaul, Platinum — AI Ecosystem Retreat (pre retreat).

**Data dependency:** This form assumes the prospect has already completed the Discovery Intake Form (Document 1). Information captured in Document 1 (name, email, phone, role, business name, website URL, business description, business age, team size, services of interest, biggest challenge, desired outcome, timeline, previous agency experience, and referral source) is stored in the unified prospect profile and is never requested again.

**No Redundancy Rule:** No field should appear on any follow up form if the data was already captured in a previous form within the Five Points intake system. Data collected once is stored in the unified prospect profile and accessed internally. The client never repeats themselves. When a field is close enough to debate, cut it.

---

## PART 1: CLIENT FACING INTAKE FORM (Website Hosted)

### Context

This form is the follow up that a prospect receives after selecting "Automating repetitive tasks and workflows" or "Website or application design and development" on the Discovery Intake Form (Document 1). It arrives via email as a link to a dedicated page on the Five Points website.

The prospect has already told Five Points who they are, what their business does, what their biggest challenge is, and what success looks like. This form goes deeper into how their business actually operates day to day, collecting the information Five Points needs to identify where AI and automation can make the biggest impact.

The questions are intentionally non technical. The prospect does not need to know what an API is or how automation platforms work. They just need to describe how their business runs.

### UX Architecture

Same multi step, one section per page layout as Documents 1 and 2. Three steps.

| Step | Section Title | Fields | Estimated Time | Emotional Weight |
|------|--------------|--------|----------------|-----------------|
| 1 | How Your Business Runs | 4 fields | Three to four minutes | Medium (requires reflection on daily operations) |
| 2 | Your Tools and Systems | 3 fields | Two to three minutes | Low to medium (inventory of what they use) |
| 3 | Where It Breaks Down | 4 fields | Two to three minutes | Medium (identifying pain points and past attempts) |

Total: 11 fields. Estimated completion time: seven to 10 minutes.

### Progress Indicator

Same format as Documents 1 and 2. Three labeled dots connected by a thin line.

```
( How You Operate )----( Your Tools )----( Where It Breaks Down )
         ●                   ○                      ○
```

### Button Copy

| Step | Button Text |
|------|------------|
| 1 | "Next: Your tools and systems" |
| 2 | "Next: Where things break down" |
| 3 | "Submit" |

### Transitions, Validation, and Mobile Behavior

All transition, validation, and mobile behavior follows the same specifications defined in Document 1. Subtle slide or fade animation between steps. Back link available on steps two and three. Validation on "Next" click with gentle inline messaging. Mobile progress indicator compresses to dots only. Next button fixed to bottom of viewport on mobile.

---

### Form Header (Visible on Step 1 Only)

**Headline:** Walk us through how your business runs.

**Subheadline:** We are looking for the honest picture, not the polished version. The more we understand about how your team spends its time, the better we can identify where AI and automation can give you that time back. This takes about seven to 10 minutes.

---

### Step 1: How Your Business Runs

**Section title displayed on page:** The day to day.
**Visual note:** This step has two long text fields and two selection fields. The long text fields should be generous in height. The prospect is being asked to describe their operations, which requires thought. Give them space to think on screen.

**Field 1 — Describe the core activities that keep your business running day to day.**
- Type: Long text (textarea)
- Required: Yes
- Context line above field: "Think about what your team does every week. Not the big picture strategy, but the actual work."
- Placeholder: "e.g. We receive client inquiries, send proposals, schedule appointments, fulfill orders, follow up on invoices, post to social media, respond to emails. Walk us through the rhythm of a typical week."
- Character limit: 1,500 characters
- Visual note: Textarea should be at least five to six lines tall. This is the most important field on the form and the prospect should feel invited to write at length.
- Logic note: This is the operational map. It gives Five Points a high level view of the business processes before the discovery call goes deeper. The language the prospect uses here reveals how they think about their operations and where they spend their attention. Prospects who describe everything in terms of what they personally do (rather than what the team does) are likely bottlenecks in their own business, which is a key finding.

**Field 2 — Which of these areas take up the most time for you or your team?**
- Type: Multi select checkboxes
- Required: Yes (at least one selection)
- Options:
  - Client communication (emails, follow ups, scheduling)
  - Sales and lead management (proposals, CRM, pipeline tracking)
  - Content creation and social media
  - Administrative tasks (invoicing, data entry, reporting)
  - Project management and internal coordination
  - Customer onboarding or fulfillment
  - Hiring, HR, or team management
  - Other (please specify)
- Logic note: This is a categorization layer on top of Field 1. It helps Five Points quickly identify which operational domains are the biggest time sinks without having to parse the open text response. The multi select format acknowledges that most businesses have pain across multiple areas.

**Field 3 — How many people are involved in your core operations?**
- Type: Single select dropdown
- Required: Yes
- Options:
  - Just me. I handle most things myself.
  - Two to three people. Small team, everyone wears multiple hats.
  - Four to 10 people. Defined roles but still a lot of overlap.
  - More than 10 people. Departments or teams with distinct responsibilities.
- Logic note: Document 1 captured team size as a firmographic filter. This field is different. It asks specifically about operational involvement, not total headcount. A 30 person company might only have four people touching the core workflows that Five Points would automate. This distinction matters for scoping.

**Field 4 — Are there tasks in your business that you know should be faster or easier but you have not had time to fix?**
- Type: Long text (textarea)
- Required: No
- Context line above field: "The things you keep meaning to get to but never do."
- Placeholder: "e.g. We still send every invoice manually. Our client onboarding is a mess of emails and shared docs. We know we should have a better system for tracking leads but we just use a spreadsheet."
- Character limit: 1,000 characters
- Logic note: This is the low hanging fruit field. Prospects often know exactly what is broken but have not prioritized fixing it. These responses frequently become the first automations Five Points builds because they are high impact, clearly defined, and the client already has buy in for the solution.

---

### Step 2: Your Tools and Systems

**Section title displayed on page:** What are you working with?
**Visual note:** This step is about inventory. It should feel straightforward and low effort. One long text field and two selection fields.

**Field 5 — What software, apps, or platforms does your business currently use?**
- Type: Long text (textarea)
- Required: Yes
- Context line above field: "List everything you can think of, even if it feels minor."
- Placeholder: "e.g. Google Workspace, QuickBooks, Mailchimp, Calendly, Slack, Trello, Shopify, Excel spreadsheets. Include anything your team uses regularly."
- Character limit: 1,000 characters
- Logic note: This is the tech stack map. It tells Five Points what systems are already in place, which determines integration possibilities and constraints. A business running Google Workspace, Slack, and QuickBooks has a very different automation landscape than one running custom enterprise software. This field also reveals the sophistication level of the client's current operations.

**Field 6 — How do your current tools talk to each other?**
- Type: Single select radio buttons
- Required: Yes
- Options:
  - They are well connected. Data flows between them automatically.
  - Some are connected, but a lot of it is manual (copy and paste, exports and imports).
  - They do not connect at all. Everything is manual.
  - I am not sure how they connect.
- Logic note: This is an integration maturity signal. "They do not connect at all" and "I am not sure" are both strong indicators that automation will produce significant time savings. "Some are connected" suggests there is a partial foundation to build on. "Well connected" is rare at the ICP stage but tells Five Points to look for optimization opportunities rather than foundational builds.

**Field 7 — Is there a tool or system you have been wanting to implement but have not gotten around to?**
- Type: Long text (textarea)
- Required: No
- Placeholder: "e.g. We have been meaning to set up a CRM. We bought a project management tool but never onboarded the team. We know we need something better for scheduling."
- Character limit: 500 characters
- Logic note: This reveals intent and awareness. A prospect who says "we bought HubSpot six months ago but never set it up" is telling Five Points there is an unused asset ready to be activated. A prospect who says "I do not even know what tools exist" is telling Five Points they need more guidance and education, which may point toward an AI Fluency Workshop as a starting point.

---

### Step 3: Where It Breaks Down

**Section title displayed on page:** Where things get stuck.
**Visual note:** This step has two selection fields and two text fields. It should feel like the final stretch, not a second round of heavy lifting. The fields are focused and specific.

**Field 8 — Have you tried to automate or streamline any part of your business before?**
- Type: Single select radio buttons
- Required: Yes
- Options:
  - Yes, and it worked well
  - Yes, but it did not stick or did not work as expected
  - No, but I have been thinking about it
  - No, and I am not sure where to start
- Logic note: This is the automation history field. "Yes, but it did not stick" is the most interesting response. It signals a prospect who understands the value of automation, has experienced the frustration of a failed attempt, and is likely ready to invest in getting it right with professional guidance. "No, and I am not sure where to start" signals a prospect who may need the Bronze Automation Audit or an AI Fluency Workshop before a larger engagement.

**Field 9 — If you could wave a magic wand and automate one thing in your business tomorrow, what would it be?**
- Type: Long text (textarea)
- Required: Yes
- Context line above field: "Do not worry about whether it is technically possible. Just tell us what would make the biggest difference."
- Placeholder: "The one thing that, if it ran itself, would change everything."
- Character limit: 500 characters
- Logic note: This is the dream automation field. It tells Five Points what the client values most and where they feel the most operational pain. It is also a powerful conversation starter for the discovery call. When Five Points can say "you mentioned that if [this thing] ran itself, it would change everything. Let us talk about that," the call immediately feels personal and relevant.

**Field 10 — How comfortable is your team with learning new tools or technology?**
- Type: Single select radio buttons
- Required: Yes
- Options:
  - Very comfortable. We adapt quickly.
  - Somewhat comfortable. We need support during the transition.
  - Not very comfortable. Change is hard for our team.
  - It varies. Some team members are more open than others.
- Logic note: This is a change readiness signal. It directly impacts how Five Points scopes the training and handoff components of any engagement. A team that "adapts quickly" may need a single training session. A team where "change is hard" may need extended support, phased rollouts, and more documentation. This affects pricing, timeline, and the amount of post deployment support included in the scope.

**Field 11 — Anything else about how your business operates that would help us understand the full picture?**
- Type: Long text (textarea)
- Required: No
- Placeholder: "Context, history, concerns, upcoming changes. Anything that helps us understand where you are."
- Character limit: 1,000 characters
- Logic note: The open catch all. Same purpose as Document 2, Field 11. A space for the prospect to share what the structured questions did not cover.

---

### Form Submission Experience

**Confirmation page headline:** "We are already mapping the possibilities."

**Confirmation page body:**
"Thank you for walking us through how your business operates. This gives us a real head start. Our team will review what you shared and reach out within one business day to schedule a conversation.

When we talk, we will have ideas ready. Not generic recommendations, but specific opportunities based on what you just told us.

Talk soon.

Five Points Digital Studio"

---

### What Happens on the Five Points Side After Submission

1. Form submission triggers a Make automation
2. The automation compiles the intake responses into the unified prospect profile alongside data from Document 1 (and Document 2 if applicable)
3. Five Points receives an internal notification with the compiled Workflow and Operations intake summary
4. The notification flags key signals: automation history (Field 8), tech stack complexity (Fields 5 and 6), change readiness (Field 10), and the magic wand response (Field 9)
5. The engagement is assigned to the appropriate team member based on the recommended tier from Document 1 routing and the operational complexity revealed in this intake

---

## PART 2: INTERNAL WORKFLOW ASSESSMENT CHECKLIST

### Purpose

This is not a scoring rubric. Operational workflows are too unique across businesses to be meaningfully scored on a universal one to five scale. Instead, this is a structured checklist and conversation guide that ensures the Five Points team evaluates the right things during discovery calls, strategy sessions, and pre engagement audits.

The checklist is organized by assessment area. Each area includes what to look for, what questions to ask the client during the discovery call, and what to document in the findings.

### How to Use This Checklist

Before the discovery call or strategy session, review the client's intake responses from Document 1 and Document 3. Use this checklist to guide the conversation and ensure nothing critical is missed. After the session, complete the documentation column for each area. The completed checklist becomes the foundation for the Automation Opportunity Report (Bronze), the Automation Architecture Document (Silver), or the implementation scope (Gold and Platinum).

---

### Area 1: Process Inventory

**What to look for:** A complete picture of the client's core business processes, who owns them, and how they flow.

**Questions to ask during discovery:**
- "Walk me through what happens when a new lead comes in. From first contact to closed deal, what are all the steps?"
- "What happens after someone becomes a client? Walk me through the onboarding and fulfillment process."
- "Who touches each step? Is it the same person or does it hand off between people?"
- "Are any of these steps documented anywhere, or does everyone just know what to do?"

**What to document:**
- List of core processes identified (lead management, sales, onboarding, fulfillment, invoicing, reporting, communication, etc.)
- Process owner for each (person or role)
- Whether the process is documented or tribal knowledge
- Estimated frequency (daily, weekly, monthly, per client)

---

### Area 2: Time and Effort Analysis

**What to look for:** Where the client and their team are spending the most time on repetitive, manual, or low leverage tasks.

**Questions to ask during discovery:**
- "Of everything you described, what takes the most time relative to the value it produces?"
- "If I shadowed your team for a week, where would I see the most copy and paste, manual data entry, or repetitive clicking?"
- "How many hours per week does your team spend on [specific task from intake Field 2]?"
- "What would your team do with that time if they got it back?"

**What to document:**
- Top five to 10 time consuming tasks ranked by estimated hours per week
- Which tasks are repetitive and predictable (strong automation candidates) versus which require judgment and creativity (AI augmentation candidates versus human only)
- Estimated hours per week recoverable through automation

---

### Area 3: Tech Stack and Integration Landscape

**What to look for:** What tools the client uses, how they connect (or do not connect), and where the gaps and redundancies are.

**Questions to ask during discovery:**
- "You mentioned you use [tools from intake Field 5]. Walk me through how data moves between them."
- "When a lead comes in through your website, what happens to that information? Where does it go?"
- "Are there tools you are paying for but not fully using?"
- "Do you ever have to manually move data from one system to another? How often?"

**What to document:**
- Complete tech stack list with purpose of each tool
- Integration status between tools (connected, partially connected, not connected)
- Data flow map: how information moves between systems (or does not)
- Redundant or underutilized tools
- Missing tools (gaps where no system exists for a key process)

---

### Area 4: Automation Readiness

**What to look for:** How prepared the client's business is to adopt automation, considering both technical infrastructure and team culture.

**Questions to ask during discovery:**
- "You mentioned your team is [response from intake Field 10] with new technology. Can you give me an example of a recent tool or process change and how it went?"
- "Who on your team would be the point person for maintaining automations after we build them?"
- "Is there anything about automation that concerns you or your team?"
- "Have you had any experiences with technology projects that went sideways? What happened?"

**What to document:**
- Technical readiness: Are the existing tools automation friendly? Do they have APIs or integrations available?
- Team readiness: Is there a champion who will own the automations? Is there resistance to change?
- Previous automation attempts: What was tried, what worked, what failed, and why (cross reference with intake Field 8)
- Risk factors: Anything that could derail implementation (team turnover, upcoming system migrations, budget constraints, etc.)

---

### Area 5: Opportunity Prioritization

**What to look for:** Which automation opportunities should be pursued first based on impact, feasibility, and client priorities.

**Questions to ask during discovery:**
- "Of all the things we have discussed, which one would make the biggest difference to you personally?"
- "If we could only build one thing, what should it be?"
- "Are there any upcoming events, seasons, or deadlines that would make certain automations more urgent?"
- "What does a quick win look like for you? Something that would make you feel like this was worth it in the first two weeks?"

**What to document:**
- Ranked list of automation opportunities (minimum five, up to 20 for Platinum engagements)
- For each opportunity: estimated time savings, estimated complexity (simple, moderate, complex), recommended tools, and dependencies
- Client's stated priority (cross reference with intake Field 9, the magic wand response)
- Recommended first build (the quick win that demonstrates value and builds trust)
- Recommended sequence for remaining builds

---

### Area 6: Data and Decision Logic

**What to look for:** Where decisions are currently made by humans that could be supported or fully handled by AI.

**Questions to ask during discovery:**
- "Are there decisions your team makes that follow a predictable pattern? For example, how you route inquiries, how you prioritize tasks, or how you segment customers?"
- "Do you ever wish you had better data to make decisions? What kind of data?"
- "Are there reports you create manually that could be generated automatically?"
- "Is there any part of your client communication that is templated or follows a script?"

**What to document:**
- Decision points that follow consistent logic (strong candidates for AI powered automation)
- Data sources available for AI analysis (CRM data, email history, financial records, client feedback)
- Reporting needs (what the client wants to see, how often, and where the data currently lives)
- Communication patterns that could be templated or AI assisted (proposals, follow ups, onboarding emails, status updates)

---

## PART 3: TIER SCOPE NOTES

### Purpose

The intake form (Part 1) is universal across all tiers. The depth of assessment (Part 2) and the deliverables scale with the engagement tier. These notes tell the Five Points team how deep to go and what to produce at each level.

---

### Bronze — Automation Audit ($497)

**Scope:** Async assessment based on intake form responses only. No live discovery call. Five Points reviews the intake data and delivers a report.

**Checklist areas to complete:**
- Area 1: Process Inventory (based on intake responses only, no live conversation)
- Area 2: Time and Effort Analysis (estimated from intake responses)
- Area 3: Tech Stack and Integration Landscape (based on intake Field 5 and Field 6)
- Area 5: Opportunity Prioritization (top 10 opportunities ranked by ROI)

**Areas to skip:**
- Area 4: Automation Readiness (requires live conversation to assess meaningfully)
- Area 6: Data and Decision Logic (requires deeper discovery than the intake provides)

**Deliverable:** Automation Opportunity Report — top 10 automation opportunities ranked by ROI, recommended tools, estimated time savings, and a prioritized implementation sequence. Plus a 15 minute Loom video walkthrough.

**Time budget:** Two to three Pomodoro sessions (50 to 75 minutes of focused work).

---

### Silver — Automation Strategy Sprint ($3,000)

**Scope:** Full assessment across all six checklist areas. Three live sessions over two weeks provide the depth needed for comprehensive evaluation.

**Checklist areas to complete:** All six areas (1 through 6), full depth.

**Discovery format:** Area 1 and Area 2 are the primary focus of Session 1. Areas 3 and 4 are explored across Sessions 1 and 2. Areas 5 and 6 are the focus of Sessions 2 and 3.

**Deliverable:** Automation Architecture Document — visual workflow diagrams for the top five automations, tool recommendations, integration architecture, decision logic mapping, and detailed build specifications.

**Time budget for assessment (separate from session delivery):** Three to four Pomodoro sessions (75 to 100 minutes of focused work) for preparation and documentation.

---

### Gold — Automation Build Out ($5,000 to $10,000)

**Scope:** Full assessment across all six checklist areas, plus hands on technical evaluation of the client's systems.

**Checklist areas to complete:** All six areas (1 through 6), full depth, with additional technical validation of integration feasibility for each proposed automation.

**Additional assessment work beyond the checklist:**
- Test API availability and authentication requirements for each tool in the client's tech stack
- Validate data formats and field mapping between systems
- Identify potential failure points and error handling requirements for each proposed automation

**Deliverable:** Detailed implementation scope document covering each automation to be built, including workflow diagrams, tool specifications, data mapping, testing plan, and training requirements. This document serves as the build blueprint.

**Time budget for assessment:** Four to five Pomodoro sessions (100 to 125 minutes of focused work).

---

### Gold — AI Transformation Day ($5,000)

**Scope:** Full assessment across all six checklist areas, conducted primarily during the pre session discovery call and the first half of the intensive day.

**Checklist areas to complete:** All six areas (1 through 6), full depth.

**Assessment timing:** Areas 1 through 4 are covered in the 60 minute pre session discovery call and the intake responses. Areas 5 and 6 are explored during the morning session of the intensive day. The afternoon is dedicated to building and deploying the priority automations identified.

**Deliverable:** AI Integration Roadmap document with prioritized implementation plan for the next six months.

**Time budget for pre session assessment:** Two to three Pomodoro sessions (50 to 75 minutes of focused work).

---

### Platinum — AI Operations Overhaul ($20,000 to $35,000)

**Scope:** Comprehensive assessment across all six checklist areas, with department level depth. The assessment may involve multiple stakeholder interviews beyond the primary contact.

**Checklist areas to complete:** All six areas (1 through 6), repeated for each department or functional area within the organization. A 30 person company with sales, operations, marketing, and finance departments would produce four separate assessments that are then synthesized into a unified operational view.

**Additional assessment work beyond the checklist:**
- Stakeholder interviews (30 minutes each) with department leads to validate intake responses and uncover department specific pain points
- Cross department data flow mapping to identify automation opportunities that span multiple teams
- Security and compliance review for any automations that handle sensitive data

**Deliverable:** Complete Automation Ecosystem Blueprint — comprehensive operational audit, full workflow mapping across all departments, prioritized implementation roadmap (10 to 20+ workflows), integration architecture, training plan, and change management recommendations.

**Time budget for assessment:** Seven to 10 Pomodoro sessions (175 to 250 minutes of focused work).

---

### Platinum — AI Ecosystem Retreat ($15,000)

**Scope:** Same comprehensive assessment as the AI Operations Overhaul, but conducted in a compressed timeline to support the two day on location intensive.

**Checklist areas to complete:** All six areas (1 through 6), full depth, completed during the pre retreat phase (two weeks before the retreat).

**Assessment timing:** The intake form is completed upon booking. Five Points conducts the assessment (including stakeholder interviews) during the two weeks before the retreat. By Day 1 of the retreat, the assessment is complete and findings are ready to present.

**Deliverable:** Complete AI Integration Blueprint — strategic document covering every department's AI roadmap for the next 12 months. Delivered post retreat.

**Time budget for pre retreat assessment:** Eight to 12 Pomodoro sessions (200 to 300 minutes of focused work).

---

## DEPENDENCIES

- Document 1 (Discovery Intake Form) must be live for the routing to work
- Unified prospect profile system must be in place so data from Document 1 is accessible (no redundant data collection)
- Make automation to compile intake data from Documents 1 and 3 into the unified prospect profile
- Internal project management system to assign and track assessment completion by tier
- Loom account for Bronze tier video walkthroughs
- Scheduling tool for discovery call booking (Silver and above)

---

*Document 3 of 7 — Five Points Workflow and Operations Intake Questionnaire*
*Part of the Standardized Document Library for Five Points Digital Studio*
