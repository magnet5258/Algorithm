T = int(input())
money = [int(input()) for _ in range(T)]
for i in money:
    coin = [0] * 4
    while i > 0:
        if i // 25 >= 1:
            coin[0] += i // 25
            i %= 25
        elif i // 10 >= 1:
            coin[1] += i // 10
            i %= 10
        elif i // 5 >= 1:
            coin[2] += i // 5
            i %= 5
        elif i // 1 >= 1:
            coin[3] += i // 1
            i %= 1
    print(*coin)