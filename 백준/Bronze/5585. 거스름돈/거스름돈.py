money_lst = [500, 100, 50, 10, 5, 1]

money = int(input())
money_diff = 1000 - money

cnt = 0
for m in money_lst:
    cnt += money_diff // m
    money_diff %= m

print(cnt)