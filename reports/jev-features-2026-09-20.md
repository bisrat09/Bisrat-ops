# Jev engagement feature discovery, 2026-09-20

Mike's 16 hypotheses as yes/no questions, answered by Jev over every posted story, split at 0.5, compared on views and saves per platform. Sample is small. Read direction and consistency across platforms, not any single number.

## Coverage

| | Count |
|---|---|
| posted stories | 103 |
| with a caption | 76 |
| with a ready-to-post folder | 34 |
| with any engagement | 42 |
| with instagram views | 35 |
| with tiktok views | 26 |
| with youtube views | 13 |
| with facebook views | 35 |
| with only the aggregate block | 5 |

## Summary: median views with vs without each feature

Ratio is median views with the feature divided by median views without. Above 1 means posts with the feature did better. Cells are blank when fewer than 3 posts on a side.

| Feature | Share yes | instagram | tiktok | youtube | facebook | all |
|---|---|---|---|---|---|---|
| names_major_ai_ceo | 13% | 1.56 (7/28) | 1.63 (7/19) | 2.88 (4/9) | 5.04 (7/28) | 1.77 (7/32) |
| rivals_agree | 2% |  |  |  |  |  |
| ai_first | 8% | 1.57 (5/30) | 0.90 (4/22) |  | 4.39 (5/30) | 1.86 (6/33) |
| named_ordinary_person | 6% |  |  |  |  |  |
| global_south | 6% |  |  |  |  |  |
| dollar_figure_central | 19% | 1.04 (8/27) | 1.19 (7/19) | 0.53 (3/10) | 0.30 (8/27) | 1.16 (8/31) |
| usable_today | 21% | 1.50 (4/31) | 0.62 (3/23) |  | 4.17 (4/31) | 1.04 (6/33) |
| harm_with_action | 8% | 1.08 (4/31) | 0.59 (4/22) |  | 0.34 (4/31) | 0.94 (4/35) |
| job_replacement | 8% | 0.83 (5/30) | 0.69 (4/22) |  | 0.17 (5/30) | 1.17 (5/34) |
| medical_claim | 11% | 0.59 (4/31) |  |  | 0.19 (4/31) | 0.54 (5/34) |
| ai_discovery | 2% |  |  |  |  |  |
| caption_leads_with_outcome | 63% | 0.84 (16/19) | 1.89 (10/16) | 5.12 (4/9) | 1.26 (16/19) | 0.68 (19/20) |
| government_actor | 10% |  |  |  |  |  |
| company_money | 8% | 0.83 (3/32) | 1.63 (3/23) |  | 0.26 (3/32) | 1.17 (3/36) |
| autonomous_agents | 4% |  |  |  |  |  |
| opens_with_question | 6% |  |  |  |  |  |


## Reading (James, 2026-09-20)

Sample is thin: 42 posts have any engagement, 35 on Instagram and Facebook, 26 on TikTok, 13 on YouTube. Most features are true for under 10 posts. Only patterns that point the same way on every platform deserve weight.

**Holds up across all four platforms**

- Naming a major AI CEO or founder (7 posts): median views 1.6x on Instagram, 1.6x on TikTok, 2.9x on YouTube, 5x on Facebook. This is the one feature with a consistent lift everywhere. It is the "named CEOs plus consensus" pattern from the 09-16 engagement report, now measured.
- Medical claims (4 to 5 posts): median views 0.6x on Instagram, 0.2x on Facebook, 0.5x overall. Down everywhere it can be measured. Consistent with the TikTok removal history.

**Points one way on two or more platforms**

- A central dollar figure (8 posts): flat on Instagram and TikTok, 0.5x on YouTube, 0.3x on Facebook. Money numbers as the hook do not travel.
- Job-replacement framing (5 posts): 0.8x Instagram, 0.7x TikTok, 0.2x Facebook. Consistent with the no-defensive-framing rule.
- Company money as the main event (3 posts): 0.3x on Facebook, 0.8x Instagram, but 1.6x TikTok. Too few posts to call.
- An AI doing something no AI had done (5 to 6 posts): 1.6x Instagram, 4.4x Facebook, 0.9x TikTok.

