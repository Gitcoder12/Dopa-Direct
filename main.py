import random
import time

from config import (
    FOCUS_LOCK_SECONDS, 
    DEFAULT_ACTIVITIES, 
    TRIGGER_OPTIONS,
    CLR_GREEN,
    CLR_CYAN,
    CLR_YELLOW,
    CLR_RED,
    CLR_RESET
)
from storage import load_data, save_data, get_all_activities
from timer import run_focus_lock
from streaks import record_success, record_failure
from analytics import log_trigger, top_triggers


def choose_trigger():
    """Prompt the user to pick what triggered the urge. Returns a clean name."""
    print(f"\n{CLR_CYAN}What's pulling you in right now?{CLR_RESET}")
    for i, option in enumerate(TRIGGER_OPTIONS, 1):
        print(f"  [{i}] {option}")

    raw = input(f"Select (1-{len(TRIGGER_OPTIONS)}): ").strip()

    try:
        index = int(raw)
        if not 1 <= index <= len(TRIGGER_OPTIONS):
            raise ValueError
        selected = TRIGGER_OPTIONS[index - 1]
    except ValueError:
        return "Unspecified"

    if selected == "Custom":
        custom = input("Name it: ").strip()
        return custom if custom else "Unspecified"

    return selected


def log_impulse(data):
    from adaptive_redirector import get_recommendations, learn_choice
    
    trigger = choose_trigger()
    log_trigger(data, trigger)

    print(f"\n{CLR_YELLOW}⚠️ Trigger Detected: {trigger}{CLR_RESET}")
    print(f"{CLR_CYAN}Recommended Redirects:{CLR_RESET}")
    
    # Pull contextual learned parameters
    recs = get_recommendations(data, trigger, limit=3)
    
    for i, rec in enumerate(recs, 1):
        count_suffix = f" (Chosen {rec['count']}x)" if rec['count'] > 0 else ""
        print(f"  [{i}] {rec['activity']}{CLR_GREEN}{count_suffix}{CLR_RESET}")
    
    # Unified escape slot fallback
    print(f"  [{len(recs) + 1}] Roll an alternative random activity option")
    
    choice_raw = input(f"\nSelect target action (1-{len(recs) + 1}): ").strip()
    
    try:
        choice_idx = int(choice_raw)
        if 1 <= choice_idx <= len(recs):
            chosen_task = recs[choice_idx - 1]["activity"]
        elif choice_idx == len(recs) + 1:
            chosen_task = random.choice(get_all_activities(data))
        else:
            raise ValueError
    except ValueError:
        print(f"\n{CLR_RED}⚠️ Invalid choice selection. Rolling fallback random activity.{CLR_RESET}")
        chosen_task = random.choice(get_all_activities(data))

    print(f"\n⚡ {CLR_GREEN}[REDIRECT INITIALIZED]{CLR_RESET}")
    print(f"Instead of checking {trigger}, commit to this now:")
    print(f"👉 {CLR_YELLOW}{chosen_task}{CLR_RESET}")

    completed = run_focus_lock(FOCUS_LOCK_SECONDS)

    if completed:
        record_success(data)
        
        # Core Optimization: Increment behavioral matrices only on success
        learn_choice(data, trigger, chosen_task)
        
        # 🔗 REAL-TIME ACHIEVEMENT ENGINE HOOK
        from achievements import check_achievements
        new_unlocks = check_achievements(data)
        
        stats = data["stats"]
        print(f"\n🏆 {CLR_GREEN}+10 points | Current streak: {stats['current_streak']} | Best: {stats['best_streak']}{CLR_RESET}")
        
        # 🌟 Instant Reward Banner Sequence
        for ach in new_unlocks:
            print(f"\n✨ {CLR_YELLOW}[ACHIEVEMENT UNLOCKED]{CLR_RESET} ✨")
            print(f"🏅 Name   : {CLR_GREEN}{ach['name']}{CLR_RESET} ({ach['rarity']}{CLR_RESET})")
            print(f"📜 Detail : {ach['desc']}")
            print(f"🎁 Reward : {CLR_YELLOW}+{ach['bonus']} Bonus Points!{CLR_RESET}\n")
    else:
        record_failure(data)
        print(f"\n❌ {CLR_RED}Streak broken. Let's rebuild it on the next run!{CLR_RESET}")

    save_data(data)


