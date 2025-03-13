from itertools import combinations_with_replacement

N, M = map(int, input().split())
nums = set(sorted(list(map(int, input().split()))))
combs = combinations_with_replacement(nums, M)
for comb in combs:
    print(*comb)