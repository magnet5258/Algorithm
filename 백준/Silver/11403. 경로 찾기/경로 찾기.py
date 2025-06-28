N = int(input())
grid = [list(map(int, input().split())) for _ in range(N)]

for k in range(N):
    for i in range(N):
        for j in range(N):
            if grid[i][k] and grid[k][j]:
                grid[i][j] = 1

for row in grid:
    print(*row)