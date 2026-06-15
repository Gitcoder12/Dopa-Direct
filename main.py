import random
import time

from config import FOCUS_LOCK_SECONDS, DEFAULT_ACTIVITIES
from storage import load_data, save_data, get_all_activities
from timer import run_focus_lock


def log_impulse(data):
    impulse = input("\nWhat app/site is trying to hijack your brain? (e.g., YouTube, Reddit): ").strip()
    if not impulse:
        impulse = "that thing"

    print(f"\n[Intercepting] Catching impulse to open {impulse}...")
    time.sleep(1)

    task = random.choice(get_all_activities(data))
    print("\n⚡ [REDIRECT SUCCESSFUL]")
    print(f"Instead of checking {impulse}, do this immediately:")
    print(f"👉 {task}")

    completed = run_focus_lock(FOCUS_LOCK_SECONDS)
    stats = data["stats"]

    if completed:
        stats["current_streak"] += 1
        stats["total_completions"] += 1
        stats["points"] += 10
        stats["best_streak"] = max(stats["best_streak"], stats["current_streak"])
        print(f"\n🏆 +10 points | Current streak: {stats['current_streak']} | Best: {stats['best_streak']}")
    else:
        stats["current_streak"] = 0

    save_data(data)


def add_custom_activity(data):
    activity = input("\nEnter your custom productive activity: ").strip()
    if not activity:
        print("\n⚠️ Activity cannot be empty. Nothing added.")
        return

    if activity in data["custom_activities"] or activity in DEFAULT_ACTIVITIES:
        print("\n⚠️ That activity already exists. Nothing added.")
        return

    data["custom_activities"].append(activity)
    save_data(data)
    print(f"\n✅ Added: \"{activity}\"")


def view_stats(data):
    stats = data["stats"]
    print("\n==================================================")
    print("                  YOUR STATS                       ")
    print("==================================================")
    print(f"Current streak     : {stats['current_streak']}")
    print(f"Best streak        : {stats['best_streak']}")
    print(f"Total cooldowns won: {stats['total_completions']}")
    print(f"Points             : {stats['points']}")
    print(f"Custom activities  : {len(data['custom_activities'])}")


def main():
    data = load_data()

    while True:
        print("\n==================================================")
        print("        DOPA-DIRECT v2.0: THE LOOP INTERCEPTOR     ")
        print("==================================================")
        print("\n[1] Log an Instant-Gratification Impulse")
        print("[2] Add Custom Productive Activity")
        print("[3] View Stats")
        print("[4] Exit Workspace")

        choice = input("\nSelect an action: ").strip()

        if choice == "1":
            log_impulse(data)
        elif choice == "2":
            add_custom_activity(data)
        elif choice == "3":
            view_stats(data)
        elif choice == "4":
            print("\nExiting workspace. Stay focused and keep building, developer!")
            break
        else:
            print("\n⚠️ Invalid choice. Pick 1-4.")


if __name__ == "__main__":
    main()