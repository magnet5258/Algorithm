N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
max_sum = 0

for i in range(N):
    for j in range(M - 3):
        max_sum = max(max_sum, sum(arr[i][j:j + 4]))

for i in range(N - 3):
    for j in range(M):
        max_sum = max(max_sum, sum(arr[i + k][j] for k in range(4)))

for i in range(N - 1):
    for j in range(M - 1):
        max_sum = max(max_sum, sum(arr[i][j:j + 2]) + sum(arr[i + 1][j:j + 2]))

for i in range(N - 1):
    for j in range(M - 2):
        max_sum = max(max_sum,
                      sum(arr[i][j:j + 2]) + sum(arr[i + 1][j + 1:j + 3]),
                      sum(arr[i + 1][j:j + 2]) + sum(arr[i][j + 1:j + 3]))

for i in range(N - 2):
    for j in range(M - 1):
        max_sum = max(max_sum,
                      sum(arr[i + k][j] for k in range(2)) + sum(arr[i + 1 + k][j + 1] for k in range(2)),
                      sum(arr[i + 1 + k][j] for k in range(2)) + sum(arr[i + k][j + 1] for k in range(2)))

for i in range(N - 1):
    for j in range(M - 2):
        max_sum = max(max_sum,
                      arr[i][j] + sum(arr[i + 1][j:j + 3]),
                      arr[i][j + 1] + sum(arr[i + 1][j:j + 3]),
                      arr[i][j + 2] + sum(arr[i + 1][j:j + 3]),
                      arr[i + 1][j] + sum(arr[i][j:j + 3]),
                      arr[i + 1][j + 1] + sum(arr[i][j:j + 3]),
                      arr[i + 1][j + 2] + sum(arr[i][j:j + 3]))

for i in range(N - 2):
    for j in range(M - 1):
        max_sum = max(max_sum,
                      sum(arr[i + k][j] for k in range(3)) + arr[i][j + 1],
                      sum(arr[i + k][j] for k in range(3)) + arr[i + 1][j + 1],
                      sum(arr[i + k][j] for k in range(3)) + arr[i + 2][j + 1],
                      sum(arr[i + k][j + 1] for k in range(3)) + arr[i][j],
                      sum(arr[i + k][j + 1] for k in range(3)) + arr[i + 1][j],
                      sum(arr[i + k][j + 1] for k in range(3)) + arr[i + 2][j])

print(max_sum)