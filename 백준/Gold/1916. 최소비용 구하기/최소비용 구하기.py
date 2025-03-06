import heapq
from collections import defaultdict

def dijkstra():
    distances = [float('inf') for _ in range(N + 1)]
    distances[start] = 0
    queue = [(distances[start], start)]
    heapq.heapify(queue)
    while queue:
        dist, now = heapq.heappop(queue)
        if distances[now] < dist:
            continue
        for next, weight in graph[now]:
            if distances[next] > dist + weight:
                distances[next] = dist + weight
                heapq.heappush(queue, (distances[next], next))

    return distances[end]


N = int(input())
M = int(input())
graph = defaultdict(list)
for _ in range(M):
    x, y, z = map(int, input().split())
    graph[x].append((y, z))
start, end = map(int, input().split())
print(dijkstra())