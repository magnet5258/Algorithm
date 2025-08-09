from collections import deque

M, N, H = map(int, input().split())
farm = [[list(map(int, input().split())) for _ in range(N)] for _ in range(H)]

dx = [-1, 1]
dy = [-1, 1, 0, 0]
dz = [0, 0, -1, 1]

queue = deque()
for i in range(H):
    for j in range(N):
        for k in range(M):
            if farm[i][j][k] == 1:
                queue.append((i, j, k, 0))

cnt = 0
while queue:
    x, y, z, day = queue.popleft()
    cnt = max(cnt, day)

    for d in range(4):
        ny, nz = y + dy[d], z + dz[d]
        if 0 <= ny < N and 0 <= nz < M:
            if farm[x][ny][nz] == 0:
                farm[x][ny][nz] = 1
                queue.append((x, ny, nz, day + 1))

    for d in range(2):
        nx = x + dx[d]
        if 0 <= nx < H:
            if farm[nx][y][z] == 0:
                farm[nx][y][z] = 1
                queue.append((nx, y, z, day + 1))

if any(0 in row for layer in farm for row in layer):
    print(-1)
else:
    print(cnt)