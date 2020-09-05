
def calc_hour(hour1, hour2):
    time_format = {
        '1' : 1,
        '2' : 2,
        '3' : 3,
        '4' : 4,
        '5' : 5,
        '6' : 6,
        '7' : 7,
        '8' : 8,
        '9' : 9,
        '10' : 10,
        '11' : 11,
        '12' : 12,
        '13' : 1,
        '14' : 2,
        '15' : 3,
        '16' : 4,
        '17' : 5,
        '18' : 6,
        '19' : 7,
        '20' : 8,
        '21' : 9,
        '22' : 10,
        '23' : 11,
        '24' : 12,
    }
    if hour1 + hour2 > 24:
        diff = hour2 % 24
        if diff:
            hour2 = diff
        else:
            hour2 = 12

    result = time_format[str(hour1 + hour2)]

    return result

def calc_min(min1, min2, hour_result):
    result = min1 + min2
    if result > 60:
        add = result // 60
        hour_result += add
        result -= 60
        if len(str(result)) == 1:
            result = '0' + str(result)
    
    return hour_result, result


def add_time(start, duration, day = 'Funday'):

    time, end = start.split()
    hour1, min1 = map(int, time.split(':'))
    hour2, min2 = map(int, duration.split(':'))

    hour_result = calc_hour(hour1, hour2)
    hour_result, min_result = calc_min(min1, min2, hour_result)
    
    if sum([hour1, hour2]) >= 12 or hour_result >= 12:
        if end == 'AM': end = 'PM'
        elif end == 'PM': end = 'AM'

    print(str(hour_result) + ':' + str(min_result) + ' ' + end)

    return 



add_time("3:00 PM", "3:10")



