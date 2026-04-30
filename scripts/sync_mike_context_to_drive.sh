#!/bin/bash
# Sync MIKE-CONTEXT.md from local bisrat-ops repo → Habesha AI Google Drive
# so Mike (Claude.ai web) can read fresh strategic context via his Drive
# integration. The bisrat-ops GitHub repo is private and Mike cannot fetch
# raw URLs from it; Drive is the canonical mirror.
#
# Wired into the Claude Code Stop hook in ~/.claude/settings.json so it runs
# at the end of every James session — after the local file has had a chance
# to be updated during the session.
#
# Idempotent: rclone copy compares sizes/mtimes and only uploads if changed.

set -u

SOURCE="$HOME/projects/bisrat-ops/MIKE-CONTEXT.md"
DEST_DIR="habesha-drive:HabeshaAI/context"
LOG="/tmp/sync-mike-context.log"

if [ ! -f "$SOURCE" ]; then
    echo "[$(date '+%Y-%m-%d %H:%M:%S')] FAIL: source missing: $SOURCE" >> "$LOG"
    exit 0  # don't block Stop hook on missing source
fi

# rclone --quiet suppresses normal output; errors still go to stderr
if rclone copy "$SOURCE" "$DEST_DIR/" --quiet 2>>"$LOG"; then
    SIZE=$(stat -f%z "$SOURCE" 2>/dev/null || stat -c%s "$SOURCE")
    echo "[$(date '+%Y-%m-%d %H:%M:%S')] OK: synced $SIZE bytes → $DEST_DIR/" >> "$LOG"
else
    echo "[$(date '+%Y-%m-%d %H:%M:%S')] FAIL: rclone exit $?" >> "$LOG"
fi

exit 0
