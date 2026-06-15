"""Streak and points bookkeeping for Dopa-Direct."""


def record_success(data):
    """Update stats after a fully completed cooldown."""
    stats = data["stats"]
    stats["current_streak"] += 1
    stats["total_redirects"] += 1
    stats["points"] += 10
    stats["best_streak"] = max(stats["best_streak"], stats["current_streak"])


def record_failure(data):
    """Reset the current streak after a bypassed cooldown."""
    data["stats"]["current_streak"] = 0
