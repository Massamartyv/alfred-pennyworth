# Document 7 of 7: Five Points Post Engagement Feedback Form

**Document type:** Client facing feedback form (website hosted)
**Location:** Dedicated page within the Five Points website, sent to the client via email after the engagement is complete and all final deliverables have been accepted.
**Purpose:** Captures client satisfaction, identifies areas for improvement, collects testimonial material, and opens the door for referrals. This form closes the loop on the client journey and turns a completed engagement into future business development fuel.
**Tone:** Warm, grateful, and genuine. The client just finished working with Five Points. This form should feel like a thoughtful closing conversation, not a corporate survey. The questions should be easy to answer and should make the client feel like their opinion genuinely matters.

**Used by:** Every completed engagement across all tiers (Bronze through Platinum).

**Data dependency:** This form is sent after the engagement is complete. The unified prospect profile already contains all client information. The form does not collect any identifying information because the email delivery links the response to the client record automatically through the Make automation.

**No Redundancy Rule:** The client has already provided all relevant business and contact information. This form collects feedback only. No identifying fields (name, email, business name) appear on the form. The automation links the response to the client record based on the unique form link sent via email.

---

## PART 1: CLIENT FACING FEEDBACK FORM (Website Hosted)

### Context

This form is sent to the client via a personalized email after the final deliverable has been accepted and the engagement is formally closed. The email includes a unique link to the form that ties the response to the client's record in the Five Points system, eliminating the need for the client to re-enter any identifying information.

The form is intentionally short. The client has already invested significant time in the intake process at the beginning of the engagement. Asking for a lengthy post engagement survey is disrespectful of that prior investment. The goal is to capture high signal feedback in the fewest possible fields.

### UX Architecture

Single page form. No multi step layout needed. The form is short enough (seven fields) to display on a single scrollable page without feeling overwhelming.

Total: 7 fields. Estimated completion time: three to five minutes.

---

### Form Header

**Headline:** How did we do?

**Subheadline:** Your honest feedback helps us get better. This takes about three minutes, and every response is read by the founder.

---

### Form Fields

**Field 1 — Overall, how would you rate your experience working with Five Points?**
- Type: Single select (visual scale)
- Required: Yes
- Format: Five point scale displayed as clickable icons or stars
  - 1 — Did not meet expectations
  - 2 — Below expectations
  - 3 — Met expectations
  - 4 — Exceeded expectations
  - 5 — Exceptional
- Visual note: Use a visual scale (stars, icons, or a horizontal selector) rather than a dropdown. Visual scales feel more intuitive and less clinical. The labels should appear on hover or below each option.
- Logic note: This is the headline metric. It tells Five Points at a glance whether the engagement was successful from the client's perspective. Track this across all engagements to identify trends by tier, pillar, and team member.

**Field 2 — What exceeded your expectations?**
- Type: Long text (textarea)
- Required: No
- Placeholder: "What stood out? What surprised you in a good way?"
- Character limit: 1,000 characters
- Visual note: Textarea should be three to four lines tall.
- Logic note: This is the testimonial mining field. Responses here often contain the exact language Five Points can use (with permission) in case studies, website copy, and social proof. Asking what "exceeded" rather than what "went well" primes the client to think about moments of delight, not just adequate performance.

**Field 3 — What could we have done better?**
- Type: Long text (textarea)
- Required: No
- Placeholder: "Be honest. This is how we improve."
- Character limit: 1,000 characters
- Visual note: Same height as Field 2.
- Logic note: This is the improvement field. It should be genuinely easy to answer honestly. The placeholder text ("Be honest. This is how we improve.") signals that Five Points can handle constructive criticism. Clients who feel safe giving honest feedback are more likely to become long term partners because they trust the relationship.

**Field 4 — Would you be open to us using your feedback as a testimonial?**
- Type: Single select radio buttons
- Required: Yes
- Options:
  - Yes, you can use my name and business name
  - Yes, but please keep it anonymous
  - I would prefer not to be quoted
