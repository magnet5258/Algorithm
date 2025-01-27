T = int(input())
for _ in range(T):
    a, b = input().split()
    ans = ''
    for i in b:
        ans += i * int(a)
    print(ans)