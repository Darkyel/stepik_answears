/step/6

def get_minutes_by_hours_and_minutes(hours, minutes):
    return hours * 60 + minutes
print(get_minutes_by_hours_and_minutes(int(input()), int(input())))

/step/7

def get_hours_and_minutes_by_minutes(minutes):
    return (minutes // 60), (minutes % 60)
for param in get_hours_and_minutes_by_minutes(int(input())):
    print(param)
    
/step/8

def get_alarm_hours_and_minutes(sleep_duration_minutes, bedtime_hours, bedtime_minutes):
    bedtime_full_minutes = bedtime_hours * 60 + bedtime_minutes
    alarm_minutes = bedtime_full_minutes + sleep_duration_minutes
    return (alarm_minutes // 60), (alarm_minutes % 60)
for param in get_alarm_hours_and_minutes(int(input()), int(input()), int(input())):
    print(param)
