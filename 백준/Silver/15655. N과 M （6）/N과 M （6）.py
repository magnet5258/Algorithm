from itertools import combinations

N, M = map(int, input().split())
lst = sorted(list(map(int, input().split())))
combs = combinations(lst, M)
for comb in combs:
    print(*comb)