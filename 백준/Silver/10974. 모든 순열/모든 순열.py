from itertools import permutations

N = int(input())
lst = list(range(1, N + 1))
combs = permutations(lst)

for comb in combs:
    print(*comb)