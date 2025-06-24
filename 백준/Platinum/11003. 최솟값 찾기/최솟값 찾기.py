from collections import deque

N, L = map(int, input().split())
A = list(map(int, input().split()))

queue = deque()
result = []

for i in range(N):
    while queue and A[queue[-1]] > A[i]:
        queue.pop()
    queue.append(i)
    if queue[0] <= i - L:
        queue.popleft()
    result.append(A[queue[0]])

print(*result)