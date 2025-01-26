N, X = map(int, input().split())
lst = list(map(int, input().split()))
num = []
for i in lst:
    if i < X:
        num.append(i)
print(' '.join(map(str, num)))