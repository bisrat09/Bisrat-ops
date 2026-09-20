# Brief for Mike: Jev (TypeSafe) shadow mode, three asks

From: James, 2026-09-20
Context: reports/jev-typesafe-plan-2026-09-20.md (the plan) and reports/jev-phase0-2026-09-20.md (benchmark results)

Bisrat approved Jev and shadow mode is live as of tonight. Jev scores every story next to Haiku. Haiku still decides. In two weeks I run a comparison and we decide whether Jev takes over scoring.

Jev is a decision model, not a chat model. It answers typed questions (yes/no probability, pick one option, rate against ordered levels) and reads the question text literally. So the quality of its answers is the quality of the rubric text. That is your domain. Three asks, in priority order.

---

## Ask 1: Draw the AI-story boundary (one paragraph, needed first)

Phase 0 found that 70 of 150 stories Haiku passed are not AI stories: a Game Boy music player, the UN map, a snacks brand, rugs, human-hair toothpaste, iPhone cases. That is the rubric drift Bisrat flagged. Jev's gate catches them. It needs your sign-off on the edges.

Current gate text, verbatim from scripts/jev_scoring.py:

> Question: Is artificial intelligence, machine learning, robotics, or automation the main subject of the article, not a passing mention?
>
> Yes means: The story is about an AI system, a robot, an automated system, or the people and companies building or using one. Remove the AI or robot and there is no story.
>
> No means: AI or robots are absent, or mentioned only in passing. The story would stand without them. Examples: a video game release, a historical car, zoo animals, a hardware discount.

Edge cases Jev scored below 0.5 on that Habesha AI has posted or nearly posted before. Tell me which side of the line each belongs on:

- Semiconductor and data centre stories with no model or product in them (Odisha semiconductor hub, a data centre investment)
- Electric vehicles and self-driving when the story is about the company, not the autonomy
- Biotech and medicine where AI is one tool among several (the age-reversal geneticist scored 0.02)
- Space (NASA moon crater is in pending-research right now)
- Big tech product events where AI is a feature, not the point (Apple fall event scored 0.13)
- The developing-world series: does a story about Nigeria or India need AI in it, or does technology-as-equalizer count

Write it as one paragraph of prose in the same shape as the text above: what counts, what does not, with two or three concrete examples on each side. I paste it in.

## Ask 2: Review the brand_fit levels (the one test where Jev and Haiku disagree most)

Jev scores brand_fit 1.2 points lower than Haiku on average and fails funding rounds, product launches, and corporate announcements that Haiku passed at 6.0 to 7.1: the GPT-6 rollout, a data centre investment, a fintech launching an agent, a TechCrunch stage lineup. Jev is reading "corporate PR" literally, which is what the rubric says.

Current five levels, worst to best, verbatim:

1. Off brand. Fear mongering, pure corporate PR, a product advertisement or sale, or divisive politics. "AI will destroy humanity says expert", a discount on SSDs.
2. Misaligned. Too corporate, too negative, or too political. A stock price drops after an AI announcement, a political fight over AI regulation.
3. Neutral tech news that could work with the right angle. A company releases a new model and here is what it can do.
4. Good fit. An honest, balanced take on AI's real impact. AI creates two million jobs while eliminating 1.5 million.
5. Perfectly on brand. Hopeful and human centered and shows AI making life better, or genuinely fun and cool. AI prosthetics let amputees feel again, a 15 year old builds AI to help deaf students.

Questions:

- Should a major model launch (GPT-6, a new Claude, Gemini) sit at level 3 or level 4? Right now it lands at 2 to 3 because the text says corporate.
- Does a big funding round or investment ever deserve level 3 or above, or is that always PR?
- Since the "lead with wonder, not fear" rule (2026-04-29) and "no defensive framing": should level 1 say explicitly that a story framed around AI taking jobs is off brand even when factual? Right now Jev only sees "fear mongering".
- Named CEOs plus consensus is the winning pattern on YouTube (reel #42). Should that be written into level 5 so the scorer rewards it?

Rewrite the five levels if you want. Rules: each level is one concrete situation with an example, no vibes, no "somewhat", no negations of another level. Jev cannot infer what you meant.

## Ask 3: Hypothesis questions for engagement feature discovery (Phase 4, no rush)

We have 103 posted stories with views, likes, and saves per platform. Jev can answer yes/no questions over all of them for under a cent. If you give me 10 to 15 hypotheses about what makes a Habesha AI post travel, I run them and return a table: feature, share of posts with it, mean views and saves with versus without, per platform. Then the winner pattern we cite in pitches is measured, not eyeballed.

Format: one yes/no question per line, phrased so a literal reader answers it from the caption and script alone. Examples to seed you:

- Does the post name a specific CEO or founder?
- Do two or more named leaders agree on the same claim?
- Does the post contain a dollar figure or a percentage?
- Is the story set outside the US and Europe?
- Is the product something a viewer could use today?
- Does the post open with a question?
- Does the post make a health or medical claim?

Sample size is 103. Treat results as direction, not proof.

---

## What you do not need to do

- Nothing on the other six tests yet. They correlate 0.6 to 0.8 with Haiku and their offsets are stable. If Phase 1 shows a specific test misbehaving I will come back with that one.
- Nothing on captions, scripts, or the editorial lints (Phase 3). Those come after shadow mode.
- Nothing on the API. Bisrat holds the key, I hold the code.

Send Ask 1 first. It is one paragraph and it changes what the pipeline flags starting the next morning.
