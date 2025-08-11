from collections import defaultdict
import heapq

N, M = map(int, input().split())
graph = defaultdict(list)
for _ in range(M):
    A, B, C = map(int, input().split())
    graph[A].append((B, C))
    graph[B].append((A, C))

dist = [float('inf')] * (N + 1)
dist[1] = 0
pq = [(0, 1)]

while pq:
    cost, u = heapq.heappop(pq)
    if cost != dist[u]:
        continue
    if u == N:
        break
    for v, w in graph[u]:
        nd = cost + w
        if nd < dist[v]:
            dist[v] = nd
            heapq.heappush(pq, (nd, v))

print(dist[N])