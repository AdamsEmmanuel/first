from datetime import datetime, timedelta

def generate_sessions(amount, interval_days, duration_dict, break_dict, start_from=None):
    """
    Generates a list of potential sessions using timedelta for automatic rollovers.
    """
    schedules = []
    # Use provided start time or default to now
    current_time = start_from or datetime.utcnow()
    
    # Convert dicts to timedelta objects for easy math
    session_duration = timedelta(hours=duration_dict['hour'], minutes=duration_dict['minute'])
    break_offset = timedelta(hours=break_dict['hour'], minutes=break_dict['minute'])

    for _ in range(amount):
        # Apply the break/offset to find start time
        session_start = current_time + break_offset
        session_end = session_start + session_duration
        
        schedules.append({
            'startTime': session_start,
            'endtime': session_end
        })
        
        # Advance the clock by the interval (e.g., 1 day) for the next session
        current_time += timedelta(days=interval_days)
        
    return schedules

def check_availability(dt, work_days, work_hours):
    """Checks if a specific datetime falls within work parameters."""
    return dt.isoweekday() in work_days and dt.hour in work_hours

def check_overlap(repo, new_session):
    """Returns True if the new session overlaps with any existing ones."""
    for s in repo:
        if new_session['startTime'] < s['endtime'] and s['startTime'] < new_session['endtime']:
            return True
    return False

def schedule_session_flow(amount, interval, duration, break_dur, repo):
    # 1. Generate sessions
    new_sessions = generate_sessions(amount, interval, duration, break_dur)
    
    for session in new_sessions:
        # 2. Check if the session is within working hours
        # This logic handles your request: "if session exceeds work hours, move to next available"
        while not (check_availability(session['startTime'], work_days, work_hours) and 
                   check_availability(session['endtime'], work_days, work_hours)):
            
            # Shift to the next hour to find a gap
            session['startTime'] += timedelta(hours=1)
            session['endtime'] += timedelta(hours=1)
            
            # If we shifted into a new day, ensure we are starting at the start of work hours
            if session['startTime'].hour > max(work_hours):
                # Move to next day, set to earliest work hour
                session['startTime'] += timedelta(days=1)
                session['startTime'] = session['startTime'].replace(hour=min(work_hours), minute=0)
                session['endtime'] = session['startTime'] + timedelta(hours=duration['hour'], minutes=duration['minute'])

        # 3. Check for overlaps in the repo
        while check_overlap(repo, session):
            # If overlap, push the session forward by 30 mins and re-check
            session['startTime'] += timedelta(minutes=30)
            session['endtime'] += timedelta(minutes=30)
            
        repo.append(session)

# --- Configuration ---
schedules_repo = []
work_days = [1, 2, 3, 4, 5, 6] # Mon-Sat
work_hours = range(6, 17) # 6am to 5pm

service_params = {
    "amount": 7,
    "interval_days": 1,
    "duration_dict": {'hour': 3, 'minute': 40},
    "break_dict": {'hour': 2, 'minute': 0}
}

# Run the flow 3 times
for _ in range(1):
    schedule_session_flow(
        service_params["amount"], 
        service_params["interval_days"], 
        service_params["duration_dict"], 
        service_params["break_dict"],
        schedules_repo
    )

# Print results
for s in sorted(schedules_repo, key=lambda x: x['startTime']):
    print(f"Start: {s['startTime'].strftime('%Y-%m-%d %H:%M')} | End: {s['endtime'].strftime('%H:%M')}")