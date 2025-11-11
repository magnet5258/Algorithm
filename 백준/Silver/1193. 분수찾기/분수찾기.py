X = int(input())
lst = []

i = 1
while True:
    num = i * (i + 1) // 2
    lst.append(num)
    if num >= X:
        break
    i += 1

k = len(lst)
total = lst[-1]
check = X - (total - k)

if k % 2 == 0:
    left = check
    right = k + 1 - check
else:
    left = k + 1 - check
    right = check

print(''.join([str(left), '/', str(right)]))