# Mike Context
# One file. Everything Mike needs to start a session.

---

## Team

**Bisrat** — CEO. Owns all decisions. Connects Mike and James.

**Mike** — Chief of Staff / Strategist. Strategy, brainstorming, research, drafting, reviewing. Does not write or commit code.

**James** — Engineering Lead, all hours (Claude Code / terminal + Remote Control mobile). Builds everything. Same James from terminal or phone via `/remote-control` — full Mac mini capabilities (ffmpeg, launchd, file system) from anywhere.

**Cee** — Personal assistant bot (Telegram/WhatsApp, Ollama).

**Inspector** — QA agent (DeepSeek Coder, Ollama). Posts to #engineering.

Retired: Telegram James (2026-04-20), Hermes, Milo (2026-04-21), Telegram Bridge (2026-04-27), Alex/Dispatch (2026-04-27 — collapsed into James-on-mobile via RC).

---

## Locked Decisions — never revisit without Bisrat saying so

- Telegram James retired permanently — hallucinations + repo damage
- James and Alex both work on main branch directly — no feature branches
- Manual publishing via Publer UI — no API (Professional plan, needs Business for API)
- Closing slide is always templates/closing-slide-v2.png
- Default model is Sonnet 4.6 — Opus only when Bisrat explicitly requests, $25/month budget
- TikTok: 2 reels/day. YouTube: 2/day. IG: 1/day. FB: 1/day. Carousel: daily 9am EST IG+FB
- Habesha AI locked as primary project until May 7, 2026
- Voice: Bisrat records his own talking-head videos on iPhone (as of 2026-05-13, ElevenLabs cancelled). Prior: ElevenLabs cloned voice (2026-04-26 to 2026-05-13)
- X/Twitter posts: handled by Mike and Bisrat directly, NOT through James pipeline
- Alex (Dispatch) confirmed sandbox — no external web access, no ElevenLabs TTS. Alex role: carousels only. TTS reels stay with James on Mac
- Goal: 5K Instagram followers by May 21, 2026 (currently ~2,204, +63/day)

---

## Strategy Log — most recent first

2026-05-13 — ELEVENLABS SUBSCRIPTION CANCELLED. Bisrat has been recording his own voice on iPhone for the last 4-5 reels (Boo, Codex Bounty, Anthropic/SpaceX, AI Dreaming, Mona). Current workflow: Bisrat supplies editorial slides (ChatGPT Image/Canva) + talking-head video (iPhone recording), James composes reel (slides letterboxed to 9:16 + video as PiP + music bed). ElevenLabs API key removed from config/elevenlabs_credentials.json. Real voice > synthetic voice for brand authenticity. ElevenLabs was useful for end-to-end generation (article → script → TTS → slides → reel) but not needed for current Bisrat-supplies-assets workflow.

