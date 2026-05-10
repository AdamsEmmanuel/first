from uuid import uuid4
from datetime import datetime
weekdays = {
    1: 'Monday',
    2: 'Tuesday',
    3: 'Wednesday',
    4: 'Thursday',
    5: 'Friday',
    6: 'Saturday',
    7: 'Sunday'    
}

'3550b582-c816-44a2-8233-741c42bab30e'

#print(weekdays[datetime.isocalendar(datetime(2026,5,22 ))[2]])

mealPlan1 = {
    'id': '9d3e7ac2-feea-4273-b8f4-dfa62cd4e080',
    'startDate': datetime.utcnow(),
    'endDate': datetime(2026,5,21 ),
    'calorieGoal': '20kcal/day',
    'micronutrientRatio': '2:3:4:5 per day',
    'restirctions': 'below 1.2mg of sodium per day', 
    'timeTableData': [
        {
            'day': 'Mon',
            'breakfast': 'rice',
            'lunch': 'beans',
            'snack': 'carrots',
            'dinner': 'chicken soup'
        },
        {
            'day': 'Tue',
            'breakfast': 'rice',
            'lunch': 'beans',
            'snack': 'carrots',
            'dinner': 'chicken soup'
        },
        {
            'day': 'Wed',
            'breakfast': 'rice',
            'lunch': 'beans',
            'snack': 'carrots',
            'dinner': 'chicken soup'
        },
        {
            'day': 'Thur',
            'breakfast': 'rice',
            'lunch': 'beans',
            'snack': 'carrots',
            'dinner': 'chicken soup'
        },
        {
            'day': 'Fri',
            'breakfast': 'rice',
            'lunch': 'beans',
            'snack': 'carrots',
            'dinner': 'chicken soup'
        }
    ]
}

mealPlan2 = {
    'id': '9d3e7ac2-feea-4273-b8f4-dfa62cd4e080',
    'startDate': datetime.utcnow(),
    'endDate': datetime(2026,5,21 ),
    'calorieGoal': '20kcal/day',
    'micronutrientRatio': '2:3:4:5 per day',
    'restirctions': 'below 1.2mg of sodium per day', 
    'timeTableData': [
        {
            'day': 'Mon',
            'breakfast': 'rice',
            'lunch': 'beans',
            'snack': 'carrots',
            'dinner': 'chicken soup'
        },
        {
            'day': 'Tue',
            'breakfast': 'rice',
            'lunch': 'fruit salad',
            'snack': 'carrots',
            'dinner': 'catfish soup'
        },
        {
            'day': 'Wed',
            'breakfast': 'rice',
            'lunch': 'beans',
            'snack': 'carrots',
            'dinner': 'chicken soup'
        },
        {
            'day': 'Thur',
            'breakfast': 'rice',
            'lunch': 'beans',
            'snack': 'carrots',
            'dinner': 'chicken soup'
        },
        {
            'day': 'Fri',
            'breakfast': 'rice',
            'lunch': 'beans',
            'snack': 'carrots',
            'dinner': 'chicken soup'
        }
    ]
}

#print(mealPlan)
def constuct_timetable(meal_plan):
    day = []
    breakfast = []
    lunch = []
    snack = []
    dinner = [] 
    for data in meal_plan['timeTableData']:
        day.append(data['day'])
        breakfast.append(data['breakfast'])
        lunch.append(data['lunch'])
        snack.append(data['snack'])
        dinner.append(data['dinner'])
        
    print (
        f"""
        day|     {day} \n
        breakfast| {breakfast}\n
        lunch| {lunch}\n
        snack| {snack}\n
        dinner| {dinner}\n    
        """
    )
    
#constuct_timetable(mealPlan)

changes1 = {
    'changes_id': '3550b582-c816-44a2-8233-892c42bab30e',
    'log_id': '3550b582-c816-44a2-8233-741c42bab30e',
}    

log = {
    'log_id': '3550b582-c816-44a2-8233-741c42bab30e',
    'user_id': '3550b582-c816-44a2-8233-741c42bab30e',
    'actionType': 'modify_mealplan',
    'resource_id': '9d3e7ac2-feea-4273-b8f4-dfa62cd4e080',
    'timestamp': datetime.timestamp,
    'ipAddress': '`122:445:0808',
    'changes_id': changes1['changes_id']
}

changes1['before'] = mealPlan1
changes1['after'] = mealPlan2
 
    
    




#work_days_letter = ["Mon","Tue","Wed","Thu","Fri","Sat"]
work_days = [1,2,3,4,5,6]
work_hours = range(6, 17)
break_duration = {
    'hour': 2,
    'minute': 59
}
today = datetime.utcnow()
print(today)
sim =[]
schedules = []
service_session_interval = 1
service_session_amount = 7
service_session_duration = {
    'hour': 2,
    'minute':43
}
service_session_amount_counter = 0
service_session_interval_counter = 0
            

def check_availability(workdays, hours):
    available=False
    current = datetime.utcnow()
    print(current.hour)
    current_day, current_hour = current.isoweekday() , current.hour 
    for day in workdays:
        for hour in hours:           
            if current_day  == day and current_hour == hour:
                available = True             
                return available
            
def check_overlap(schedules, new_schedule):
    
    new_start = new_schedule['starttime']
    new_end = new_schedule['endtime']
    
    for s in schedules:
       
        if new_start < s['end'] and s['start'] < new_end:
            print(f'Conflict found on {s}')
            conflicts.append(s)
            return conflicts
         
