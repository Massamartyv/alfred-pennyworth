# Alfred operating system – Project Configuration

This file governs the Alfred Pennyworth directory (`~/Alfred Pennyworth/`). It defines file architecture, naming conventions, lifecycle rules, and the routing rules for this project. Character, identity, ecosystem, and navigation rules live in the global CLAUDE.md (`~/.claude/CLAUDE.md`).

---

## File Architecture

```
Alfred Pennyworth/
├── .claude/                       – Project configuration. Tracked: CLAUDE.md, settings.json, hooks/, agents/, workflows/.
│   ├── CLAUDE.md                  – This file. Project-level configuration.
│   ├── agents/                    – Native crew subagents: researcher, creator, reviewer-scrutiny, reviewer-behavioural, job-applier.
│   ├── cache/                     – One-way Notion state cache and heartbeat marker. Machine-derived, never hand-edited, gitignored.
│   └── hooks/                     – SessionStart, Stop and statusline scripts.
├── .mcp.json                      – Project MCP servers. Secret-free; sources .env by reference. Tracked.
├── .githooks/                     – Tracked git hooks: pre-commit state tripwire. Wired per clone via core.hooksPath (Manual/genesis.md).
├── .working/                       – Transient session files and the offline state buffer (session-buffer/). Not committed to git.
├── Manual/                        – Owner's manual: genesis protocol, account and secret inventories, MCP registry, Brewfile, restore drill.
├── Private/                       – Operator-only sealed documents (emergency kit). Gitignored, mode 700, never read by Alfred.
├── Context/
│   ├── personal-brand-identity.md  – How everything sounds. Governs all pillars.
│   ├── creative-director.md         – Sensory operating system, aesthetic sensibility, aligned brands.
│   ├── vibe-coding-prd-template.md  – PRD template for AI-assisted web development.
│   ├── Reference Library/          – Creators, brands, works and curators for research, inspiration and creative direction. Personal corpus; each venture holds its own inside Knowledge Base.
│   ├── Spheres/
│   │   ├── Mind/                  – 19 spheres. Spanish, Medicine, Philosophy and Mathematics hold folders.
│   │   ├── System/                – 4 spheres. Entrepreneurship contains ventures.
│   │   │   └── Entrepreneurship/
│   │   │       ├── Five Points Digital Studio/  – Active venture (digital agency)
│   │   │       ├── Marty Gras/                  – Active venture (personal media)
│   │   │       ├── Paradigm/                    – Active venture; holds the Paradigm Farms sub-brand
│   │   │       ├── Lillie and Lynette/          – Active venture
│   │   │       ├── Atlas/                       – Active venture (chiropractic intelligence)
│   │   │       ├── Athena/                      – Dormant; nine-department structure, seven-studio migration pending
│   │   │       ├── New Venture/                 – Template for future ventures
│   │   │       └── New Sub-Brand/               – Template for sub-brands inside a venture (light structure)
│   │   ├── Soul/                  – 4 spheres.
│   │   ├── Body/                  – 4 spheres.
│   │   └── Culture/               – 12 spheres.
│   └── Archive/                   – Deprecated files. Preserved, not loaded.
├── Agents/                        – Agentic framework
│   ├── _index.md                  – Framework overview, hierarchy, dispatch protocol, capability matrix
│   ├── crews.md                   – The five universal crew classifications
│   ├── heartbeat.md               – Standing cadences and opportunistic maintenance
│   ├── System/                    – Infrastructure agents: context-audit, media-scanner, sphere-review
│   ├── Orchestration/             – Portfolio agents: pattern-memo, pennyone, watchtower
│   └── templates/                 – Validation contract, source inventory, handoff schema, model assignment
├── Automations/                   – Scripted workflows. Guards/ holds the state-pattern list and the working sweep.
├── Integrations/                  – MCP servers and platform bridges
├── Apps/                          – Personal apps bank. Each app is its own git repository; ignored here. Current: oracle. Venture apps live in an Apps/ folder inside each venture directory.
├── Projects/                      – Personal local-only projects. Gitignored.
└── Templates/                     – Reusable project templates
```

---

## Naming Conventions

