def cover(x, y, used):
    global min_used

    if used >= min_used:
        return

    if x == 10:
        min_used = used
        return

    if paper[x][y] == 0:
        if y < 9:
            cover(x, y + 1, used)
        else:
            cover(x + 1, 0, used)
        return

    for size in range(5, 0, -1):
        if paper_cnt[size] == 0 or x + size > 10 or y + size > 10:
            continue

        can_attach = True
        for i in range(x, x + size):
            for j in range(y, y + size):
                if paper[i][j] != 1:
                    can_attach = False
                    break
            if not can_attach:
                break

        if can_attach:
            for i in range(x, x + size):
                for j in range(y, y + size):
                    paper[i][j] = 0
            paper_cnt[size] -= 1

            if y < 9:
                cover(x, y + 1, used + 1)
            else:
                cover(x + 1, 0, used + 1)

            for i in range(x, x + size):
                for j in range(y, y + size):
                    paper[i][j] = 1
            paper_cnt[size] += 1


paper = [list(map(int, input().split())) for _ in range(10)]
paper_cnt = [0, 5, 5, 5, 5, 5]
min_used = float('inf')
cover(0, 0, 0)
if min_used == float('inf'):
    print(-1)
else:
    print(min_used)