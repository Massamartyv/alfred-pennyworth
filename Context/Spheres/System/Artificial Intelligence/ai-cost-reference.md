---
file_type: reference
document_type: ai_cost
scope: system-level reasoning about agent cost
last_updated: 2026-04-23
source: Extracted from retired alfred-os/lib/cost/calculator.ts on 2026-04-23
---

# AI Cost Reference

Per-model token pricing and the formulas that turn it into burn-rate and projections. Preserved from the retired `alfred-os/` cost calculator so that agent dispatching and budgeting decisions can reason about cost without deriving the maths from scratch.

All pricing is USD per 1,000 tokens. The rates below were current as of April 2026 – verify against the provider pricing page before making a cost-sensitive decision.

---

## Pricing Table

| Model | Input ($/1k) | Output ($/1k) | Ratio (out/in) |
|---|---|---|---|
| Claude Opus 4.6 | 0.015 | 0.075 | 5.0× |
| Claude Sonnet 4 | 0.003 | 0.015 | 5.0× |
| Gemini 2.5 Pro | 0.00125 | 0.010 | 8.0× |

**Updates since extraction:** Claude Opus 4.7 and Claude Haiku 4.5 have shipped since this table was written. Add new rows when verifying against the provider pricing page. Retain older rows if workloads may still route to older models for cost reasons.

---

## Cost Formula

For a single task execution:

```
task_cost = (input_tokens / 1000) × input_rate_per_1k
          + (output_tokens / 1000) × output_rate_per_1k
```

Straightforward. Both sides sum; there is no overhead, no prompt-cache discount accounted for here. If prompt caching is in play, input tokens charged should reflect the cached vs uncached split before applying this formula.

---

## Burn Rate

Current-hour or current-day spend is sum of task costs in that window.

```
burn_rate_per_hour = sum(task_cost) over the last 60 minutes
burn_rate_per_day  = sum(task_cost) since midnight local time
```

---

## Monthly Projection

Linear projection from current daily burn:

```
projected_monthly = burn_rate_per_day × days_in_current_month
```

Naive but useful as a first-order signal. For more accuracy, weight weekdays vs weekends and account for known seasonality in agent workload.

---

## Model-Selection Cost Heuristic

Combining this pricing table with the Model Selection Protocol in the global `CLAUDE.md`:

- **Opus** at ~5× Sonnet and ~25× Gemini Pro. Reserve for tasks where quality materially outweighs cost – deep reasoning, creative direction, architectural calls.
- **Sonnet** is the workhorse default. Best quality-to-cost ratio for most agent workloads.
- **Haiku** (not in this table – add when pricing verified) is the classification and transformation default for high-volume, low-judgement tasks.
- **Gemini Pro** is the external-provider alternative for heavy workloads where Anthropic pricing is a constraint. Factor in the provider switch cost (different API, different behaviour) before routing there.

---

## Token Budget Framework Reference

The Five Points `Agents/token-budget-framework.md` defines Light (5k output), Standard (15k output), Heavy (30k output) and a 100k per-session ceiling. Translating those into dollars at the rates above:

| Tier | Output Tokens | Output Cost (Opus) | Output Cost (Sonnet) |
|---|---|---|---|
| Light | 5,000 | $0.375 | $0.075 |
| Standard | 15,000 | $1.125 | $0.225 |
| Heavy | 30,000 | $2.250 | $0.450 |
| Ceiling | 100,000 | $7.500 | $1.500 |

Input cost adds on top, typically 3–5× output tokens for typical agent workloads (context-heavy, generation-moderate). Multiply the table above by ~1.6× for a rough all-in-cost estimate.

---

*Source file `lib/cost/calculator.ts` in the retired Alfred operating system Backend has been archived with the rest of that codebase. This reference captures the load-bearing numbers and formulas; the calculator implementation itself is not worth preserving because Claude Code and the Anthropic Console provide cost tracking natively.*
