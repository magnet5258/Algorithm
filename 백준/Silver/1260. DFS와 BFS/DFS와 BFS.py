from collections import defaultdict, deque

def dfs(x):
    visited_dfs[x] = True
    dfs_lst.append(x)
    for neighbor in graph[x]:
        if not visited_dfs[neighbor]:
            dfs(neighbor)


def bfs(x):
    visited_bfs = [False] * (N + 1)
    queue = deque([x])
    bfs_lst.append(x)
    visited_bfs[x] = True
    while queue:
        node = queue.popleft()
        for neighbor in graph[node]:
            if not visited_bfs[neighbor]:
                bfs_lst.append(neighbor)
                queue.append(neighbor)
                visited_bfs[neighbor] = True


N, M, V = map(int, input().split())
graph = defaultdict(list)
for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

for i in range(1, N + 1):
    graph[i].sort()

dfs_lst = []
bfs_lst = []

visited_dfs = [False] * (N + 1)
visited_bfs = [False] * (N + 1)

dfs(V)
bfs(V)

print(*dfs_lst)
print(*bfs_lst)