def count_coin(coins):
    dp = [0] * (num + 1)
    dp[0] = 1

    for i in range(1, num + 1):
        for coin in coins:
            if i - coin >= 0:
                dp[i] += dp[i - coin]

    return dp[num]

T = int(input())
for i in range(T):
    num = int(input())
    coins = [1, 2, 3]
    print(count_coin(coins))