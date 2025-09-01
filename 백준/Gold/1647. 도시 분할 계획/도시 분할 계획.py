def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

def union(a, b):
    a, b = find(a), find(b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

N, M = map(int, input().split())
edges = []
for _ in range(M):
    A, B, C = map(int, input().split())
    edges.append((C, A, B))

edges.sort()
parent = [i for i in range(N + 1)]

total_cost = 0
max_edge = 0

for cost, a, b in edges:
    if find(a) != find(b):
        union(a, b)
        total_cost += cost
        max_edge = cost

print(total_cost - max_edge)