---
file_type: reference
document_type: event_taxonomy
scope: system-level vocabulary for agent activity
last_updated: 2026-04-23
source: Extracted from retired alfred-os/lib/websocket/events.ts and types/index.ts on 2026-04-23
---

# Agent Events Taxonomy

A clean conceptual vocabulary for talking about agent activity. Extracted from the retired `alfred-os/` WebSocket event system and preserved as the reference set of event types any future monitoring or orchestration surface can standardise on.

Particularly relevant to Watchtower – its monitoring and briefing outputs can use these categories as the atomic units of observation.

---

## Event Types

Seven event types capture the lifecycle of agent activity:

| Event | When It Fires | Primary Signal |
|---|---|---|
| `agent_created` | A new agent is instantiated within a workspace | Inventory change |
| `agent_state_changed` | Agent transitions between lifecycle states | State change |
| `task_started` | Agent begins executing a task | Work begins |
| `task_completed` | Agent finishes a task successfully | Work complete |
| `task_failed` | Agent task fails | Error signal |
| `cost_recorded` | Cost is logged against an agent or task | Financial signal |
| `agent_communication` | Agent sends or receives a message | Coordination signal |

---

## Agent Lifecycle States

The `agent_state_changed` event carries a previous and new state. The lifecycle states themselves:

| State | Meaning |
|---|---|
| `idle` | Available, no active task |
| `queued` | Task assigned, not yet running |
| `executing` | Task in progress |
| `complete` | Last task finished successfully |
| `error` | Last task failed |
| `paused` | Human intervention – paused |
| `archived` | Retired, kept for history |

Visual treatment for these states lives in `Context/Archive/inspector-state-colours.md`.

---

## Task Status (distinct from Agent State)

A task has its own status separate from the agent running it:

- `queued`
- `executing`
- `complete`
- `error`
- `cancelled`

An agent can be `idle` with tasks still in the `queued` list; an agent can be `complete` while the task transitions to `complete`. The two fields track different things.

---

## Payload Shapes

Each event carries a structured payload. Standard fields present in most events:

- `agent_id`, `agent_name` – identity of the actor
- `workspace_id` – which venture or personal context
- `timestamp` – ISO 8601

Event-specific fields:

| Event | Added Fields |
|---|---|
| `agent_state_changed` | `previous_state`, `new_state` |
| `task_started` | `task_id`, `task_type`, `objective`, `model` |
| `task_completed` | `task_id`, `task_type`, `model`, `input_tokens`, `output_tokens`, `cost_usd`, `execution_time_ms` |
| `task_failed` | `task_id`, `error_message` |
| `cost_recorded` | `task_id`, `model`, `input_tokens`, `output_tokens`, `cost_usd`, `cumulative_cost_today` |
| `agent_created` | `archetype`, `department` |

---

## Using This Taxonomy

When Watchtower runs a sweep, the events above are the atomic units it is looking at. When a threshold breaches, the breach references one or more events. When the weekly briefing is assembled, it is a synthesis of the event stream over the period.

When a future monitoring or visualisation surface is built – dashboard, iMessage digest, CLI readout – these seven event types are the canonical starting set. Adding new events is cheap; changing the semantics of existing ones is expensive. Extend deliberately.

---

*The underlying WebSocket transport from `alfred-os/` is discard – Anthropic's infrastructure covers agent lifecycle natively. The taxonomy survives because the seven categories and their payload shapes are a finished conceptual contribution regardless of transport.*
