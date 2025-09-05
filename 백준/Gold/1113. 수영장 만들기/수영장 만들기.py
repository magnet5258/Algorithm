from collections import deque

N, M = map(int, input().split())
pool = [list(map(int, input())) for _ in range(N)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

water = 0

for h in range(2, 10):
    visited = [[False] * M for _ in range(N)]
    for i in range(N):
        for j in range(M):
            if pool[i][j] < h and not visited[i][j]:
                queue = deque([(i, j)])
                visited[i][j] = True
                region = [(i, j)]
                can_fill = True

                while queue:
                    x, y = queue.popleft()
                    if x == 0 or y == 0 or x == N - 1 or y == M - 1:
                        can_fill = False

                    for d in range(4):
                        nx, ny = x + dx[d], y + dy[d]
                        if 0 <= nx < N and 0 <= ny < M:
                            if pool[nx][ny] < h and not visited[nx][ny]:
                                visited[nx][ny] = True
                                queue.append((nx, ny))
                                region.append((nx, ny))

                if can_fill:
                    for x, y in region:
                        water += h - pool[x][y]
                        pool[x][y] = h

print(water)