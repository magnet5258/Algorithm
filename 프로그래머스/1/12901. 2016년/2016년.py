from datetime import datetime

def solution(a, b):
    days_of_week = ['FRI', 'SAT', 'SUN', 'MON', 'TUE', 'WED', 'THU']
    date1 = datetime(2016, 1, 1)
    date2 = datetime(2016, a, b)
    diff = (date2 - date1).days
    return days_of_week[diff % 7]