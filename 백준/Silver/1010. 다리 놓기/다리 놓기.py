T = int(input())
dp = [[0] * 30 for _ in range(30)]

for i in range(1, 30):
    dp[i][0] = 1
    dp[i][i] = 1
    for j in range(1, i):
        dp[i][j] = dp[i - 1][j - 1] + dp[i - 1][j]

for _ in range(T):
    N, M = map(int, input().split())
    print(dp[M][N])