N = int(input())
divisor_sum = [0] * (N + 1)
for i in range(1, N + 1):
    for j in range(i, N + 1, i):
        divisor_sum[j] += i

dp = [0] * (N + 1)
for i in range(1, N + 1):
    dp[i] = dp[i - 1] + divisor_sum[i]

print(dp[N])