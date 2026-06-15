"""Trigger logging and ranking for Dopa-Direct."""


def log_trigger(data, trigger):
    """Record one occurrence of the given trigger (app/site name)."""
    trigger = trigger.strip()
    trigger = trigger.title() if trigger else "Unspecified"

    data["triggers"][trigger] = data["triggers"].get(trigger, 0) + 1


def top_triggers(data, limit=5):
    """Return up to `limit` (trigger_name, count) pairs, most frequent first."""
    return sorted(data["triggers"].items(), key=lambda item: item[1], reverse=True)[:limit]
