def when(hour=0, weekday = '', dir = False):
    week = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    word = weekday.lower()
    day = 0
    fir = [
        char.lower()
        for char in week]
    if dir == False:
        if hour >= 24:
            day += (hour // 24 + 1)
            return f'{day} days later' 
        elif hour < 24:
            day += hour // 12
            if hour >= 12:
                return f'next day'
            else:
                pass
    if dir == True:
        if word in fir:
            if hour > 24:
                word = week[(fir.index(weekday.lower()) + (((hour // 24) + 1) % len(week))) % len(week)]
            elif hour < 24:
                word = week[fir.index(weekday.lower()) + ((hour // 24) % len(week))]
            return word

def cons(new_time, new_min, new_hour, annum):
    if new_min < 10:
        new_time = f'{new_hour}:0{new_min} {annum}'
        return new_time
    elif new_min >= 10:
        new_time = f'{new_hour}:{new_min} {annum}'
        return new_time 
 
def add_time(val, adt, days=''):
    rate = val.split(':')
    zone = {'hour':rate[0], 'min':rate[1].split(' ')[0], 'days':0}
    duration = adt.split(':')
    trans = {'hour':duration[0], 'min':duration[1], 'days':0}
    min_list = [int(zone['min']), int(trans['min'])]
    h_list = [int(zone['hour']) + (sum(min_list) // 60), int(trans['hour'])]
    new_hour = 0
    new_min = 00
    annum = rate[1].split(' ')[1]
    new_time = ''
    if sum(min_list) >= 60:
        minute = sum(min_list) % 60
        new_min = minute
    else:
        new_min = sum(min_list)
    if sum(h_list) >= 12:
        hour = sum(h_list) % 24
        new_hour = hour
        if ((sum(h_list) // 12) % 2)  == 0:
            annum == 'AM'
            time = cons(new_time, new_min, new_hour, annum)
            if sum(h_list) >= 24:
                if sum(h_list) > 35:
                    new_time = f"{time} ({when(hour=sum(h_list), weekday=days)})"
                elif sum(h_list) <= 35:
                    new_time = f"{time}"
            else:
                new_time = time
        elif ((sum(h_list) // 12) % 2)  == 1:    
            if new_hour == 12:
                new_hour = 12
            elif new_hour > 12:
                new_hour = hour % 12
            if annum == 'PM':
                annum = 'AM'
                time = cons(new_time, new_min, new_hour, annum)
                new_time = f"{time} ({when(hour=sum(h_list), weekday=days)})"
            elif annum == 'AM':
                annum = 'PM'
                time = cons(new_time, new_min, new_hour, annum)
                if sum(h_list) >= 24:
                    if sum(h_list) >= 35:
                        new_time = f"{time} ({when(hour=sum(h_list), weekday=days)})"
                    elif sum(h_list) < 35:
                        new_time = f"{time}"
                else:
                    if days == '':
                        new_time = time
                    else:
                        new_time = f"{time} {when(weekday=days, hour=sum(h_list), dir=True)}"
    else:
        new_hour = sum(h_list)
        new_time = cons(new_time, new_min, new_hour, annum)
    if days != '':
        time = cons(new_time, new_min, new_hour, annum)
        if annum == 'AM':
            if sum(h_list) <= 35:
                rate = sum(h_list) % 24
                rewrite = f'{when(weekday=days, hour=sum(h_list) , dir=True)}'
                rewrite2 = f'{when(weekday=rewrite, hour=sum(h_list), dir=True)}'
                rewrite3 = f'{when(weekday=rewrite2, hour=sum(h_list), dir=True)}'
                new_time = f"{time}, {when(weekday=rewrite3, hour=sum(h_list), dir=True)} (next day)"
            else:
                new_time = f"{time}, {when(weekday=days, hour=sum(h_list), dir=True)} ({when(hour=sum(h_list), weekday=days)})"
        elif annum == 'PM':
            if sum(h_list) >= 12:
                new_time = f"{time}, {when(weekday=days, hour=sum(h_list), dir=True)} ({when(hour=sum(h_list), weekday=days)})"
            elif sum(h_list) < 12:
                new_time = f"{time}, {when(weekday=days, hour=sum(h_list), dir=True)}"
    return new_time

print(add_time("2:59 AM", "24:00"))

def add_time(start, duration, day=None):
    start_time, period = start.split()
    start_hour, start_minute = map(int, start_time.split(":"))
    add_hour, add_minute = map(int, duration.split(":"))

    if period == "PM":
        start_hour += 12

    new_hour = start_hour + add_hour
    new_minute = start_minute + add_minute

    if new_minute >= 60:
        new_hour += 1
        new_minute -= 60

    days_later = new_hour // 24
    new_hour = new_hour % 24

    if new_hour >= 12:
        new_period = "PM"
        if new_hour > 12:
            new_hour -= 12
    else:
        new_period = "AM"
        if new_hour == 0:
            new_hour = 12

    if day:
        days_of_week = ["monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday"]
        day_index = days_of_week.index(day.lower())
        new_day_index = (day_index + days_later) % 7
        new_day = days_of_week[new_day_index].capitalize()
        result = f"{new_hour}:{new_minute:02} {new_period}, {new_day}"
    else:
        result = f"{new_hour}:{new_minute:02} {new_period}"

    if days_later == 1:
        return f"{result} (next day)"
    elif days_later > 1:
        return f"{result} ({days_later} days later)"
    else:
        return result
    
print(add_time("2:59 AM", "24:00"))