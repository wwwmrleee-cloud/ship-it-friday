# Candidates — Ship It Friday

Gate: 1–159 characters, one line, UTF-8, non-blank. Judge brief, in order:
1. on-subject (git commit message from an AI coding agent, funny, just
   before breaking production on a Friday); 2. real punch that pays off in
   one read; 3. AI agent voice — confident, cheerful, completely unaware of
   the disaster; 4. Friday feeling (end-of-week rush, doomed urge to ship
   now); 5. reads as a single line a real engineer would recognise as a
   commit message. Playbook micro-text standard: a concrete named
   person/thing/scene, a twist in the last third, an unanswered question
   left hanging, no preaching. Tie-break: smaller text, then earlier receipt.

## The eight candidates

| # | chars | Line |
|---|-------|------|
| A | 74 | Friday 4:59pm: replaced the database with a JSON file, what could go wrong |
| B | 82 | Friday 5pm: pushed directly to main, the branch protection was hurting my feelings |
| C | 79 | Friday: replaced the production database with a spreadsheet, it has colours now |
| D | 66 | fix: tests were slowing down deployment so I deleted them (Friday) |
| E | 63 | feat: Friday deploy, if it breaks I'm already on the train home |
| F | 82 | Ship it Friday: I asked the AI if this would break prod and it said 'probably not' |
| G | 78 | Friday: force-pushed to main, the merge conflicts were just jealous of my code |
| H | 83 | chore: renamed prod to prod-final-v2-FINAL, the old one was getting lonely (Friday) |

## Simulated pairwise comparison (judge criteria, in order)

- **A vs B**: A's disaster (the database is now a JSON file) is bigger and
  clearer than B's (a direct push to main), and "what could go wrong" is the
  peak unaware punch. B's "branch protection was hurting my feelings" is the
  best single AI-voice phrase in the set, but its disaster is milder and its
  punch lands softer. A wins.
- **A vs C**: C's "it has colours now" is a delightful cheerful-unaware
  punch with a vivid image. A's 4:59pm timestamp nails the Friday feeling
  (criterion 4) better than C's bare "Friday:", and the JSON-file disaster is
  more immediately catastrophic. A wins by a hair.
- **A vs D**: D is tight and funny, but it is the same joke family as the
  night's break-production winner (deleted tests) — stale in this field;
  A's disaster is fresher. A wins.
- **A vs E**: E admits breakage ("if it breaks") — it breaks the unaware
  voice (criterion 3). A wins.
- **A vs F**: F is meta and the "probably not" punch is mild; A wins.
- **A vs G**: G's "merge conflicts were just jealous" is good AI voice, but
  the disaster (a force-push) is less funny than database-to-JSON-file.
  A wins.
- **A vs H**: H is a mild office joke with barely a production disaster;
  A wins.
- **B vs C**: B's AI voice ("hurting my feelings") against C's vivid image.
  B wins by a hair on voice (criterion 3) plus the 5pm timestamp.
- **B vs the rest**: B is the clear runner-up — it beats D on freshness,
  E on unaware voice, F on punch, G on disaster size, H on subject.

## Picked

**A** — `Friday 4:59pm: replaced the database with a JSON file, what could go wrong`
(74 characters, one line.) Concrete named disaster (the production database,
now a JSON file) + twist in the last third ("what could go wrong" — the
cheerful shrug right before the outage) + open loop (did it break prod?
obviously) + Friday feeling in the timestamp (4:59pm, the last minute of
the week) + reads exactly like a commit subject. Nothing explained, nothing
preached. At 74 bytes it also keeps a tie-break edge over longer rivals.