**Mixed, needs more data**

- Caption leads with the outcome (16 of 35 on Instagram): 0.8x Instagram, 1.9x TikTok, 5x YouTube, 1.3x Facebook. Splits by platform. Instagram may reward the setup, short-video platforms the payoff. Worth watching as the sample grows.

**Cannot be measured yet** (fewer than 3 posts with the feature on any platform): rivals agreeing, a named ordinary person, developing world, government actor, autonomous agents, AI discovery, opens with a question. The rivals-agree feature is true for two posts, one of which is Dario Is Right at 916 YouTube views. That is a single data point, not a pattern.

**Two cautions.** Instagram "views" are reach on older posts where video views were not logged. And 61 of 103 posts have no engagement data at all, mostly March to May carousels. If those numbers exist in Publer they would double the sample.

**What this means for pitches.** Cite the named-CEO lift with the platform numbers. Flag medical claims and dollar-figure hooks as measured drags. Everything else is a hypothesis still.

Re-run cost: 101k tokens, half a cent. This can run after every batch of engagement imports: `python3 scripts/jev_features.py`.

## Detail per platform

### instagram

| Feature | n with / without | Views median with / without | Views mean with / without | Saves mean with / without | Spearman(prob, views) |
|---|---|---|---|---|---|
| names_major_ai_ceo | 7 / 28 | 192 / 123 | 181 / 150 | 0.14 / 0.14 | 0.22 |
| rivals_agree | 1 / 34 | 192 / 123 | 192 / 156 | 0 / 0.15 | 0.42 |
| ai_first | 5 / 30 | 190 / 121 | 246 / 142 | 0 / 0.17 | 0.14 |
| named_ordinary_person | 2 / 33 | 142 / 123 | 142 / 157 | 0 / 0.15 | -0.15 |
| global_south | 2 / 33 | 68 / 137 | 68 / 162 | 0 / 0.15 | -0.17 |
| dollar_figure_central | 8 / 27 | 128 / 123 | 146 / 160 | 0 / 0.19 | -0.1 |
| usable_today | 4 / 31 | 184 / 123 | 174 / 154 | 0.25 / 0.13 | -0.03 |
| harm_with_action | 4 / 31 | 132 / 123 | 146 / 158 | 0 / 0.16 | 0.17 |
| job_replacement | 5 / 30 | 108 / 130 | 135 / 160 | 0 / 0.17 | 0.08 |
| medical_claim | 4 / 31 | 82 / 137 | 94 / 164 | 0 / 0.16 | -0.28 |
| ai_discovery | 2 / 33 | 204 / 123 | 204 / 154 | 0 / 0.15 | 0.09 |
| caption_leads_with_outcome | 16 / 19 | 116 / 137 | 152 / 160 | 0.06 / 0.21 | -0.23 |
| government_actor | 1 / 34 | 97 / 130 | 97 / 158 | 0 / 0.15 | -0.16 |
| company_money | 3 / 32 | 108 / 130 | 139 / 158 | 0 / 0.16 | -0.06 |
| autonomous_agents | 1 / 34 | 101 / 130 | 101 / 158 | 0 / 0.15 | 0.16 |
| opens_with_question | 0 / 35 |  / 123 |  / 156 |  / 0.14 | -0.13 |

### tiktok

