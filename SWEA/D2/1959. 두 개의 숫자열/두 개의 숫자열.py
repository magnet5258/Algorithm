T = int(input())
for test_case in range(1, T + 1):
    N, M = map(int, input().split())
    lst1 = list(map(int, input().split()))
    lst2 = list(map(int, input().split()))
    max_sum = -float('inf')
    if N < M:
        for i in range(M - N + 1):
            lst_sum = 0
            for j in range(N):
                lst_sum += lst1[j] * lst2[j + i]
            max_sum = max(max_sum, lst_sum)
    else:
        for i in range(N - M + 1):
            lst_sum = 0
            for j in range(M):
                lst_sum += lst2[j] * lst1[j + i]
            max_sum = max(max_sum, lst_sum)
    print(f'#{test_case} {max_sum}')
