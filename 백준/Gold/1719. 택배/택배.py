from collections import defaultdict
import heapq

n, m = map(int, input().split())
graph = defaultdict(list)
for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))

def dijkstra(start):
    dist = [float('inf')] * (n + 1)
    firstHop = [0] * (n + 1)
    pq = []
    dist[start] = 0
    heapq.heappush(pq, (0, start))
    while pq:
        cost, now = heapq.heappop(pq)
        if dist[now] < cost:
            continue
        for next, w in graph[now]:
            new_cost = cost + w
            if new_cost < dist[next]:
                dist[next] = new_cost
                heapq.heappush(pq, (new_cost, next))
                if now == start:
                    firstHop[next] = next
                else:
                    firstHop[next] = firstHop[now]
    return firstHop

answer = [[0] * (n + 1) for _ in range(n + 1)]
for i in range(1, n + 1):
    hops = dijkstra(i)
    for j in range(1, n + 1):
        if i == j:
            answer[i][j] = '-'
        else:
            answer[i][j] = hops[j]

for i in range(1, n + 1):
    print(' '.join(map(str, answer[i][1:])))