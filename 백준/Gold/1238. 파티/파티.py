import heapq
from collections import defaultdict

INF = float('inf')
N, M, X = map(int, input().split())
graph = defaultdict(list)
reverse_graph = defaultdict(list)
for _ in range(M):
    u, v, w = map(int, input().split())
    graph[u].append((v, w))
    reverse_graph[v].append((u, w))

def party(start, graph):
    dist = [INF] * (N + 1)
    dist[start] = 0
    heap = [(0, start)]

    while heap:
        d, u = heapq.heappop(heap)
        if d > dist[u]:
            continue
        for v, w in graph[u]:
            nd = d + w
            if nd < dist[v]:
                dist[v] = nd
                heapq.heappush(heap, (nd, v))

    return dist

dist_from_X = party(X, graph)
dist_to_X = party(X, reverse_graph)

result = 0
for i in range(1, N + 1):
    result = max(result, dist_from_X[i] + dist_to_X[i])

print(result)