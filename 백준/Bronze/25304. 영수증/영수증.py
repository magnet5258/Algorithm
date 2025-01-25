price_sum = int(input())
N = int(input())
price_lst = []
for _ in range(N):
    cnt, price = map(int, input().split())
    price_lst.append(cnt * price)
if sum(price_lst) == price_sum:
    print('Yes')
else:
    print('No')