from itertools import product

N, M = map(int, input().split())
lst = list(range(1, N + 1))
combs = product(lst, repeat=M)
for comb in combs:
    print(*comb)