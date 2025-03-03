def cnt_tile(tiles, n):
    dp = [0] * (n + 1)
    dp[0] = 1

    for i in range(1, n + 1):
        for tile in tiles:
            if i - tile >= 0:
                if tile == 2:
                    dp[i] += 2 * dp[i - tile]
                else:
                    dp[i] += dp[i - tile]

    return dp[n]

n = int(input())
tiles = [1, 2]
print(cnt_tile(tiles, n) % 10007)