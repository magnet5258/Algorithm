from collections import deque

N = int(input())
grid = [list(input()) for _ in range(N)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
visited = [[False] * N for _ in range(N)]
house = []

for i in range(N):
    for j in range(N):
        if not visited[i][j] and grid[i][j] == '1':
            queue = deque()
            queue.append((i, j))
            visited[i][j] = True
            cnt = 1
            while queue:
                x, y = queue.popleft()
                for d in range(4):
                    nx, ny = x + dx[d], y + dy[d]
                    if 0 <= nx < N and 0 <= ny < N:
                        if not visited[nx][ny] and grid[nx][ny] == '1':
                            visited[nx][ny] = True
                            queue.append((nx, ny))
                            cnt += 1
            house.append(cnt)

print(len(house))
house.sort()
for h in house:
    print(h)