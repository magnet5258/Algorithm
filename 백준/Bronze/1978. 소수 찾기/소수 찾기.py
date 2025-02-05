N = int(input())
lst = list(map(int, input().split()))
ans = 0
for num in lst:
    if num < 2:
        continue
    prime = True
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            prime = False
            break
    if prime:
        ans += 1
print(ans)
            