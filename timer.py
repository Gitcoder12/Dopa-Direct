import sys
import time


def run_focus_lock(seconds):
    """Live countdown timer. Returns True if completed, False if interrupted."""
    print("\n🔒 [FOCUS LOCK ACTIVE] Do not close this terminal. Let your craving fade...")
    try:
        while seconds > 0:
            mins, secs = divmod(seconds, 60)
            sys.stdout.write(f"\r⏳ Time remaining: {mins:02d}:{secs:02d} ")
            sys.stdout.flush()
            time.sleep(1)
            seconds -= 1
        sys.stdout.write("\r" + " " * 30 + "\r")
        print("✅ Cooldown complete! Loop broken. Now go build something great.")
        return True
    except KeyboardInterrupt:
        sys.stdout.write("\r" + " " * 30 + "\r")
        print("⚠️ Focus lock bypassed early! Streak reset. Stay disciplined next time!")
        return False
