from collections import Counter

N = int(input())
nums = sorted([int(input()) for _ in range(N)])
count = Counter(nums)
max_value = max(count.values())
max_keys = [k for k, v in count.items() if v == max_value]

if len(max_keys) == 1:
    mode = max_keys[0]
else:
    mode = sorted(max_keys)[1]

print(round(sum(nums) / N))
print(nums[N // 2])
print(mode)
print(max(nums) - min(nums))