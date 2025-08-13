from collections import defaultdict, deque

N, M = map(int, input().split())
graph = defaultdict(list)
for _ in range(M):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

visited = [False] * (N + 1)
queue = deque()
queue.append(1)
visited[1] = True
cnt = 1

for i in range(1, N + 1):
    if not visited[i]:
        cnt += 1
        queue.append(i)
    while queue:
        node = queue.popleft()
        for neighbor in graph[node]:
            if not visited[neighbor]:
                visited[neighbor] = True
                queue.append(neighbor)

print(cnt)