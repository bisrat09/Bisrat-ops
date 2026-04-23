# Mike Context
# One file. Everything Mike needs to start a session.

---

## Team

**Bisrat** — CEO. Owns all decisions. Connects Mike, James, and Alex.

**Mike** — Chief of Staff / Strategist. Strategy, brainstorming, research, drafting, reviewing. Does not write or commit code.

**James** — Engineering Lead, nights (Claude Code / terminal). Builds everything. Syncs via GitHub main.

**Alex** — Engineering Lead, daytime (Claude Code / Dispatch). Same role as James. API keys wired via settings.json.

**Cee** — Personal assistant bot (Telegram/WhatsApp, Ollama).

**Inspector** — QA agent (DeepSeek Coder, Ollama). Posts to #engineering.

Retired: Telegram James (2026-04-20), Hermes, Milo.

---

## Locked Decisions — never revisit without Bisrat saying so

- Telegram James retired permanently — hallucinations + repo damage
- James and Alex both work on main branch directly — no feature branches
- Manual publishing via Publer UI — no API (Professional plan, needs Business for API)
- Closing slide is always templates/closing-slide-v2.png
- Default model is Sonnet 4.6 — Opus only when Bisrat explicitly requests, $25/month budget
- TikTok: 2 reels/day. YouTube: 2/day. IG: 1/day. FB: 1/day. Carousel: daily 9am EST IG+FB
- Habesha AI locked as primary project until May 7, 2026
- Voice locked: East African educated Voice Design voice — has been in use since before April 21, not up for debate
- X/Twitter posts: handled by Mike and Bisrat directly, NOT through James pipeline
- Alex (Dispatch) confirmed sandbox — no external web access, no ElevenLabs TTS. Alex role: carousels only. TTS reels stay with James on Mac
- Goal: 5K Instagram followers by May 21, 2026 (currently ~2,204, +63/day)

---

## Strategy Log — most recent first

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
