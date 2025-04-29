from itertools import combinations

N = int(input())
S = [list(map(int, input().split())) for _ in range(N)]
p = list(range(N))
min_diff = float('inf')

for size in range(1, N // 2 + 1):
    for team1 in combinations(p, size):
        team2 = [i for i in p if i not in team1]
        sum_t1 = sum(S[a][b] + S[b][a] for a, b in combinations(team1, 2))
        sum_t2 = sum(S[c][d] + S[d][c] for c, d in combinations(team2, 2))
        min_diff = min(min_diff, abs(sum_t1 - sum_t2))

print(min_diff)