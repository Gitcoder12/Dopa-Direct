"""Attention Guardian Lite Daemon for Dopa-Direct v5.0."""
import ctypes
import time
import threading
from config import DISTRACTION_KEYWORDS, GUARDIAN_POLL_INTERVAL_SECONDS, CLR_RED, CLR_CYAN, CLR_RESET

# Native Windows API Setup
user32 = ctypes.windll.user32

def get_active_window_title():
    """Returns the title string of the current foreground window on Windows."""
    hwnd = user32.GetForegroundWindow()
    length = user32.GetWindowTextLengthW(hwnd)
    if length > 0:
        buffer = ctypes.create_unicode_buffer(length + 1)
        user32.GetWindowTextW(hwnd, buffer, length + 1)
        return buffer.value
    return ""

def guardian_worker(data_ref, save_callback):
    """Background loop checking active apps without blocking the CLI loop."""
    drift_counter = 0
    
    while True:
        time.sleep(GUARDIAN_POLL_INTERVAL_SECONDS)
        
        try:
            title = get_active_window_title().lower()
            if not title:
                continue
                
            # Scan title against your specific distraction watch list
            matched_keyword = next((kw for kw in DISTRACTION_KEYWORDS if kw in title), None)
            
            if matched_keyword:
                drift_counter += 1
                stats = data_ref["stats"]
                
                # Apply focus score penalty bounded safely at zero
                stats["focus_score"] = max(0, stats.get("focus_score", 100) - 10)
                save_callback(data_ref)
                
                # Flash the non-intrusive terminal warning block
                print(f"\n\n{CLR_RED}╔══════════════════════════════════════════════════╗")
                print(f"║  🧭  ATTENTION GUARDIAN ALERT                    ║")
                print(f"╠══════════════════════════════════════════════════╣")
                print(f"║ Your attention may be drifting...                ║")
                print(f"║ Detected Active Window Match: {matched_keyword.title():<19}║")
                print(f"║ Drift Count: {drift_counter:<4} | Current Focus Score: {stats['focus_score']}/100 ║")
                print(f"╠══════════════════════════════════════════════════╣")
                print(f"║   👉 [Option 1] Log an Impulse to break loop!     ║")
                print(f"╚══════════════════════════════════════════════════╝{CLR_RESET}\nSelect an action: ", end="", flush=True)
                
        except Exception:
            pass  # Ensure the background thread never crashes out silently

def start_attention_guardian(data, save_function):
    """Initializes and detaches the asynchronous daemon monitor."""
    guardian_thread = threading.Thread(
        target=guardian_worker, 
        args=(data, save_function), 
        daemon=True  # Thread safely self-destructs when main.py exits
    )
    guardian_thread.start()
