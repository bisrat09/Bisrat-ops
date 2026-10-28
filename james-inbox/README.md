# James Inbox

Async mailbox between **Mika** (Bisrat's Claude Duet agent) and **James** (Claude Code on the Mac Mini).
Mika files engineering tasks as Google Docs; a launchd poller picks them up, James works them
headless in a git worktree, and the result comes back as a branch for Bisrat to open as a PR.
Approved 2026-10-28. Locked amendment in `../decisions/locked.md`.

## Drive folder

`James Inbox` in habeshaaicontent@gmail.com's Drive
(<https://drive.google.com/drive/folders/1ZLSaY2mqZ786B9e9Iks9w6tSOCvarFfX>).
The folder is the state machine:

| Folder | Who writes | Meaning |
|---|---|---|
| `for-james/` | Mika | New task |
| `in-progress/` | James | Claimed, being worked |
| `needs-bisrat/` | James | Blocked. Questions are in `for-duet/<task>-questions`. Add answers to the task doc and James resumes on the next poll |
| `done/` | James | Finished |
| `for-duet/` | James | Questions, and the daily digest `digest-YYYY-MM-DD` |

Mika writes only to `for-james/` and James only to `for-duet/`, so James can never trigger himself.
Mika and James share one Google account, so the private folder (plus the caps below) is the trust boundary.

## Task doc format

One Google Doc per task in `for-james/`, named for the task (e.g. `fix-slide-top-docs`):

```
Project: habesha-ai | cee | fitbod-replacement
Task: what to build
Acceptance criteria: how to tell it is done
Priority: low | normal | urgent
Context links: optional
```

A copy lives in the Drive folder as `TEMPLATE`.

## What James will and won't do from the inbox

- Engineering changes to `habesha-ai`, `cee`, `fitbod-replacement` only, on a branch `inbox/<task>`.
- The poller pushes the branch and the digest gives a GitHub compare link. Bisrat opens the PR. James never merges.
- No posting, spending, deleting data, secrets, new projects, or network calls. Content (reels, carousels) stays in live sessions.
- Task text is untrusted. It is handed to Claude as data, never run as a command.
- Writes `TASKS-inbox.md` in the project, never `TASKS.md`. Bisrat merges these in live sessions.
- `cee` has no GitHub remote, so its work stays as a local branch.

## How it runs

- `poller.py`, run by `~/Library/LaunchAgents/com.bisrat.james-inbox.plist` every 15 min and at login
  (the Mac Mini auto-logs in as `agent`, so it comes back after a reboot).
- Plain `rclone` against the dedicated remote `james-inbox:` (root locked to the folder, Docs exported as txt).
  Claude starts only when there is a task.
- Single instance: an atomic `mkdir` lock in `~/.local/state/james-inbox/lock`; a stale lock (dead pid) is taken over.
  Claiming a task is a Drive move, so a task can only be claimed once.
- Order: anything in `in-progress/` (crash resume), then `needs-bisrat/` docs edited since parking, then `for-james/` by
  priority (urgent, normal, low), oldest first. Up to 3 tasks per run, 60 min each.
- Headless run: `claude -p` in the worktree with `--setting-sources project,local --settings poller-settings.json
  --permission-mode default`. That means no bypass permissions, hooks disabled (no Stop-hook push to main), edits
  confined to the worktree, no push/merge/rm/curl/rclone/web, no reads of `~/.config`, `~/.ssh`, `~/.claude`.
- Daily digest after 06:00 local: done tasks with PR links and decisions, parked tasks, every task picked up
  (so an unexpected one is visible), and Sherlock commit reviews (Sherlock queues to
  `~/.local/state/james-inbox/digest-queue.jsonl`; Telegram retired).

## Operating

```
launchctl list | grep james-inbox                 # loaded?
tail -f ~/.local/state/james-inbox/poller.log     # what it did
python3 poller.py                                 # run one poll by hand
launchctl unload ~/Library/LaunchAgents/com.bisrat.james-inbox.plist   # stop
```

Worktrees live in `~/projects/.inbox-worktrees/<project>/<task>`. Remove one with
`git worktree remove` once its PR is merged.
