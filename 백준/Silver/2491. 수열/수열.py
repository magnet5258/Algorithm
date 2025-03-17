N = int(input())
nums = list(map(int, input().split()))

dp_1 = [1] * N
dp_2 = [1] * N

for i in range(1, len(nums)):
    if nums[i] >= nums[i - 1]:
        dp_1[i] += dp_1[i - 1]

    if nums[i] <= nums[i - 1]:
        dp_2[i] += dp_2[i - 1]

print(max(max(dp_1), max(dp_2)))