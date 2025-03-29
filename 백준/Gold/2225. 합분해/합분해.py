N, K = map(int, input().split())
dp = [[0] * (N + 1) for _ in range(K + 1)]
for i in range(1, K + 1):
    dp[i][1] = i
for j in range(1, N + 1):
    dp[1][j] = 1
for k in range(2, K + 1):
    for l in range(2, N + 1):
        dp[k][l] = dp[k - 1][l] + dp[k][l - 1]
print(dp[K][N] % 1000000000)