# Notion AI Subscription Analysis

**Date:** 2026-05-28
**Trigger:** Touch-point audit Optimisation #2. Operator not subscribed to Notion AI, open to evaluating.
**Decision owner:** Martavious.

---

## The pricing reality

The standalone Notion AI add-on at roughly $10 per member per month was **eliminated in May 2025**. As of 2026, full AI access is bundled only into the **Business plan at $20 per user per month billed annually, $24 monthly**.

This reframes the question. It is not "add $10 of AI to my current plan." It is "upgrade my whole plan to Business to unlock AI." If the operator is currently on Plus at $10/month, the delta is $10 to $14/month, $120 to $168/year. If on Free, the delta is the full $20 to $24/month.

## What the Business plan AI tier includes

- **AI Agents and Custom Agents** – autonomous agents with skills, triggers, schedules. Build specialised workflows that run 24/7 inside the workspace.
- **AI Autofill** – database properties auto-completed by AI on entry. Predict Sphere, Type, summary, tags at capture time.
- **Ask Notion** – workspace-wide AI search across Notion and connected sources (Google Drive, Slack, GitHub).
- **AI inline writing and Q&A** – compose and interrogate inside any page.
- **External Agents API access** – the Claude-Code-as-agent path, gated behind both Business plan and the alpha waitlist.

## What we have already built that overlaps

| Notion AI feature | Our existing coverage | Verdict |
|---|---|---|
| Custom Agents with schedules | The four remote routines we are shipping via claude.ai (Weekly, Quarterly, Annual, Content gap) plus the pattern-memo heartbeat agent | Largely redundant. Our routines do the scheduling without the upgrade |
| AI Autofill | Claude Code can enrich on demand via MCP, but not inline at capture time | Genuine gap. This is the one feature Claude Code cannot replicate natively |
| Ask Notion | Claude Code queries the workspace via the official Notion MCP | Redundant in capability, different in surface. Ask Notion is in-app; Claude Code is a context switch |
| AI inline writing | Claude Code drafts in operator voice via CLAUDE.md | Redundant in capability; Notion's is inline, ours is richer |
| External Agents API | Same waitlist either way | Neutral |

## The honest marginal value

For a solo operator who already runs Claude Code with full MCP access, the upgrade buys essentially one unique capability the current stack cannot match: **AI Autofill at capture time**. Everything else is either redundant with Claude Code or replaced by the remote routines we just built.

AI Autofill is genuinely useful for the capture-friction problem identified in the audit. The operator captures to Inbox; AI Autofill predicts Sphere and Type the moment the entry lands, with no manual tagging and no Claude Code dispatch. That is the daily-cadence friction reducer.

But $120 to $288/year for one feature is a steep single-feature price, especially when Claude Code can do the same enrichment on a nightly sweep for the cost of tokens already being spent.

## Recommendation

**Hold the upgrade. Re-evaluate on a specific trigger.**

The remote routines close the scheduling gap that was the strongest argument for Notion AI. That removes most of the upgrade's value in one move. What remains is AI Autofill, which is real but not $200-plus-per-year real on its own.

Two triggers that would flip the recommendation to upgrade:

1. **Capture volume climbs and nightly Claude Code enrichment proves too slow.** If the operator wants Sphere and Type predicted the instant an entry lands rather than that night, AI Autofill earns its place. Test this by running a Claude Code nightly enrichment sweep first; if the latency annoys, upgrade.
2. **In-Notion AI Q&A becomes a felt need.** If the operator finds himself wishing he could ask the workspace a question without switching to Claude Code, Ask Notion earns its place.

**Interim move:** build the Claude Code nightly enrichment sweep as the AI Autofill stand-in. A routine or local agent that reads un-enriched Inbox and Permanent Notes entries, predicts Sphere and Type, and either applies them or surfaces them for one-tap approval. This tests the value of capture-time enrichment at token cost before committing $200+/year.

## If the operator wants to trial regardless

Notion offers Business plan trials. A two-week trial would let the operator feel AI Autofill and Ask Notion directly before committing. The clean test: does AI Autofill change the daily capture habit enough to justify the standing cost. If the habit does not change, the upgrade is not earning its place.

## Sources

- [Notion Pricing 2026: Free, $10 Plus, $18 Business – Automation Atlas](https://automationatlas.io/answers/notion-pricing-explained-2026/)
- [Notion AI Pricing 2026: Plans, Cost and Add-On Status – Fello AI](https://felloai.com/notion-ai-pricing/)
- [Notion Pricing Plans – official](https://www.notion.com/pricing)
