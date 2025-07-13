from collections import deque

N, M = map(int, input().split())
grid = [list(input()) for _ in range(N)]
visited = [[False] * M for _ in range(N)]
cnt = [[0] * M for _ in range(N)]

queue = deque([(0, 0)])
visited[0][0] = True
cnt[0][0] = 1

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

while queue:
    x, y = queue.popleft()
    for d in range(4):
        nx, ny = x + dx[d], y + dy[d]
        if 0 <= nx < N and 0 <= ny < M:
            if not visited[nx][ny] and grid[nx][ny] == '1':
                queue.append((nx, ny))
                visited[nx][ny] = True
                cnt[nx][ny] = cnt[x][y] + 1

print(cnt[N - 1][M - 1])