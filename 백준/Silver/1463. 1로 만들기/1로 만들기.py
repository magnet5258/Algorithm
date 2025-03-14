N = int(input())
dp = [0] * (N + 1)
dp[1] = 0
for i in range(2, N + 1):
    dp[i] = min(dp[i - 1] + 1,
                dp[i // 2] + 1 if i % 2 == 0 else float('inf'),
                dp[i // 3] + 1 if i % 3 == 0 else float('inf'))
print(dp[N])