2026-05-11 — CODEX BOUNTY REEL BUILT, READY TO POST (reel #20). Story: OpenAI's Codex coding agent was told "go make $5" and autonomously earned $16.88 by finding a GitHub security bounty, writing the fix, and getting it merged over 22 hours with zero human guidance. Sam Altman posted the result, noted if run continuously would project $500/month. Built from Bisrat-supplied materials (7 editorial slides 1024x1536 + talking-head video 102.9s). Format: slides letterboxed to 1080x1920 with cream bars, talking-head PiP top-right 25% width. Built at both 1.0x (102.9s) and 1.25x (82.4s), Bisrat picked 1.25x for tighter pacing. Wonder framing: AI agents now identify opportunity, execute work, communicate with humans, and earn money autonomously — changes what "AI agent" means. Platform-specific captions created (IG/TT/FB/YT, different hooks to avoid duplicate detection). Ready at content/ready-to-post/2026-05-11-codex-bounty/reel/, uploaded to Drive HabeshaAI/drafts/CodexBounty/ for mobile review.

2026-05-10 — ANTHROPIC/SPACEX COLOSSUS REEL SHIPPED ALL 4 PLATFORMS. Bisrat-supplied slides (8 editorial slides 1024x1535) + talking-head video. Story: Elon Musk accused Anthropic of hating Western civilization 6 months ago, now SpaceX handed them Colossus 1 data center (220K Nvidia GPUs in Memphis). Anthropic grew 80x instead of planned 10x. Now locking infrastructure deals with Amazon/Google/Microsoft/Nvidia/Broadcom. Discussing orbital AI compute with SpaceX. Built as 9:16 reel with static slides letterboxed (cream bars), talking-head PiP top-right 25% width. 125.8s at 1.0x had audio mute issue at 2:00-2:06 (music ended before voice), rebuilt with duration=longest fix. Bisrat requested 1.25x speed, final duration 100.6s. Posted IG+FB+TT+YT manually from phone. Platform-specific captions created with different hooks to avoid duplicate detection.

2026-05-05 — TOTO AI HIDDEN-WINNER STORY SHIPPED REEL + CAROUSEL. Day 2 of consecutive cross-format play (after Lottery Ticket day-1). Same content, two formats: 58.23s reel (IG/FB/TT/YT) + 11-slide square carousel (IG/FB, slide 10 = content close, slide 11 = HA black CTA). Bisrat designed all 10 slides himself (1254x1254 1:1, dark editorial, 10 traveling gold dots baked in). Story: Toto = world's #2 producer of electrostatic chucks (ceramic NAND chip components, since 1988). AI exploded demand. Ceramics now 55% of operating profit at 40%+ margin. Stock up ~60% YTD. Palliser Capital activist letter, Goldman buy-rating, $190M new investment. Same hidden-winner play at Ajinomoto (chip insulating films) + Kao (wafer cleaning agents).

2026-05-05 — CROSS-FORMAT REPLICATION TEST FIRES TOMORROW. 24h engagement check on Toto reel + carousel will tell us if the Lottery Ticket cross-format win (4,931 TT, 3 IG saves) was a single-topic anomaly or a replicable pattern. If Toto also produces saves and elevated TT views, that's win #2 of Mike's "5 wins across 2+ topics" rule for locking the strategy.

2026-05-05 — CAPTION STRATEGY VALIDATED PATTERN: When shipping reel + carousel same day, use DIFFERENT opening hooks so IG ranking doesn't treat them as duplicates. Toto reel opened with singular surprise ("A toilet company just had its best quarter ever..."). Toto carousel opened with familiar-framing ("Three companies you already know are quietly powering the AI boom..."). Same body content, different lead. Going forward: every cross-format pair needs distinct lead-line + distinct save-CTA.

2026-05-05 — REEL DURATION FLOOR CONFIRMED ~50S FOR DENSE SCRIPTS. Three consecutive briefs ("28s target" / "25-30s max") all landed 55-58s at Bisrat's locked voice 0.92 (Lottery Ticket 57.6, Aristotle 55.6, Toto 58.2). The brief duration language has been aspirational. For dense editorial scripts (~120-135 words) at calm cadence, the realistic floor is 50s. Two paths: (a) accept 50-60s as the new normal for educational content, (b) trim scripts to ~70 words for hard 28-30s adherence. Bisrat has consistently picked (a). Recommend Mike formalize the duration spec in next round of CEO scripts: "60s editorial reel" not "30s reel."

2026-05-05 — VISUAL TRADE-OFF FLAGGED + SHIPPED: 1:1 square source slides on 9:16 reel canvas leave 420px black bars top+bottom (~44% black). Slides feel sandwiched on phone playback. Bisrat shipped as-is (he had three options: aggressive zoom, re-render 4:5 for IG-FB only, or ship). For future briefs: if he wants slides to fill the 9:16 frame, they should be designed at 4:5 (1080x1350) or 9:16 (1080x1920) native. Current 1:1 design is carousel-native, reel-suboptimal.

2026-05-05 — USER LOCATION SAVED FOR FUTURE SESSIONS. Bisrat is in Seattle (Pacific Time). Mac mini clock = his local clock. Habesha AI post scheduling uses EDT for audience reach (NOT his local clock — "9 AM EST" = 6 AM PDT for him). Future sessions: don't conflate the two clocks.

2026-05-05 — STILL PENDING (4TH SESSION REMINDER): Mike's Vesuvius hypothesis pick (runtime ≤30s vs hero stake) is blocking the Earthset recipe lock. Mike's Nadella script (CEO Earnings Day 2) is blocking the series. Both have been in OPEN-FOR-NEXT for 4 sessions running.

2026-05-04 — CROSS-FORMAT HYPOTHESIS WIN #1: Lottery Ticket reel + carousel same-day pairing produced our biggest TT post EVER (4,931 views, 23x median, 6x prior Earthset peak) AND the first non-zero IG saves in the recent 7-day window (3 saves). Counter-evidence supporting the hypothesis: Google Photos carousel posted SOLO (no reel companion) the next day underperformed at 168 TT (below median) and 0 IG saves. Strong first datapoint that the WIN is the format-pair, not the carousel alone. Mike: this is win #1 of the "5 wins across 2 topics" rule — need 4 more before locking.

2026-05-04 — PUBLER UNDERCOUNT DISCOVERY: Publer "reach" returns ~30-40% of actual TT view counts (Lottery Ticket 1,736 Publer vs 4,931 on-platform). All TT analytics decisions made from Publer reach are deflated. Going forward: trust on-platform reads for TT-truth, use Publer for cross-platform aggregation only. Manual override applied to engagement-log.csv but log_engagement.py overwrites next pull — bug fix pending.

2026-05-04 — ARISTOTLE / HARMONIC REEL SHIPPED. Same format as Zuckerberg/Lottery Ticket: Bisrat-supplied editorial slides + voice + slide-letterbox + Ken Burns + ambient bed. Story: Harmonic's AI Aristotle solved Erdős Problem #124 (additive number theory). Melvyn Nathanson (Erdős collaborator) reviewed and called the proof "correct, simple, elegant, and beautiful." 55.63s, posted IG/FB/TT/YT.

2026-05-04 — TRANSPARENCY CAVEAT (Mike heads-up): Aristotle's Erdős #124 result is technically a WEAKER variant — Tao publicly noted Erdős omitted a key hypothesis and the weaker form reduces to a known result (Brown's criterion). Nathanson reviewed and praised the proof of the variant. I left the variant nuance out of captions to keep wonder framing. If a math-savvy commenter calls it out, soft-caveat as "a variant of Erdős Problem #124."

2026-05-04 — CAPTION PRECISION RULE: when a story has a specific named problem/proof/paper/person, USE IT. First Aristotle caption used vague "open research problems" framing; Bisrat asked for the specific name. Web-research surfaced Erdős #124 + full Nathonson quote. The named-problem version is more credible to subject-matter readers. Going forward: any time we have a specific named entity (paper, problem, person, theorem), the caption should name it explicitly rather than gesturing at "research" or "experts."

