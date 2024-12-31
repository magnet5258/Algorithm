T = 10
for t in range(1, T + 1):
    a = int(input())
    lst = list(map(int, input().split()))
    ans = 100
    for i in range(a):
        lst.sort()
        lst[0] += 1
        lst[-1] -= 1
        if ans > max(lst) - min(lst):
            ans = max(lst) - min(lst)
    print(f'#{t} {ans}')

    
