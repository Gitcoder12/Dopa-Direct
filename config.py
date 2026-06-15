DATA_FILE = "dopa_data.json"
FOCUS_LOCK_SECONDS = 60

DEFAULT_ACTIVITIES = [
    "Write 10 lines of code for Dopa-Direct.",
    "Read 5 pages of your current research paper or book.",
    "Do a 2-minute stretching or breathing exercise.",
    "Review your Git repository status and plan your next feature.",
    "Learn 3 new terminal navigation shortcuts.",
    "Drink a glass of water and close your eyes for 60 seconds.",
]

TRIGGER_OPTIONS = [
    "YouTube",
    "Instagram",
    "Reddit",
    "Twitter/X",
    "WhatsApp",
    "Custom",
]

DEFAULT_DATA = {
    "custom_activities": [],
    "unlocked_achievements": [],
    "stats": {
        "current_streak": 0,
        "best_streak": 0,
        "total_redirects": 0,
        "points": 0,
        "focus_score": 100,
    },
    "triggers": {},
}

# Simple, dependency-free ANSI Colors
CLR_GREEN = "\033[92m"
CLR_CYAN = "\033[96m"
CLR_YELLOW = "\033[93m"
CLR_RED = "\033[91m"
CLR_RESET = "\033[0m"

# ==================== v5.0 ATTENTION GUARDIAN CONFIGS ====================
GUARDIAN_POLL_INTERVAL_SECONDS = 60

DISTRACTION_KEYWORDS = [
    "youtube", "reddit", "instagram", "facebook", 
    "twitter", "x.com", "shorts", "reels", "netflix"
]
