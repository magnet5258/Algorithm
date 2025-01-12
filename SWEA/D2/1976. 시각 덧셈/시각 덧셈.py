T = int(input())
for test_case in range(1, T + 1):
    lst = list(map(int, input().split()))
    hour = lst[0] + lst[2]
    minute = lst[1] + lst[3]
    if minute >= 60:
        hour += 1
        minute -= 60
    if hour >= 13:
        hour -= 12
    print(f'#{test_case} {hour} {minute}')