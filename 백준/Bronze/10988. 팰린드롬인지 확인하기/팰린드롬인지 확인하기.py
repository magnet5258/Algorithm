pal = input()
x = len(pal) // 2
y = len(pal) - 1
ans = 1
for i in range(x):
    if pal[i] != pal[y - i]:
        ans = 0
        break
print(ans)
        