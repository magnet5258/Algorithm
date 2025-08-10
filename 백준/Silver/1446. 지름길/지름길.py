from collections import defaultdict

N, D = map(int, input().split())
shortcuts = defaultdict(list)
for _ in range(N):
    s, e, l = map(int, input().split())
    if e <= D and l < e - s:
        shortcuts[s].append((e, l))

dp = [float('inf')] * (D + 1)
dp[0] = 0

for i in range(D):
    if dp[i + 1] > dp[i] + 1:
        dp[i + 1] = dp[i] + 1
    for e, l in shortcuts[i]:
        if dp[e] > dp[i] + l:
            dp[e] = dp[i] + l

print(dp[D])