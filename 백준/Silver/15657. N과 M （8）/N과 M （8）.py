from itertools import combinations_with_replacement

N, M = map(int, input().split())
lst = sorted(list(map(int, input().split())))
combs = combinations_with_replacement(lst, M)
for comb in combs:
    print(*comb)