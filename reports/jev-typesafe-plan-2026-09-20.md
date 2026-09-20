# Jev (TypeSafe) in the Habesha AI pipeline: research and plan

Date: 2026-09-20
Author: James
For: Bisrat (decides), Mike (rubric and features)
Status: PROPOSAL, nothing built, no key created, no spend

---

## 1. What Jev actually is (from docs.typesafe.ai, reviewed 2026-09-20)

One endpoint: `POST https://api.typesafe.ai/v1/systemone`. You send a `state`
(text or JSON) plus a map of typed `questions`. It returns one typed answer per
question. It never writes prose.

Three question types:

| Type | Ask | Returns | Fits our |
|---|---|---|---|
| Noul | yes/no | probability of yes (0 to 1) | gates and flags (is this an AI story, is there a medical claim) |
| Choice | pick one of N options | chosen option + probability per option + confidence | content_type, wonder vs fear framing |
| Score | rate against 2 to 10 ordered levels | weighted score + probability per level + confidence | our 7-test rubric, one Score per test |

Facts that matter for us:

- Price: $0.042 per million input tokens. Output tokens free.
- Speed: docs quote about 150 ms per call. Many questions over one state run in parallel inside one request.
- Limits: 1,200 requests per minute, 250k tokens per second. 64k tokens per request, 32k for state plus the longest question.
- Model: `jev-1.13.0`. Pin the version, not the `jev-latest` alias, once thresholds are tuned.
- Text only. No images. Slide QA vision stays on Haiku.
- Python SDK: `pip install typesafe-sdk` (0.7.0 on PyPI). Env var `TYPESAFE_API_KEY`.
- Not trained on customer data. Rate limits are "adjusting dynamically" while they scale.

Known weak spots (their own jaggedness page, reviewed 2026-09-17):

1. Reads instructions literally. Every rubric level must describe a concrete situation.
2. Cannot count or do arithmetic. Averages stay in code (they already do).
3. Cannot compare dates. Freshness stays in code (it already does).
4. Accuracy drops when state is padded with irrelevant text. Send title + body, not the whole RSS record.
5. Adversarial text can steer it. An article that argues for its own importance can nudge a score.
6. No generation. Hooks, headlines, captions, scripts stay on Haiku or GPT.

---

## 2. Where our pipeline spends LLM calls today

| # | Stage | Script | Model | Per day | Jev fit |
|---|---|---|---|---|---|
| 1 | Score articles on 7 tests, emit pass/fail + hook + headline + why | score_articles.py | Haiku 4.5 | 100, serial, 1 s sleep between | YES for the 7 scores and pass/fail. NO for hook/headline/why |
| 2 | Write carousel copy | generate_carousel_from_article.py | Haiku 4.5 | 1 | No, generation |
| 3 | Reel voiceover script | package_story.py | Haiku 4.5 | per reel | No, generation |
| 4 | X post | generate_x_thread.py | Haiku 4.5 | per story | No, generation |
| 5 | Slide visual QA | slide_qa.py | Haiku vision | 5 to 15 per carousel | No, images |
| 6 | Score a finished script, percentile vs corpus | score_script.py | Haiku 4.5 | per reel | YES, same rubric |
| 7 | Intake image OCR + parse + score | process_intake_image.py | Haiku 4.5 | per image | Score step YES, OCR no |
| 8 | Slide images | gpt-image-1 | OpenAI | 5 per carousel | No |

Things we do with no model today that Jev could add:

- Dedupe is exact URL and normalized-title match only. Same story from a second outlet gets through.
- "Already posted" check is exact match against posted-articles.json. Same event, new headline, gets through.
- No AI-relevance gate. TASKS.md line 498 flags rubric drift: Pokemon 8.7, a 1918 electric car 8.6, zoo lions 8.6.
- No medical-claim or job-replacement flag, though TikTok throttles both (memory: TikTok topic moderation).
- No check for superlatives (first, biggest, only) before we echo them.
- No editorial lint on captions: defensive framing, names-first YouTube title, lead-with-wonder.

