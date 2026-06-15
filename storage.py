import json
import os

from config import DATA_FILE, DEFAULT_ACTIVITIES, DEFAULT_DATA


def load_data():
    """Load persisted state. Falls back to defaults if missing or corrupted."""
    if not os.path.exists(DATA_FILE):
        return json.loads(json.dumps(DEFAULT_DATA))

    try:
        with open(DATA_FILE, "r", encoding="utf-8") as f:
            data = json.load(f)
    except (json.JSONDecodeError, OSError) as e:
        print(f"\n⚠️ Could not read {DATA_FILE} ({e}). Starting fresh.")
        return json.loads(json.dumps(DEFAULT_DATA))

    data.setdefault("custom_activities", [])
    stats = data.setdefault("stats", {})
    for key, default_val in DEFAULT_DATA["stats"].items():
        stats.setdefault(key, default_val)

    return data


def save_data(data):
    """Persist state to disk. Warns on failure but never crashes."""
    try:
        with open(DATA_FILE, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=2)
    except OSError as e:
        print(f"\n⚠️ Could not save progress ({e}).")


def get_all_activities(data):
    return DEFAULT_ACTIVITIES + data["custom_activities"]