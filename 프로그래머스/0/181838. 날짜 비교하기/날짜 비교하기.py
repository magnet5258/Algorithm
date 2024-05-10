def solution(date1, date2):
    d1 = int(''.join(map(str, date1)))
    d2 = int(''.join(map(str, date2)))
    return int(d1 < d2)