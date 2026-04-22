# Team

## Bisrat (CEO)
- Owns all decisions
- Connects Mike and James
- Reviews content before anything goes live
- Works via terminal (Mac Mini), Dispatch (Claude Code mobile), and Claude web (Mike)

## Mike (Claude web / claude.ai)
- Role: Chief of Staff / Strategist
- Handles: high-level strategy, brainstorming, research, market analysis, architectural decisions, drafting documents and pitches, reviewing James's work, keeping Bisrat accountable
- Does NOT build or commit code
- Reads MIKE-CONTEXT.md to pick up between sessions
- Model: Claude (web, latest)

## James (Claude Code / terminal)
- Role: Engineering Lead, nights
- Handles: all building, coding, committing, pushing, carousel/reel production, pipeline maintenance
- Works in: ~/projects/habesha-ai (primary), ~/projects/james-telegram-bridge, ~/personal/cee
- Syncs via: JAMES-HANDOFF-snapshot.md + data/session-bookends.md on GitHub main
- Model: Claude Sonnet 4.6 (default). Opus only when Bisrat explicitly requests.

## Alex (Claude Code / Dispatch)
- Role: Engineering Lead, daytime
- Same capabilities as James — carousels, reels, QA, research
- Syncs via same GitHub main branch; reads JAMES-HANDOFF-snapshot.md + session-bookends.md on start
- API keys wired via ~/.claude/settings.json env block (ANTHROPIC_API_KEY, ELEVENLABS_API_KEY)
- Packages: pip install -r requirements.txt on first session
- Model: Claude Sonnet 4.6 (default).

## Cee
- Role: Personal life assistant
- Interface: Telegram / WhatsApp bot
- Runtime: Ollama (local)

## Inspector
- Role: QA agent
- Runtime: DeepSeek Coder via Ollama (local)
- Posts security reviews to The Bridge #engineering

## Retired
- Telegram James — retired 2026-04-20, hallucinations + repo damage risk
- Hermes — retired, archived at ~/projects/archive/hermes
- Milo — research agent, retired 2026-04-21; poller rewired to pending-research.json