- Logic note: This is the permission gate. Never use client feedback as a testimonial without explicit permission. The anonymous option captures clients who want to help but are not comfortable being public facing. Even anonymous testimonials ("A healthcare CEO in Atlanta") carry social proof.

**Field 5 — Is there anyone in your network who could benefit from working with Five Points?**
- Type: Long text (textarea)
- Required: No
- Placeholder: "If someone comes to mind, share their name and the best way to reach them. We will mention you sent us."
- Character limit: 500 characters
- Logic note: This is the referral field. It is positioned after the satisfaction and testimonial questions intentionally. A client who just gave a 4 or 5 rating and offered testimonial permission is in the right emotional state to think about referrals. A client who gave a 2 and said "you could have communicated better" is not, and they will naturally skip this field.

**Field 6 — Would you be interested in continuing to work with Five Points?**
- Type: Single select radio buttons
- Required: Yes
- Options:
  - Yes, I have additional projects in mind
  - Possibly, but not right now
  - No, this engagement covered what I needed
- Logic note: This is the upsell signal. "Yes, I have additional projects in mind" should trigger an internal notification to Five Points to schedule a follow up conversation. "Possibly, but not right now" should trigger a 90 day follow up reminder. "No" is respected and closes the loop.

**Field 7 — Anything else you want to share?**
- Type: Long text (textarea)
- Required: No
- Placeholder: "Open floor. Anything on your mind."
- Character limit: 1,000 characters
- Logic note: The open catch all. Consistent with all previous forms in the document library. Some of the most meaningful feedback comes from this field because the client is no longer thinking within the structure of the form.

---

### Form Submission Experience

**Confirmation page headline:** "Thank you. This means a lot to us."

**Confirmation page body:**
"We read every response, and your feedback directly shapes how we work. It has been a genuine pleasure working with [Business Name].

If you ever need anything down the road, you know where to find us.

Five Points Digital Studio"

**Design note:** The confirmation page should feel like a warm goodbye, not a transaction receipt. Consider including a subtle, branded visual element. Keep it brief.

---

### What Happens on the Five Points Side After Submission

1. Form submission triggers a Make automation
2. The automation links the response to the client's record in the unified profile using the unique form link identifier
3. Five Points receives an internal notification with the feedback summary, including:
   - Overall rating (Field 1)
   - Testimonial permission status (Field 4)
   - Referral information if provided (Field 5)
   - Continuation interest (Field 6)
4. Automated follow up actions based on responses:
   - If Field 1 is 4 or 5 AND Field 4 is "Yes" (named): Flag for case study development and add testimonial to the social proof library
   - If Field 1 is 4 or 5 AND Field 4 is "Yes" (anonymous): Add anonymous testimonial to the social proof library
   - If Field 1 is 1 or 2: Flag for founder review and personal follow up within 48 hours
   - If Field 5 contains referral information: Create a new lead record and schedule outreach within five business days, mentioning the referral source
   - If Field 6 is "Yes, additional projects": Schedule a follow up conversation within one week
   - If Field 6 is "Possibly, not right now": Create a 90 day follow up reminder

---

## DELIVERY EMAIL

### When to send:

Send the feedback form email within 48 hours of the client accepting the final deliverable. Do not wait weeks. The engagement is freshest in the client's mind immediately after delivery, and that is when you get the most detailed and accurate feedback.

For retainer engagements, send the feedback form at the end of the minimum commitment period, and then annually if the retainer continues.

### Email template:

**Subject line:** "One last thing, [First Name]."

**Body:**

"Now that we have wrapped up your [engagement name], I wanted to ask: how did we do?

We put together a short feedback form (about three minutes) that helps us keep getting better. Your honest perspective matters more than you know.

[Link to feedback form]

It has been a real pleasure working with you and the [Business Name] team. Whatever comes next, we are rooting for you.

Five Points Digital Studio"

---

## PART 2: INTERNAL FEEDBACK ANALYSIS FRAMEWORK

### Purpose

