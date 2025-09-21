n = int(input())
m = int(input())
dist = [[float('inf')] * (n + 1) for _ in range(n + 1)]
path = [[[] for _ in range(n + 1)] for _ in range(n + 1)]

for i in range(1, n + 1):
    for j in range(1, n + 1):
        if i == j:
            dist[i][j] = 0

for _ in range(m):
    a, b, c = map(int, input().split())
    dist[a][b] = min(dist[a][b], c)
    path[a][b] = [a, b]

for k in range(1, n + 1):
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if dist[i][j] > dist[i][k] + dist[k][j]:
                dist[i][j] = dist[i][k] + dist[k][j]
                path[i][j] = path[i][k][:-1] + path[k][j]

for i in range(1, n + 1):
    for j in range(1, n + 1):
        if dist[i][j] == float('inf'):
            dist[i][j] = 0

for i in range(1, n + 1):
    print(*dist[i][1:])

for i in range(1, n + 1):
    for j in range(1, n + 1):
        if len(path[i][j]) == 0:
            print(0)
        else:
            print(len(path[i][j]), *path[i][j])