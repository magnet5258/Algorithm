T = int(input())
money_dic = {50000 : 0, 10000 : 1, 5000 : 2, 1000 : 3, 500 : 4, 100 : 5, 50 : 6, 10 : 7}
for test_case in range(1, T + 1):
    money = int(input())
    lst = [0] * 8
    for i in money_dic:
        x = money // i
        if x >= 1:
            lst[money_dic[i]] += x
            money -= i * x
    print(f'#{test_case}')
    print(' '.join(map(str, lst)))
        