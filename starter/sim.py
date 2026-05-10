# help revise and simplify this code using best practices,feel free to ask questions about the code for clarity about its requirement when and if neccessary, do not make any assumptions about the code  
from datetime import datetime
    
def generate_sessions(service_session_amount,service_session_interval,service_session_duration,break_duration):
    schedules = []    
    service_session_amount_counter = 0
    service_session_interval_counter = 0
    while service_session_amount_counter < service_session_amount:    
        startTime_date = today.day + service_session_interval_counter
        endTime_date = startTime_date
        month = today.month
        year = today.year
        startTime_hour = today.hour + break_duration['hour']
        startTime_minute = today.minute + break_duration['minute']
        endTime_hour = startTime_hour + service_session_duration['hour']
        endTime_minute = startTime_minute + service_session_duration['minute']
        




        if startTime_date < 31:
            if startTime_hour < 23  :
                if startTime_minute < 60 :               
                    session_startTime = datetime(year, month, startTime_date, startTime_hour, startTime_minute)
                   
                    if endTime_minute < 60:
                        session_endTime = datetime(year, month, endTime_date, endTime_hour, endTime_minute)
                    else:
                        endTime_hour += 1
                        endTime_minute -= 60
                        session_endTime = datetime(year, month, endTime_date, endTime_hour, endTime_minute)    
                    session = {
                        'startTime': session_startTime,
                        'endtime': session_endTime
                    } 
                    schedules.append(session)       
                    
                else:                    
                    startTime_hour += 1
                    startTime_minute -= 60                
  
                    session_startTime = datetime(year, month, startTime_date, startTime_hour, startTime_minute)
                    if endTime_minute < 60:
                        session_endTime = datetime(year, month, endTime_date, endTime_hour, endTime_minute)
                    else:
                        endTime_hour += 1
                        endTime_minute -= 60
                        session_endTime = datetime(year, month, endTime_date, endTime_hour, endTime_minute)
                   # endTime_minute = startTime_minute + service_session_duration['minute'] 
                    endTime_minute -= 60
                   # endTime_hour += 1
                    
                    session = {
                        'startTime': session_startTime,
                        'endtime': session_endTime
                    }  
                    schedules.append(session)       
                   
                     
                    
            else:
                if startTime_minute < 60:                 
                    startTime_hour -= 23
                    startTime_date += 1 
                             
                    session_startTime = datetime(year, month, startTime_date, startTime_hour, int(startTime_minute) )
                    session_endTime = datetime(year, month, endTime_date, endTime_hour, endTime_minute)
                    session = {
                        'startTime': session_startTime,
                        'endtime': session_endTime
                    }  
                    schedules.append(session)        
                    
                else:
                    startTime_minute -= 60
                    startTime_hour += 1
                    startTime_hour -= 23                    
                    startTime_date += 1 
                             
                    session_startTime = datetime(year, month, startTime_date, startTime_hour, int(startTime_minute))
                    if endTime_minute < 60:
                        session_endTime = datetime(year, month, endTime_date, endTime_hour, endTime_minute)
                    else:
                        endTime_minute -= 60
                        endTime_hour += 1
                        endTime_hour -= 23
                        session_endTime = datetime(year, month, endTime_date, endTime_hour, endTime_minute)
                    session = {
                        'startTime': session_startTime,
                        'endtime': session_endTime
                    }  
                    schedules.append(session)        
                   
                    
        else:
            if startTime_hour < 23:
                if startTime_minute < 60:                        
                    startTime_date -= 31
                    month += 1               
                    session_startTime = datetime(year, month, startTime_date, startTime_hour, startTime_minute )
                    session_endTime = datetime(year, month, endTime_date, endTime_hour, endTime_minute)
                    session = {
                        'startTime': session_startTime,
                        'endtime': session_endTime
                    }  
                    schedules.append(session)        
                   
                else:
                    startTime_minute -= 60
                    startTime_hour += 1
                    endTime_minute -= 60
                    endTime_hour += 1
                    startTime_date -= 31
                    month += 1               
                    session_startTime = datetime(year, month, startTime_date, startTime_hour, startTime_minute )
                    session_endTime = datetime(year, month, endTime_date, endTime_hour, endTime_minute)
                    session = {
                        'startTime': session_startTime,
                        'endtime': session_endTime
                    }  
                    schedules.append(session)        
                    
                    
                    
            else:
                if startTime_minute < 60:
                    startTime_hour -= 23
                    endTime_hour -= 23     
                    startTime_date += 1
                    startTime_date -= 31
                    month += 1  
                    session_startTime = datetime(year, month, startTime_date, startTime_hour, startTime_minute )
                    session_endTime = datetime(year, month, endTime_date, endTime_hour, endTime_minute)
                    session = {
                        'startTime': session_startTime,
                        'endtime': session_endTime
                    }  
                    schedules.append(session)        
                    
                    
                else:
                    startTime_minute -= 60
                    startTime_hour += 1
                    startTime_hour -= 23 
                    endTime_minute -= 60
                    endTime_hour += 1
                    endTime_hour -= 23     
                    startTime_date += 1
                    startTime_date -= 31
                    month += 1  
                    session_startTime = datetime(year, month, startTime_date, startTime_hour, startTime_minute )
                    session_endTime = datetime(year, month, startTime_date, endTime_hour, endTime_minute)
                    session = {
                        'startTime': session_startTime,
                        'endtime': session_endTime
                    }  
                    schedules.append(session)        
                    
        service_session_interval_counter += service_session_interval  
        service_session_amount_counter += 1 
    print(schedules)
    return schedules            

