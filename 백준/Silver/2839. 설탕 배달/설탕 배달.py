N = int(input())

ans = 2000
x = N // 5
for i in range(x + 1):
    y = N - i * 5
    if y % 3 == 0:
        result = i + y // 3
        ans = min(ans, result)

if ans == 2000:
    ans = -1

print(ans)