def add_custom_activity(data):
    activity = input("\nEnter your custom productive activity: ").strip()
    if not activity:
        print(f"\n{CLR_RED}⚠️ Activity cannot be empty. Nothing added.{CLR_RESET}")
        return

    if activity in data["custom_activities"] or activity in DEFAULT_ACTIVITIES:
        print(f"\n{CLR_RED}⚠️ That activity already exists. Nothing added.{CLR_RESET}")
        return

    data["custom_activities"].append(activity)
    save_data(data)
    print(f"\n{CLR_GREEN}✅ Added: \"{activity}\"{CLR_RESET}")


def view_progress(data):
    from achievements import ACHIEVEMENT_MANIFEST, get_next_achievement
    from adaptive_redirector import get_top_adaptive_pairings
    
    stats = data["stats"]
    triggers = top_triggers(data)
    unlocked_ids = data.setdefault("unlocked_achievements", [])
    focus_score = stats.setdefault("focus_score", 100)
    adaptive_pairings = get_top_adaptive_pairings(data)
    width = 50

    print(f"\n{CLR_CYAN}┌" + "─" * width + "┐")
    print("│" + "YOUR PROGRESS".center(width) + "│")
    print("├" + "─" * width + "┤")
    print(f"│{CLR_RESET} Current Streak    : {CLR_GREEN}{stats['current_streak']:<33}{CLR_CYAN}│")
    print(f"│{CLR_RESET} Best Streak       : {CLR_YELLOW}{stats['best_streak']:<33}{CLR_CYAN}│")
    print(f"│{CLR_RESET} Total Redirects   : {stats['total_redirects']:<33}{CLR_CYAN}│")
    print(f"│{CLR_RESET} Points            : {CLR_GREEN}{stats['points']:<33}{CLR_CYAN}│")
    print(f"│{CLR_RESET} Custom Activities : {len(data['custom_activities'])}".ljust(width + 1) + f"{CLR_CYAN}│")
    
    score_bar_width = 15
    score_filled = int((focus_score / 100) * score_bar_width)
    score_bar = "█" * score_filled + "░" * (score_bar_width - score_filled)
    score_str = f"[{score_bar}] {focus_score}%"
    print(f"│{CLR_RESET} Focus Score       : {CLR_CYAN}{score_str:<33}{CLR_CYAN}│")
    
    print("├" + "─" * width + "┤")
    print("│" + "TOP TRIGGERS".center(width) + "│")
    print("├" + "─" * width + "┤" + CLR_RESET)

    if not triggers:
        print(f"{CLR_CYAN}│{CLR_RESET}" + " No triggers logged yet.".ljust(width) + f"{CLR_CYAN}│")
    else:
        for i, (name, count) in enumerate(triggers, 1):
            display_name = name if len(name) <= 25 else name[:22] + "..."
            line = f" {i}. {display_name} - {count}x"
            print(f"{CLR_CYAN}│{CLR_RESET}" + f"{CLR_YELLOW}{line:<50}"[5:] + f"{CLR_CYAN}│")

    # ==================== NEW: TOP ADAPTIVE REDIRECTS ====================
    print(f"{CLR_CYAN}├" + "─" * width + "┤")
    print("│" + "TOP ADAPTIVE REDIRECTS".center(width) + "│")
    print("├" + "─" * width + "┤" + CLR_RESET)
    
    if not adaptive_pairings:
        print(f"{CLR_CYAN}│{CLR_RESET}" + " No patterns learned yet. Build history!".ljust(width) + f"{CLR_CYAN}│")
    else:
        for trigger, pair in adaptive_pairings.items():
            clean_t = trigger if len(trigger) <= 12 else trigger[:9] + "..."
            clean_a = pair["activity"] if len(pair["activity"]) <= 22 else pair["activity"][:19] + "..."
            line = f" {clean_t} -> {clean_a} ({pair['count']}x)"
            print(f"{CLR_CYAN}│{CLR_RESET}" + f"{CLR_GREEN}{line:<50}"[5:] + f"{CLR_CYAN}│")

    # ==================== UNLOCKED BADGES GRID ====================
    print(f"{CLR_CYAN}├" + "─" * width + "┤")
    print("│" + "UNLOCKED BADGES".center(width) + "│")
    print("├" + "─" * width + "┤" + CLR_RESET)

    if not unlocked_ids:
        print(f"{CLR_CYAN}│{CLR_RESET}" + " No milestones unlocked yet. Build discipline!".ljust(width) + f"{CLR_CYAN}│")
    else:
        for ach_id in unlocked_ids:
            meta = ACHIEVEMENT_MANIFEST.get(ach_id)
            if meta:
                badge_str = f" {meta['name']} ({meta['rarity']}{CLR_RESET})"
                plain_len = len(f" {meta['name']} (⚪ Common)")
                padding = width - plain_len
                print(f"{CLR_CYAN}│{CLR_RESET}" + badge_str + (" " * padding) + f"{CLR_CYAN}│")

    # ==================== NEXT MILESTONE TRACKER ====================
    print(f"{CLR_CYAN}├" + "─" * width + "┤")
    print("│" + "NEXT MILESTONE TRACKER".center(width) + "│")
    print("├" + "─" * width + "┤" + CLR_RESET)
    
    next_ach = get_next_achievement(data)
    if not next_ach:
        print(f"{CLR_CYAN}│{CLR_RESET}" + f" 👑 {CLR_YELLOW}MAX LEVEL: All redirection badges unlocked!{CLR_RESET}".ljust(width + 9) + f"{CLR_CYAN}│")
    else:
        bar_width = 20
        filled = int((next_ach['pct'] / 100) * bar_width)
        bar = "█" * filled + "░" * (bar_width - filled)
        
        line1 = f" Target: {next_ach['name']}"
        line2 = f" Progress: [{bar}] {next_ach['current']}/{next_ach['target']}"
        
        print(f"{CLR_CYAN}│{CLR_RESET}" + line1.ljust(width) + f"{CLR_CYAN}│")
        print(f"{CLR_CYAN}│{CLR_RESET}" + line2.ljust(width) + f"{CLR_CYAN}│")

    print(f"{CLR_CYAN}└" + "─" * width + f"┘{CLR_RESET}")