| Feature | n with / without | Views median with / without | Views mean with / without | Saves mean with / without | Spearman(prob, views) |
|---|---|---|---|---|---|
| names_major_ai_ceo | 7 / 19 | 263 / 161 | 249 / 495 |  /  | 0.25 |
| rivals_agree | 1 / 25 | 321 / 168 | 321 / 433 |  /  | 0.44 |
| ai_first | 4 / 22 | 157 / 174 | 174 / 475 |  /  | -0.06 |
| named_ordinary_person | 2 / 24 | 108 / 186 | 108 / 455 |  /  | -0.17 |
| global_south | 2 / 24 | 101 / 186 | 101 / 456 |  /  | -0.07 |
| dollar_figure_central | 7 / 19 | 192 / 161 | 223 / 504 |  /  | 0.04 |
| usable_today | 3 / 23 | 113 / 181 | 137 / 467 |  /  | -0.36 |
| harm_with_action | 4 / 22 | 129 / 220 | 142 / 481 |  /  | -0.11 |
| job_replacement | 4 / 22 | 147 / 214 | 146 / 480 |  /  | -0.15 |
| medical_claim | 2 / 24 | 810 / 164 | 810 / 397 |  /  | -0.01 |
| ai_discovery | 2 / 24 | 283 / 164 | 283 / 441 |  /  | 0.47 |
| caption_leads_with_outcome | 10 / 16 | 264 / 140 | 346 / 480 |  /  | 0.45 |
| government_actor | 0 / 26 |  / 174 |  / 429 |  /  | 0.07 |
| company_money | 3 / 23 | 263 / 161 | 284 / 447 |  /  | -0.04 |
| autonomous_agents | 1 / 25 | 122 / 181 | 122 / 441 |  /  | -0.1 |
| opens_with_question | 0 / 26 |  / 174 |  / 429 |  /  | -0.05 |

### youtube

| Feature | n with / without | Views median with / without | Views mean with / without | Saves mean with / without | Spearman(prob, views) |
|---|---|---|---|---|---|
| names_major_ai_ceo | 4 / 9 | 12 / 4 | 236 / 18 |  /  | 0.3 |
| rivals_agree | 1 / 12 | 916 / 5.0 | 916 / 16 |  /  | 0.09 |
| ai_first | 2 / 11 | 18 / 4 | 18 / 97 |  /  | 0.1 |
| named_ordinary_person | 2 / 11 | 54 / 6 | 54 / 91 |  /  | 0.1 |
| global_south | 1 / 12 | 105 / 5.0 | 105 / 84 |  /  | 0.26 |
| dollar_figure_central | 3 / 10 | 4 / 7.5 | 37 / 100 |  /  | 0.21 |
| usable_today | 1 / 12 | 17 / 5.0 | 17 / 91 |  /  | 0.06 |
| harm_with_action | 2 / 11 | 3.0 / 9 | 3 / 100 |  /  | 0.15 |
| job_replacement | 2 / 11 | 61 / 4 | 61 / 90 |  /  | 0.34 |
| medical_claim | 0 / 13 |  / 6 |  / 85 |  /  | 0.23 |
| ai_discovery | 1 / 12 | 3 / 7.5 | 3 / 92 |  /  | -0.53 |
| caption_leads_with_outcome | 4 / 9 | 20 / 4 | 240 / 16 |  /  | 0.12 |
| government_actor | 0 / 13 |  / 6 |  / 85 |  /  | 0.44 |
| company_money | 0 / 13 |  / 6 |  / 85 |  /  | 0.4 |
| autonomous_agents | 1 / 12 | 19 / 5.0 | 19 / 91 |  /  | 0.08 |
| opens_with_question | 0 / 13 |  / 6 |  / 85 |  /  | -0.44 |

### facebook

