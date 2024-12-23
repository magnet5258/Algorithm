T = int(input())
for t in range(1, T + 1):
    n = int(input())
    matrix = [[0] * n for i in range(n)]
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    direction_idx = 0
    row, col = 0, 0
    for i in range(1, n * n + 1):
        matrix[row][col] = i
        next_row = row + directions[direction_idx][0]
        next_col = col + directions[direction_idx][1]
        if (next_row < 0 or next_row >= n or next_col < 0 or next_col >= n or matrix[next_row][next_col] != 0):
            direction_idx = (direction_idx + 1) % 4
            next_row = row + directions[direction_idx][0]
            next_col = col + directions[direction_idx][1]
        row, col = next_row, next_col
    print(f'#{t}')
    for row in matrix:
        print(' '.join(map(str, row)))
        
        