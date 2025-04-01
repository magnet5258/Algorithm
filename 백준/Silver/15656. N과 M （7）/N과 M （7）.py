from itertools import product

N, M = map(int, input().split())
lst = sorted(list(map(int, input().split())))
combs = product(lst, repeat=M)
for comb in combs:
    print(*comb)