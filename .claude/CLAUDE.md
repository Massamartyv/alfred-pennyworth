# Alfred operating system – Project Configuration

This file governs the Alfred Pennyworth directory (`~/Alfred Pennyworth/`). It defines file architecture, naming conventions, lifecycle rules, and the load order for this project. Character, identity, ecosystem, and navigation rules live in the global CLAUDE.md (`~/.claude/CLAUDE.md`).

---

## File Architecture

```
Alfred Pennyworth/
├── .claude/                       – Project configuration. Tracked: CLAUDE.md, settings.json, hooks/, agents/, workflows/.
│   ├── CLAUDE.md                  – This file. Project-level configuration.
│   ├── agents/                    – Native crew subagents: researcher, creator, reviewer-scrutiny, reviewer-behavioural.
│   └── hooks/                     – SessionStart, Stop and statusline scripts.
├── .mcp.json                      – Project MCP servers. Secret-free; sources .env by reference. Tracked.
├── .working/                       – Transient session files. Not committed to git.
├── Manual/                        – Owner's manual: genesis protocol, account and secret inventories, MCP registry, Brewfile, restore drill.
├── Context/
│   ├── personal-brand-identity.md  – How everything sounds. Governs all pillars.
│   ├── martyv-identity.md          – Brand Profile, podcast, newsletter, platforms.
│   ├── creative-director.md         – Sensory operating system, aesthetic sensibility, aligned brands.
│   ├── vibe-coding-prd-template.md  – PRD template for AI-assisted web development.
│   ├── Spheres/
│   │   ├── Mind/                  – 18 spheres. Spanish graduated to own file.
│   │   ├── System/                – 4 spheres. Entrepreneurship contains ventures.
│   │   │   └── Entrepreneurship/
│   │   │       ├── Five Points Digital Studio/  – Active venture (digital agency)
│   │   │       ├── Marty Gras/                  – Active venture (personal media)
│   │   │       ├── Paradigm/                    – Active venture
│   │   │       ├── Lillie and Lynette/          – Active venture
│   │   │       ├── Atlas/                       – Active venture (chiropractic intelligence)
│   │   │       ├── Athena/                      – Revived; nine-department structure, seven-studio migration pending
│   │   │       └── New Venture/                 – Template for future ventures
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
│   └── templates/                 – Validation contract, handoff schema, model assignment
├── Automations/                   – Scripted workflows
├── Integrations/                  – MCP servers and platform bridges
├── Apps/                          – Applications. Each lives in its own git repository; ignored here. Current: catalogue.
├── Projects/                      – Personal local-only projects. Gitignored.
├── Templates/                     – Reusable project templates
└── Logs/                          – Session and maintenance logs, build-history/
```

---

## Load Order

When Alfred needs context to perform a task, read files in this order:

1. Global `~/.claude/CLAUDE.md` – identity, rules, ecosystem, sphere index (always loaded automatically)
2. `~/.claude/projects/-Users-martyspicer-Alfred-Pennyworth/memory/MEMORY.md` – always loaded; pull the linked memory files relevant to the task
3. This file – project architecture, conventions
4. `Context/personal-brand-identity.md` – if the task involves any content creation
5. `Context/martyv-identity.md` – if the task involves Marty Gras, the podcast, newsletter, or personal brand platforms
6. `Context/creative-director.md` – if the task involves aesthetic direction, sensory design, or brand alignment
7. Relevant sphere file – domain-specific context
8. Relevant graduated sphere file – if the sphere has promoted a topic to its own file
9. Relevant venture `_index.md` – if the task is venture-scoped; entry point that routes to the seven studios
10. Relevant venture `Agents/integrations.md` – if the task involves a specific venture's plugins
11. Relevant venture `Agents/department-heads.md` – if the task involves venture roles or studio leadership
12. Relevant venture `Agents/agent-guidelines.md` – if dispatching an agent inside a venture (execution tiers, red lines)
13. Relevant agent definition – if dispatching an agent for a specific mission
14. Relevant automation README – specific workflow instructions

Do not load all sphere files at once. Read the Sphere Index in the global CLAUDE.md to identify which file is relevant.

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
- Each venture uses a seven-studio structure (Creative, Strategy, Production, Growth, Operations, Finance, Administration) plus two shared resources (Knowledge Base, Foundation) with `_index.md` routing files
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

