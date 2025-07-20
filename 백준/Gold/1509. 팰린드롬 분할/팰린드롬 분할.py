word = input()

is_pal = [[False] * len(word) for _ in range(len(word))]
for length in range(1, len(word) + 1):
    for start in range(len(word) - length + 1):
        end = start + length - 1
        if word[start] == word[end]:
            if length <= 2:
                is_pal[start][end] = True
            elif is_pal[start + 1][end - 1]:
                is_pal[start][end] = True

dp = [float('inf')] * len(word)

for i in range(len(word)):
    if is_pal[0][i]:
        dp[i] = 1
    else:
        for j in range(i):
            if is_pal[j + 1][i]:
                dp[i] = min(dp[i], dp[j] + 1)

print(dp[len(word) - 1])