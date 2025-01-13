T = int(input())
date_lst = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
for test_case in range(1, T + 1):
    lst = list(map(int, input().split()))
    if lst[2] - lst[0] == 0:
        ans = lst[3] - lst[1] + 1
    elif lst[2] - lst[0] == 1:
        ans = date_lst[lst[0] - 1] - lst[1] + 1 + lst[3]
    else:
        ans = date_lst[lst[0] - 1] - lst[1] + 1 + lst[3] + sum(date_lst[lst[0]:lst[2] - 1])
    print(f'#{test_case} {ans}')