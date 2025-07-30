N = int(input())
matrix = []
for _ in range(N):
    r, c = map(int, input().split())
    matrix.append((r, c))

dp = [[0] * N for _ in range(N)]
for length in range(1, N):
    for i in range(N - length):
        j = i + length
        dp[i][j] = float('inf')
        for k in range(i, j):
            dp[i][j] = min(dp[i][j], dp[i][k] + dp[k + 1][j] + matrix[i][0] * matrix[k][1] * matrix[j][1])

print(dp[0][N - 1])