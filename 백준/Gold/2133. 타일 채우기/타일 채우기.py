N = int(input())
if N % 2 == 1:
    print(0)
else:
    dp = [0] * (N + 1)
    dp[0] = 1
    for i in range(2, N + 1, 2):
        dp[i] = dp[i - 2] * 3
        for j in range(i - 4, -1, -2):
            dp[i] += dp[j] * 2
    print(dp[N])