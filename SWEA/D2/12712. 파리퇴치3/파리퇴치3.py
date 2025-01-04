T = int(input())
for t in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    max_flies = 0
    for i in range(N):
        for j in range(N):
            plus_sum = arr[i][j]
            for k in range(1, M):
                if i - k >= 0:
                    plus_sum += arr[i - k][j]
                if i + k < N:
                    plus_sum += arr[i + k][j]
                if j - k >= 0:
                    plus_sum += arr[i][j - k]
                if j + k < N:
                    plus_sum += arr[i][j + k]

            cross_sum = arr[i][j]
            for k in range(1, M):
                if i - k >= 0 and j - k >= 0:
                    cross_sum += arr[i - k][j - k]
                if i - k >= 0 and j + k < N:
                    cross_sum += arr[i - k][j + k]
                if i + k < N and j - k >= 0:
                    cross_sum += arr[i + k][j - k]
                if i + k < N and j + k < N:
                    cross_sum += arr[i + k][j + k]

            max_flies = max(max_flies, plus_sum, cross_sum)
            
    print(f'#{t} {max_flies}')