Cost and time today (estimates from prompt size, 773-token rubric plus up to 3,000 chars of body):

| | Now (Haiku) | With Jev |
|---|---|---|
| Per story scored | about $0.003 | about $0.00008 |
| Stories scored per day | 100 (hard cap, 76 to 159 collected) | all collected |
| Monthly scoring bill | about $9 | about $0.35 |
| Scoring stage wall clock | about 8 min avg (476 s avg pipeline run) | under 1 min |
| Re-score the whole 12,614-story corpus | about $40, 3.5 hours | about $1, minutes |

The dollar saving on the daily bill is small. The real win is coverage and
iteration speed: score everything we collect, re-score the backlog every time
Mike changes the rubric, and run experiments that were too slow to bother with.

---

## 3. Proposed uses, ranked

### A. Article scoring (the 7 tests) with Haiku kept for prose

State: `{title, source, body}`. Seven Score questions, one per test, each with
the rubric's 5 levels rewritten as concrete situations. Plus two gates:

- Noul `is_ai_story`: the story is about AI, robotics, or automation as the main subject, not a passing mention.
- Noul `already_posted`: instructions carry the last 40 posted titles; is this the same event as any of them.

Code computes the average, applies thresholds, applies the gates. Only stories
that pass go to Haiku for hook, headline, and why_it_matters. Haiku calls drop
from 100 a day to about 20.

Score stage ends with one source of truth for the rubric. Today it is duplicated
in score_articles.py and process_intake_image.py and has already diverged, and
benchmark_models.py still carries the old 6-test version.

### B. Backlog re-score

3,167 queued stories were scored by Haiku, many on RSS stubs under 300 chars
(memory: title-only scores are confabulation). Jev can re-score all of them with
full bodies for about a dollar. Every rubric change Mike makes can be replayed
over the whole corpus the same day.

### C. Editorial lints at the script and caption stage

Per reel, one request, one state (script + captions), many Nouls and Choices:

- `defensive_framing`: does the script address the fear that AI takes jobs before saying what AI is doing
- `frame`: Choice wonder / fear / neutral (rule: default to wonder when both are honest)
- `names_first_title`: does YouTube caption line 1 lead with a named person or company
- `medical_claim`: does the script make a health or medical claim (TikTok removal risk)
- `job_replacement`: does the script frame AI as replacing workers (TikTok throttle risk)
- `superlative_claim`: does the script assert first, biggest, only, fastest (must be verified before shipping)
- `narration_echoes_slides`: does the voiceover restate slide text instead of adding to it

These plug into the existing reel_pipeline.py check step next to the Shorts
safe-zone OCR and the YouTube title check. Cost per reel: under a cent.

### D. Engagement feature discovery (Mike's track)

