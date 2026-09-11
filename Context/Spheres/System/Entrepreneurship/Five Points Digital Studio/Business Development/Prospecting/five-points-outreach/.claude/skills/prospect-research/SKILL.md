---
name: prospect-research
description: Research a prospect's business across LinkedIn, Instagram and the open web, and produce an evidence-based brief naming three problems Five Points can address. Use when researching anyone in data/prospects.csv.
---

# Prospect research

Produce `queue/<slug>/research.md`. One prospect per run. Twelve minutes
of work, not two hours.

## The honesty rule — this is the important part

Every claim in the brief is tagged. No exceptions.

    [OBSERVED]  You saw it. Quote it or cite the URL.
    [INFERRED]  You reasoned to it. State the reasoning.
    [UNKNOWN]   You could not determine it. Say so.

An empty field marked `[UNKNOWN]` is worth more than a confident guess.
The guess ends up in a message, the message reaches a business owner who
knows their own business, and the credibility is gone in one line.

Never estimate anyone's personal income, net worth or salary. Company
revenue only when a source states it, cited. Sector benchmarks are
allowed and must be labelled as benchmarks.

## Sources, in order

1. **LinkedIn profile** — current role, tenure, headcount, recent posts.
   Recent posts are the highest-value source in the whole process. What
   someone posted last month tells you what they are thinking about.
2. **Company website** — services, locations, team size, booking flow.
   Try to book an appointment as a patient or customer would. How many
   clicks? Is there a form? Does anything confirm? This is direct
   observation of the exact problem Five Points solves.
3. **Instagram** — post cadence, who runs the account, whether DMs are
   open, whether they answer comments. Cadence that collapsed six months
   ago is a signal about capacity.
4. **Google Business / reviews** — read the one and two-star reviews
   specifically. Operational complaints live there: no callback, waited
   forty minutes, could not reach anyone. That is your evidence.

Stop at four sources or twelve minutes, whichever comes first.

## Output format

    # <Name> — <Company>
    slug: <slug>
    cohort: <A|B|C|D|E>
    channel: <linkedin|instagram|both>
    researched: <date>

    ## Business
    [OBSERVED] What they do, where, how big.
    [UNKNOWN]  What you could not establish.

    ## Signals
    Recent posts, cadence changes, hiring, expansion, anything dated.

    ## The three problems

    ### 1. <Short name>
    Evidence: [OBSERVED] ...
    Why it costs them: ...
    What Five Points does about it: ...
    Confidence: high | medium | low

    ### 2. ...
    ### 3. ...

    ## The hook
    The one specific, true, non-obvious thing to open with. Must be
    something only someone who actually looked would know.

    ## Do not mention
    Anything sensitive, personal, or that would reveal uncomfortably
    close reading. Health, family, politics, anything from a personal
    account. If the hook came from their personal life, discard it.

## Hard limits

- Public professional information only.
- Never contact anyone in the target's orbit for information.
- Anything that would make the recipient feel surveilled rather than
  noticed is a failure, however impressive the research.
- If a prospect has no observable problems, mark them `passed` with the
  reason. A thin brief padded out is worse than no brief.
