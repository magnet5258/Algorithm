N, K = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
ans = 0
x = []
y = []
for lst in arr:
    if lst[0] == 1:
        x.append(lst[1])
        if x.count(lst[1]) == 1:
            ans += 1
        elif x.count(lst[1]) > K:
            x = [i for i in lst if i != lst[1]]
            x.append(lst[1])
            ans += 1
    else:
        y.append(lst[1])
        if y.count(lst[1]) == 1:
            ans += 1
        elif y.count(lst[1]) > K:
            y = [i for i in lst if i != lst[1]]
            y.append(lst[1])
            ans += 1
print(ans)
            