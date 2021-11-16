/step/5

def get_sleep_status(min_hours, max_hours, sleep_hours):
    status = ''
    if min_hours <= sleep_hours <= max_hours:
        status = 'Это нормально'
    elif sleep_hours < min_hours:
        status = 'Недосып'
    elif sleep_hours > max_hours:
        status = 'Пересып'
    return status
print(get_sleep_status(int(input()), int(input()), int(input())))

/step/6

def is_leap_year(year):
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)
def get_year_status(year):
    return 'Високосный' if is_leap_year(year) else 'Обычный'
print(get_year_status(int(input())))
