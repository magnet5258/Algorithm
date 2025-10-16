lst = [False] * 10001
for i in range(1, 10001):
    num = i + sum(map(int, str(i)))
    if num <= 10000:
        lst[num] = True

for i in range(1, 10001):
    if not lst[i]:
        print(i)