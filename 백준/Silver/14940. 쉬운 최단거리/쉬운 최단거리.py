from collections import deque

n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]
len_grid = [[-1] * m for _ in range(n)]
sx, sy = 0, 0

for i in range(n):
    for j in range(m):
        if grid[i][j] == 2:
            sx, sy = i, j
            len_grid[i][j] = 0
        elif grid[i][j] == 0:
            len_grid[i][j] = 0

queue = deque([(sx, sy)])
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

while queue:
    x, y = queue.popleft()
    for d in range(4):
        nx, ny = x + dx[d], y + dy[d]
        if 0 <= nx < n and 0 <= ny < m:
            if len_grid[nx][ny] == -1 and grid[nx][ny] == 1:
                len_grid[nx][ny] = len_grid[x][y] + 1
                queue.append((nx, ny))

for row in len_grid:
    print(*row)