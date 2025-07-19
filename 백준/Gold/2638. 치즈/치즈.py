from collections import deque

N, M = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(N)]

time = 0
while True:
    queue = deque([(0, 0)])
    visited = [[False] * M for _ in range(N)]
    visited[0][0] = True
    grid[0][0] = -1

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    while queue:
        x, y = queue.popleft()
        for d in range(4):
            nx, ny = x + dx[d], y + dy[d]
            if 0 <= nx < N and 0 <= ny < M:
                if not visited[nx][ny] and grid[nx][ny] == 0:
                    visited[nx][ny] = True
                    grid[nx][ny] = -1
                    queue.append((nx, ny))
                elif not visited[nx][ny] and grid[nx][ny] == -1:
                    visited[nx][ny] = True
                    queue.append((nx, ny))

    cheese_exist = False
    to_remove = []
    for i in range(N):
        for j in range(M):
            if grid[i][j] == 1:
                cheese_exist = True
                cnt = 0
                for d in range(4):
                    ni, nj = i + dx[d], j + dy[d]
                    if 0 <= ni < N and 0 <= nj < M:
                        if grid[ni][nj] == -1:
                            cnt += 1
                if cnt >= 2:
                    to_remove.append((i, j))

    for i, j in to_remove:
        grid[i][j] = -1

    if not cheese_exist:
        break

    time += 1

print(time)