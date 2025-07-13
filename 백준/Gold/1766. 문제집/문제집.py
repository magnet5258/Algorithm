from collections import defaultdict
import heapq

N, M = map(int, input().split())
graph = defaultdict(list)
for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    
indegree = [0] * (N + 1)
for x in graph:
    for y in graph[x]:
        indegree[y] += 1

heap = []
for i in range(1, N + 1):
    if indegree[i] == 0:
        heapq.heappush(heap, i)

result = []
while heap:
    current = heapq.heappop(heap)
    result.append(current)
    for neighbor in graph[current]:
        indegree[neighbor] -= 1
        if indegree[neighbor] == 0:
            heapq.heappush(heap, neighbor)

print(*result)