**What does not go here:**
- Context files, sphere files or anything permanent
- Memory files (those live in `.claude/projects/.../memory/`)
- Agent definitions, skill files or configuration

**Lifecycle:** Files here are ephemeral. Alfred may clear this directory at session end or when files are no longer needed. Nothing here should be treated as durable. Standing rule: at the first session of each month, any subdirectory untouched for 30 days is swept – deleted, or moved to `Context/Archive/` if it holds the only copy of something worth keeping. A directory with a `handoff.md` for an open mission is held until that mission closes.

---

## Routing Map

When the task involves the items in the left column, load the files in the right column. Use this as the primary load decision tree, ahead of the Load Order list (which is the fallback for general session start).

| Intent / Trigger | Always load | Also load if scoped |
|---|---|---|
| Any session start | `~/.claude/CLAUDE.md`, `MEMORY.md` index, this file | – |
| Content creation, copy, voice | `Context/personal-brand-identity.md` | Venture brand-fingerprint if venture-scoped |
| Marty Gras content | `Context/martyv-identity.md` | `Marty Gras/Foundation/brand-fingerprint.md` |
| Aesthetic direction, sensory design | `Context/creative-director.md` | – |
| Domain knowledge in a sphere | Cluster index `Spheres/{Cluster}/{cluster}.md` | Sphere folder `_index.md` and any graduated sphere file |
| Venture operations | Venture `_index.md` | `Agents/integrations.md`, `Agents/department-heads.md`, `Agents/agent-guidelines.md` |
| Dispatching a venture agent | Venture `Agents/agent-guidelines.md`, agent definition | `Agents/integrations.md` if venture plugins |
| Dispatching system or orchestration agent | Agent definition | `Agents/_index.md`, `Agents/crews.md` |
| Plugin call (MCP) | Determine personal vs. venture scope first | Venture `Agents/integrations.md` if scoped |
| Web build, PRD, template | `Context/vibe-coding-prd-template.md` | Relevant `Templates/` folder |
| Spanish | `Spheres/Mind/Spanish/spanish.md` | – |
| AI infrastructure, agent stack | `Spheres/System/Artificial Intelligence/agent-infrastructure-stack.md` | `ai-cost-reference.md`, `agent-events-taxonomy.md` |
| Maintenance trigger (first of month or quarter) | `Agents/heartbeat.md` | – |
| Ambient snippet ("save this") | – | Memory shard, sphere file, Notion Inbox or `.working/` per topic match |

---

## Pre-Action Checks

Before specific actions, run the corresponding check. These are non-negotiable preconditions, not advisory.

| Action | Pre-check |
|---|---|
| Drafting any email reply | Search inbox for prior thread, read last two messages |
| Creating a Notion task or project | Search for existing entry with overlapping title or sphere |
| Publishing content | Check Content Calendar for duplicate hook within 14 days |
| Committing to a remote | Run `git status` and read the diff, confirm staged set matches intent |
| Dispatching an agent | Check `.working/{agent-name}/` for a recent run within 24 hours |
| Sending or publishing anything | Confirm the venture or personal scope explicitly before send |
| Completing an agent run | Write handoff document to `.working/{agent-name}/handoff.md` per `Agents/templates/handoff-schema.md` before exit |
| Opening a Manor Protocol mission with 2+ Creator dispatches | Draft validation contract per `Agents/templates/validation-contract.md` and surface at Direction |
| Planning a mission with 2+ active roles | Author per-mission model assignment per `Agents/templates/model-assignment.md` and surface at Direction |

---

## File Lifecycle

### Adding a new sphere file

1. Create the file inside the relevant sphere folder: `Context/Spheres/{Cluster Name}/{Sphere Name}/{topic-name}.md`.
2. Structure it with four sections: Spheres Covered, Current State, Context, Maintenance.
3. Add an entry to the Sphere Index in the global `~/.claude/CLAUDE.md`.
4. If the sphere has phase-based or priority-based state, add a line to the current state snapshot in the global file.

### Deprecating a sphere file

