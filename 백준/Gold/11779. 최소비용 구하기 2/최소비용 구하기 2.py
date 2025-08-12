from collections import defaultdict
import heapq

n = int(input())
m = int(input())
graph = defaultdict(list)
for _ in range(m):
    s, e, c = map(int, input().split())
    graph[s].append((e, c))

start, end = map(int, input().split())
dist = [float('inf')] * (n + 1)
parent = [0] * (n + 1)

dist[start] = 0
hq = [(0, start)]
while hq:
    cost, node = heapq.heappop(hq)
    if cost != dist[node]:
        continue
    for nxt, w in graph[node]:
        nd = cost + w
        if nd < dist[nxt]:
            dist[nxt] = nd
            parent[nxt] = node
            heapq.heappush(hq, (nd, nxt))

path = []
cur = end
while cur != 0:
    path.append(cur)
    cur = parent[cur]
path.reverse()

print(dist[end])
print(len(path))
print(*path)