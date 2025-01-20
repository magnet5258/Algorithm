n = int(input())
ans = 0
for x in range(1, n + 1):
    for y in range(1, int(x ** 0.5) + 1):
        if x % y == 0:
            z = x // y
            if y <= z:
                ans += 1
print(ans)