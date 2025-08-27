from collections import deque

N = int(input())
grid = [list(map(int, input().split())) for _ in range(N)]

for x in range(N):
    for y in range(N):
        if grid[x][y] == 9:
            sx, sy = x, y
            grid[x][y] = 0
            break

size = 2
eaten = 0
time = 0

dx = [-1, 0, 0, 1]
dy = [0, -1, 1, 0]

while True:
    queue = deque([(sx, sy, 0)])
    visited = [[False] * N for _ in range(N)]
    visited[sx][sy] = True
    fishes = []
    min_dist = None

    while queue:
        x, y, dist = queue.popleft()
        if min_dist is not None and dist > min_dist:
            break
        if 0 < grid[x][y] < size:
            fishes.append((dist, x, y))
            min_dist = dist
            continue

        for d in range(4):
            nx, ny = x + dx[d], y + dy[d]
            if 0 <= nx < N and 0 <= ny < N and not visited[nx][ny]:
                if grid[nx][ny] <= size:
                    visited[nx][ny] = True
                    queue.append((nx, ny, dist + 1))

    if not fishes:
        break

    fishes.sort()
    dist, fx, fy = fishes[0]

    sx, sy = fx, fy
    grid[fx][fy] = 0
    time += dist
    eaten += 1
    
    if eaten == size:
        size += 1
        eaten = 0

print(time)