N, M = map(int, input().split())
lst = list(map(int, input().split()))
max_sum = 0
for i in range(N - 2):
    for j in range(i + 1, N - 1):
        for k in range(j + 1, N):
            cur_sum = lst[i] + lst[j] + lst[k]
            if cur_sum <= M:
                max_sum = max(max_sum, cur_sum)
print(max_sum)