def prev_permutation(a):
    i = len(a) - 1
    while i > 0 and a[i - 1] <= a[i]:
        i -= 1
    if i <= 0:
        return -1
    j = len(a) - 1
    while a[j] >= a[i - 1]:
        j -= 1
    a[i - 1], a[j] = a[j], a[i - 1]
    a[i:] = reversed(a[i:])
    return a

N = int(input())
perm = list(map(int, input().split()))
res = prev_permutation(perm)
if res == -1:
    print(-1)
else:
    print(*res)
