from itertools import combinations

N = int(input())
S = [list(map(int, input().split())) for _ in range(N)]
p = list(range(N))

comb = list(combinations(p, N // 2))
set_comb = comb[:len(comb) // 2]
min_diff = float('inf')
for c1 in set_comb:
    c2 = [i for i in p if i not in c1]
    sum_c1 = 0
    sum_c2 = 0
    for a in c1:
        for b in c1:
            if a != b:
                sum_c1 += S[a][b]
    for c in c2:
        for d in c2:
            if c != d:
                sum_c2 += S[c][d]
    min_diff = min(min_diff, abs(sum_c1 - sum_c2))

print(min_diff)