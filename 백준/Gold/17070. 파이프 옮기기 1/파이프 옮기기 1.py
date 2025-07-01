def pipe(x, y, direction):
    if x == N - 1 and y == N - 1:
        return 1

    if dp[x][y][direction] != -1:
        return dp[x][y][direction]

    cnt = 0

    if direction in (0, 2):
        nx, ny = x, y + 1
        if ny < N and grid[nx][ny] == 0:
            cnt += pipe(nx, ny, 0)

    if direction in (1, 2):
        nx, ny = x + 1, y
        if nx < N and grid[nx][ny] == 0:
            cnt += pipe(nx, ny, 1)

    nx, ny = x + 1, y + 1
    if nx < N and ny < N:
        if grid[x + 1][y] == 0 and grid[x][y + 1] == 0 and grid[nx][ny] == 0:
            cnt += pipe(nx, ny, 2)

    dp[x][y][direction] = cnt
    return cnt

N = int(input())
grid = [list(map(int, input().split())) for _ in range(N)]
dp = [[[-1] * 3 for _ in range(N)] for _ in range(N)]
print(pipe(0, 1, 0))
