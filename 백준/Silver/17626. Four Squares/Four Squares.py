n = int(input())
dp = [0] * (n + 1)
dp[1] = 1
for i in range(2, n + 1):
    if int(i ** 0.5) ** 2 == i:
        dp[i] = 1
    else:
        dp[i] = min(dp[i - j * j] for j in range(1, int(i ** 0.5) + 1)) + 1

print(dp[n])