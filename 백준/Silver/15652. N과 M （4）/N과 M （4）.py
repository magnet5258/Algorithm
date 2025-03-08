from itertools import combinations_with_replacement

N, M = map(int, input().split())
nums = list(range(1, N + 1))
combs = list(combinations_with_replacement(nums, M))
for comb in combs:
    print(*comb)