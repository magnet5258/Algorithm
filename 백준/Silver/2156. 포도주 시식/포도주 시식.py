n = int(input())
wine = []
for _ in range(n):
    glass = int(input())
    wine.append(glass)

dp = [0] * len(wine)
for i in range(len(wine)):
    if i == 0:
        dp[i] = wine[i]
    elif i == 1:
        dp[i] = wine[i] + dp[i - 1]
    else:
        dp[i] = max(dp[i - 1], dp[i - 2] + wine[i], dp[i - 3] + wine[i - 1] + wine[i])

print(dp[n - 1])