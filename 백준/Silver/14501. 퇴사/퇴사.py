N = int(input())
lst1 = []
lst2 = []
for _ in range(N):
    T, P = map(int, input().split())
    lst1.append(T)
    lst2.append(P)

dp = [0] * (N + 1)

for i in range(N):
    dp[i + 1] = max(dp[i + 1], dp[i])
    if i + lst1[i] <= N:
        dp[i + lst1[i]] = max(dp[i + lst1[i]], dp[i] + lst2[i])

print(dp[N])