a = check_availability(workdays=work_days, hours=work_hours)
if a is not None:
    while service_session_amount_counter < service_session_amount:    
        session_date = today.day + service_session_interval_counter
        month = today.month
        year = today.year
        startTime_hour = today.hour + break_duration['hour']
        startTime_minute = today.minute + break_duration['minute']
        endTime_hour = startTime_hour + service_session_duration['hour']
        endTime_minute = startTime_minute + service_session_duration['minute']
        




        if session_date < 31:
            if startTime_hour < 23 :
                if startTime_minute < 60:               
                    session_startTime = datetime(year, month, session_date, startTime_hour, startTime_minute)
                    #session_endTime = datetime(year, month, session_date, startTime_hour, startTime_minute) 
                    schedules.append(session_startTime)       
                    sim.append(f'{session_startTime.day}/{session_startTime.month}/{weekdays[session_startTime.isoweekday()]}--{session_startTime.hour} : {session_startTime.minute}')
                else:
                    startTime_hour += 1
                    startTime_minute -= 60
                    session_startTime = datetime(year, month, session_date, startTime_hour, startTime_minute)
                    #session_endTime = datetime(year, month, session_date, startTime_hour, startTime_minute) 
                    schedules.append(session_startTime)       
                    sim.append(f'{session_startTime.day}/{session_startTime.month}/{weekdays[session_startTime.isoweekday()]}--{session_startTime.hour} : {session_startTime.minute}')
                     
                    
            else:
                if startTime_minute < 60:                 
                    startTime_hour -= 23
                    session_date += 1 
                             
                    session_startTime = datetime(year, month, session_date, startTime_hour, int(startTime_minute) )        
                    sim.append(f'{session_startTime.day}/{session_startTime.month}/{weekdays[session_startTime.isoweekday()]}--{session_startTime.hour} : {session_startTime.minute}') 
                else:
                    startTime_minute -= 60
                    startTime_hour += 1
                    startTime_hour -= 23
                    session_date += 1 
                             
                    session_startTime = datetime(year, month, session_date, startTime_hour, int(startTime_minute) )        
                    sim.append(f'{session_startTime.day}/{session_startTime.month}/{weekdays[session_startTime.isoweekday()]}--{session_startTime.hour} : {session_startTime.minute}') 
                    
        else:
            if startTime_hour < 23:
                if startTime_minute < 60:                        
                    session_date -= 31
                    month += 1               
                    session_startTime = datetime(year, month, session_date, startTime_hour, startTime_minute )        
                    sim.append(f'{session_startTime.day}/{session_startTime.month}/{weekdays[session_startTime.isoweekday()]}--{session_startTime.hour} : {session_startTime.minute}')
                else:
                    startTime_minute -= 60
                    startTime_hour += 1
                    session_date -= 31
                    month += 1               
                    session_startTime = datetime(year, month, session_date, startTime_hour, startTime_minute )        
                    sim.append(f'{session_startTime.day}/{session_startTime.month}/{weekdays[session_startTime.isoweekday()]}--{session_startTime.hour} : {session_startTime.minute}')
                    
                    
            else:
                if startTime_minute < 60:
                    startTime_hour -= 23     
                    session_date += 1
                    session_date -= 31
                    month += 1  
                    session_startTime = datetime(year, month, session_date, startTime_hour, startTime_minute )        
                    sim.append(f'{session_startTime.day}/{session_startTime.month}/{weekdays[session_startTime.isoweekday()]}--{session_startTime.hour} : {session_startTime.minute}')
                    
                else:
                    startTime_minute -= 60
                    startTime_hour += 1
                    startTime_hour -= 23     
                    session_date += 1
                    session_date -= 31
                    month += 1  
                    session_startTime = datetime(year, month, session_date, startTime_hour, startTime_minute )        
                    sim.append(f'{session_startTime.day}/{session_startTime.month}/{weekdays[session_startTime.isoweekday()]}--{session_startTime.hour} : {session_startTime.minute}')
        service_session_interval_counter += service_session_interval  
        service_session_amount_counter += 1   
    print(sim)
else:
    print('Specialist is not available')









today = datetime.utcnow()
sim =[]
interval = 0
i = 0
while interval < 7:    
    session_startTime_date = today.day + i
    session_startTime = datetime(today.year, today.month, session_startTime_date)
    sim.append(weekdays[session_startTime.isoweekday()])
    i += 1  
    interval += 1    
    
    
    
#print(sim)
    








conflicts = []
schedules1 = [  {
                    'name': 'session1',
                    'start': datetime(2026,5,5,12),
                    'end': datetime(2026,5,5,14)
                    },
                {
                    'name': 'session2',
                    'start': datetime(2026,5,6,9),
                    'end': datetime(2026,5,6,11)
                    },
                {
                    'name': 'session3',
                    'start': datetime(2026,5,7,9),
                    'end': datetime(2026,5,7,11) 
                    }]
                
                
            

new_schedule = {
                    'name': 'session4',
                    'starttime': datetime(2026,5,6,9),
                    'endtime': datetime(2026,5,6,10),
                    }

                

       
       
                
    

#c = check_overlap(schedules=schedules1, new_schedule=new_schedule)




        
        