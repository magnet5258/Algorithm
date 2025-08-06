n = int(input())
num_lst = []
dp = []
for _ in range(n):
    nums = list(map(int, input().split()))
    num_lst.append(nums)
    dp.append([0] * len(nums))

dp[0] = num_lst[0]
for i in range(1, n):
    for j in range(len(dp[i])):
        if j == 0:
            dp[i][j] = dp[i - 1][j] + num_lst[i][j]
        elif j == len(dp[i]) - 1:
            dp[i][j] = dp[i - 1][j - 1] + num_lst[i][j]
        else:
            dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - 1]) + num_lst[i][j]

print(max(dp[n - 1]))