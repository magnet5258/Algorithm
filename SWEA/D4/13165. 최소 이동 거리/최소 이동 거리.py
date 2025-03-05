import heapq
from collections import defaultdict

def dijkstra():
    distances = [float('inf') for _ in range(N + 1)]
    distances[0] = 0
    queue = [(distances[0], 0)]
    heapq.heapify(queue)
    while queue:
        dist, now = heapq.heappop(queue)
        if distances[now] < dist:
            continue
        for next, weight in graph[now]:
            if distances[next] > dist + weight:
                distances[next] = dist + weight
                heapq.heappush(queue, (distances[next], next))

    return distances[N]


T = int(input())
for test_case in range(1, T + 1):
    N, E = map(int, input().split())
    graph = defaultdict(list)
    for _ in range(E):
        x, y, z = map(int, input().split())
        graph[x].append((y, z))

    print(f'#{test_case} {dijkstra()}')