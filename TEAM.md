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

## James (Claude Code)
- Role: Engineering Lead
- Handles: all building, coding, committing, pushing, carousel/reel production, pipeline maintenance
- Works in: ~/projects/habesha-ai (primary), ~/projects/james-telegram-bridge, ~/personal/cee
- Two instances: Terminal James (Mac Mini, nights) and Dispatch (Claude Code mobile, daytime)
- Syncs via: JAMES-HANDOFF-snapshot.md + data/session-bookends.md on GitHub main
- Model: Claude Sonnet 4.6 (default). Opus only when Bisrat explicitly requests.

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
