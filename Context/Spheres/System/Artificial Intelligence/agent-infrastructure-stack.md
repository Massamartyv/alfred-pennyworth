# Agent Infrastructure Stack

The six-layer framework for understanding the primitives that agents require to operate in the world. This is the mental model for evaluating tools, identifying gaps and making architectural decisions across Alfred OS and all ventures.

---

## The Six Layers

The agent economy is assembling a new infrastructure stack analogous to the cloud shift of 2006 to 2010 and the microservices shift of 2012 to 2016. The new customer for infrastructure is the agent. Each layer represents a class of primitive that agents need to function.

### Layer 1 – Compute and Sandboxing

**What it solves:** Agents need somewhere safe to run code. Not on your laptop, not in production, not unsupervised. Isolated, sandboxed, auditable execution.

**Key players:** E2B (firecracker microVMs, ephemeral sessions), Daytona (Docker containers, persistent state, fast cold start), Modal (GPU-heavy workloads), Browserbase (headless browser automation).

**The architectural split:** Ephemeral vs persistent. Disposable sandboxes assume short sessions with no state. Persistent environments assume the agent installs dependencies, creates files and comes back later. This is not a style preference – it is a bet on how long agent sessions will run and whether state matters.

**Alfred OS mapping:** Claude Code runs locally on the Mac. For deployed agents and client-facing automations, this layer becomes relevant. The `.working/` directory is an early local analogue – a transient execution space.

**Maturity:** Most production-ready layer in the stack. Multiple viable options.

### Layer 2 – Identity and Communication

**What it solves:** Agents need to exist on the internet as entities. They need to send and receive messages, authenticate with services and hold verifiable identity.

**Current state:** Email is the pragmatic shim. Startups like Agent Mail give agents real email addresses because email is a universal key to SaaS signup, verification and communication. But email was designed for humans – threading is brittle, rate limits were designed to stop automation, signal-to-noise is terrible for context windows.

**The deeper need:** Agent-native identity and communication protocols that do not require pretending to be human. On-chain identity, dedicated agent-to-agent communication standards and MCP-based service discovery are all emerging but nothing has a right to win yet.

**Alfred OS mapping:** Alfred uses the Email Directory (global CLAUDE.md) for human-facing communication and MCP connections for service authentication. iMessage is the notification layer. This is a shim-heavy setup – functional today, but worth watching for agent-native alternatives.

**Maturity:** Transitional. Email works because it is everywhere, not because it is the right protocol.

### Layer 3 – Memory and State

**What it solves:** Agents need to remember what happened – not just within a session but across sessions, tasks and days.

**Key insight:** Memory is not saving the conversation. Memory is active curation – storing important information, deliberately forgetting outdated details and only recalling relevant context at inference time. Mem0 uses a hybrid architecture (graph, vector, key-value) to treat memory as managed infrastructure rather than a bolted-on feature.

**Platform risk:** Every frontier lab is building memory into its models. If memory becomes a model-level feature, standalone memory companies face commoditisation. The counter-thesis is portability – no one should own your memory.

**Alfred OS mapping:** The `.claude/projects/.../memory/` system with MEMORY.md index, typed memory files and active curation rules. Alfred already follows the active-curation pattern: save what is non-obvious and future-useful, update or remove what is stale, verify before acting on recalled memories. The risk here is lock-in to Claude's memory system. Notion serves as the durable, portable layer underneath.

**Maturity:** Early but real. Platform risk is equally real.

### Layer 4 – Tools and Integration

**What it solves:** Agents need to interact with external services – Slack, Jira, Salesforce, GitHub, Google Workspace. Without middleware, every agent builder independently manages credentials, auth flows, rate limits, error handling and API schema changes for every tool. This is the N times M integration nightmare.

**Key players:** Composio ($29 million, managed integration layer with pre-built connectors and observability). MCP is the emerging standard that could reduce the need for managed middleware.

**Long-term risk:** If MCP becomes truly universal, managed integration layers lose value. The bet for companies like Composio is that enterprises are slow to adopt – and that gap is where the entire thesis sits.

**Alfred OS mapping:** MCP is the primary integration layer. The `integrations.md` files per venture document which plugins are in scope and how they route. The MCP routing map (in memory) tracks the full connection topology. This is one of the strongest layers in the current Alfred architecture – but it is entirely dependent on the MCP ecosystem maturing. Monitor for gaps where MCP connections do not exist and manual integration is needed.

**Maturity:** Growing explosively. Solves real and immediate pain.

