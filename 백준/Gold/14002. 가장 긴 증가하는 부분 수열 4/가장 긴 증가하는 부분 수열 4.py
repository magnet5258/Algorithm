N = int(input())
nums = list(map(int, input().split()))
dp = [1] * len(nums)

for i in range(N):
    for j in range(i):
        if nums[j] < nums[i]:
            dp[i] = max(dp[j] + 1, dp[i])

asc_lst = []
max_len = max(dp)
curr_len = max_len
for i in range(N - 1, -1, -1):
    if dp[i] == curr_len:
        asc_lst.append(nums[i])
        curr_len -= 1

asc_lst.reverse()
print(len(asc_lst))
print(*asc_lst)