from itertools import permutations

N, M = map(int, input().split())
lst = sorted(list(map(int, input().split())))
combs = permutations(lst, M)
for comb in combs:
    print(*comb)