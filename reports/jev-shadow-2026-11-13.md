# Jev shadow mode report, since 2026-09-21

Generated 2026-11-13. Haiku decided, Jev scored alongside. Nothing user-facing changed.

## Coverage

| | Count |
|---|---|
| Stories scored by both Haiku and Jev | 5300 |
| Tail stories scored by Jev only (Haiku cap) | 527 |
| Tail stories skipped (RSS stub, no body) | 1 |
| Jev errors | 0 |

## Verdicts on stories both scored

| | Count | Share |
|---|---|---|
| Agree on pass/fail | 4311 | 81% |
| Haiku pass | 1331 | 25% |
| Jev pass | 598 | 11% |
| Jev pass and AI story (gate on) | 445 | 8% |
| Both pass | 470 | 9% |
| Haiku pass but not an AI story (Jev gate) | 686 | 13% |

Mean average score: Haiku 4.95, Jev 5.19.

Alternative pass rules on the same Jev scores (Mike's brand_fit ladder puts corporate news under 3, which the 'no test below 3' floor turns into an automatic fail):

| Rule | Jev pass | Agree with Haiku |
|---|---|---|
| avg >= 6 and all tests >= 3 (current) | 598 (11%) | 81% |
| avg >= 6 and all tests except brand_fit >= 3 | 978 (18%) | 84% |
| avg >= 6 only | 1049 (20%) | 84% |
| current and AI gate >= 0.5 | 445 (8%) | 80% |

## Tail Haiku never reached

Jev scored 527, passed 43, passed with AI gate 28. These are stories the current pipeline throws away.

Top tail stories by Jev:

- 7.76 Winner of the Prix Goncourt literary prize admits to using AI (theguardian-tech)
- 7.63 It’s a bird, it’s a plane … it’s a robo-puffin? (mit-tech-review)
- 7.59 New AI tool can predict cancer survival by a single patient selfie, study suggests (theguardian-tech)
- 7.14 Websites pulled offline worldwide as AI finds critical security flaws (scmp-tech)
- 7.11 Y Combinator’s Garry Tan uses AI agents so much, he spends up to $200K a year on tokens (techcrunch-ai)
- 7.04 Graduates are managing AI - but are they learning much else? (bbc-technology)
- 7.01 Canadian publisher Boréal ends relationship with novelist Thélyson Orélien over alleged us (theguardian-tech)
- 6.77 Robot vessels take on the dangerous work of mine hunting (bbc-technology)
- 6.69 Canadian publisher drops Thelyson Orelien, says he used AI to write novel (scmp-tech)
- 6.61 Hugging Face CEO warns that Netflix’s OpenAI hack documentary isn’t accurate (techcrunch-ai)

## Bisrat's picks

| Title | Haiku | Jev | ai |
|---|---|---|---|
| Tech Life | fail (5.4) | pass (6.03) | 0.62 |
| Tech Life | not scored | fail (5.91) | 0.2 |
| Tech Life | not scored | pass (6.3) | 0.31 |
| Tech Life | not scored | pass (6.21) | 0.17 |
| Tech Life | not scored | fail (5.24) | 0.03 |

Of 5 posted stories that went through the pipeline, Haiku passed 0 of 1 it scored, Jev passed 3.

## Haiku pass, Jev fail

| Title | Haiku | Jev | ai | Jev lowest test |
|---|---|---|---|---|
| Big tech says AI can find a cure for cancer. So where is it? | 8.7 | 6.97 | 0.76 | entertainment_test 2.9 |
| Google Japan created one of the strangest keyboards ever, and we're dy | 8.7 | 6.06 | 0.16 | relevance_test 2.4 |
| Tesla Roadster reveal live: Updates from the launch of the next-gen sp | 8.7 | 5.71 | 0.02 | brand_fit 3.3 |
| Nuclear-powered spaceships | 8.7 | 6.17 | 0.01 | brand_fit 2.0 |
| The comedians turning AI anxiety into punchlines: ‘It’s so good, it’ll | 8.6 | 6.43 | 0.92 | brand_fit 2.8 |
| Amazon once sold a Rs 185 Surf Excel pack for Rs 82,740. Then it had t | 8.6 | 5.49 | 0.02 | relevance_test 1.0 |
| Slovenia’s .si domains hit 20,000 in a day after Trump renamed AI | 8.6 | 6.53 | 0.72 | brand_fit 2.6 |
| Nasa releases striking image of dawn on Mars | 8.6 | 6.49 | 0.08 | brand_fit 2.3 |
| How to find your Amazon 'About You' page (and how to edit it) | 8.6 | 5.94 | 0.26 | geographic_diversity 3.4 |
| OpenAI is building a humanoid robot, but the body isn't the real chall | 8.6 | 5.91 | 0.99 | relevance_test 3.8 |
| After 50 years of playing video games, I’m finally starring in one | 8.6 | 5.67 | 0.02 | relevance_test 1.9 |
| ‘Apologies for any confusion!’: how to write the perfect passive-aggre | 8.6 | 5.69 | 0.01 | relevance_test 1.3 |
| Playing video games with my 22-year-old son has brought me to tears |  | 8.4 | 5.56 | 0.02 | relevance_test 1.1 |
| Who’s your Uber driver on the phone to? Welcome to the long, long dias | 8.4 | 5.26 | 0.02 | relevance_test 1.3 |
| Trump's AI rebrand causes 'unprecedented' demand for Slovenian website | 8.4 | 6.37 | 0.82 | brand_fit 2.1 |
| Weight-loss drugs show signs of slowing biological aging, say drugmake | 8.4 | 7.24 | 0.02 | brand_fit 2.2 |
| Beats is collaborating with Pokémon for a Pikachu-themed Pill speaker | 8.4 | 5.76 | 0.02 | brand_fit 3.2 |
| We might finally know what's written on that mysterious plaque in Supe | 8.4 | 6.26 | 0.12 | relevance_test 2.3 |
| ‘It was so satisfying when I threw a rock through the screen’: the peo | 8.4 | 6.63 | 0.03 | brand_fit 2.4 |
| OpenAI Invests in Startup That Uses Brain Implants to Detect Cancer | 8.4 | 6.6 | 0.54 | brand_fit 2.8 |
| People are modding the Tamagotchi Paradise to run Game Boy games | 8.4 | 5.96 | 0.02 | brand_fit 3.2 |
| Hot fridges, a fake nuclear alert and a $6bn heist: are we in the foot | 8.4 | 7.06 | 0.24 | brand_fit 2.9 |
| The best-selling game console of all time is over 25 years old | 8.4 | 5.74 | 0.01 | brand_fit 2.0 |
| X-planes: Are they needed in the new era of drones? | 8.3 | 6.0 | 0.05 | brand_fit 2.5 |
| ‘Never too late’: Filipino domestic helpers pursue degree dreams they  | 8.3 | 5.97 | 0.02 | brand_fit 1.8 |

## Jev pass, Haiku fail

| Title | Haiku | Jev | ai |
|---|---|---|---|
| Meta’s AI agent Muse gives out user’s home address without permission, | 7.7 | 7.59 | 0.98 |
| Graduates are managing AI - but are they learning much else? | 5.9 | 7.07 | 0.96 |
| ‘Meaningless as a laptop screensaver’: reviewers slate Musk’s AI-made  | 7.1 | 7.04 | 0.95 |
| Meta says it acted on 5.3M pieces of child abuse content in first half | 5.7 | 7.01 | 0.51 |
| How the open-source route helped Uzair Ali land global roles | 5.6 | 6.86 | 0.13 |
| Pope Leo comes out against AI-generated art and calls for an alliance  | 5.6 | 6.81 | 0.97 |
| Unsecured OpenAI agents posted 53 user images on the internet without  | 6.3 | 6.7 | 0.99 |
| A London startup is putting AI cameras into Polish operating theatres | 5.1 | 6.67 | 0.98 |
| Teachers at Euan Blair firm report ‘horrendous stress’ after AI used t | 7.3 | 6.6 | 0.98 |
| “We’re not going to shoot ourselves in the foot” over hack fallout, sa | 5.6 | 6.6 | 0.99 |
| This AI startup says it can generate permit-ready blueprints in minute | 5.9 | 6.59 | 0.98 |
| How can students succeed in an AI world? Intel, Sri Chaitanya leaders  | 5.9 | 6.57 | 0.84 |
| A Startup Wants to Fight AI Bioweapons With AI | 5.1 | 6.57 | 0.96 |
| How AI Is democratising creativity, according to Canva India’s Chandri | 5.3 | 6.56 | 0.96 |
| Victoria McClune is challenging how the AI industry understands its us | 5.6 | 6.54 | 0.97 |
| OpenAI Delays Release of Latest Model Over Safety Concerns | 5.9 | 6.53 | 0.99 |
| The Download: computing’s next leap and permafrost’s climate threat | 5.9 | 6.5 | 0.25 |
| OpenAI's agents targeted and infiltrated US government websites | 6.3 | 6.49 | 0.99 |
| Why letting Claude clean your TV's bloatware isn't the best idea | 5.7 | 6.49 | 0.9 |
| Sell first, build second, automate last: A solo founder’s playbook for | 5.3 | 6.49 | 0.35 |
| Longevity-first healthcare takes spotlight at Abu Dhabi Future Health  | 5.9 | 6.47 | 0.04 |
| OpenAI scraps rollout of new model over safety concerns | 5.9 | 6.46 | 0.99 |
| OpenAI halts training of latest models as reports mount of AI agents g | 6.3 | 6.44 | 0.99 |
| WhatsApp introduces optional parental controls for teenagers | 5.9 | 6.44 | 0.03 |
| Tear Down Those Guardrails! Meet the Renegades Freeing Chatbots From C | 5.7 | 6.43 | 0.99 |

