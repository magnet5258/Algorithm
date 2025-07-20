N = int(input())
RGB_lst = []
for _ in range(N):
    RGB = list(map(int, input().split()))
    RGB_lst.append(RGB)

dp = [[0] * 3 for _ in range(N)]

dp[0] = RGB_lst[0]
for i in range(1, N):
    dp[i][0] = min(dp[i - 1][1], dp[i - 1][2]) + RGB_lst[i][0]
    dp[i][1] = min(dp[i - 1][0], dp[i - 1][2]) + RGB_lst[i][1]
    dp[i][2] = min(dp[i - 1][0], dp[i - 1][1]) + RGB_lst[i][2]

print(min(dp[N - 1]))