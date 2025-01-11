T = int(input())
for test_case in range(1, T + 1):
    lst = list(map(int, input().split()))
    lst.sort()
    x = sum(lst) + lst[5]
    y = x % 7
    ans = lst[5] + 7 - y
    print(ans)
