magic = [list(map(int, input().split())) for _ in range(3)]

sum_lst = []
for i in range(3):
    if 0 not in magic[i]:
        sum_lst.append(sum(magic[i]))
for j in range(3):
    col = [magic[i][j] for i in range(3)]
    if 0 not in col:
        sum_lst.append(sum(col))
diag1 = [magic[k][k] for k in range(3)]
if 0 not in diag1:
    sum_lst.append(sum(diag1))
diag2 = [magic[k][2 - k] for k in range(3)]
if 0 not in diag2:
    sum_lst.append(sum(diag2))

if sum_lst:
    max_sum = max(sum_lst)

    for _ in range(10):
        for i in range(3):
            row = magic[i]
            if row.count(0) == 1:
                j = row.index(0)
                magic[i][j] = max_sum - sum(row)

        for j in range(3):
            col = [magic[i][j] for i in range(3)]
            if col.count(0) == 1:
                i = col.index(0)
                magic[i][j] = max_sum - sum(col)

        diag1 = [magic[k][k] for k in range(3)]
        if diag1.count(0) == 1:
            k = diag1.index(0)
            magic[k][k] = max_sum - sum(diag1)

        diag2 = [magic[k][2 - k] for k in range(3)]
        if diag2.count(0) == 1:
            k = diag2.index(0)
            magic[k][2 - k] = max_sum - sum(diag2)
else:
    if magic[0][0] == magic[1][1] == magic[2][2] == 0:
        s = magic[0][1] + magic[0][2] + magic[1][0] + magic[1][2] + magic[2][0] + magic[2][1]
        target = s // 2
        magic[0][0] = target - (magic[0][1] + magic[0][2])
        magic[1][1] = target - (magic[1][0] + magic[1][2])
        magic[2][2] = target - (magic[2][0] + magic[2][1])
    elif magic[0][2] == magic[1][1] == magic[2][0] == 0:
        s = magic[0][0] + magic[0][1] + magic[1][0] + magic[1][2] + magic[2][1] + magic[2][2]
        target = s // 2
        magic[0][2] = target - (magic[0][0] + magic[0][1])
        magic[1][1] = target - (magic[1][0] + magic[1][2])
        magic[2][0] = target - (magic[2][1] + magic[2][2])

for row in magic:
    print(*row)