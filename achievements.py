"""Achievement Engine for Dopa-Direct v4.0."""

# Rarity Color Formatting Constants
R_COMMON = "\033[37m⚪ Common"
R_RARE = "\033[96m🔵 Rare"
R_EPIC = "\033[95m🟣 Epic"
R_LEGENDARY = "\033[93m🟡 Legendary"
CLR_RESET = "\033[0m"
CLR_GREEN = "\033[92m"

ACHIEVEMENT_MANIFEST = {
    "first_step": {
        "name": "First Redirect",
        "desc": "Intercept your very first digital impulse.",
        "rarity": R_COMMON,
        "bonus": 50,
        "check": lambda stats, data: stats.get("total_redirects", 0) >= 1
    },
    "bronze_redirect": {
        "name": "Interception Novice",
        "desc": "Successfully break 10 impulsive loops.",
        "rarity": R_COMMON,
        "bonus": 100,
        "check": lambda stats, data: stats.get("total_redirects", 0) >= 1
    },
    "silver_redirect": {
        "name": "Focus Warrior",
        "desc": "Successfully break 50 impulsive loops.",
        "rarity": R_RARE,
        "bonus": 250,
        "check": lambda stats, data: stats.get("total_redirects", 0) >= 50
    },
    "gold_redirect": {
        "name": "Habit Breaker",
        "desc": "Reach 100 total documented impulse redirections.",
        "rarity": R_EPIC,
        "bonus": 500,
        "check": lambda stats, data: stats.get("total_redirects", 0) >= 100
    },
    "streak_3": {
        "name": "Consistency Spark",
        "desc": "Maintain a solid 3-session focus streak.",
        "rarity": R_COMMON,
        "bonus": 150,
        "check": lambda stats, data: stats.get("current_streak", 0) >= 3
    },
    "streak_7": {
        "name": "Week of Fire",
        "desc": "Maintain a burning 7-session focus streak.",
        "rarity": R_RARE,
        "bonus": 300,
        "check": lambda stats, data: stats.get("current_streak", 0) >= 7
    },
    "streak_30": {
        "name": "Volcanic Discipline",
        "desc": "Unstoppable force. Maintain a 30-session streak.",
        "rarity": R_LEGENDARY,
        "bonus": 1000,
        "check": lambda stats, data: stats.get("current_streak", 0) >= 30
    },
    "custom_builder": {
        "name": "Intentional Architect",
        "desc": "Register your first custom high-utility activity.",
        "rarity": R_COMMON,
        "bonus": 75,
        "check": lambda stats, data: len(data.get("custom_activities", [])) >= 1
    }
}

def check_achievements(data):
    """
    Evaluates current system states against the Achievement Manifest.
    Appends newly unlocked IDs, grants bonus points, and returns unlocked names.
    """
    stats = data["stats"]
    unlocked_list = data.setdefault("unlocked_achievements", [])
    newly_unlocked = []

    for ach_id, meta in ACHIEVEMENT_MANIFEST.items():
        if ach_id not in unlocked_list:
            # Safe evaluation utilizing your >= comparison design
            if meta["check"](stats, data):
                unlocked_list.append(ach_id)
                stats["points"] += meta["bonus"]
                newly_unlocked.append(meta)
                
    return newly_unlocked

def get_next_achievement(data):
    """Calculates progress details for the closest locked redirection achievement."""
    stats = data["stats"]
    unlocked = data.setdefault("unlocked_achievements", [])
    redirects = stats.get("total_redirects", 0)
    
    # Trackers for redirect thresholds
    thresholds = [
        ("first_step", "First Redirect", 1),
        ("bronze_redirect", "Interception Novice", 10),
        ("silver_redirect", "Focus Warrior", 50),
        ("gold_redirect", "Habit Breaker", 100)
    ]
    
    for ach_id, name, target in thresholds:
        if ach_id not in unlocked:
            progress_pct = min(100, int((redirects / target) * 100))
            return {"name": name, "current": redirects, "target": target, "pct": progress_pct}
            
    return None
