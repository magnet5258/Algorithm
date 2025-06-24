from itertools import permutations

N = int(input())
nums = list(map(int, input().split()))
combs = list(permutations(nums))
max_sum = 0

for comb in combs:
    num_sum = 0
    for i in range(1, N):
        num_sum += abs(comb[i - 1] - comb[i])
    max_sum = max(max_sum, num_sum)

print(max_sum)