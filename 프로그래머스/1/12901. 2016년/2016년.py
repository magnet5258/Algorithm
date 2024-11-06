from datetime import datetime

def solution(a, b):
    date1 = datetime(2016, 1, 1)
    date2 = datetime(2016, a, b)
    diff = (date2 - date1).days
    if diff % 7 == 0:
        return 'FRI'
    elif diff % 7 == 1:
        return 'SAT'
    elif diff % 7 == 2:
        return 'SUN'
    elif diff % 7 == 3:
        return 'MON'
    elif diff % 7 == 4:
        return 'TUE'
    elif diff % 7 == 5:
        return 'WED'
    elif diff % 7 == 6:
        return 'THU'