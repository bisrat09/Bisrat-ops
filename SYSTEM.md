# System

How everything fits together as of 2026-04-21.

## Content Pipeline (habesha-ai)
1. James poller runs daily, writes scored stories to `pending-research.json`
2. Dispatch James (or Terminal James) picks top story, researches, builds carousel + reel
3. Bisrat reviews via Publer before anything goes live
4. James logs posted content to `analytics/posted-articles.json` and `analytics/reels.json`

## Session Sync (James instances)
- Both instances work on `main` branch of github.com/bisrat09/habesha-ai
- `git pull` before any work, `git push` after every commit
- `JAMES-HANDOFF-snapshot.md` — auto-generated on session end (git log, services, posts, reels, open tasks)
- `data/session-bookends.md` — human-readable dated blocks, one per session
- Stop hook in ~/.claude/settings.json auto-runs update_handoff.py on session end

## Publishing
- All content staged to `ready-to-post/<slug>/` first
- Manual upload via Publer UI (app.publer.io)
- Platforms: Instagram (@habesha.ai), Facebook (Habesha AI), TikTok (@habesha.ai_), YouTube (Habesha AI)
- Carousel cadence: daily 9am EST (IG + FB)
- Reel cadence: TikTok 2/day, YouTube 2/day, IG 1/day, FB 1/day

## Active Services (Mac Mini)
- com.bisrat.cee — personal assistant
- com.bisrat.james-bridge-v2 — primary bridge
- com.bisrat.james-poller — daily pipeline
- com.bisrat.milo — research daemon (being retired)
- com.bisrat.sherlock-watcher — security watcher

## Key Repos
- github.com/bisrat09/habesha-ai — PRIMARY content + AI pipeline
- github.com/bisrat09/Bisrat-ops — this repo, cross-project ops
- ~/projects/james-telegram-bridge — bridge service
- ~/personal/cee — Cee assistant
