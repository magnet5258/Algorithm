from collections import defaultdict, deque

N, M, K = map(int, input().split())
c = [0] + list(map(int, input().split()))
friends = defaultdict(list)
for _ in range(M):
    a, b = map(int, input().split())
    friends[a].append(b)
    friends[b].append(a)

visited = [False] * (N + 1)
total_c = []

for i in range(1, N + 1):
    if visited[i]:
        continue
    queue = deque([i])
    visited[i] = True
    total = c[i]
    cnt = 1
    while queue:
        num = queue.popleft()
        for friend in friends[num]:
            if not visited[friend]:
                visited[friend] = True
                total += c[friend]
                cnt += 1
                queue.append(friend)

    total_c.append((cnt, total))

dp = [0] * K
for cnt, total in total_c:
    for w in range(K - 1, cnt - 1, -1):
        dp[w] = max(dp[w], dp[w - cnt] + total)

print(max(dp))