dp = [0] * 100
dp[0] = dp[1] = dp[2] = 1
dp[3] = dp[4] = 2
for i in range(5, 100):
    dp[i] = dp[i - 1] + dp[i - 5]

T = int(input())
for _ in range(T):
    N = int(input())
    print(dp[N - 1])