| Feature | n with / without | Views median with / without | Views mean with / without | Saves mean with / without | Spearman(prob, views) |
|---|---|---|---|---|---|
| names_major_ai_ceo | 7 / 28 | 204 / 40 | 134 / 83 |  /  | 0.12 |
| rivals_agree | 1 / 34 | 221 / 40 | 221 / 90 |  /  | 0.19 |
| ai_first | 5 / 30 | 145 / 33 | 146 / 85 |  /  | -0.04 |
| named_ordinary_person | 2 / 33 | 86 / 39 | 86 / 94 |  /  | -0.03 |
| global_south | 2 / 33 | 82 / 39 | 82 / 94 |  /  | 0.19 |
| dollar_figure_central | 8 / 27 | 27 / 90 | 67 / 101 |  /  | -0.12 |
| usable_today | 4 / 31 | 162 / 39 | 137 / 88 |  /  | -0.13 |
| harm_with_action | 4 / 31 | 18 / 52 | 43 / 100 |  /  | 0.06 |
| job_replacement | 5 / 30 | 12 / 71 | 55 / 100 |  /  | -0.1 |
| medical_claim | 4 / 31 | 10 / 52 | 30 / 102 |  /  | -0.4 |
| ai_discovery | 2 / 33 | 156 / 39 | 156 / 90 |  /  | -0.12 |
| caption_leads_with_outcome | 16 / 19 | 53 / 42 | 94 / 93 |  /  | 0.01 |
| government_actor | 1 / 34 | 10 / 47 | 10 / 96 |  /  | -0.17 |
| company_money | 3 / 32 | 12 / 47 | 97 / 93 |  /  | -0.13 |
| autonomous_agents | 1 / 34 | 145 / 40 | 145 / 92 |  /  | -0.09 |
| opens_with_question | 0 / 35 |  / 42 |  / 94 |  /  | -0.0 |

### all

| Feature | n with / without | Views median with / without | Views mean with / without | Saves mean with / without | Spearman(prob, views) |
|---|---|---|---|---|---|
| names_major_ai_ceo | 7 / 32 | 413 / 234 | 380 / 262 | 0.14 / 0.13 | 0.44 |
| rivals_agree | 1 / 38 | 413 / 258 | 413 / 280 | 0 / 0.14 | 0.31 |
| ai_first | 6 / 33 | 410 / 221 | 362 / 269 | 0 / 0.16 | 0.25 |
| named_ordinary_person | 2 / 37 | 228 / 270 | 228 / 286 | 0 / 0.14 | -0.11 |
| global_south | 2 / 37 | 150 / 270 | 150 / 290 | 0 / 0.14 | 0.21 |
| dollar_figure_central | 8 / 31 | 286 / 246 | 283 / 283 | 0 / 0.17 | 0.03 |
| usable_today | 6 / 33 | 280 / 270 | 243 / 290 | 0.17 / 0.12 | -0.02 |
| harm_with_action | 4 / 35 | 252 / 270 | 255 / 286 | 0 / 0.15 | 0.22 |
| job_replacement | 5 / 34 | 301 / 258 | 270 / 285 | 0 / 0.15 | 0.22 |
| medical_claim | 5 / 34 | 150 / 278 | 274 / 284 | 0 / 0.15 | -0.16 |
| ai_discovery | 2 / 37 | 360 / 246 | 360 / 279 | 0 / 0.14 | 0.26 |
| caption_leads_with_outcome | 19 / 20 | 190 / 278 | 276 / 290 | 0.06 / 0.2 | 0.04 |
| government_actor | 2 / 37 | 54 / 270 | 54 / 296 | 0 / 0.14 | -0.16 |
| company_money | 3 / 36 | 301 / 258 | 354 / 277 | 0 / 0.14 | 0.11 |
| autonomous_agents | 1 / 38 | 246 / 270 | 246 / 284 | 0 / 0.14 | 0.32 |
| opens_with_question | 1 / 38 | 11 / 270 | 11 / 290 | 0 / 0.14 | -0.01 |

## Feature flags per post

