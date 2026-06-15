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
    trigger = choose_trigger()
    log_trigger(data, trigger)

    print(f"\n{CLR_YELLOW}[Intercepting] Catching impulse to open {trigger}...{CLR_RESET}")
    time.sleep(1)

    task = random.choice(get_all_activities(data))
    print(f"\n⚡ {CLR_GREEN}[REDIRECT SUCCESSFUL]{CLR_RESET}")
    print(f"Instead of checking {trigger}, do this immediately:")
    print(f"👉 {CLR_YELLOW}{task}{CLR_RESET}")

    completed = run_focus_lock(FOCUS_LOCK_SECONDS)

    if completed:
        record_success(data)
        stats = data["stats"]
        print(f"\n🏆 {CLR_GREEN}+10 points | Current streak: {stats['current_streak']} | Best: {stats['best_streak']}{CLR_RESET}")
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
    stats = data["stats"]
    triggers = top_triggers(data)
    width = 50

    # Colorful Dashboard Layout
    print(f"\n{CLR_CYAN}┌" + "─" * width + "┐")
    print("│" + "YOUR PROGRESS".center(width) + "│")
    print("├" + "─" * width + "┤")
    print(f"│{CLR_RESET} Current Streak    : {CLR_GREEN}{stats['current_streak']:<33}{CLR_CYAN}│")
    print(f"│{CLR_RESET} Best Streak       : {CLR_YELLOW}{stats['best_streak']:<33}{CLR_CYAN}│")
    print(f"│{CLR_RESET} Total Redirects   : {stats['total_redirects']:<33}{CLR_CYAN}│")
    print(f"│{CLR_RESET} Points            : {CLR_GREEN}{stats['points']:<33}{CLR_CYAN}│")
    print(f"│{CLR_RESET} Custom Activities : {len(data['custom_activities'])}".ljust(width + 1) + f"{CLR_CYAN}│")
    print("├" + "─" * width + "┤")
    print("│" + "TOP TRIGGERS".center(width) + "│")
    print("├" + "─" * width + "┤" + CLR_RESET)

    if not triggers:
        print(f"{CLR_CYAN}│{CLR_RESET}" + " No triggers logged yet.".ljust(width) + f"{CLR_CYAN}│")
    else:
        for i, (name, count) in enumerate(triggers, 1):
            display_name = name if len(name) <= 25 else name[:22] + "..."
            line = f" {i}. {display_name} - {count}x"
            # Keep string length calculated cleanly for the box format
            print(f"{CLR_CYAN}│{CLR_RESET}" + f"{CLR_YELLOW}{line:<50}"[5:] + f"{CLR_CYAN}│")

    print(f"{CLR_CYAN}└" + "─" * width + f"┘{CLR_RESET}")


def main():
    data = load_data()

    while True:
        print(f"\n{CLR_CYAN}=================================================={CLR_RESET}")
        print(f"        {CLR_GREEN}DOPA-DIRECT v3.0: THE LOOP INTERCEPTOR{CLR_RESET}     ")
        print(f"{CLR_CYAN}=================================================={CLR_RESET}")
        print("\n[1] Log an Instant-Gratification Impulse")
        print("[2] Add Custom Productive Activity")
        print("[3] View Progress")
        print("[4] Exit Workspace")

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