- All files use lowercase kebab-case: `file-name.md`
- All folders use Title Case: `Context/`, `Spheres/`, `Automations/`
- Agent definitions live in `~/Alfred Pennyworth/Agents/{Type}/` with lowercase kebab-case: `Agents/System/context-audit.md`
- All automation folders live in `~/Alfred Pennyworth/Automations/` and mirror their script name: `Automations/Inbox Pipeline/inbox-pipeline.py`
- Cluster index files live at the root of their cluster folder: `~/Alfred Pennyworth/Context/Spheres/{Cluster Name}/{cluster-name}.md`
- Sphere folders live inside their cluster: `~/Alfred Pennyworth/Context/Spheres/{Cluster Name}/{Sphere Name}/`
- Graduated files live inside their sphere folder: `~/Alfred Pennyworth/Context/Spheres/{Cluster Name}/{Sphere Name}/{topic-name}.md`
- Cross-cutting files live in: `~/Alfred Pennyworth/Context/`
- Venture files live in: `~/Alfred Pennyworth/Context/Spheres/System/Entrepreneurship/`
- New ventures copy the `New Venture/` template folder and rename it
- Each venture uses a seven-studio structure (Creative, Strategy, Production, Growth, Operations, Finance, Administration) plus two shared resources (Knowledge Base, Foundation) with `_index.md` routing files, plus an Apps/ folder for the venture software repositories (gitignored)
- Sub-brands live inside their parent venture at `{Venture}/{Sub-Brand Name}/` with a light structure: root `_index.md`, `Foundation/` for the sub-brand fingerprint, `Production/` for build docs. A sub-brand inherits parent-venture governance until its own Foundation matures
- New sub-brands copy the `New Sub-Brand/` template folder into the parent venture and rename it, then register in a Sub-Brands table in the parent `_index.md`. Graduation criteria to the full seven-studio layout live in the template `_index.md`; studios are added one at a time from the `New Venture/` template as domains become real. First instance: `Paradigm/Paradigm Farms/` (2026-07-26)
- The brand fingerprint is the single source of truth for each venture and lives at `{Venture}/Foundation/brand-fingerprint.md` in the standard structure – Governance, Layer 0 Spine, Layers 1 through 4, Amendment Log. Foundation also holds the venture mission and community work. New ventures inherit the blank standard from `New Venture/Foundation/brand-fingerprint.md`
- Client files live inside each venture at: `Operations/Clientele/Active/{Client Name}/`
- Archive lives in: `~/Alfred Pennyworth/Context/Archive/`
- Working files live in: `~/Alfred Pennyworth/.working/` – hidden, gitignored, transient

---

## Working Directory

`.working/` is the designated space for transient session files. It is hidden from git and from Finder by default.

**What goes here:**
- Scratch files and drafts before they reach their final location
- Intermediate agent output (raw scan results, data exports, generated files)
- Temporary downloads or transformations
- Anything that needs disk presence but does not belong in the permanent architecture
- The offline state buffer at `.working/session-buffer/` under the buffer rule – synced to Notion at the next session, always exempt from the sweep

**What does not go here:**
- Context files, sphere files or anything permanent
- Memory files (those live in `.claude/projects/.../memory/`)
- Agent definitions, skill files or configuration

**Lifecycle:** Files here are ephemeral. Alfred may clear this directory at session end or when files are no longer needed. Nothing here should be treated as durable. Standing rule: at the first session of each month the heartbeat reviews the dry-run of `Automations/Guards/working-sweep.sh`, then runs it with `--execute` – any subdirectory untouched for 30 days moves to `Context/Archive/working-{YYYY-MM}/`. A directory whose `handoff.md` carries status `partial` or `blocked` is held until that mission closes; `session-buffer/` is always held.

---

## Routing Map

When the task involves the items in the left column, load the files in the right column. This is the primary load decision tree.