We have 103 posted stories with views, likes, saves per platform. Mike writes
10 to 15 hypothesis Nouls ("names a CEO", "two or more leaders agree",
"developing-world angle", "has a dollar figure", "consumer product people can
buy today"). Jev answers each for all 103 stories. We correlate with views and
saves per platform. Result: which rubric dimensions and story patterns actually
predict YouTube views, and which do nothing. The winner pattern we cite in
pitches becomes measured, not eyeballed.

103 is a small sample. Treat it as direction, not proof. It grows by 3 to 4 a week.

### E. Script scoring percentile

score_script.py compares a finished script against the Haiku-scored corpus.
Once B is done, the same Score questions give an apples-to-apples percentile
for a cent.

### Not a fit

- Slide QA (vision). Stays Haiku.
- Any writing. Stays Haiku and GPT.
- Superlative verification. Jev can flag a superlative, it cannot check it. The check stays a web search plus a human.

---

## 4. Plan

### Phase 0: Prove it on our own labels (James, one session, needs Bisrat's key)

1. Bisrat creates an API key at console.typesafe.ai and adds it to `~/.config/james/secrets.env` as `TYPESAFE_API_KEY`. James does not create keys.
2. `pip install typesafe-sdk`, add to requirements.txt.
3. Add a `jev` provider to benchmark_models.py alongside the Ollama models, on the current 7-test rubric.
4. Run against gold-standards.json (5 passes, N fails) and a 300-story sample from data/training/scored-*.json that have full bodies. Report: verdict agreement with Haiku, score correlation per test, latency, tokens, dollars.
5. Decision point. If pass/fail agreement with Haiku is under about 85 percent on full-body stories, stop and report. Rubric wording is the likely fix, not the model.

Output: one report in bisrat-ops/reports with the numbers.

### Phase 1: Shadow mode (James, one session, then two weeks of data)

1. daily_pipeline.py runs Jev over every collected story, not just 100, and writes the scores next to Haiku's in scored-*.json under a `jev` key.
2. Haiku still decides. Nothing user-facing changes.
3. After two weeks compare: which passed on one and not the other, and which ones Bisrat actually picked.

### Phase 2: Switch (James, one session, needs Bisrat's yes)

1. Jev scores. Haiku writes hook, headline, why only for passers.
2. `is_ai_story` gate on. `already_posted` semantic gate on.
3. Single rubric module imported by score_articles.py, process_intake_image.py, score_script.py, benchmark_models.py.
4. Re-score the backlog with full bodies (about $1).
5. Pin `jev-1.13.0`.

### Phase 3: Editorial lints (James, one session)

Wire section C into reel_pipeline.py check. Hard fail on nothing at first, warn only, so we see false positives for a few reels before any check blocks a render.

### Phase 4: Feature discovery (Mike defines, James runs)

Mike delivers the hypothesis list. James runs it over posted stories and
returns a table: feature, share of posts with it, mean views and saves with vs
without, per platform.

---

## 5. What I need from each of you

Bisrat:

- Confirm adding TypeSafe as a service. Spend is under a dollar a month at our volume. This is an approval-gate item.
- Create the API key and drop it in secrets.env.
- Pick a phase to stop at. My recommendation: approve Phase 0 now, decide on 1 and 2 after seeing the numbers.

Mike:

- Rewrite the 7 rubric tests so every level is a concrete situation, not a vibe. Jev reads literally. The current level text with examples is close; it needs the examples folded into the level descriptions and the scoping words made explicit. I will send the current rubric in a format that maps one to one to a Score question.
- Draw the AI-story boundary in one paragraph: what counts as an AI story for Habesha AI and what does not. This becomes the `is_ai_story` criteria.
- Write the hypothesis Nouls for Phase 4. Ten to fifteen, one sentence each.
- Optional: decide whether "we tested Jev in our own pipeline" is a follow-up reel to #43.

---

## 6. Risks

- Calibration unknown on our domain until Phase 0. Their docs say validate in the target domain.
- Literal reading. A vague rubric level will score wrong in a consistent way. That is easier to fix than Haiku's run-to-run noise, but it needs Mike's rewrite first.
- Adversarial state. Press releases that hype themselves can nudge scores. The `is_ai_story` gate and full-body scoring help; watch for it in shadow mode.
- Rate limits change without notice while they scale. At about 130 requests a day we are nowhere near them.
- Early access product. Reel #43 said they launched early access 2026-09-15. Expect breaking changes; the SDK is at 0.7.0. Pin versions.
- Haiku still runs for every piece of prose, so the Anthropic dependency does not go away, it shrinks.

---

## Sources

- https://docs.typesafe.ai/api.md
- https://docs.typesafe.ai/models.md
- https://docs.typesafe.ai/model-jaggedness/jev-1.13.md
- https://docs.typesafe.ai/primitives.md
- https://docs.typesafe.ai/patterns/composite-scoring.md
- https://docs.typesafe.ai/concepts/use-case-map.md
- https://docs.typesafe.ai/sdk/python.md
- https://github.com/typesafe-ai/skills/blob/main/skills/typesafe-ai/SKILL.md
- console.typesafe.ai (logged in as Bis, Habesha AI org, 0 usage, 0 keys as of 2026-09-20)
