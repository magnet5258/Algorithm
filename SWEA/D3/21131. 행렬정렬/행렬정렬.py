T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    cnt = 0
    lst = arr[0]
    for i in range(1, N):
        if lst[i - 1] == i and lst[i] != i + 1:
            if i == 1:
                cnt += 1
            else:
                cnt += 2
    print(cnt)
