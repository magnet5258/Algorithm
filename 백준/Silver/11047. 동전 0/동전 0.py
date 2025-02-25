N, K = map(int, input().split())
money_lst = [int(input()) for _ in range(N)]
money_lst.sort(reverse=True)
ans = 0
for money in money_lst:
    if K // money > 0:
        ans += K // money
        K %= money
        if K == 0:
            break
print(ans)