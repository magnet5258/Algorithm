width, height = map(int, input().split())
N = int(input())
lst = []
for i in range(N):
    a, b = map(int, input().split())
    lst.append((a, b))
x = [0, width]
y = [0, height]
for a, b in lst:
    if a == 1:
        x.append(b)
    elif a == 0:
        y.append(b)
x.sort()
y.sort()
size = []
for i in range(1, len(x)):
    for j in range(1, len(y)):
        size.append((x[i] - x[i - 1]) * (y[j] - y[j - 1]))
print(max(size))