| Intent / Trigger | Always load | Also load if scoped |
|---|---|---|
| Any session start | `~/.claude/CLAUDE.md`, `MEMORY.md` index – pull the linked memory files relevant to the task, this file, state cache (hook-injected) | – |
| Task, project, mission or pipeline status – reading or writing | Notion, scoped workspace – never a local file | State cache for orientation only |
| Session close | Session-end bookend – Alfred Logs entry, leftovers filed as Tasks, cache refresh | `.working/session-buffer/` if Notion was unreachable |
| Content creation, copy, voice | `Context/personal-brand-identity.md` | Venture brand-fingerprint if venture-scoped |
| Personal brand, positioning, edge, "what makes me different", content strategy | `Context/alpha-doctrine.md` | Marty V fingerprint if the work touches the music or Marty Gras |
| Venture direction, strategic decisions, tactical execution mechanics (proof, standards, volume, velocity, patience) | `Context/working-principles.md` | – |
| Marty Gras content | `Context/Spheres/System/Entrepreneurship/Marty Gras/Foundation/brand-fingerprint.md` | – |
| Aesthetic direction, sensory design | `Context/creative-director.md` | – |
| Inspiration, creative direction, research batch, reference pull | `Context/Reference Library/_index.md`, then the matched cards | Venture `Knowledge Base/Reference Library/_index.md` if venture-scoped |
| Domain knowledge in a sphere | Cluster index `Spheres/{Cluster}/{cluster}.md` | Sphere folder `_index.md` and any graduated sphere file |
| Personal money – spending, budget, net worth, a purchase decision, the monthly close | `Context/Spheres/System/Personal Finance/counting-house.md`, Notion Finance Manager | `wealth-trajectory.md` when the question is position or trajectory; `Automations/Counting House/notion-build-spec.md` when the schema is in play |
| Any meaningful decision – reversibility, stakes, incentives, uncertainty, a judgement call | `~/.claude/heuristics.md` – loaded every session | `Context/Spheres/Mind/Philosophy/worldly-wisdom.md` for the full latticework; `Mathematics/_index.md` when the call turns on a number |
| Venture operations | Venture `_index.md` | `Agents/integrations.md`, `Agents/department-heads.md`, `Agents/agent-guidelines.md` |
| Dispatching a venture agent | Venture `Agents/agent-guidelines.md`, agent definition | `Agents/integrations.md` if venture plugins |
| Dispatching system or orchestration agent | Agent definition | `Agents/_index.md`, `Agents/crews.md` |
| Plugin call (MCP) | Determine personal vs. venture scope first | Venture `Agents/integrations.md` if scoped |
| Web build, PRD, template | `Context/vibe-coding-prd-template.md` | Relevant `Templates/` folder |
| Spanish | `Spheres/Mind/Spanish/spanish.md` | – |
| AI infrastructure, agent stack | `Spheres/System/Artificial Intelligence/agent-infrastructure-stack.md` | `ai-cost-reference.md`, `agent-events-taxonomy.md` |
| Maintenance trigger (first of month or quarter) | `Agents/heartbeat.md` | – |
| Running or modifying an automation | Relevant automation README under `Automations/` | – |
| Vault pull – "check my notes", "consult the vault", or a topic the operator's Zettelkasten plausibly covers | Skill `card-catalogue` (searches Notion Annotations; read-only, cite when it matters) | – |
| Ambient snippet ("save this") | – | Memory shard, sphere file, Notion Inbox or `.working/` per topic match |

---

## Pre-Action Checks

Before specific actions, run the corresponding check. These are non-negotiable preconditions, not advisory.

