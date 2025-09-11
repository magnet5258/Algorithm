lst_1 = list(input())
lst_2 = list(input())
n, m = len(lst_1), len(lst_2)

dp = [[0] * (m + 1) for _ in range(n + 1)]

for i in range(1, n + 1):
    for j in range(1, m + 1):
        if lst_1[i - 1] == lst_2[j - 1]:
            dp[i][j] = dp[i - 1][j - 1] + 1
        else:
            dp[i][j] = max(dp[i][j - 1], dp[i - 1][j])

print(dp[n][m])

i, j = n, m
lcs = ''
while i > 0 and j > 0:
    if lst_1[i - 1] == lst_2[j - 1]:
        lcs += lst_1[i - 1]
        i -= 1
        j -= 1
    else:
        if dp[i][j - 1] >= dp[i - 1][j]:
            j -= 1
        else:
            i -= 1

print(lcs[::-1])