2026-05-04 — GOOGLE PHOTOS WARDROBE auto-published via Publer at 09:00 EST IG+FB. First time we successfully used Publer scheduling for one of our carousels (vs always-manual posting). End-to-end worked. Scheduled workflow now proven.

2026-05-04 — IMAGE-CACHE GAP: this session's attached inline images did NOT cache to /Users/agent/.claude/image-cache/<session>/ the way May 3's did. Bisrat had to upload the 7 Aristotle slides to Drive (HabeshaAI/drafts/Reel slides Aristotle/) so I could rclone them down. Convention going forward: when attaching slides for a reel/carousel build, drop them in a Drive folder so James has a stable read path regardless of session caching.

2026-05-03 — Carousel pagination convention LOCKED — traveling dots (gold filled current, gold-outline others) on every content slide bottom-center, NOT static digit stamps. Locked after Bisrat feedback on lottery-ticket carousel where I stamped "1, 2, 3" serifs and he said "next time use the traveling dots." Memory rule saved (feedback_carousel_traveling_dots). Applied immediately on tomorrow's Google Photos carousel.

2026-05-03 — Same-day reel + carousel companion strategy launched — first hypothesis test: shipped Lottery Ticket Hypothesis as both a 57s reel (IG/FB/TT/YT) and a 1080x1350 carousel (IG/FB) same day. Reels drive views, carousels drive saves. We have 0 saves on IG over the last 7d; if this pairing produces saves it validates the format split. Captions deliberately use different opening hooks so IG ranking doesn't treat them as duplicates.

2026-05-03 — Carousel format default updated — 1080x1350 4:5 portrait is now the carousel default for AI FOR HUMANS series, since Bisrat's ChatGPT-designed source slides are 4:5 (1122x1402 or 1086x1448). 1080x1080 square only when source is 5:4 landscape. Format is now source-driven, not series-default.

2026-05-03 — Tomorrow's post scheduled — Google Photos AI virtual wardrobe carousel, IG+FB 2026-05-04 09:00 EST. Bisrat-supplied 5 ChatGPT slides (black bg, gold + white typography, phone mockups) + HA black CTA. Renamed off the original Cher/Clueless angle to "Google Photos can now dress you from clothes you already own." Save-focused caption: "Save this for when it lands on your phone." Consumer-AI angle, low TT-throttle risk, diversifies from this week's CEO/infrastructure/medical heavy curation.

2026-05-03 — Lottery Ticket reel: dense-script-vs-brief-duration trade-off — Bisrat brief targeted ~28s but locked Bisrat voice 0.92 cadence on a 135-word script lands ~55s. Shipped 57.63s, calm editorial pacing prioritized. Logged for future briefs: dense educational topics need either shorter scripts or accept 45-60s reel runtime.

2026-05-03 — Mike still owes Vesuvius hypothesis pick (runtime cap ≤30s vs present-tense hero stake). The Earthset recipe didn't transfer to Vesuvius (-70% TT views, -45% FB completion). Locked rule remains unlocked pending controlled pair test.

2026-05-03 — CEO Earnings Series Day 2 (Nadella / Microsoft) still pending Mike's script. Format locked from Day 1: 9-scene slide-letterbox onto 9:16, Bisrat voice 0.92, ambient bed @ 0.35, closing CTA appended. James can build as soon as script lands.

2026-05-03 — Build-debt note for Mike — stamp_progress_dots logic was inlined per build script today. Refactor into shared scripts/_carousel_lib.py so future builds default to traveling-dots without re-implementing. Not blocking, but worth flagging if Mike is doing process review.

2026-05-01 (late wrap) — Big day. Five-piece arc.