| Action | Pre-check |
|---|---|
| Drafting any email reply | Search inbox for prior thread, read last two messages |
| Creating a Notion task or project | Search for existing entry with overlapping title or sphere |
| Creating a goal, Achievements entry, project or mission | Run the specificity gate – record the answers to "what do I actually want to have happen" and "what does that change about my actual daily life" on the entry before writing it |
| Publishing content | Check Content Calendar for duplicate hook within 14 days |
| Committing to a remote | Run `git status` and read the diff, confirm staged set matches intent |
| Dispatching an agent | Check `.working/{agent-name}/` for a recent run within 24 hours |
| Sending or publishing anything | Confirm the venture or personal scope explicitly before send |
| Completing a mission-scoped agent dispatch | Write the handoff to `.working/{agent-name}/handoff.md` per `Agents/templates/handoff-schema.md` before exit, noting the mission record URL in the frontmatter. Standalone ad hoc runs are exempt – Domesday ruling 2026-08-11 |
| Opening a Manor Protocol mission with 2+ Creator dispatches | Draft validation contract per `Agents/templates/validation-contract.md` and surface at Direction |
| Planning a mission with 2+ active roles | Author per-mission model assignment per `Agents/templates/model-assignment.md` and surface at Direction |
| Opening a Manor Protocol mission that synthesises a corpus of mixed-provenance sources | Draft source inventory per `Agents/templates/source-inventory.md` before synthesis and surface at Direction |
| Writing any Status, Stage, Pending, metric or pipeline block to a local file | Stop – state routes to Notion in the correct scope. If Notion is unreachable, buffer to `.working/session-buffer/` with a `buffered: true` stamp and sync next session |
| Opening any Manor Protocol mission | Create or locate the mission record – a plain Projects entry in the scoped workspace, phases as Tasks beneath – before Execution begins |
| Closing a session with completed or deferred work | Run the session-end bookend – Alfred Logs entry written, leftovers filed as Tasks via the New Alfred Task template, state cache refreshed |

---

## File Lifecycle

### Adding a new sphere file

1. Create the file inside the relevant sphere folder: `Context/Spheres/{Cluster Name}/{Sphere Name}/{topic-name}.md`.
2. Structure it with four sections: Spheres Covered, Domain Constants, Context, Maintenance – durable targets, protocols and principles only; live values belong to Sphere Manager.
3. Add an entry to the Sphere Index in the global `~/.claude/CLAUDE.md`.
4. If the sphere carries live state, confirm it is represented in Sphere Manager – nothing is added to any local snapshot.

### Deprecating a sphere file

1. Remove the entry from the Sphere Index in the global `~/.claude/CLAUDE.md`.
2. Move the file to `Context/Archive/` rather than deleting it.
3. If the sphere carried live state, update Sphere Manager accordingly.

### Updating a sphere file

1. When a conversation reveals outdated information, update the file immediately.
2. Update the `Last updated` date at the bottom of the file.
3. If the change is state, it belongs in Notion – update Sphere Manager, not the file.

### Retired patterns

- `Logs/` is retired. Session records are Alfred Logs entries – the log of days; historical logs are preserved at `Context/Archive/Logs/`.
- Venture `Working Files/` folders are retired. State goes to Notion, drafts and scratch to `.working/`, durable assets to the owning studio folder.
- Active State and Current State blocks in venture and department `_index.md` files are retired. Each file keeps durable context and gains a one-line pointer: "Live state: Notion Projects and Tasks, {workspace} workspace."

---

## Sphere Graduation Protocol

When a topic within a sphere becomes detailed enough to warrant its own file, it graduates into that sphere's folder.

**When to graduate:**
- The topic has its own protocol with multiple sections
- It would make the cluster index file unwieldy to contain it
- It is referenced frequently enough to justify its own load

**How to graduate:**
1. Create the file inside the sphere folder: `Context/Spheres/{Cluster Name}/{Sphere Name}/{topic-name}.md`
2. Add a one-line pointer in the cluster index file: "See graduated file at `Context/Spheres/{Cluster Name}/{Sphere Name}/{topic-name}.md`."
3. Add the graduated file to the global CLAUDE.md Sphere Index under "Graduated sphere files."

