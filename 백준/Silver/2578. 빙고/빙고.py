bingo = [list(map(int, input().split())) for _ in range(5)]
ans_lst = []
for _ in range(5):
    ans_lst += list(map(int, input().split()))
pos_lst = [0] * 26
for i in range(5):
    for j in range(5):
        pos_lst[bingo[i][j]] = (i, j)
        
v = [[0] * 10 for _ in range(4)]
for n in ans_lst:
    i, j = pos_lst[n]
    v[0][j] += 1
    v[1][i] += 1
    v[2][i - j] += 1
    v[3][i + j] += 1
    cnt = 0
    for lst in v:
        cnt += lst.count(5)
    if cnt >= 3:
        break

print(sum(v[0]))