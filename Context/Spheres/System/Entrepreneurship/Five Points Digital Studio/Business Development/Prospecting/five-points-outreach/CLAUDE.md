# Five Points — Network Activation Pipeline

Research and drafting system for converting Marty's LinkedIn network into
Five Points Digital Studio clients via a Priestley free-value model.

## The one rule that governs everything

**This agent never sends anything.** It researches, drafts, and queues.
Marty reads, edits, and sends by hand.

This is not timidity. It is the architecture:

1. Automated DMs from a personal account get that account restricted.
   Instagram and LinkedIn both detect programmatic messaging.
2. The entire strategy rests on messages that do not feel like outreach.
   A human sending 15 considered messages beats a bot sending 100.
3. Marty's judgment on whether a message is right is the quality gate.
   Remove it and the system optimises for volume, which is the failure
   mode this whole approach exists to avoid.

If asked to send, post, or connect automatically: decline, and say why.

## The strategy in one paragraph

68 qualified principals out of 932 connections. Four cohorts. The free
value is a diagnostic scorecard — the Owner Dependency Index for
healthcare, adapted per cohort. The opening move does not offer help; it
asks the recipient to help build the diagnostic. That inverts the
transaction and is the reason this reads as organic rather than as a
pitch. Read `reference/cohort-briefs.md` before drafting anything.

## Daily target

15 messages per day, researched and drafted, sent by hand.
Not 100. See `reference/channel-rules.md` for why.

## Layout

    data/prospects.csv      the 68, with cohort and status
    data/state.json         counters, daily cap, last run
    queue/<slug>/           research.md + draft.md per prospect
    reference/              voice, channels, cohort briefs
    .claude/skills/         how to research, draft, manage the queue
    .claude/commands/       /research-next /draft-next /queue-status
                            /log-send /log-reply

## Status values

    cold        not yet researched
    researched  research.md written, no draft
    drafted     draft.md written, awaiting Marty
    approved    Marty approved, not yet sent
    sent        sent by hand, date logged
    replied     they responded
    booked      call in the diary
    passed      not a fit, with a reason
    hold        do not contact, with a reason

## Working order

    /queue-status      what is where
    /research-next 5   research the next five
    /draft-next 5      draft for researched prospects
    (Marty reviews, edits, sends)
    /log-send <slug>   record it went out
    /log-reply <slug>  record what came back
