#!/usr/bin/env python3
"""Keep MIKE-CONTEXT.md's Strategy Log from silently falling behind what shipped.

The failure this exists to prevent (2026-07-29 → 2026-08-18): five reels went out
on all four platforms and none reached Mike, because appending to the Strategy Log
was a manual step that depended on a James remembering it. The Drive sync ran fine
the whole time; it just mirrored a stale file.

What this does, in order:

  1. Reads habesha-ai/analytics/posted-articles.json for posted reels.
  2. Finds any whose slug is not already mentioned anywhere in MIKE-CONTEXT.md.
  3. Appends a factual AUTO-LOGGED stub for each, newest first, at the top of the
     Strategy Log — verified fields only (title, platforms, notes, engagement).
  4. Commits and pushes bisrat-ops if MIKE-CONTEXT.md is dirty for any reason,
     including hand-written edits made during the session.

It deliberately does NOT write strategy. Mike's value comes from analysis, and a
model inventing a strategic read at Stop-hook time would be worse than a gap
because it would look authoritative. Stubs are tagged so Mike can tell the
difference, and the script prints which ones still need a human note.

Idempotent: re-running appends nothing once a slug is present in the file.
Never blocks the Stop hook — all failures exit 0 with a message.
"""

import json
import os
import re
import subprocess
import sys
from datetime import datetime, timedelta, timezone

OPS = os.path.expanduser("~/projects/bisrat-ops")
CONTEXT = os.path.join(OPS, "MIKE-CONTEXT.md")
TRACKER = os.path.expanduser(
    "~/projects/habesha-ai/analytics/posted-articles.json"
)
LOG_HEADER = "## Strategy Log — most recent first"
STUB_TAG = "[AUTO-LOGGED — needs James's strategic note]"
DATE_LINE = re.compile(r"^(\d{4}-\d{2}-\d{2})", re.MULTILINE)

# How far back of the newest logged entry we are willing to look. Bounds the
# backfill so a one-off tracker repair can't dump months of history into Mike's
# file, while still tolerating entries written slightly out of date order.
LOOKBACK_DAYS = 21


def load_posted_reels():
    """Return posted reels from the tracker, oldest first. [] on any problem.

    A reel counts as posted if status says so OR it has platforms recorded.
    Six reels in the tracker as of 2026-08-18 (including kimi-k3, the last one
    Mike ever saw) have platforms_posted set but status unset, so keying on
    status alone would silently skip exactly the entries this script exists to
    catch.
    """
    try:
        with open(TRACKER, encoding="utf-8") as f:
            data = json.load(f)
    except Exception as e:
        print(f"[sync_mike_context] cannot read tracker: {e}")
        return []

    posts = data if isinstance(data, list) else data.get("posts", [])
    reels = []
    for p in posts:
        if not isinstance(p, dict):
            continue
        if p.get("content_type") != "reel":
            continue
        if not p.get("slug") or not p.get("posted_at"):
            continue
        if p.get("status") != "posted" and not p.get("platforms_posted"):
            continue
        reels.append(p)

    reels.sort(key=lambda p: str(p.get("posted_at")))
    return reels


def lookback_floor(text):
    """Earliest posted_at we will consider, as a YYYY-MM-DD string.

    Anchored to the newest date already in the file so the window travels
    forward as the log is maintained. Returns None if no dates are parseable,
    in which case the caller falls back to slug-presence alone.
    """
    dates = DATE_LINE.findall(text)
    if not dates:
        return None
    try:
        newest = max(datetime.strptime(d, "%Y-%m-%d") for d in dates)
    except ValueError:
        return None
    return (newest - timedelta(days=LOOKBACK_DAYS)).strftime("%Y-%m-%d")


def format_engagement(post):
    """One line per platform we actually have numbers for."""
    eng = post.get("engagement") or {}
    by_platform = eng.get("by_platform") or {}
    if not by_platform:
        return "  Engagement: not yet pulled."

    lines = []
    for platform, v in sorted(by_platform.items()):
        reach = v.get("reach")
        er = v.get("engagement_rate")
        likes = v.get("likes")
        shares = v.get("shares")
        if reach is None:
            continue
        lines.append(
            f"  {platform}: reach={reach} likes={likes} "
            f"shares={shares} ER={er}%"
        )

    if not lines:
        return "  Engagement: no per-platform data returned."
    return "\n".join(lines)


