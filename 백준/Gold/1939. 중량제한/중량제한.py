from collections import defaultdict
import heapq

N, M = map(int, input().split())
graph = defaultdict(list)

for _ in range(M):
    A, B, C = map(int, input().split())
    graph[A].append((B, C))
    graph[B].append((A, C))

start, end = map(int, input().split())
capacity = [0] * (N + 1)
capacity[start] = float('inf')

pq = [(-capacity[start], start)]
while pq:
    cap, node = heapq.heappop(pq)
    cap = -cap
    if node == end:
        print(cap)
        break
    for nxt, w in graph[node]:
        new_cap = min(cap, w)
        if new_cap > capacity[nxt]:
            capacity[nxt] = new_cap
            heapq.heappush(pq, (-new_cap, nxt))