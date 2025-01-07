T = int(input())
for test_case in range(1, T + 1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    max_sum = 0
    for i in range(N - M + 1):
        for j in range(N - M + 1):
            cur_sum = 0
            for x in range(i, i + M):
                for y in range(j, j + M):
                    cur_sum += arr[x][y]
            max_sum = max(max_sum, cur_sum)
    print(f'#{test_case} {max_sum}')
            