"""Windows foreground-window monitor for Dopa-Direct's optional Attention Guardian."""

from __future__ import annotations

import ctypes
import os
import threading
import time
from typing import Callable

from config import (
    CLR_CYAN,
    CLR_RED,
    CLR_RESET,
    DISTRACTION_KEYWORDS,
    GUARDIAN_POLL_INTERVAL_SECONDS,
)

# The Windows foreground-window API is unavailable on Linux and macOS.
# Keep the CLI importable everywhere and disable only this optional feature.
user32 = ctypes.WinDLL("user32", use_last_error=True) if os.name == "nt" else None


def get_active_window_title() -> str:
    """Return the active Windows window title, or an empty string elsewhere."""
    if user32 is None:
        return ""

    hwnd = user32.GetForegroundWindow()
    length = user32.GetWindowTextLengthW(hwnd)
    if length <= 0:
        return ""

    buffer = ctypes.create_unicode_buffer(length + 1)
    user32.GetWindowTextW(hwnd, buffer, length + 1)
    return buffer.value


def guardian_worker(data_ref: dict, save_callback: Callable[[dict], None]) -> None:
    """Poll foreground window titles locally and flag configured keywords."""
    if user32 is None:
        return

    drift_counter = 0
    while True:
        time.sleep(GUARDIAN_POLL_INTERVAL_SECONDS)

        try:
            title = get_active_window_title().lower()
            if not title:
                continue

            matched_keyword = next(
                (keyword for keyword in DISTRACTION_KEYWORDS if keyword in title),
                None,
            )
            if not matched_keyword:
                continue

            drift_counter += 1
            stats = data_ref["stats"]
            stats["focus_score"] = max(0, stats.get("focus_score", 100) - 10)
            save_callback(data_ref)

            print(f"\n\n{CLR_RED}╔══════════════════════════════════════════════════╗")
            print(f"║    ATTENTION GUARDIAN ALERT                    ║")
            print(f"╠══════════════════════════════════════════════════╣")
            print(f"║ Your attention may be drifting...                ║")
            print(f"║ Detected keyword: {matched_keyword.title():<27}║")
            print(f"║ Drift Count: {drift_counter:<4} | Focus: {stats['focus_score']}/100             ║")
            print(f"╚══════════════════════════════════════════════════╝{CLR_RESET}")
            print(f"{CLR_CYAN}Return to your chosen task when ready.{CLR_RESET}")
        except Exception as exc:  # A monitor failure must not crash the CLI.
            print(f"{CLR_RED}Attention Guardian warning: {exc}{CLR_RESET}")


def start_attention_guardian(
    data: dict,
    save_function: Callable[[dict], None],
) -> threading.Thread | None:
    """Start the optional monitor on Windows; do nothing on other platforms."""
    if user32 is None:
        return None

    guardian_thread = threading.Thread(
        target=guardian_worker,
        args=(data, save_function),
        name="DopaDirectAttentionGuardian",
        daemon=True,
    )
    guardian_thread.start()
    return guardian_thread