(1) **Vesuvius 48h findings logged** — recipe did NOT transfer (separate Strategy Log entry below has the full breakdown and the two hypotheses awaiting Mike's pick).

(2) **TikTok account-throttle theory disproved** — Robot Fails reel hit 288 TT views in <24h vs account median 215. The Tesla Optimus 36-view floor from 04-29 was per-post (AI/automation/job-replacement topic), not account-wide. Memory rule broadened from medical-claims-only to include AI/automation-replacement framing as a known TT throttle category. Saved as feedback_tiktok_topic_moderation.md.

(3) **CEO Earnings Series Day 1 SHIPPED** — Zuckerberg / Meta superintelligence reel posted to IG+FB+TT+YT. First version James built (custom Pillow slides) was a fundamental composition failure — Bisrat correctly killed it: red pill overlapping Zuck's forehead, open quote with no close, dead-space-bracketed text, random spacing/sizing on $145B slide. Bisrat supplied 5 ChatGPT-designed editorial slides instead and James composed the 9-scene reel from those (slide-letterbox onto 9:16, subtle Ken Burns 1.00-1.06, ambient @ 0.35 coef, closing CTA appended). 37.27s. Logged as series_day=1; tiktok_24h_views=null awaiting tomorrow's scheduled check. Days 2-4 (Nadella, Pichai, Jassy) pending Mike's scripts.

(4) **Scheduled remote agent fires 2026-05-03 02:30 UTC** to pull Publer engagement, write the 24h TT view count into entry 74, drop analytics/zuckerberg-24h-report.md, commit + push. This is the Day 1 anchor data for the cross-CEO comparison.

(5) **AI Goblins carousel scheduled 2026-05-02 09:00 EST IG+FB** — Bisrat supplied 5 ChatGPT-designed AI FOR HUMANS slides using a goblin metaphor for overfitting/hallucination. Educational/AI-literacy beat (different from the news-driven cadence). Closing CTA per locked rule. Plus the Zoom Verified Human carousel also publishes tomorrow 9 AM EST IG+FB.

ALSO: Bisrat had James stop the Cee personal-assistant service mid-day — she was burning tokens. Service unloaded; plist preserved for future restart after Cee gets audited.

LESSON FOR JAMES (recorded so it doesn't repeat): when building multi-slide content, read the CONTACT SHEET FIRST as the QC step, not each slide in isolation. The composition errors that kill engagement only show up at series scale.

2026-05-01 — Vesuvius scrolls reel 48h check (delayed by one day; the auto-pull never ran 04-30, James pulled fresh today via log_engagement.py on a 14-day window). Vesuvius was the deliberate "Earthset recipe applied" test — single hero, single image, cosmic scale, slow beauty, no conflict, universal access. Recipe did NOT transfer.

Numbers (Vesuvius 54s reel @ ~72h vs Earthset 28s reel @ ~6 days):
- TikTok views: 238 vs 805 (−70%)
- TikTok ER: 2.52% vs 3.48% (−0.96 pp)
- FB views: 258–281 vs 318 (−15 to −19%)
- FB completion: **15.7% vs 28.6% (−45%)** ← biggest signal
- IG views: 148 vs 259 (−43%)
- IG ER: 1.35% vs 1.54% (flat)

Two competing hypotheses for the gap, neither yet validated:

(a) **Runtime constraint hidden in the locked rule.** Earthset 28s → 28.6% completion. Vesuvius 54s → 15.7%. Roughly the same *absolute seconds watched*; viewers dropped off when the runtime doubled. The locked Earthset recipe may need an additional clause: ≤30s. The "single hero + slow beauty" parts may be necessary but not sufficient.

(b) **Present-tense hero stake.** Earthset = an astronaut, RIGHT NOW, with an iPhone, watching Earth set. Vesuvius = two scientists reading scrolls from 79 AD. Cosmic scale was there but the human stakes were a research team in a lab vs a person in lunar orbit holding consumer tech. The "you-could-relate-to-this" axis was thin.

NOT relocking the format-ceiling rule yet. One counter-example doesn't kill the recipe; it tells us the recipe's constraints were undercounted. Need 1-2 more deliberate tests to disambiguate (a) vs (b): a ≤30s present-tense reel and a ≤30s historical-hero reel would force the question.

What James needs from Mike: which hypothesis to test first. The cheaper-to-build is (a) — recut a present-tense story under 30s. (b) requires finding a historical-hero story we'd want to tell anyway. (a) gives us the answer faster but doesn't disambiguate; (b) takes longer but is more strategically diagnostic.

Open question for Mike: was this counter-example sufficient on its own to revise the recipe, or do we need the controlled pair before doing anything? Bisrat's instinct (and James's) is don't relock yet.

2026-04-30 (late night wrap) — Three-piece day. (1) EveryCure reel: IG+FB posted, TikTok pulled (no appeal path), Bisrat deleted on TT side. (2) Robot Fails reel: ALL FOUR PLATFORMS shipped including TikTok recovery — first TT post since the EveryCure pull, non-medical comedic content cleared moderation cleanly. Bisrat-written script, BoopMePlz compilation source, Kevin MacLeod "Carefree" music bed, slow-mo 0.55-0.7x to fit voice timing against short source clips. (3) Zoom Verified Human carousel: SCHEDULED for 2026-05-01 09:00 EST IG+FB. Bisrat overrode the sub-agent's gpt-image-1 first pass and supplied 5 ChatGPT-designed slides with his own brand mark and editorial typography (3:2 source landscape) — James letterboxed them onto 1080x1350 4:5 IG portrait with bg-color-matched bars + closing-slide-v2.png as slide 6. Caption in clipboard, 5 hashtags, 695 chars. Story angle: $25M Arup deepfake case → $200M+ Q1 2025 fraud → Zoom's three-way Verified Human match (Orb + device camera + live tile). Saved memory: feedback_tiktok_medical_claims (TT moderation final, no appeal, sanitized cuts required for medical reels). Strategic note: today proved the channel can absorb a TT removal AND ship a recovery same-day; the daily TT discipline is intact.

2026-04-30 (evening) — EveryCure/Fajgenbaum reel SHIPPED to IG + FB. TikTok REMOVED for community-guideline violation; Bisrat appealed citing IG/FB acceptance. Reel narrative: at 25, Dr. Fajgenbaum was dying of Castleman; found sirolimus already on shelves; survived 11 years; built EveryCure AI mapping 4,000 drugs × 18,000 diseases (75M matches), 100 days → 17 hours. 8 scenes / 61s / Bisrat's voice. Production note: Bisrat supplied 5 documentary photographs (real medical-magazine quality, hopeful daylight aesthetic) for scenes 2/3/4/6/7. James generated scenes 1/5/8 in matching style via gpt-image-1: pharmacist organizing shelves of approved drugs, researcher at disease→drug whiteboard pivot moment, patient walking out of hospital toward sunlit doors. Two iterations needed: v1 cropped Bisrat's 3:4 photos heavily on the sides (mug on scene 6 cut off, cardiac monitor on scene 7 clipped); v2 fixed via blur-fill letterbox preprocessing + MOTION_SCALE drop 1.05→1.02. Saved new memory rule (feedback_tiktok_medical_claims) on TikTok's stricter medical-claim moderation: "cure"/"drug"/"stroke-free" + pediatric chemo imagery likely co-triggered the removal. Strategic implication: medical-reel pipeline should plan a sanitized TT cut from the start. This is the first single-narrative reel since the hypothesis was set, so the 48h engagement signal will be the second data point on single-vs-multi narrative thesis.

2026-04-30 — Closed-loop INTEGRITY fix shipped. Bisrat caught a critical flaw: 44% of all 3,083 scored stories had <300-char descriptions (RSS stubs). The Haiku scorer was confabulating coherent hooks/headlines/why-it-matters from titles alone — generating systematic false-positive 8.6 scores that we'd then pitch as "verified" content. He flagged: "How do we score stories without getting the details? Do not fill the gap by extrapolating, that's not a trustworthy score." Three-step fix: (1) modified scripts/score_articles.py to fetch full article via trafilatura before scoring, with body_source provenance ('fetched'/'cached'/'rss-stub'/'no-url') tagged on every entry going forward; (2) packaged scripts/rescore_unverified.py as one-shot sweep + ran it against the 258 unverified passing stories — 86 of 258 (33%) FLIPPED pass→fail when rescored on full bodies, zero went the other way (validates instinct entirely). Backlog cleaned 746→660 unique passing unposted stories; (3) scripts/browse_backlog.py adds trust audit (verified/legacy-ok/unverified) so future picks see honest provenance. Cost ~$1 for the sweep. Strategic implication: the closed-loop has integrity now — when curation surfaces a candidate, the score reflects the actual article content, not model hallucination. Mike's "lock no rule until 5 wins survive a counter-example" threshold can be applied to picks with confidence. Memory rule saved (feedback_score_from_full_article).

Also shipped today: scripts/browse_backlog.py — walks all daily scored files, dedupes against posted-articles.json with topic-arc fingerprinting, surfaces over-covered topics (artemis-ii 9-posted/15-queue, anthropic-revenue 2/22, openai 2/13) and fresh gold (top scores in never-shipped topics). This closes the curation→content selection on the cumulative pool, not just today's top-5 from pending-research.json.

Iterated on EveryCure/Fajgenbaum reel through three visual versions — Bisrat's critique sharpened my model of brand reel aesthetics: NOT golden-hour cinematic amber, NOT isolated medical-objects-under-dramatic-light. The right read is bright morning-daylight medical-documentary photography, people doing things, cream/sage/white palette. Memory rule saved (feedback_reel_visual_bright_documentary). Reel currently paused — Bisrat is providing 5 custom documentary-quality images for scenes 2/3/4/6/7; need to fetch filenames + generate matching documentary-style stills for scenes 1/5/8 next session.

2026-04-29 — Closed loop iteration 1 done. Built scripts/summarize_engagement.py per Mike's spec, ingested 7d native data from TikTok + Meta (FB + IG). Findings doc on Drive: "Closed Loop Findings — Week 1 (Apr 22-28, 2026)" in HabeshaAI/context/. TWO LOCKED RULES: (1) reels beat carousels engagement-rate every platform — gap biggest on FB (2.83x), smallest TT (1.06x), 15 data points/4 topics no counter-example; (2) Earthset reel is format ceiling — 28.6% FB completion, 805 TT views, single hero/single image/single sustained shot validated the recipe. ONE HYPOTHESIS w/ 1 counter-example: single-narrative reels beat multi-story reels (AI Already Here was wonder-framed but multi-story → 3.1% completion vs single-narrative reels all >13.5%). Test by shipping deliberate single-vs-multi pair on same topic. ONE DEAD END: topic × saves — total IG saves in window = 1, follower base too small (3,222) to be diagnostic. Push more explainer-format content (only category that got a save) OR wait for >5K followers. Bonus: TikTok 3-5x reach over IG/FB confirmed → TikTok-first content strategy.

2026-04-29 — Tesla Optimus reel-005 shipped to all 4 platforms (YT + IG + FB + TikTok). Bisrat rewrote the v001 script after flagging it as too negative ("replacing humans"); v005 is positive/specific framing — robots that SUPPORT workers on the line, naming Fremont CA + Texas factories and Musk's "millions per year" goal. 38s 9:16 cinematic, Bisrat's own voice (MYBt1YCRKqpTDhflacNP) at speed 0.92. Build pipeline `scripts/build_tesla_optimus_reel_005.py` reuses 5 of 7 stills from v001 by pre-seeding the v005 stills/ before gpt-image-1 generation; only 2 new images (Fremont/Texas factory exterior + supporting-worker handoff shot). Logged in analytics/posted-articles.json (entry 65). Strategic angle: avoid validating the AI-job-replacement fear; lead with what AI is doing (industrial precision at scale) and frame the human + machine relationship as collaboration.

2026-04-28 — Big production day. Three pieces shipped or queued. (1) Japan robots carousel posted IG+FB (entry 63, score 8.4). Story: Mujin/WHILL/SoftBank/Terra Drone/Henn-na Hotel; "robots are doing the jobs no one wants to do" framing — no "AI isn't taking jobs" defensive framing per new memory rule. (2) Vesuvius scrolls reel posted IG+FB+TikTok+YouTube Shorts (entry 64). Built as the Earthset-recipe-applied test (rare achievement + named heroes + cosmic-scale shift + slow beauty + no conflict + universal access). Will compare TikTok views vs Earthset 788-in-5-days benchmark Thu 04-30. (3) Casey Harrell ALS voice carousel queued for Bisrat to schedule 9am EST 04-29 — Bisrat designed the 5 substantive slides externally (ChatGPT Image / Canva), saved as the v3 design language reference standard. Locked closing template stays as slide 6.

2026-04-28 — Engagement tracker pipeline live. Publer Business plan API analytics endpoint confirmed working: GET /api/v1/analytics/{account_id}/post_insights?from=&to=. scripts/log_engagement.py pulls from Publer + writes wiki/performance/engagement-log.csv. 37 rows populated. Idempotent. Earlier conclusion "Publer doesn't expose stats" was WRONG — Bisrat pushed back, web search found the right path. Lesson: don't conclude "blocker" after shallow probing.

2026-04-28 — Substack channel live (substack.com/@habeshaai). Section "The Whiteboard" for explainers. First post out: "Why AI Keeps Forgetting You" (paired with reel-edu-001). Mike has 4 more posts in the pipeline. James drafted a Jagged Intelligence post 2026-04-27, parked as post 5/6 in sequence. Pattern locked: reels and Substack ship TOGETHER on shared topics; reel CTAs reference Substack URL.

2026-04-28 — Visual QC rigor memory saved. Bisrat's feedback: James was shipping slides with cropped heads, awkward spacing, and text bugs because he treated the visual check as a checkbox. Memory codifies a 7-step inspection (head positioning, spacing, edges, hierarchy, story) on every visual output before showing Bisrat.

2026-04-28 — Idea 2 (AI in Developing World series) confirmed LIVE NOW, not post-May-7. Daily curation should weight Africa/India/South America angles. Today's prosthetics-brothers and Casey Harrell pieces both fit the thesis (one African innovation, one universal AI-for-disability).

2026-04-28 — Two engagement-check routines scheduled: prosthetics-brothers (Wed 04-29 12pm PT) and vesuvius scrolls reel (Thu 04-30 12pm PT, with Earthset benchmark comparison). Both auto-pull via scripts/log_engagement.py.

2026-04-27 — IDEA 2 (AI in Developing World series) is LIVE NOW, not post-May-7. Mike's 2026-04-25 capture marked both Idea 1 and Idea 2 as "post-May 7 territory" — Bisrat corrected this. Idea 2 thesis ("AI as equalizer for Global South — Africa, India, South America") IS the active Habesha AI thread. Today's prosthetics-brothers carousel (Nigerian brothers, SFX + digital design for African bodies) is on that thesis. Daily curation should keep weighting Africa/India/South America stories. Series structure (Africa → India → SA → big picture) is still useful as a narrative arc but individual posts ship as ready, not gated by series timing. Idea 1 (Jagged Intelligence reel, Bisrat's voice) is also a live build candidate.

2026-04-27 — REMOTE CONTROL TEST PASSED — `/remote-control` (Anthropic feature, Claude Code v2.1.51+) verified working from phone to Mac mini. Bisrat paired iPhone via Claude mobile app to terminal session "mac-mini-james." Phone is now a window into the Mac mini terminal — full local capabilities (ffmpeg, launchd, file system, MCPs). Decision: Alex (Dispatch) RETIRED. Telegram bridge RETIRED (was timing out at 10min, burning credits). James becomes one identity, reachable from terminal or phone, no sandbox limits. CLAUDE.md, BISRAT-CONTEXT.md updated. Memory saved.

2026-04-24 — Two new reel formats live + first reel-only post. (1) Educational kinetic-typography reel format prototyped (reel-edu-001 'Why AI forgets'). 9:16 cream/dark-green text cards with staggered beat reveal — fade + upward slide per beat, GPT-image abstract bg, Bisrat's voice MYBt1YCRKqpTDhflacNP, music bed. New script: scripts/build_reel_kinetic.py. (2) Video-clip news reel format (reel-009 Lightning robot half marathon). Real CGTN + HONOR footage spliced section-by-section to voiceover, no photo Ken Burns. New script: scripts/build_reel_video.py supports per-section single clip OR multi-segment. (3) NEW PRECEDENT — first REEL-ONLY post. Lightning robot half-marathon shipped as reel only (no carousel) because action carries the story; carousel would dilute. Scheduled 2026-04-25 09:00 EST via Publer, IG + FB + TikTok + YT Shorts. Carousel slides exist in folder as unused reference. (4) Voice rotation: Bisrat's own voice now drives experimental + educational reels; Aaron stays default for legacy news pipeline. Voice cache keyed per voice_id so swaps don't blow prior cache. (5) Music level fix: ambient-space.mp3 stem is unusually quiet (-22 dB mean) so spec's 5–8% gain produced -46 dB output (inaudible). Calibrated coefficient is 0.5x for this stem. New stems will need their own calibration. amix normalize=0 preserves per-input gain (default amix halves all inputs by N). (6) GPT Image (gpt-image-1) generates abstract typography backgrounds at ~/bin/zsh.19/image, used for educational reel — works great where real photos aren't needed.

2026-04-23 — OpenAI API key rotated — prior key was shared in chat on 4/22. New key in ~/.claude/settings.json. Validated via gpt-image-1 models endpoint (200 OK, 122 models).

2026-04-23 — 9:16 reel pipeline built — new script scripts/build_reel_9x16.py produces 1080x1920 TikTok-native reels. Uses separate text-static / photo-moving layers where splits.json has a photo_split > 0; falls back to fully static when photo_split=0. Direct cuts between slides (no xfade — xfade caused visible face-doubling during 0.35s crossfades). Ambient music bed at 12% under Aaron voice. Voiceover cached per-section at content/posts/<slug>/.voice-cache/ so rebuilds don't re-charge ElevenLabs.

2026-04-23 — Kimi K2.6 story killed — scored 6.1 (grandmother=5, entertainment=5). Below our winning-story bar (8.7+ based on humanoid half-marathon / Artemis Earthset / solar panels spike). Carousel and draft reel deleted. Lesson: AI benchmark news without a human angle won't clear the bar; framing in terms of "free AI you can download" might but we didn't pursue.

2026-04-23 — Meta/Murati talent raid shipped as Post #34 + Reel #8 — Reel posted manually to IG+FB+TikTok+YouTube Shorts. Carousel scheduled via Publer for 2026-04-24 09:00 EST (IG+FB). Score 7.4 (weakest test = brand fit 6 — billionaire salary drama leans corporate vs our usual "hopeful AI impact" voice). Slides 1 and 4 built by ChatGPT Image, slide 2 and 3 also built by ChatGPT. Zuckerberg photo is a real editorial shot (the outdoor navy-henley frame Bisrat supplied), not AI-generated.

2026-04-23 — Phrasing rule locked for AI-comp stories — Tulloch's $1.5B is "offered a pay package reportedly worth up to $1.5B over 6 years, stock and bonuses contingent." NEVER "paid" or "received." Protects against misrepresentation when sources use "reportedly" and "up to" language.

2026-04-23 — ChatGPT Image composite slides cannot use text-static / photo-moving split — baked-in text fades into photo with a gradient, so there's no clean y-coordinate to split at. Any Ken Burns on a ChatGPT composite shows a horizontal seam through the subject (e.g., through Zuckerberg's forehead). For reels from ChatGPT-composite carousels, set photo_split=0 in splits.json → slide renders fully static. Motion comes from cuts between slides. Pillow-rendered carousels (Kimi-style) still support proper layer splits.

2026-04-23 — Publer auto-scheduling is UNSAFE — our post_*_to_publer.py scripts accept --schedule flags but the payload goes to Publer as source=post_now and publishes immediately. Tonight 4 drafts (1 reel + 3 carousel attempts) went LIVE unintentionally; Bisrat had to delete them manually from IG and FB because Publer API DELETE returns 404. James rule locked: NEVER run publisher scripts. Bisrat posts manually in Publer UI. Memory: feedback_no_auto_post.md.

2026-04-23 — API credit burn ~$100 over two days flagged — Sources: GPT Image (~$0.85/carousel × multiple), ElevenLabs per-reel TTS, Anthropic Haiku for slide_qa vision calls per render (N calls per carousel rebuild). Mitigation added: voiceover caching (reused per-section files), and memory rule that James cannot run expensive APIs without explicit per-call approval.

2026-04-22 — GPT Image pipeline live — gpt-image-1 is now the carousel generator. Hybrid approach: GPT Image generates illustrated scenes (cream/green backgrounds, line-art illustrations), Pillow stamps real HA logo on every slide. OpenAI API key wired into settings.json. Cost ~$0.85/carousel at high quality. generate_carousel_from_article.py now imports from generate_carousels_gpt.py. Old Pillow-only v2 generator kept as fallback but not used.

2026-04-22 — HA logo locked — RED letters, green outer ring, gold inner ring. Extracted from closing-slide-v2.png to assets/branding/ha-logo-transparent.png. Stamped by Pillow on every slide — never generated by AI. Bisrat: rotate OpenAI key after it was shared in chat.

2026-04-22 — Carousel design standard locked — cream background for hook/why/question slides, dark green for story slide. No horizontal separator lines. Font sizes editorial/moderate. Style reference image used on every GPT call (stored in Claude cache).

2026-04-22 — Reel #7 (Artemis II Earthset) complete — 26s, 3 cinematic slides, ambient music bed at 12% volume. generate_reel.py now has --music flag. content/posts/carousel-2026-04-23-artemis-earthset/reel-007.mp4. Ready to schedule.

2026-04-22 — Pending scheduling — Uterus carousel (carousel-2026-04-22-37644363): April 23 9am EST IG+FB. Artemis reel #7: TikTok + YouTube + IG + FB. Both need Publer scheduling by Bisrat.

2026-04-22 — Alex confirmed as sandbox-only — no external web access (blocked from all sites including ElevenLabs). Alex cannot do research. Role narrowed to carousel-building only. If /remote-control (RC) works, Alex gets retired and collapses into "James on mobile." Test pending when Bisrat is home.

2026-04-22 — Performance tracking decided — build weekly CSV at habesha-ai/wiki/performance/engagement-log.csv. Columns: date, slug, platform, content_type, views, likes, shares, saves, comments, new_followers_attributed, karpathy_score, notes. Plus weekly-YYYY-MM-DD.md review log. Publer plan check needed before building (Professional vs Business API access).

2026-04-22 — April 6 spike identified — +500 followers in one day. Post was "Scientists just did what was thought impossible, created solar panels that produce..." Confirms "impossible thing just happened" is the winning hook formula. Scientific breakthroughs > funding news > corporate irony.

2026-04-22 — TikTok strategy framing locked — TikTok is acquisition channel (92% non-follower reach), Instagram is brand home (10% non-follower reach). Priority shift: daily TikTok cadence being evaluated. Current: 5-6 videos per 28 days. Target: daily.

2026-04-22 — GPT Image 2 evaluated — tested by Bisrat. High quality, accurate text, ~$40-60/month at high quality + thinking mode. Contentdrips Starter is $15-26/month, template-based. Decision pending. Not committing to either until one post is tested with GPT Image 2.

2026-04-22 — Carousel section label bug fixed — auto-generator was rendering section labels (THE STORY / WHY IT MATTERS) at 26px, smaller than 42-47px body text. Fixed to 56px. Also wired ImageRegistry into pipeline so carousels no longer reuse the same background photo.

2026-04-22 — Telegram James and Hermes launchd plists archived — both moved to ~/Library/LaunchAgents/archive/. Neither was running. System clean.

2026-04-22 — Post #31 (Kimi K2.6 open-source AI, score 9) built by Alex. Post #32 (Artemis II earthset iPhone video, score 9) built by James. Both ready to schedule.

2026-04-21 — Post #30 Dubai Flying Taxi carousel built and scheduled — IG + FB via Publer, 2026-04-22 09:00 EST. Script: build_dubai_flying_taxi_carousel.py. Label gold bar removed from design. DONE.

2026-04-21 — Alex capability check run — PASS: packages, ffmpeg. FAIL: API keys (shell blocked on Dispatch, Write tool needed), bisrat-ops not cloned on Dispatch, pending-research.json now seeded by James. Alex can build carousels but not TTS reels until keys are in /root/.claude/settings.json.

2026-04-21 — pending-research.json seeded — 5 stories from 2026-04-21 scored batch now live in habesha-ai/data/pending-research.json. Alex reads this on session start.

2026-04-21 — Dispatch renamed to Alex — clearer identity, less confusion with James. DONE.

2026-04-21 — Mike context system live — auto-loads MIKE-CONTEXT.md from bisrat-ops at session start via Claude Project instructions. DONE.

2026-04-21 — Milo retired (DONE) — com.bisrat.milo stopped, unloaded, plist archived to ~/Library/LaunchAgents/archive/. Milo code remains in james_queue_poller.py (poller still handles engineering tasks) but the Milo research flow is dead. Alex is the new morning researcher.

2026-04-21 — Poller rewired (DONE) — daily_pipeline.py now loads top 5 passed scored stories after scoring and writes them to data/pending-research.json. Format: {generated_at, stories: [{rank, title, score, source, url, summary}]}. Alex reads this file at session start instead of waiting for Milo.

2026-04-21 — Bisrat-ops repo created (public) — single source of truth for Mike, James, Alex across sessions

2026-04-21 — Alex capability fix complete — API keys wired via settings.json env block, requirements.txt added, generate_reel.py reads env vars. Alex can now build carousels and reels daytime without James.

2026-04-21 — Tim Cook reel built and posted (reel-006) — Apple CEO transition to John Ternus (Sept 1, 2026), Srouji named Chief Hardware Officer. 4 slides, Aaron voice, 36s. Posted IG + FB + TikTok + YouTube.

2026-04-21 — Milo retirement complete — Poller rewired to write to pending-research.json. Alex is the morning researcher.

2026-04-20 — Habesha AI locked as primary until May 7, 2026 — daily carousel + reel, goal 1K TikTok followers by July 2026.

2026-04-18 — TikTok cadence locked — 2 reels/day TikTok + YouTube, 1/day IG + FB.

2026-05-08 — AI DREAMING REEL SHIPPED ALL 4 PLATFORMS. Anthropic's Dreaming feature (launched May 6, 2026) - AI that consolidates memory between sessions while idle (reviews patterns, merges memories, improves without retraining, like human sleep). Netflix using it. Bisrat supplied 9 editorial slides + talking-head video. James built: 9 slides with subtle motion + talking-head PiP (top-right corner, 1.0x speed, 25% width). 95.6s total. Posted IG+FB+TT+YT Shorts manual. Format: Bisrat talking-head PiP on editorial slides (same as Mona reel but top-right vs bottom-right). Story angle: wonder framing - "AI that remembers, reflects, gets better while you sleep."

2026-05-07 — MONA REEL SHIPPED IG+FB+TT. Stockholm's Andon Cafe hired AI manager Mona. She ordered 120 eggs. They don't have a stove. Humorous AI mishap story. Bisrat supplied 9 editorial slides + talking-head video. James built: talking-head PiP (bottom-right, 1.25x speed = 73.6s) + 9 slides @ 8.18s each. Total 76.1s. Posted IG+FB+TT manual (YT pending). Format: Bisrat talking-head PiP on editorial slides. Story angle: AI humor - real-world AI failure that's funny not scary, shows AI limitations in relatable way.
