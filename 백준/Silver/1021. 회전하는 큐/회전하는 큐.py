from collections import deque

N, M = map(int, input().split())
target = list(map(int, input().split()))
queue = deque(list(range(1, N + 1)))
cnt = 0

for num in target:
    while queue[0] != num:
        if queue.index(num) <= len(queue) // 2:
            queue.rotate(-1)
            cnt += 1
        else:
            queue.rotate(1)
            cnt += 1
    queue.popleft()

print(cnt)