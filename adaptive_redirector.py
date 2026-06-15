"""Adaptive Redirector Engine for Dopa-Direct v5.2."""
import random
from storage import get_all_activities
from config import CLR_GREEN, CLR_YELLOW, CLR_RESET

def get_recommendations(data, trigger, limit=3):
    """
    Analyzes historical success counts for a given trigger.
    Returns a structured list of custom choice mappings, falling back
    to default pool weights if history doesn't exist.
    """
    history = data.setdefault("redirect_history", {})
    trigger_history = history.setdefault(trigger, {})
    all_acts = get_all_activities(data)
    
    # Sort existing options descending by selection frequency
    sorted_history = sorted(trigger_history.items(), key=lambda x: x[1], reverse=True)
    
    recommendations = []
    seen_activities = set()
    
    # 1. Pull from established successful routines first
    for activity, count in sorted_history:
        if activity in all_acts and len(recommendations) < limit:
            recommendations.append({"activity": activity, "count": count})
            seen_activities.add(activity)
            
    # 2. Backfill missing recommendations using random activities
    remaining_pool = [a for a in all_acts if a not in seen_activities]
    random.shuffle(remaining_pool)
    
    while len(recommendations) < limit and remaining_pool:
        act = remaining_pool.pop()
        recommendations.append({"activity": act, "count": 0})
        
    return recommendations

def learn_choice(data, trigger, activity):
    """
    Increments execution tracking frequency matrix for a given trigger/activity map.
    Only triggered upon absolute focus lock survival block loop validation.
    """
    history = data.setdefault("redirect_history", {})
    trigger_history = history.setdefault(trigger, {})
    trigger_history[activity] = trigger_history.get(activity, 0) + 1

def get_top_adaptive_pairings(data):
    """Extracts the single most successful activity routing for every recorded trigger."""
    history = data.setdefault("redirect_history", {})
    pairings = {}
    
    for trigger, activities in history.items():
        if activities:
            top_act = max(activities.items(), key=lambda x: x[1])
            if top_act[1] > 0:
                pairings[trigger] = {"activity": top_act[0], "count": top_act[1]}
                
    return pairings
