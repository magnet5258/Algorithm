N, M = map(int, input().split())
paper = [list(map(int, list(input()))) for _ in range(N)]
max_total = 0

for bitmask in range(1 << (N * M)):
    total = 0
    for i in range(N):
        row_sum = 0
        for j in range(M):
            idx = i * M + j
            if bitmask & (1 << idx):
                row_sum = row_sum * 10 + paper[i][j]
            else:
                total += row_sum
                row_sum = 0
        total += row_sum

    for j in range(M):
        col_sum = 0
        for i in range(N):
            idx = i * M + j
            if not (bitmask & (1 << idx)):
                col_sum = col_sum * 10 + paper[i][j]
            else:
                total += col_sum
                col_sum = 0
        total += col_sum

    max_total = max(max_total, total)

print(max_total)