def check_availability(workdays, hours):
    available=False
    current = datetime.utcnow()
    current_day, current_hour = current.isoweekday() , current.hour 
    for day in workdays:
        for hour in hours:           
            if current_day  == day and current_hour == hour:
                available = True             
                return available
            
def check_overlap(schedules, new_schedule):
    conflicts = []
    new_start = new_schedule['startTime']
    new_end = new_schedule['endtime']
    
    for s in schedules:
       
        if new_start < s['endtime'] and s['startTime'] < new_end:
            print(f'Conflict found on {s}')
            conflicts.append(s)
            return conflicts

def schedule_session_flow(service_session_amount,service_session_interval,service_session_duration,break_duration):
             
    a = check_availability(workdays=work_days, hours=work_hours)
    if a is not None:      
        schedules =  generate_sessions(service_session_amount,service_session_interval,service_session_duration,break_duration)
    
        if len(schedules_repo) == 0:       
            for schedule in schedules:
               schedules_repo.append(schedule)
        else:
            for schedule in schedules:
                conflict =  check_overlap(schedules_repo, schedule)
                if len(conflict) == 0:
                   schedules_repo.append(schedule)
                else:
                    # pls help generate a logic that will adjust session time range to the next avialable time slot in compliance to th workers working days and working hours (if  session time exceedes working how move to the next working days the repeat the work flow)  
                    print(conflict)
                       
    else:
        print('Specialist is not available')


schedules_repo = [] 


weekdays = {
    1: 'Monday',
    2: 'Tuesday',
    3: 'Wednesday',
    4: 'Thursday',
    5: 'Friday',
    6: 'Saturday',
    7: 'Sunday'    
}


#work_days_letter = ["Mon","Tue","Wed","Thu","Fri","Sat"]
work_days = [1,2,3,4,5,6]
work_hours = range(6, 17)
break_duration = {
    'hour': 2,
    'minute': 0
}
today = datetime.utcnow()
print(today)

service_session_interval = 1
service_session_amount = 7
service_session_duration = {
    'hour': 3,
    'minute': 40
}
c = 0
while c < 3:
    schedule_session_flow(service_session_amount,service_session_interval,service_session_duration,break_duration)
    c += 1
    
    
 
 
 
# gemini code
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
for _ in range(3):
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
    
    