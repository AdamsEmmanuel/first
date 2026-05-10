from datetime import datetime, timedelta

def get_next_work_start(dt, work_days, work_hours):
    """Resets the clock to 06:00 (or min work hour) of the next valid work day."""
    next_day = dt + timedelta(days=1)
    while next_day.isoweekday() not in work_days:
        next_day += timedelta(days=1)
    return next_day.replace(hour=min(work_hours), minute=0, second=0, microsecond=0)

def is_within_work_hours(start, end, work_days, work_hours):
    """Checks if the session stays within the allowed daily window."""
    if start.isoweekday() not in work_days:
        return False
    # Check if start is too early or end is too late
    if start.hour < min(work_hours):
        return False
    if end.hour > max(work_hours) or (end.hour == max(work_hours) and end.minute > 0):
        return False
    return True

def find_available_slot(proposal_start, duration, repo, work_days, work_hours):
    """
    The core logic: Finds the first valid gap that fits the session duration
    while respecting work hours and existing appointments.
    """
    search_dt = proposal_start
    # Safety: Don't search more than 60 days into the future
    max_search_date = search_dt + timedelta(days=60)
    
    while search_dt < max_search_date:
        proposal_end = search_dt + duration
        
        # 1. Rule: If it exceeds work hours, jump to next morning
        if not is_within_work_hours(search_dt, proposal_end, work_days, work_hours):
            search_dt = get_next_work_start(search_dt, work_days, work_hours)
            continue

        # 2. Rule: Check for overlaps with existing sessions
        # Using a 5-minute buffer to prevent back-to-back friction
        conflict = any(search_dt < s['endtime'] + timedelta(minutes=5) and 
                       s['startTime'] < proposal_end + timedelta(minutes=5) 
                       for s in repo)
        
        if conflict:
            # If busy, nudge forward by 30 mins and re-check
            search_dt += timedelta(minutes=30)
            continue
            
        return search_dt, proposal_end
        
    return None, None

def schedule_sessions(amount, interval_days, duration_dict, break_dict, repo, work_days, work_hours):
    """Generates a series of sessions based on the interval and availability."""
    session_dur = timedelta(hours=duration_dict['hour'], minutes=duration_dict['minute'])
    break_offset = timedelta(hours=break_dict['hour'], minutes=break_dict['minute'])
    
    # Start looking from the current time
    base_time = datetime.utcnow()

    for i in range(amount):
        # Initial target: Today + Break + (i * Interval Days)
        target_start = base_time + break_offset + timedelta(days=i * interval_days)
        
        start_slot, end_slot = find_available_slot(target_start, session_dur, repo, work_days, work_hours)
        
        if start_slot:
            repo.append({
                'startTime': start_slot,
                'endtime': end_slot
            })
        else:
            print(f"Could not find a slot for session {i+1}")

# --- API Configuration & Mock Data ---

schedules_repo = [] # This would usually be your database
WORK_DAYS = [1, 2, 3, 4, 5, 6] # Mon - Sat
WORK_HOURS = range(6, 17)      # 06:00 to 17:00 (5 PM)

session_params = {
    "amount": 7,
    "interval_days": 1,
    "duration_dict": {'hour': 3, 'minute': 40},
    "break_dict": {'hour': 2, 'minute': 0} # Initial delay before first session
}

# Simulate 3 different clients booking sessions
for client_id in range(1, 4):
    print(f"Scheduling for Client {client_id}...")
    schedule_sessions(**session_params, repo=schedules_repo, work_days=WORK_DAYS, work_hours=WORK_HOURS)

# --- Display Results ---
schedules_repo.sort(key=lambda x: x['startTime'])

print(f"\n{'Date':<12} | {'Start':<8} | {'End':<8}")
print("-" * 35)
for s in schedules_repo:
    print(f"{s['startTime'].strftime('%Y-%m-%d')} | {s['startTime'].strftime('%H:%M')} | {s['endtime'].strftime('%H:%M')}")