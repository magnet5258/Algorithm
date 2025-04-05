T = int(input())
nums = [int(input()) for _ in range(T)]
max_n = max(nums)

divisor_sum = [0] * (max_n + 1)
for i in range(1, max_n + 1):
    for j in range(i, max_n + 1, i):
        divisor_sum[j] += i

dp = [0] * (max_n + 1)
for i in range(1, max_n + 1):
    dp[i] = dp[i - 1] + divisor_sum[i]

for n in nums:
    print(dp[n])