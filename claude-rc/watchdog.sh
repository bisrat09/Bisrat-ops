#!/bin/bash
# Keeps `claude remote-control` (server mode) alive in tmux session "claude-rc".
# Run every 60s by launchd (com.bisrat.claude-rc). Phone: Claude app > Code, or claude.ai/code.
# Attach locally: tmux attach -t claude-rc   (detach: Ctrl-b d)
# Stop for good: launchctl unload ~/Library/LaunchAgents/com.bisrat.claude-rc.plist && tmux kill-session -t claude-rc
export PATH=/opt/homebrew/bin:/usr/local/bin:/usr/bin:/bin:/usr/sbin:/sbin
export HOME=/Users/agent
SESSION=claude-rc
LOG=$HOME/.local/state/claude-rc/watchdog.log
mkdir -p "$(dirname "$LOG")"
if tmux has-session -t "$SESSION" 2>/dev/null; then exit 0; fi
echo "$(date '+%F %T') starting $SESSION" >> "$LOG"
cd "$HOME/projects" || exit 1
# The loop restarts the server if it exits (e.g. after ~10 min without network).
tmux new-session -d -s "$SESSION" -x 200 -y 50 \
  "while true; do claude remote-control --name 'Mac Mini' --spawn same-dir --permission-mode auto; echo \"\$(date '+%F %T') server exited \$?\" >> $LOG; sleep 15; done"
