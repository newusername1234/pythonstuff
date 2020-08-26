
def add_time(start,duration,start_day=''):
    try:
        time,ampm = start.split()
        hours,mins = map(int,time.split(':'))
    except ValueError:
        time = start[:-2]
        ampm = start[-2:]
    finally:
        hours,mins = map(int,time.split(':'))

    # convert to 24hr clock to determine am/pm
    if ampm.lower() == 'am' and hours == 12:
        hours = 0
    elif ampm.lower() == 'pm' and hours < 12:
        hours += 12

    add_hours,add_mins = map(int,duration.split(':'))
    hours += add_hours
    mins += add_mins
    
    days = [
        'monday','tuesday','wednesday',
        'thursday','friday','saturday','sunday'
        ]

    while mins >= 60:
        hours += 1
        mins -= 60

    days_later = ''

    if hours >= 24:
        days_later = int(hours/24)
        hours %= 24

    end_day = ''

    if start_day:
        if not days_later:
            i = days.index(start_day.lower())
            end_day = f', {days[i%7].capitalize()}'
        else:    
            i = days.index(start_day.lower()) + days_later
            end_day = f', {days[i%7].capitalize()}'

    if days_later and days_later == 1:
        days_later = '(next day)'
    elif days_later and days_later > 1:
        days_later = f'({days_later} days later)'


    ampm = 'AM' if hours < 12 else 'PM'

    # convert back to 12hr
    if hours == 0:
        hours = 12
    
    if ampm == 'PM' and hours != 12:
        hours -= 12

    # zero fill hours and mins
    hours,mins = [f'0{x}' if len(x) < 2 else x for x in (str(hours),str(mins))]

    return f'{hours}:{mins} {ampm}{end_day} {days_later}'
