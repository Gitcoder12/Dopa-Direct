import time
import random

# Core list of productive alternative tasks
PRODUCTIVE_ACTIVITIES = [
    "Write 10 lines of code for Dopa-Direct.",
    "Read 5 pages of your current research paper or book.",
    "Do a 2-minute stretching or breathing exercise.",
    "Review your Git repository status and plan your next feature.",
    "Learn 3 new terminal navigation shortcuts."
]

def main():
    print("\n=========================================")
    print("      DOPA-DIRECT: ANTIDOTE TO THE LOOP   ")
    print("=========================================\n")
    
    # Quick logging step
    print("[1] Log a Distraction Impulse")
    print("[2] Exit Workspace")
    choice = input("\nSelect an option: ").strip()
    
    if choice == "1":
        impulse = input("\nWhat is trying to hijack your focus right now? (e.g., YouTube, Reddit): ")
        print(f"\n[Intercepting] Acknowledging impulse to check {impulse}...")
        time.sleep(1.5)
        
        # Actionable replacement
        suggestion = random.choice(PRODUCTIVE_ACTIVITIES)
        print("\n--> IMPULSE REDIRECTED SUCCESSFULY! <--")
        print(f"Instead of opening that app, do this right now:\n👉 {suggestion}\n")
    else:
        print("\nExiting workspace. Stay focused out there!")

if __name__ == "__main__":
    main()
