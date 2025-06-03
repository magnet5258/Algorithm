from collections import deque, defaultdict

N = int(input())
graph = defaultdict(list)
for _ in range(N - 1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

parents = [0] * (N + 1)
visited = [False] * (N + 1)

def find_root(start):
    queue = deque([start])
    visited[start] = True
    while queue:
        node = queue.popleft()
        for neighbor in graph[node]:
            if not visited[neighbor]:
                visited[neighbor] = True
                parents[neighbor] = node
                queue.append(neighbor)

find_root(1)
for i in range(2, N + 1):
    print(parents[i])