### Layer 5 – Provisioning and Billing

**What it solves:** Agents need to acquire services and pay for them securely. Until now, account creation and infrastructure provisioning required a human for authentication.

**Key development:** Stripe Projects launched with CLI commands that let agents provision databases, upgrade hosting tiers and handle payments with tokenised credentials. Databases ready in 350 milliseconds, free to start, scale to zero.

**What is missing:** Agent-to-agent payments, metered billing mapped to agent compute patterns, dynamic budget allocation (Agent A can spend X without approval, Agent B needs approval above Y), FinOps observability across workflows.

**Alfred OS mapping:** The token-budget-framework in Five Points is an early analogue for budget allocation. The execution tiers (full autonomy, execute then notify, approval required) are a proto-version of dynamic spending authority. As ventures scale and agents provision real infrastructure, this layer needs a formal billing and spend-control protocol.

**Maturity:** Brand new. Stripe is the first credible entry. Here to stay.

### Layer 6 – Orchestration and Coordination

**What it solves:** Agents need to work with other agents reliably at scale – with fallback handling, audit trails, cost controls and human escalation paths.

**The gap:** Current tooling is at the framework level, not the infrastructure level. The difference between spinning up three agents in a notebook and reliably running 50 agents across enterprise systems with failure recovery and cost controls is enormous. That latter piece is hand-rolled everywhere.

**What does not exist yet but needs to:**
1. Scheduling and lifecycle layer – agent creation, assignment, health checking, scaling, termination as a managed service
2. Merge and coordination infrastructure – merge queues, conflict detection, resolution protocols for parallel agent work
3. Supervision hierarchies – meta-agents that monitor and course-correct other agents, as infrastructure you configure rather than code you write
4. Financial observability – cost per agent, cost per successful task, outcome quality metrics (FinOps for agents)
5. Standard failure and recovery patterns – when a tool call fails, standard provisioning for what happens next

**Alfred OS mapping:** Penny One and Watchtower ARE the orchestration layer. Penny One aggregates intelligence (scheduling, lifecycle, briefing). Watchtower monitors thresholds and alerts (supervision, failure detection). The six-crew classification system provides the horizontal capability model. This is the most valuable position in the stack and the one we are already building toward.

**Maturity:** Biggest opportunity. Biggest gap. Whoever solves this at infrastructure grade owns the most valuable position in the agent economy.

---

## Builder Lessons for 2026

### Reliability compounds in the wrong direction

When an agent depends on five different primitives, end-to-end reliability is the product of five separate reliabilities. 99% uptime per layer yields 95% system uptime. 97% per layer yields 86%. Every primitive you compose by hand stacks its liabilities onto your system. Build with this in mind.

### Transitional lock-in is real

Building on shims (email as identity, any single vendor's memory, bespoke integration patterns) creates migration costs when native protocols arrive. Every shim is a bet that it either becomes the standard or that you are willing to swap it out. Make that bet deliberately, not accidentally.

### Agent sprawl is coming

The same disease that plagued microservices in 2018 – everything decomposed into services because it was fashionable, not because it was needed. Agents proliferating across an organisation without observability, orchestration or cost controls. The antidote is investing in orchestration now, even if it means hand-rolling it.

---

## How Alfred OS Maps to the Stack

| Layer | What We Have | What We Need |
|---|---|---|
| 1. Compute and sandboxing | Local Mac execution, `.working/` for transient files | Cloud sandbox strategy when deploying agents for clients |
| 2. Identity and communication | Email Directory, iMessage, MCP auth | Watch for agent-native identity protocols |
| 3. Memory and state | `.claude/` memory system, Notion as durable layer | Portability strategy if memory moves model-level |
| 4. Tools and integration | MCP connections, per-venture `integrations.md` | Gap analysis for services without MCP support |
| 5. Provisioning and billing | Token budget framework, execution tiers | Formal billing protocol as agents provision real infrastructure |
| 6. Orchestration and coordination | Penny One, Watchtower, six-crew system | Implementation. Move from design to production. |

---

## Stack Literacy as a Competitive Advantage

Understanding these six layers is not optional for anyone deploying agents at scale. The builders who survive – whether entrepreneurs, individual builders or enterprise leaders – need to understand which layers are mature, which are shims, which are hand-rolled and how changes in the stack affect their business.

For Five Points clients deploying automation and digital architecture, stack literacy is part of the value proposition. For the ventures, it is the lens through which every infrastructure decision should be evaluated.

---

*Last updated: April 2026*
