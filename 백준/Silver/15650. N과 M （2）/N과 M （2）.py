from itertools import combinations

N, M = map(int, input().split())
lst = list(range(1, N + 1))
combs = combinations(lst, M)
for comb in combs:
    print(*comb)