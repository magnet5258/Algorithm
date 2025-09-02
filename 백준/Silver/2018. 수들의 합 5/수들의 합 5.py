N = int(input())
nums = list(range(1, N + 1))
left, right = 0, 1
cnt = 0

while right < N + 1:
    if sum(nums[left:right]) == N:
        cnt += 1
        right += 1
    elif sum(nums[left:right]) < N:
        right += 1
    else:
        left += 1

print(cnt)