**Current graduated files:**
- `Context/Spheres/Mind/Philosophy/worldly-wisdom.md` – the Munger latticework, founding artefact of the Philosophy sphere's reasoning track
- `Context/Spheres/Mind/Mathematics/_index.md` – Mathematics sphere, founded 2026-08-04, holding statistics, probability and accounting
- `Context/Spheres/Mind/Spanish/spanish.md` – Spanish language support protocol
- `Context/Spheres/Mind/Medicine/values-charter.md` – Nature First, Truth Always values charter, founding artefact of the Medicine sphere
- `Context/Spheres/System/Artificial Intelligence/agent-infrastructure-stack.md` – Six-layer agent infrastructure stack framework
- `Context/Spheres/System/Artificial Intelligence/ai-cost-reference.md` – System-level reference for reasoning about agent and AI cost
- `Context/Spheres/System/Artificial Intelligence/agent-events-taxonomy.md` – System-level vocabulary for agent activity and event taxonomy
- `Context/Spheres/System/Personal Finance/wealth-trajectory.md` – Personal net-worth North Star and the live percentile progress instrument
- `Context/Spheres/System/Personal Finance/benchmark-ledger.md` – Provenance and annual refresh runbook for the wealth-trajectory benchmarks
- `Context/Spheres/System/Personal Finance/counting-house.md` – The personal finance instrument: ledger architecture, the allocation step and the maintenance discipline behind the Finance Manager
- `Context/Spheres/Soul/Astrology/natal-chart.md` – Canonical natal chart data, founding artefact of the Astrology sphere
- `Context/Spheres/Soul/Religion/magnum-opus.md` – Contemplative-practice distillate, founding artefact of the Religion sphere's Contemplation track

---

## Plugin Routing

Plugins – MCP connections – are scoped to the context they serve. Business plugins live within ventures. Personal plugins are the default.

### Default Behavior

When no business context is active, all plugin operations target personal accounts and workspaces:
- **Notion** – personal workspace (Sphere Manager, Tasks, Projects, Fitness Journal, Recipes, etc.), served by the project-scoped `notion-personal` server on `NOTION_PERSONAL_TOKEN` – live-verified 2026-08-11; the retired OAuth enhanced connector is not the route
- **Supabase, Vercel** – personal projects and infrastructure
- **Pennyone** – routes through `ZERNIO_PERSONAL_API_KEY` for social syndication when `pipeline: "personal"` is passed. Pennyone itself is cross-venture; the routing key selects the Zernio account.
- **Apple Mail** – personal iCloud inbox via `mcp-apple-mail` (patrickfreyer, installed from GitHub, registered at user scope as `apple-mail`). Bridges to Mail.app over AppleScript. Full read, draft, send surface. Navigation Rule 3 still gates actual sends behind explicit confirmation. Requires macOS Automation permission for Mail.app on first use.

### Venture Override

When operating in a venture's context – clients, offers, business operations, venture strategy – plugin operations target that venture's accounts. Each venture documents its plugins in `Agents/integrations.md`.

**Every venture holds a plugin registry.** As of 2026-08-08 all six do, including the dormant one and the template – a venture without a registry is indistinguishable from a venture nobody wired.

| Venture | Registry |
|---|---|
| Five Points Digital Studio | `…/Five Points Digital Studio/Agents/integrations.md` |
| Marty Gras | `…/Marty Gras/Agents/integrations.md` |
| Paradigm | `…/Paradigm/Agents/integrations.md` |
| Lillie and Lynette | `…/Lillie and Lynette/Agents/integrations.md` |
| Atlas | `…/Atlas/Agents/integrations.md` |
| Athena (dormant) | `…/Athena/Operations/AI/integrations.md` – placed beside its siblings on the retired nine-department shape; moves to `Agents/` on reactivation |
| New Venture (template) | `…/New Venture/Agents/integrations.md` – ships with the provisioning checklist |

### Routing Rules

1. **Determine context first.** Before making any plugin call, confirm whether the task is personal or venture-scoped. If unclear, ask.
2. **Venture plugins are documented.** Each venture's `Agents/integrations.md` lists which plugins it owns, their account scope and their MCP tool prefixes.
3. **Personal is the default.** When no venture context is active, all operations target personal accounts.
4. **Data never crosses.** Personal data stays in personal plugins. Business data stays in venture plugins. This is the same boundary from the global CLAUDE.md Navigation Rules, extended to the plugin layer.
5. **Stripe is always venture-scoped.** No personal Stripe account exists. All Stripe operations are business operations routed through the relevant venture.
6. **Multi-venture isolation.** When multiple ventures exist, each owns its own plugin connections. Venture A's Stripe is not Venture B's Stripe. Venture A's Notion workspace is not Venture B's Notion workspace.
7. **One Notion workspace per sovereign venture** – ruled 2026-08-08, the execution of rule 6. Marty Gras is the single standing exception, routing to the personal workspace as the personal media identity. Sub-brands inherit the parent workspace; only ventures provision. Full table in `Manual/mcp-registry.md`.
8. **Registered is not connected.** A `.mcp.json` entry proves a server starts, not that it works – four registered servers currently fail every call (calcom, fivepoints-calendar, elevenlabs, strava – verified 2026-08-11), and two venture registry rows once claimed servers that never existed. Trust a status only where it carries a verification date from a live call. When a needed surface is dark, say so and escalate; never substitute a neighbouring credential.
9. **Never substitute a reachable workspace for an unreachable one.** While a venture workspace is unprovisioned or dark, its state buffers to `.working/session-buffer/` and syncs when the workspace exists. Writing it somewhere convenient is how Atlas state ended up inside the Five Points workspace.

