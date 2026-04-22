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

---

## Strategy Log — most recent first

2026-04-21 — Dispatch renamed to Alex — clearer identity, less confusion with James

2026-04-21 — Bisrat-ops repo created (public) — single source of truth for Mike, James, Alex across sessions

2026-04-21 — Alex capability fix complete — API keys wired via settings.json env block, requirements.txt added, generate_reel.py reads env vars. Alex can now build carousels and reels daytime without James.

2026-04-21 — Tim Cook reel built and posted (reel-006) — Apple CEO transition to John Ternus (Sept 1, 2026), Srouji named Chief Hardware Officer. 4 slides, Aaron voice, 36s. Posted IG + FB + TikTok + YouTube.

2026-04-21 — Milo retirement pending — Poller to be rewired to write to pending-research.json. Alex becomes the morning researcher.

2026-04-20 — Habesha AI locked as primary until May 7, 2026 — daily carousel + reel, goal 1K TikTok followers by July 2026.

2026-04-18 — TikTok cadence locked — 2 reels/day TikTok + YouTube, 1/day IG + FB.
