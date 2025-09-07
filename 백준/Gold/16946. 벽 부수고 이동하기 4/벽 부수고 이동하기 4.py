from collections import deque

N, M = map(int, input().split())
grid = [list(map(int, input())) for _ in range(N)]

area_id = [[-1] * M for _ in range(N)]
area_size = []

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

area_idx = 0
for i in range(N):
    for j in range(M):
        if grid[i][j] == 0 and area_id[i][j] == -1:
            queue = deque([(i, j)])
            area_id[i][j] = area_idx
            cnt = 1
            while queue:
                x, y = queue.popleft()
                for d in range(4):
                    nx, ny = x + dx[d], y + dy[d]
                    if 0 <= nx < N and 0 <= ny < M:
                        if grid[nx][ny] == 0 and area_id[nx][ny] == -1:
                            cnt += 1
                            area_id[nx][ny] = area_idx
                            queue.append((nx, ny))

            area_size.append(cnt)
            area_idx += 1

result = [[0] * M for _ in range(N)]
for i in range(N):
    for j in range(M):
        if grid[i][j] == 1:
            seen = set()
            val = 1
            for d in range(4):
                nx, ny = i + dx[d], j + dy[d]
                if 0 <= nx < N and 0 <= ny < M:
                    if grid[nx][ny] == 0 and area_id[nx][ny] not in seen:
                        val += area_size[area_id[nx][ny]]
                        seen.add(area_id[nx][ny])

            result[i][j] = val % 10

for row in result:
    print(''.join(map(str, row)))