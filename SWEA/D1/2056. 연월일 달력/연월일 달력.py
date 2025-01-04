T = int(input())
days_in_month = {
    '01' : 31, '02' : 28, '03' : 31, '04' : 30,
    '05' : 31, '06' : 30, '07' : 31, '08' : 31,
    '09' : 30, '10' : 31, '11' : 30, '12' : 31
}
for t in range(1, T + 1):
    date = input()
    year, month, day = date[:4], date[4:6], date[6:]
    if month in days_in_month and 1 <= int(day) <= days_in_month[month]:
        print(f'#{t} {year}/{month}/{day}')
    else:
        print(f'#{t} -1')
    