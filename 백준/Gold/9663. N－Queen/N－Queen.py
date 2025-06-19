def n_queen(row):
    global cnt
    if row == N:
        cnt += 1
        return

    for col in range(N):
        safe = True
        for i in range(row):
            if queens[i] == col or abs(row - i) == abs(col - queens[i]):
                safe = False
                break
        if safe:
            queens[row] = col
            n_queen(row + 1)


N = int(input())
queens = [0] * N
cnt = 0
n_queen(0)
print(cnt)