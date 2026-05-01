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
- Voice: Bisrat's own cloned voice (ElevenLabs voice_id MYBt1YCRKqpTDhflacNP) is the default for all reels/TikToks as of 2026-04-26, replacing Aaron until further notice
- X/Twitter posts: handled by Mike and Bisrat directly, NOT through James pipeline
- Alex (Dispatch) confirmed sandbox — no external web access, no ElevenLabs TTS. Alex role: carousels only. TTS reels stay with James on Mac
- Goal: 5K Instagram followers by May 21, 2026 (currently ~2,204, +63/day)

---

## Strategy Log — most recent first

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
