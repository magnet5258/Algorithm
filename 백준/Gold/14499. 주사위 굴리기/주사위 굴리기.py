N, M, x, y, K = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(N)]
orders = list(map(int, input().split()))

dice = [0] * 7
i, j = x, y
top, bottom, east, west, north, south = 1, 6, 3, 4, 2, 5
for order in orders:
    if order == 1 and j + 1 < M:
        top, bottom, east, west = west, east, top, bottom
        if grid[i][j + 1] == 0:
            grid[i][j + 1] = dice[bottom]
        else:
            dice[bottom] = grid[i][j + 1]
            grid[i][j + 1] = 0
        j += 1
        print(dice[top])
    elif order == 2 and j - 1 >= 0:
        top, bottom, east, west = east, west, bottom, top
        if grid[i][j - 1] == 0:
            grid[i][j - 1] = dice[bottom]
        else:
            dice[bottom] = grid[i][j - 1]
            grid[i][j - 1] = 0
        j -= 1
        print(dice[top])
    elif order == 3 and i - 1 >= 0:
        top, bottom, north, south = south, north, top, bottom
        if grid[i - 1][j] == 0:
            grid[i - 1][j] = dice[bottom]
        else:
            dice[bottom] = grid[i - 1][j]
            grid[i - 1][j] = 0
        i -= 1
        print(dice[top])
    elif order == 4 and i + 1 < N:
        top, bottom, north, south = north, south, bottom, top
        if grid[i + 1][j] == 0:
            grid[i + 1][j] = dice[bottom]
        else:
            dice[bottom] = grid[i + 1][j]
            grid[i + 1][j] = 0
        i += 1
        print(dice[top])