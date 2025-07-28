from collections import deque

N, M = map(int, input().split())
campus = [list(input()) for _ in range(N)]
visited = [[False] * M for _ in range(N)]

sx, sy = 0, 0
found = False
for x in range(N):
    for y in range(M):
        if campus[x][y] == 'I':
            sx, sy = x, y
            found = True
            break
    if found:
        break

queue = deque()
queue.append((sx, sy))
visited[sx][sy] = True

cnt = 0
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
while queue:
    x, y = queue.popleft()
    for d in range(4):
        nx, ny = x + dx[d], y + dy[d]
        if 0 <= nx < N and 0 <= ny < M:
            if not visited[nx][ny] and campus[nx][ny] == 'P':
                cnt += 1
                queue.append((nx, ny))
                visited[nx][ny] = True
            elif not visited[nx][ny] and campus[nx][ny] == 'O':
                queue.append((nx, ny))
                visited[nx][ny] = True

if cnt == 0:
    print('TT')
else:
    print(cnt)