This is not a scoring template or a checklist. It is a framework for how Five Points should analyze and act on the feedback collected through this form across all engagements over time.

### Tracking Metrics

Five Points should track the following metrics on a rolling basis:

**Client Satisfaction Score (CSS):** Average of all Field 1 responses across engagements. Track overall, by tier, by pillar, and by team member. Target: 4.2 or higher.

**Testimonial Conversion Rate:** Percentage of clients who give permission to use their feedback as a testimonial (Field 4, "Yes" responses). Target: 60% or higher.

**Referral Rate:** Percentage of clients who provide at least one referral (Field 5). Target: 25% or higher.

**Continuation Rate:** Percentage of clients who indicate interest in additional work (Field 6, "Yes" or "Possibly"). Target: 50% or higher.

### Quarterly Review Process

At the end of each quarter, review all feedback collected during that period. Look for:

- Patterns in the "exceeded expectations" responses (Field 2): What is Five Points consistently doing well? These are differentiators to emphasize in marketing.
- Patterns in the "could be better" responses (Field 3): What comes up repeatedly? These are systemic issues to address in process, not one off complaints.
- Correlation between tier and satisfaction: Are certain tiers consistently scoring higher or lower? This may indicate pricing misalignment, scope issues, or delivery inconsistencies.
- Correlation between pillar and satisfaction: Are certain service areas outperforming others? This may indicate where Five Points has the strongest expertise and where additional training or process improvement is needed.

### Low Score Response Protocol

Any engagement that receives a Field 1 score of 1 or 2 requires a personal follow up from the founder within 48 hours. The goal of this follow up is not to defend the work. It is to:

1. Listen to the client's experience without defensiveness
2. Identify what went wrong and whether it was a process failure, a communication failure, or a scope misalignment
3. Determine whether there is anything Five Points can do to make it right
4. Document the lessons learned and implement process changes to prevent recurrence

This follow up is not optional. A dissatisfied client who is ignored becomes a detractor. A dissatisfied client who is heard and addressed often becomes a stronger advocate than one who was satisfied from the start.

---

## DEPENDENCIES

- Completed and accepted engagement (all final deliverables delivered and approved)
- Unique form link generation through Make automation (links response to client record without requiring client to re-enter identifying information)
- Internal notification system for automated follow up actions
- Client feedback tracking system (spreadsheet, CRM, or project management tool) for rolling metrics
- Founder availability for low score follow up within 48 hours

---

## DOCUMENT LIBRARY COMPLETION NOTE

This is the seventh and final document in the Five Points Standardized Document Library. The complete library is:

1. **Discovery Intake Form** — Front door. Website hosted. Routes prospects to the appropriate follow up form.
2. **Digital Presence Audit** — Follow up for marketing prospects. Client facing intake plus internal scoring template plus tier scope notes.
3. **Workflow and Operations Intake** — Follow up for automation and development prospects. Client facing intake plus internal assessment checklist plus tier scope notes.
4. **Brand Strategy Intake** — Follow up for design prospects. Client facing intake plus internal brand assessment checklist plus tier scope notes.
5. **Project Scope and Agreement** — Contract template. Modular structure assembled per engagement.
6. **Client Onboarding Packet** — Welcome document. Branded PDF delivered after signing.
7. **Post Engagement Feedback Form** — Closing form. Website hosted. Captures satisfaction, testimonials, referrals, and continuation interest.

Together, these seven documents create a complete client journey from first website visit through post engagement follow up. Every touchpoint is standardized, every document references the unified prospect profile, and no information is ever requested twice.

The next step in the offer suite roadmap is **Next Step 2: Map the full customer journey**, which documents every touchpoint from first website visit through post engagement follow up, identifying where each standardized document is triggered and how the experience flows across offers. With all seven documents now specified, that mapping exercise has a complete foundation to work from.

---

*Document 7 of 7 — Five Points Post Engagement Feedback Form*
*Part of the Standardized Document Library for Five Points Digital Studio*