def main():
    data = load_data()
    
    # 🧭 INITIALIZE PASSIVE BACKGROUND ATTENTION GUARDIAN
    from guardian import start_attention_guardian
    start_attention_guardian(data, save_data)

    while True:
        # 👑 UPDATED VERSION HEADER FOR THE ADAPTIVE LOOP
        print(f"\n{CLR_CYAN}=================================================={CLR_RESET}")
        print(f"     {CLR_GREEN}DOPA-DIRECT v5.2: THE ADAPTIVE REDIRECTOR{CLR_RESET}     ")
        print(f"{CLR_CYAN}=================================================={CLR_RESET}")
        
        print(f" [1] Log an Instant-Gratification Impulse")
        print(f" [2] Add Custom Productive Activity")
        print(f" [3] View Progress")
        print(f" [4] Exit Workspace")

        choice = input("\nSelect an action: ").strip()

        if choice == "1":
            log_impulse(data)
        elif choice == "2":
            add_custom_activity(data)
        elif choice == "3":
            view_progress(data)
        elif choice == "4":
            print(f"\n{CLR_GREEN}Exiting workspace. Stay focused and keep building, developer!{CLR_RESET}")
            break
        else:
            print(f"\n{CLR_RED}⚠️ Invalid choice. Pick 1-4.{CLR_RESET}")


if __name__ == "__main__":
    main()
