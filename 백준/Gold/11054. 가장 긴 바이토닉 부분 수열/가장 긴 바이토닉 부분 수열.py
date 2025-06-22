N = int(input())
A = list(map(int, input().split()))

dp_up = [1] * N
for i in range(N):
    for j in range(i):
        if A[j] < A[i]:
            dp_up[i] = max(dp_up[j] + 1, dp_up[i])

dp_down = [1] * N
for i in range(N - 1, -1, -1):
    for j in range(N - 1, i, -1):
        if A[j] < A[i]:
            dp_down[i] = max(dp_down[j] + 1, dp_down[i])

max_len = 0
for i in range(N):
    max_len = max(dp_up[i] + dp_down[i] - 1, max_len)

print(max_len)