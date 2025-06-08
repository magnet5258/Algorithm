A = input()
B = input()
N, M = len(A), len(B)

dp = [[0] * (M + 1) for _ in range(N + 1)]
dp[0][0] = dp[1][0] = dp[0][1] = 0

for i in range(1, N + 1):
    for j in range(1, M + 1):
        if A[i - 1] == B[j - 1]:
            dp[i][j] = dp[i - 1][j - 1] + 1
        else:
            dp[i][j] = max(dp[i][j - 1], dp[i - 1][j])

print(dp[N][M])