| Post | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 | 13 | 14 | 15 | 16 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| EP #40 No More Waiting on Heart Transplants? w/ Dr | . | . | . | . | . | . | . | . | . | Y | . | Y | . | . | . | Y |
| Jury rules against Meta and YouTube in social medi | . | . | . | . | . | Y | Y | . | . | . | . | Y | . | . | . | . |
| I was paid to write fake Google reviews – then my  | . | . | . | . | . | . | . | . | . | . | . | Y | . | . | . | . |
| Campaigners welcome Meta and YouTube's defeat in l | . | . | . | . | . | Y | . | . | . | . | . | Y | . | . | . | . |
| Number of AI chatbots ignoring human instructions  | . | . | . | . | . | . | Y | Y | . | . | . | Y | . | . | Y | . |
| How AI Is Helping Solve Extinction w/ Ben Lamm | E | Y | . | . | . | . | . | . | . | . | . | . | . | . | . | . | Y |
| EP#42 What It’s Really Like to Live in Space w/ An | . | . | . | . | . | Y | . | . | . | . | . | . | . | . | . | . |
| EP #26 Amber Straughn’s AMA: Are Wormholes Real? w | . | . | . | . | . | . | . | . | . | . | . | Y | . | . | . | Y |
| EP #17 David Sinclair’s AMA: Age Reversal Breakthr | . | . | . | . | . | . | . | . | . | Y | . | Y | . | . | . | . |
| EP #2 I Almost Killed Stephen Hawking (True Story  | . | . | . | . | . | . | . | . | . | . | . | Y | . | . | . | . |
| A woman’s uterus has been kept alive outside the b | . | . | . | . | . | . | . | . | . | Y | . | Y | . | . | . | . |
| OpenAI $1B to Cure Diseases | . | . | . | . | . | Y | . | . | . | . | . | Y | . | Y | . | . |
| Indian AI Helps 300,000 Farmers | . | . | . | . | Y | . | Y | . | . | . | . | Y | . | . | . | . |
| AI & GPT-4 Revolutionize Education w/ Sal Khan | . | . | . | . | . | . | Y | . | . | . | . | . | . | . | . | . |
| Meta Shuts Down VR Comedy Club | . | . | . | . | . | . | Y | . | . | . | . | Y | . | . | . | . |
| OpenAI Sora Made Fake Videos of Dead People | . | . | . | . | . | Y | . | Y | . | . | . | Y | . | . | . | . |
| The snow gods: How a couple of ski bums built the  | . | . | . | . | . | . | Y | . | . | . | . | Y | . | . | . | . |
| We Know You Can Pay a Million by Anja Shortland re | . | . | . | . | . | Y | . | . | . | . | . | Y | . | . | . | . |
| 14-Year-Old Parineeti Drops Out of School to Build | . | . | . | Y | Y | . | . | . | . | . | . | . | . | . | . | . |
| Does your business English let you down? Turn it i | . | . | . | . | . | . | Y | . | . | . | . | . | . | . | . | Y |
| The Download: brainless human clones and the first | . | . | . | . | . | . | . | . | . | Y | . | Y | . | Y | . | . |
| Tech Life | . | . | . | . | . | . | . | . | . | . | . | Y | . | . | . | Y |
| AI Doesn't Reduce Work — It Intensifies It (Harvar | . | . | . | . | . | . | . | . | . | . | . | Y | . | . | . | . |
| Man Uses ChatGPT to Design Cancer Vaccine for His  | . | . | . | Y | . | . | . | . | . | Y | . | . | . | . | . | . |
| 15-Year-Old AI Founder Hires 38-Year-Old as First  | . | . | . | Y | . | . | . | . | . | . | . | Y | . | . | . | . |
| Artemis II crew is just like us, needs help with M | . | . | . | . | . | . | Y | . | . | . | . | Y | . | . | . | . |
| The gig workers who are training humanoid robots a | . | . | . | Y | Y | . | . | . | . | . | . | Y | . | . | . | . |
| World’s oldest tortoise caught in viral crypto dea | . | . | . | . | . | . | . | . | . | . | . | Y | . | . | . | . |
| From Rocket Lab to Cow Lab: The $2B AI Collar Stor | Y | . | . | . | . | Y | Y | . | . | . | . | Y | . | Y | . | . |
| NASA did eventually solve Artemis II&#8217;s Outlo | . | . | . | . | . | . | Y | . | . | . | . | Y | Y | . | . | . |
| Microsoft says Copilot is 'for entertainment purpo | . | . | . | . | . | . | Y | Y | . | . | . | Y | . | . | . | . |
| Frontier Labs Intelligence Sharing — OpenAI/Anthro | . | . | . | . | . | . | . | . | . | . | . | Y | . | . | . | . |
| First photos of solar eclipse from Artemis II crew | . | . | . | . | . | . | . | . | . | . | . | Y | . | . | . | . |
| Claude Mythos: Anthropic built the most powerful A | . | . | . | . | . | . | . | . | . | . | . | Y | . | . | . | . |
| AI Singer Eddie Dalton Holds 11 iTunes Top 100 Slo | . | . | Y | . | . | . | . | . | . | . | . | Y | . | . | . | . |
| NASA shares incredible photos from the far side of | . | . | . | . | . | . | . | . | . | . | . | Y | Y | . | . | . |
| South Korea Robo-Grandma Dolls (Hyodol) Fight Elde | . | . | . | . | . | . | Y | . | . | Y | . | . | Y | . | . | . |
| Artemis II astronaut puts all of our iPhone moon p | . | . | . | . | . | . | Y | . | . | . | . | Y | Y | . | . | . |
| Artemis II Astronaut Takes iPhone Moon Photo That  | . | . | . | . | . | . | Y | . | . | . | . | Y | . | . | . | . |
| Honda CEO: We Have No Chance Against This | . | . | . | . | . | . | . | . | Y | . | . | . | . | . | . | . |
| NASA's Artemis II crew just flew farther away from | . | . | . | . | . | . | . | . | . | . | . | Y | Y | . | . | . |
| This $100 AI Device is Revolutionizing Breast Canc | . | . | . | . | Y | Y | Y | . | . | Y | . | Y | . | . | . | . |
| China's One-Person Company AI Boom | . | . | . | . | . | Y | . | . | Y | . | . | Y | Y | . | . | . |
| I used Gmail's AI tool to do hours of work for me  | . | . | . | . | . | . | Y | . | . | . | . | . | . | . | . | . |
| Cancer Vanished After One Injection | . | . | . | . | . | . | . | . | . | Y | . | Y | . | . | . | . |
| Nasa’s Artemis crew snaps historic Earthset photo  | . | . | . | . | . | . | . | . | . | . | . | . | Y | . | . | . |
| How the Netherlands Feeds the World | . | . | . | . | . | . | . | . | . | . | . | . | . | . | . | . |
| Meet the Swiss founder building robots that make c | . | . | . | . | . | . | . | . | . | . | . | . | . | . | . | . |
| Humanoid Robot Race: China vs USA | . | . | . | . | . | . | . | . | . | . | . | . | . | . | . | . |
| The FAA is encouraging gamers to get jobs in air t | . | . | . | . | . | Y | . | . | . | . | . | Y | Y | . | . | . |
| One-Person AI Conglomerates | Y | . | . | . | . | Y | . | . | Y | . | . | Y | . | Y | . | . |
|  | . | . | . | . | . | . | . | . | . | . | . | . | . | . | . | . |
| The Artemis II mission has started its 10-day jour | . | . | . | . | . | . | . | . | . | . | . | . | . | . | . | . |
| This Beanie Is Designed to Read Your Thoughts | . | . | . | . | . | . | . | . | . | . | . | Y | . | . | . | . |
| Dubai Just Built the World's First Flying Taxi Sta | . | . | . | . | . | . | . | . | . | . | . | Y | . | . | . | . |
| Artemis II commander shares a remarkable video of  | . | . | . | . | . | . | . | . | . | . | . | Y | . | . | . | . |
| A woman’s uterus has been kept alive outside the b | . | . | . | . | . | . | . | . | . | Y | . | Y | . | . | . | . |
| A woman’s uterus has been kept alive outside the b | . | . | . | . | . | . | . | . | . | Y | . | Y | . | . | . | . |
| Meta offered Mira Murati $1 billion. She said no.  | Y | . | . | . | . | Y | . | . | . | . | . | . | . | Y | . | . |
| AI Just Beat a Pro Athlete and Dropped Your Grocer | . | . | Y | . | . | Y | Y | Y | Y | . | . | Y | . | . | . | . |
| Meet Emma, The Care Home Robot Who Called Every Re | . | . | . | . | . | . | . | Y | . | . | . | . | . | . | . | . |
| 'Prosthetics aren't made for people like us': the  | . | . | . | . | Y | . | Y | . | . | . | . | Y | . | . | . | . |
| In Japan, the robot isn’t coming for your job; it’ | . | . | . | . | . | . | . | . | . | . | . | . | . | . | . | . |
| AI just read a scroll buried by Vesuvius for 2,000 | . | . | Y | . | . | . | . | . | . | . | Y | Y | . | . | . | . |
| Tesla Optimus: Inside the Plan for Millions of Rob | Y | . | . | . | . | . | . | . | . | . | . | . | . | . | . | . |
| Researchers say we’re talking less than ever | . | . | . | . | . | . | . | . | . | . | . | Y | . | . | . | . |
| Only 24 humans have ever watched Earth set behind  | . | . | . | . | . | . | . | . | . | . | . | Y | . | . | . | . |
| Most people think AI remembers everything you say. | . | . | . | . | . | . | Y | . | . | . | . | . | . | . | . | . |
| A robot named Lightning just outran us all | . | . | . | . | . | . | . | . | . | . | . | Y | . | . | . | . |
| This week, AI beat a professional athlete and brok | . | . | Y | . | . | . | . | . | . | . | . | Y | . | . | . | . |
| The cure for your disease might already exist | . | . | . | . | . | . | . | . | . | Y | . | Y | . | . | . | . |
| Some robots are having a really rough week | . | . | . | . | . | . | . | . | . | . | . | . | . | . | . | . |
| $25 million approved. The faces on the call weren' | . | . | . | . | . | Y | . | . | . | . | . | Y | . | Y | . | . |
| Meta's $56B quarter and Zuckerberg's superintellig | Y | . | . | . | . | Y | . | . | . | . | . | . | . | Y | . | . |
| OpenAI accidentally trained their AI to see goblin | . | . | . | . | . | . | . | Y | . | . | . | Y | . | . | . | . |
| The Lottery Ticket Hypothesis: a 7-year-old paper  | . | . | . | . | . | . | . | . | . | . | . | . | . | . | . | . |
| Google Photos can now dress you from clothes you a | . | . | . | . | . | . | . | . | . | . | . | . | . | . | . | . |
| A toilet company just became one of the biggest wi | . | . | . | . | . | . | . | . | . | . | . | . | . | Y | . | . |
| Anthropic taught AI to dream. Literally. | . | . | . | . | . | . | . | . | . | . | . | Y | . | . | . | . |
| A cafe in Stockholm hired an AI as manager. She or | . | . | . | . | . | . | . | . | Y | . | . | . | . | . | Y | . |
| Anthropic + SpaceX: The Colossus Deal | Y | Y | . | . | . | . | . | . | . | . | . | . | . | . | . | . |
| Codex Earned $16.88 Autonomously | . | . | . | . | . | Y | Y | . | . | . | . | Y | . | . | Y | . |
| UK AI Security Institute: AI Capability Doubling E | . | . | . | . | . | . | . | . | . | . | . | Y | Y | . | . | . |
| Albania Appoints World's First AI Government Minis | . | . | Y | . | . | . | . | . | . | . | . | Y | Y | . | . | . |
| Mira Murati Left OpenAI, Went Silent for a Year, a | . | . | . | . | . | . | . | . | . | . | . | . | . | . | . | . |
| Demis Hassabis at Google I/O: AGI Is the Destinati | Y | . | . | . | . | . | . | . | . | . | . | . | . | . | . | . |
| The CEO of Google's AI Lab Says AGI Could Arrive b | Y | . | . | . | . | . | . | . | . | . | . | Y | . | . | . | . |
| 2026-05-30-sam-change-of-mind | Y | . | . | . | . | . | . | . | Y | . | . | Y | . | . | . | . |
| AI Can Now Clone Itself | . | . | Y | . | . | . | Y | . | . | . | . | Y | . | . | . | . |
| 2026-06-04-internet-traffic | . | . | . | . | . | . | . | . | . | . | . | Y | . | . | . | . |
| 100 AI Models Predicted the 2026 World Cup Winner | . | . | . | . | . | . | . | . | . | . | . | . | . | . | . | . |
| Claude Opus 5: One Sentence Built a Working Video  | Y | . | Y | . | . | . | Y | . | Y | . | . | . | . | . | . | . |
| The Free AI Almost Nobody Can Run: Kimi K3 | . | . | . | . | . | . | . | . | . | . | . | Y | . | . | . | . |
| The AI Adoption Gap: 88% Say They Use AI, 1 in 5 A | . | . | . | . | . | . | . | . | . | . | . | . | . | . | . | . |
| Google's Two Most Senior AI Leaders Both Stepped B | Y | . | . | . | . | . | . | . | . | . | . | Y | . | . | . | . |
| Life May Have Begun Twice | . | . | . | . | . | . | . | . | . | . | . | . | . | . | . | . |
| An AI Just Advanced One of Math's Hardest Unsolved | . | . | . | . | . | Y | . | . | . | . | Y | . | . | . | . | . |
| A Farmer Trusted AI for a Year. Then One Answer Ki | . | . | . | Y | . | Y | . | Y | . | . | . | . | . | . | . | . |
| The Photo That Robs You | . | . | . | . | . | . | . | Y | . | . | . | . | . | . | . | . |
| The Civilization That Built Itself | . | . | Y | . | . | . | . | . | . | . | . | Y | . | . | Y | . |
| The Ghostwriters | . | . | . | Y | Y | Y | . | . | Y | . | . | . | . | . | . | . |
| Dario Is Right | Y | Y | . | . | . | . | . | . | . | . | . | Y | . | . | . | . |
| The AI That Can't Talk | . | . | . | . | . | Y | . | . | . | . | . | . | . | . | . | Y |

