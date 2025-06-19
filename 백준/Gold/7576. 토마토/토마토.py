from collections import deque

M, N = map(int, input().split())
box = [list(map(int, input().split())) for _ in range(N)]
queue = deque()
for i in range(N):
    for j in range(M):
        if box[i][j] == 1:
            queue.append((i, j))

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

while queue:
    x, y = queue.popleft()
    for d in range(4):
        nx, ny = x + dx[d], y + dy[d]
        if 0 <= nx < N and 0 <= ny < M and box[nx][ny] == 0:
            box[nx][ny] = box[x][y] + 1
            queue.append((nx, ny))

day_cnt = 0
for row in box:
    for tomato in row:
        if tomato == 0:
            print(-1)
            exit(0)
        day_cnt = max(day_cnt, tomato)

print(day_cnt - 1)