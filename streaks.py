"""Streak and points bookkeeping for Dopa-Direct v5.0."""

def record_success(data):
    """Update stats after a fully completed cooldown."""
    stats = data["stats"]
    stats["current_streak"] += 1
    stats["total_redirects"] += 1
    stats["points"] += 10
    stats["best_streak"] = max(stats["best_streak"], stats["current_streak"])
    
    # 🎯 v5.0 Focus Score Reward (Capped at 100 Max)
    stats["focus_score"] = min(100, stats.get("focus_score", 100) + 10)

def record_failure(data):
    """Reset the current streak after a bypassed cooldown."""
    stats = data["stats"]
    stats["current_streak"] = 0
    
    # Severe penalty if they violently escape focus lock mid-timer
    stats["focus_score"] = max(0, stats.get("focus_score", 100) - 20)
