N, K = map(int, input().split())
items = []
for _ in range(N):
    W, V = map(int, input().split())
    items.append((W, V))

dp = [0] * (K + 1)
for W, V in items:
    for weight in range(K, W - 1, -1):
        dp[weight] = max(dp[weight], dp[weight - W] + V)

print(dp[-1])