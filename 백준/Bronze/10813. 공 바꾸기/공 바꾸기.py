N, M = map(int, input().split())
lst = [i for i in range(1, N + 1)]
for _ in range(M):
    i, j = map(int, input().split())
    lst[i - 1], lst[j - 1] = lst[j - 1], lst[i - 1]
print(' '.join(map(str, lst)))