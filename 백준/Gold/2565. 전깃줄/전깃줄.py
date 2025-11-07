N = int(input())
lst = []
for _ in range(N):
    A, B = map(int, input().split())
    lst.append((A, B))
lst.sort(key=lambda x: x[0])

dp = [1] * N
for i in range(N):
    for j in range(i):
        if lst[j][1] < lst[i][1]:
            dp[i] = max(dp[i], dp[j] + 1)

print(N - max(dp))