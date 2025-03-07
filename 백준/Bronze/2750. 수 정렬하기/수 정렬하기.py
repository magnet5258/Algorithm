N = int(input())
nums = [int(input()) for _ in range(N)]
for i in range(1, len(nums)):
    for j in range(i, 0, -1):
        if nums[j - 1] > nums[j]:
            nums[j - 1], nums[j] = nums[j], nums[j - 1]
        else:
            break

for num in nums:
    print(num)