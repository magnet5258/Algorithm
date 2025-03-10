import heapq
from collections import defaultdict

V, E = map(int, input().split())
K = int(input())
path = [list(map(int, input().split())) for _ in range(E)]
graph = defaultdict(list)
for u, v, w in path:
    graph[u].append((v, w))
distances = [float('inf')] * (V + 1)
distances[K] = 0
queue = [(0, K)]
heapq.heapify(queue)

while queue:
    dist, node = heapq.heappop(queue)
    if distances[node] < dist:
        continue
    for neighbor, weight in graph[node]:
        new_dist = dist + weight
        if new_dist < distances[neighbor]:
            distances[neighbor] = new_dist
            heapq.heappush(queue, (new_dist, neighbor))

for i in range(1, V + 1):
    print('INF' if distances[i] == float('inf') else distances[i])