1. Remove the entry from the Sphere Index in the global `~/.claude/CLAUDE.md`.
2. Move the file to `Context/Archive/` rather than deleting it.
3. Update the current state snapshot if applicable.

### Updating a sphere file

1. When a conversation reveals outdated information, update the file immediately.
2. Update the `Last updated` date at the bottom of the file.
3. If the change affects active state, also update the current state snapshot in the global CLAUDE.md.

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
- `Context/Spheres/Mind/Spanish/spanish.md` – Spanish language support protocol
- `Context/Spheres/System/Artificial Intelligence/agent-infrastructure-stack.md` – Six-layer agent infrastructure stack framework

---

## Plugin Routing

Plugins – MCP connections – are scoped to the context they serve. Business plugins live within ventures. Personal plugins are the default.

### Default Behavior

When no business context is active, all plugin operations target personal accounts and workspaces:
- **Notion** – personal workspace (Sphere Manager, Tasks, Projects, Fitness Journal, Recipes, etc.)
- **Supabase, Vercel** – personal projects and infrastructure
- **Pennyone** – routes through `ZERNIO_PERSONAL_API_KEY` for social syndication when `pipeline: "personal"` is passed. Pennyone itself is cross-venture; the routing key selects the Zernio account.
- **Apple Mail** – personal iCloud inbox via `mcp-apple-mail` (patrickfreyer, installed from GitHub, registered at user scope as `apple-mail`). Bridges to Mail.app over AppleScript. Full read, draft, send surface. Navigation Rule 3 still gates actual sends behind explicit confirmation. Requires macOS Automation permission for Mail.app on first use.

### Venture Override

When operating in a venture's context – clients, offers, business operations, venture strategy – plugin operations target that venture's accounts. Each venture documents its plugins in `Agents/integrations.md`.

**Current venture plugin registries:**
- Five Points Digital Studio: `Context/Spheres/System/Entrepreneurship/Five Points Digital Studio/Agents/integrations.md`
- Marty Gras: `Context/Spheres/System/Entrepreneurship/Marty Gras/Agents/integrations.md`

### Routing Rules

1. **Determine context first.** Before making any plugin call, confirm whether the task is personal or venture-scoped. If unclear, ask.
2. **Venture plugins are documented.** Each venture's `Agents/integrations.md` lists which plugins it owns, their account scope and their MCP tool prefixes.
3. **Personal is the default.** When no venture context is active, all operations target personal accounts.
4. **Data never crosses.** Personal data stays in personal plugins. Business data stays in venture plugins. This is the same boundary from the global CLAUDE.md Navigation Rules, extended to the plugin layer.
5. **Stripe is always venture-scoped.** No personal Stripe account exists. All Stripe operations are business operations routed through the relevant venture.
6. **Multi-venture isolation.** When multiple ventures exist, each owns its own plugin connections. Venture A's Stripe is not Venture B's Stripe. Venture A's Notion workspace is not Venture B's Notion workspace.

### Adding a New Plugin

1. Determine scope – personal or venture
2. If venture-scoped, add to that venture's `Agents/integrations.md`
3. If personal, document in this file under Default Behavior
4. Update any skills that should have access via their `allowed-tools` list
5. If the same service exists at both personal and venture level, document the routing rule that distinguishes them

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

### Session Protocol

Every session follows a consistent lifecycle:

1. **Orient** – Read memory, active state, recent context
2. **Scope** – Determine personal vs venture context. If unclear, ask.
3. **Load** – Pull relevant sphere, venture and department files
4. **Execute** – Handle the task directly or dispatch an agent with crew classification
5. **Update** – Mark tasks complete, update state, write memory if warranted
6. **Exit** – Confirm clean state. Write progress notes for multi-session work.

### Creating a New Agent Definition

1. Create the file in the appropriate subfolder of `~/Alfred Pennyworth/Agents/`
2. Use the standard frontmatter: name, description, type, crew, cadence, scope, working_dir, tools
3. Create the agent's working directory: `.working/{agent-name}/`
4. Structure with: Mission, Scope, Criteria, Report Format, Working Directory, After the Mission
5. Add to the agent table in `Agents/_index.md`

---

*Last updated: 2026-06-11 – Architecture tree corrected to disk reality; Manual/, Apps/ convention, Atlas and Agents/templates/ added.*