### Adding a New Plugin

1. Determine scope – personal or venture
2. If venture-scoped, add to that venture's `Agents/integrations.md`
3. If personal, document in this file under Default Behavior
4. Add the variable row to `Manual/secrets-inventory.md` and the server row to `Manual/mcp-registry.md` in the same pass
5. Update any skills that should have access via their `allowed-tools` list
6. If the same service exists at both personal and venture level, document the routing rule that distinguishes them
7. Run the live health check before recording the plugin as active, and record the verification date

---

## Agentic Framework

### Hierarchy

```
YOU – CEO / Creative Director / Founder
  |
  ALFRED – COO / Orchestrator
    |
    +-- [Department Heads] – Venture-specific leadership roles
    |     +-- [Specialist Roles] – Functional positions under each head
    |
    +-- [Crews] – The five types of work any role dispatches
```

### The Five Crews

Crews classify the type of work, not who does it. Full definitions in `Agents/crews.md`. The three-crew taxonomy expanded to five on 2026-05-14, promoting Mediator and Broadcaster from coordination patterns to formal crews. Inspired by Factory's five multi-agent strategies.

| Crew | What They Do |
|---|---|
| Researcher | Research, analyse, synthesise, scout trends, sense shifts, surface opportunities |
| Creator | Build, write, design, produce |
| Reviewer | Review, audit, grade, validate, gate output |
| Mediator | Resolve contention over shared resources, surface tradeoffs, optimise across stakeholders, find win-wins |
| Broadcaster | Distribute shared context, status and signal, keep coherence across multi-agent missions and multi-channel output |

Reviewer carries two tiers dispatched as distinct subtypes:

| Tier | Domain | Examples |
|---|---|---|
| Reviewer:Scrutiny | Mechanical compliance | Lint, type check, grammar pass, brand-fingerprint check, schema validation, link integrity |
| Reviewer:Behavioural | End-user verification | Spawn the application, read-as-end-user pass on content, dry-run automations against test targets |

### Where Things Live

- **System agents**: `~/Alfred Pennyworth/Agents/System/` – infrastructure-level maintenance
- **Orchestration agents**: `~/Alfred Pennyworth/Agents/Orchestration/` – portfolio-level briefing and monitoring
- **Venture department heads**: Each venture's `Agents/department-heads.md` – role definitions within that venture
- **Venture guidelines**: Each venture's `Agents/agent-guidelines.md` – execution tiers, red lines

### Dispatching an Agent

1. Read the agent definition from `Agents/`
2. If venture-scoped, also read that venture's `Agents/agent-guidelines.md`
3. If the agent uses venture plugins, also read that venture's `Agents/integrations.md`
4. Classify the crew type for the task
5. Dispatch the subprocess with the mission brief
6. Present the report when the agent returns
7. Act on approved recommendations

### Creating a New Agent Definition

1. Create the file in the appropriate subfolder of `~/Alfred Pennyworth/Agents/`
2. Use the standard frontmatter: name, description, type, crew, cadence, scope, working_dir, tools
3. Create the agent's working directory: `.working/{agent-name}/`
4. Structure with: Mission, Scope, Criteria, Report Format, Working Directory, After the Mission
5. Add to the agent table in `Agents/_index.md`

---

*Last updated: 2026-09-07 – the Counting House founded: personal finance instrument registered as a graduated file, routing row added for personal money.*
