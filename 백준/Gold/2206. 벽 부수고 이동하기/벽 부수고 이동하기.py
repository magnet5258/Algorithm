from collections import deque

N, M = map(int, input().split())
grid = [list(map(int, input())) for _ in range(N)]
visited = [[[False] * 2 for _ in range(M)] for _ in range(N)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

queue = deque()
queue.append((0, 0, 0, 1))
visited[0][0][0] = True

while queue:
    x, y, brick, dist = queue.popleft()

    if x == N - 1 and y == M - 1:
        print(dist)
        exit()

    for d in range(4):
        nx, ny = x + dx[d], y + dy[d]
        if 0 <= nx < N and 0 <= ny < M:
            if grid[nx][ny] == 1 and brick == 0:
                if not visited[nx][ny][1]:
                    visited[nx][ny][1] = True
                    queue.append((nx, ny, 1, dist + 1))
            elif grid[nx][ny] == 0:
                if not visited[nx][ny][brick]:
                    visited[nx][ny][brick] = True
                    queue.append((nx, ny, brick, dist + 1))

print(-1)