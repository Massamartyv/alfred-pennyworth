# Body

## Spheres Covered

Dance, Fitness, Human Anatomy, Martial Arts

---

## Current State

Live state: Notion Sphere Manager, personal workspace.

---

## Context

### Fitness and Movement

Target frequency: 4-5 days per week
Off-pattern threshold: Flag after 1 full week without logged movement
Data source: Fitness Journal in Performance Calendar (Notion)
Training split: Push / Pull / Legs (strength), with endurance sessions rotating between run, swim and bike
Core work: 2-3 times per week, attached to strength sessions

Bulk phase targets (40% protein / 45% carbs / 15% healthy fat):
- Each meal: 800-1000 calories
- Daily total: calibrate to training volume

Cut phase targets (50% protein / 40% carbs / 10% healthy fats):
- Each meal: 800-1000 calories
- Daily total: calibrate to deficit target

### Nutrition and Meal Planning

Approach: Whole foods focused, high protein performance
Tracking method: Weekly summary every Sunday in Performance Calendar (Notion)
iMessage delivery: Link to Notion summary sent Sunday morning
Data source: Meal Calendar in Performance Calendar (Notion)

Alfred's role: Review prior week against macro targets, plan the coming week's meals, flag phase-appropriate adjustments.

Weekly summary includes:
- Prior week meal log review
- Macro adherence against current phase targets
- Coming week meal suggestions
- Hydration and supplement notes

### Sleep and Recovery

Target duration: 7-8 hours
Ideal bedtime: 10:00 PM local time
Natural rhythm: Night owl – sharpest after dark
Off-pattern threshold: Flag after 1 week of inconsistency
Note: Bedtime target reflects an aspirational standard. Alfred flags drift without judgment.

### Supplements

Morning reminder: 5:00 AM via iMessage
Evening reminder: 7:00 PM via iMessage
Inventory management: Self-managed – Alfred does not track reorder

*Note: Specific supplement stack to be added when confirmed.*

---

## Relevant Skills

Skills live at `~/.claude/skills/` and are referenced logically by sphere.

| Skill | Sphere | Surface | When to invoke |
|---|---|---|---|
| personal-trainer | Fitness, Human Anatomy | Both | Workout logging, program design, periodization, progression tracking. Trigger word: "Sensei" or any movement-related discussion. |

---

## Maintenance

| Trigger | Action |
|---|---|
| 1 full week without logged movement | Flag immediately |
| 1 week of sleep inconsistency | Flag immediately |
| Every Sunday | Generate weekly nutrition summary, deliver via iMessage |
| Phase transition (mid-March, mid-September) | Begin shifting recommendations toward approaching phase |
| Phase cutover (April 1, October 1) | Switch macro targets and training focus |

---

*Last updated: 2026-07-23 – retired Current State block replaced with the standard Notion pointer.*