Columns: 1 names_major_ai_ceo; 2 rivals_agree; 3 ai_first; 4 named_ordinary_person; 5 global_south; 6 dollar_figure_central; 7 usable_today; 8 harm_with_action; 9 job_replacement; 10 medical_claim; 11 ai_discovery; 12 caption_leads_with_outcome; 13 government_actor; 14 company_money; 15 autonomous_agents; 16 opens_with_question

## Questions as asked

- names_major_ai_ceo: The story names a CEO or founder of a major AI company.
- rivals_agree: More than one named public figure who are usually rivals take the same public position.
- ai_first: The main event is an AI system doing something no AI had done before.
- named_ordinary_person: The story names a specific non-famous person whose life was directly changed by AI.
- global_south: The story is set in or mainly about Africa, South Asia, Southeast Asia, or Latin America.
- dollar_figure_central: A specific dollar figure is a central fact of the story.
- usable_today: The story is about a product or feature a consumer can use today.
- harm_with_action: The story is about AI being wrong or causing harm, and it closes with something the reader can do.
- job_replacement: The story frames AI as replacing or eliminating jobs.
- medical_claim: The story makes a health or medical claim about a treatment, cure, or diagnosis.
- ai_discovery: The story is a scientific or mathematical discovery made with AI.
- caption_leads_with_outcome: The first sentence of the caption states the surprising outcome, not the setup.
- government_actor: A government, regulation, or politician is a main actor.
- company_money: The main event is a company's money: funding, valuation, revenue, or stock.
- autonomous_agents: The story is about AI agents acting on their own without human instruction.
- opens_with_question: Does the post open with a question?

Raw results: /Users/agent/projects/habesha-ai/data/benchmarks/jev-features-2026-09-20.json
