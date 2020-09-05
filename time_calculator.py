

def add_time(start, duration, ):
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
    time, end = start.split()
    hour1, min1 = map(int, time.split(':'))
    hour2, min2 = map(int, duration.split(':'))

    hour_result = time_format[str(hour1 + hour2)]
    min_result = min1 + min2
    if min_result > 60:
        add = min_result // 60
        hour_result += add
        min_result -= 60

    print(str(hour_result) + ':' + str(min_result) + ' ' + end)

    return 



add_time("11:30 AM", "2:32")



