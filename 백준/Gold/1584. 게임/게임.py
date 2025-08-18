from collections import deque

grid = [[0] * 501 for _ in range(501)]

N = int(input())
for _ in range(N):
    X1, Y1, X2, Y2 = map(int, input().split())
    sX, eX = min(X1, X2), max(X1, X2)
    sY, eY = min(Y1, Y2), max(Y1, Y2)
    for i in range(sX, eX + 1):
        for j in range(sY, eY + 1):
            grid[i][j] = 1

M = int(input())
for _ in range(M):
    X1, Y1, X2, Y2 = map(int, input().split())
    sX, eX = min(X1, X2), max(X1, X2)
    sY, eY = min(Y1, Y2), max(Y1, Y2)
    for i in range(sX, eX + 1):
        for j in range(sY, eY + 1):
            grid[i][j] = -1

dist = [[float('inf')] * 501 for _ in range(501)]
queue = deque()
dist[0][0] = 0
queue.append((0, 0))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

while queue:
    x, y = queue.popleft()
    for d in range(4):
        nx, ny = x + dx[d], y + dy[d]
        if 0 <= nx < 501 and 0 <= ny < 501:
            if grid[nx][ny] == -1:
                continue
            w = 1 if grid[nx][ny] == 1 else 0
            if dist[nx][ny] > dist[x][y] + w:
                dist[nx][ny] = dist[x][y] + w
                if w == 0:
                    queue.appendleft((nx, ny))
                else:
                    queue.append((nx, ny))

print(dist[500][500] if dist[500][500] != float('inf') else -1)