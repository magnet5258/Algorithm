squares = [list(map(int, input().split())) for _ in range(4)]
max_x = max(square[2] for square in squares)
max_y = max(square[3] for square in squares)
arr = [[0] * max_x for _ in range(max_y)]
for x1, y1, x2, y2 in squares:
    for i in range(y1, y2):
        for j in range(x1, x2):
            arr[i][j] = 1
print(sum(map(sum, arr)))