def build_stub(post):
    date = str(post.get("posted_at"))[:10]
    title = post.get("title") or post.get("slug")
    platforms = post.get("platforms_posted") or []
    notes = (post.get("notes") or "").strip()

    body = [
        f"{date} — {STUB_TAG} {title}",
        f"  Slug: {post.get('slug')}",
        f"  Posted to: {', '.join(platforms) if platforms else 'unknown'}",
    ]
    if notes:
        body.append(f"  Build notes from tracker: {notes}")
    body.append(format_engagement(post))
    return "\n".join(body)


def already_logged(post, text):
    """True if this reel plausibly already has an entry, stub or hand-written.

    The slug itself is the reliable signal, but James writes prose headlines
    ("KIMI K3 REEL SHIPPED ALL 4 PLATFORMS") that never contain the slug. So we
    also look for the slug's descriptive tail as a phrase with flexible
    separators, which matches "KIMI K3", "DEAN / HASSABIS", "WU SESAME".
    Erring toward "already logged" would recreate the original bug, so this
    stays deliberately strict: every token must appear, in order.
    """
    slug = str(post.get("slug", ""))
    if not slug:
        return True
    if slug in text:
        return True

    tail = re.sub(r"^\d{4}-\d{2}-\d{2}-", "", slug)
    tokens = [t for t in tail.split("-") if t]
    if not tokens:
        return False

    phrase = r"[\s\-/]+".join(re.escape(t) for t in tokens)
    return re.search(phrase, text, re.IGNORECASE) is not None


def insert_stub(text, date, block):
    """Insert one stub in date order, preserving most-recent-first."""
    idx = text.find(LOG_HEADER)
    if idx == -1:
        print("[sync_mike_context] Strategy Log header not found, appending at end")
        return text.rstrip() + "\n\n" + block + "\n"

    cut = idx + len(LOG_HEADER)
    # Land above the first existing entry that is older than this one.
    for m in DATE_LINE.finditer(text, cut):
        if m.group(1) < date:
            return text[:m.start()] + block + "\n\n" + text[m.start():]

    # Older than everything logged: append at the very end of the file.
    return text.rstrip() + "\n\n" + block + "\n"


def git(*args):
    return subprocess.run(
        ["git", "-C", OPS, *args],
        capture_output=True,
        text=True,
    )


def main():
    if not os.path.exists(CONTEXT):
        print(f"[sync_mike_context] missing {CONTEXT}, nothing to do")
        return

    with open(CONTEXT, encoding="utf-8") as f:
        text = f.read()

    reels = load_posted_reels()

    missing = [p for p in reels if not already_logged(p, text)]

    # Bound how far back we reach, so old tracker rows stay out of Mike's file.
    floor = lookback_floor(text)
    if floor:
        skipped = [p for p in missing if str(p.get("posted_at"))[:10] < floor]
        missing = [p for p in missing if str(p.get("posted_at"))[:10] >= floor]
        if skipped:
            print(
                f"[sync_mike_context] {len(skipped)} unlogged reel(s) older "
                f"than {floor} left alone (outside {LOOKBACK_DAYS}-day window):"
            )
            for p in skipped:
                print(f"    {str(p.get('posted_at'))[:10]}  {p.get('slug')}")

    if missing:
        for p in missing:  # oldest first, so each lands above the one before
            text = insert_stub(text, str(p.get("posted_at"))[:10], build_stub(p))
        with open(CONTEXT, "w", encoding="utf-8") as f:
            f.write(text)
        print(
            f"[sync_mike_context] appended {len(missing)} auto-logged "
            f"entr{'y' if len(missing) == 1 else 'ies'}:"
        )
        for p in missing:
            print(f"    {str(p.get('posted_at'))[:10]}  {p.get('slug')}")
        print("[sync_mike_context] these are FACTS ONLY and still need a "
              "strategic note from James.")
    else:
        print("[sync_mike_context] Strategy Log is current, no reels missing")

    # Commit whatever is dirty — stubs above, or James's own edits this session.
    status = git("status", "--porcelain", "MIKE-CONTEXT.md")
    if not status.stdout.strip():
        print("[sync_mike_context] MIKE-CONTEXT.md clean, nothing to push")
        return

    stamp = datetime.now(timezone.utc).strftime("%Y-%m-%d")
    git("add", "MIKE-CONTEXT.md")
    commit = git("commit", "-m", f"chore: update mike context ({stamp})")
    if commit.returncode != 0:
        print(f"[sync_mike_context] commit failed: {commit.stderr.strip()}")
        return

    push = git("push")
    if push.returncode != 0:
        print(f"[sync_mike_context] push failed: {push.stderr.strip()}")
        return

    print("[sync_mike_context] committed and pushed MIKE-CONTEXT.md")


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        # Never block the Stop hook.
        print(f"[sync_mike_context] unexpected error, continuing: {e}")
    sys.exit(0)
