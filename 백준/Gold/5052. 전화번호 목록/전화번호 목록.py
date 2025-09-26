t = int(input())
for _ in range(t):
    n = int(input())
    nums = [input().strip() for _ in range(n)]
    nums.sort()
    consistent = True
    
    for i in range(n - 1):
        if len(nums[i]) <= len(nums[i + 1]):
            if nums[i] == nums[i + 1][:len(nums[i])]:
                consistent = False
                break

    if consistent:
        print('YES')
    else:
        print('NO')