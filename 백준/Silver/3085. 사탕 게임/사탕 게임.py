N = int(input())
arr = [list(input()) for _ in range(N)]
max_cnt = 0
for i in range(N):
    for j in range(N):
        if j < N - 1:
            arr[i][j], arr[i][j + 1] = arr[i][j + 1], arr[i][j]
            for x in [i, j, j + 1]:
                row_cnt = 1
                col_cnt = 1
                for k in range(1, N):
                    if x == i and arr[x][k] == arr[x][k - 1]:
                        row_cnt += 1
                    else:
                        max_cnt = max(max_cnt, row_cnt)
                        row_cnt = 1
                    if x != i and arr[k][x] == arr[k - 1][x]:
                        col_cnt += 1
                    else:
                        max_cnt = max(max_cnt, col_cnt)
                        col_cnt = 1
                max_cnt = max(max_cnt, row_cnt, col_cnt)
            arr[i][j], arr[i][j + 1] = arr[i][j + 1], arr[i][j]

        if i < N - 1:
            arr[i][j], arr[i + 1][j] = arr[i + 1][j], arr[i][j]
            for x in [j, i, i + 1]:
                row_cnt = 1
                col_cnt = 1
                for k in range(1, N):
                    if x != j and arr[x][k] == arr[x][k - 1]:
                        row_cnt += 1
                    else:
                        max_cnt = max(max_cnt, row_cnt)
                        row_cnt = 1
                    if x == j and arr[k][x] == arr[k - 1][x]:
                        col_cnt += 1
                    else:
                        max_cnt = max(max_cnt, col_cnt)
                        col_cnt = 1
                max_cnt = max(max_cnt, row_cnt, col_cnt)
            arr[i][j], arr[i + 1][j] = arr[i + 1][j], arr[i][j]

print(max_cnt)