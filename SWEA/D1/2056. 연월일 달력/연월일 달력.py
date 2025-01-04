T = int(input())
for t in range(1, T + 1):
    date = input()
    year = date[:4]
    month = date[4:6]
    day = date[6:]
    if month in ['01', '03', '05', '07' ,'08', '10', '12']:
        if 1 <= int(day) and int(day) <= 31:
            print(f'#{t} {year}/{month}/{day}')
        else:
            print(f'#{t} -1')
    elif month in ['04' ,'06', '09', '11']:
        if 1 <= int(day) and int(day) <= 30:
            print(f'#{t} {year}/{month}/{day}')
        else:
            print(f'#{t} -1')
    elif month == '02':
        if 1 <= int(day) and int(day) <= 28:
            print(f'#{t} {year}/{month}/{day}')
        else:
            print(f'#{t} -1')
    else:
        print(f'#{t} -1')
    