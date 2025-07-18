from itertools import combinations
from collections import deque
import copy

N, M = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(N)]

safe = []
virus = []
for i in range(N):
    for j in range(M):
        if grid[i][j] == 0:
            safe.append((i, j))
        elif grid[i][j] == 2:
            virus.append((i, j))

combs = list(combinations(safe, 3))
max_cnt = 0

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

for comb in combs:
    grid_copy = copy.deepcopy(grid)
    queue = deque(virus)
    for x, y in comb:
        grid_copy[x][y] = 1
    while queue:
        x, y = queue.popleft()
        for d in range(4):
            nx, ny = x + dx[d], y + dy[d]
            if 0 <= nx < N and 0 <= ny < M:
                if grid_copy[nx][ny] == 0:
                    queue.append((nx, ny))
                    grid_copy[nx][ny] = 2

    cur_cnt = sum(row.count(0) for row in grid_copy)
    max_cnt = max(max_cnt, cur_cnt)

print(max_cnt)