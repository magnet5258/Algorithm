from itertools import permutations

N, M = map(int, input().split())
nums = sorted(list(map(int, input().split())))
combs = set(permutations(nums, M))
for comb in combs:
    print(*comb)