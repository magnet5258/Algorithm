from collections import deque

T = int(input())
for i in range(T):
    N, M = map(int, input().split())
    lst = list(map(int, input().split()))
    queue = deque(enumerate(lst))
    count = 0

    while queue:
        cur_idx, cur_val = queue.popleft()
        if any(cur_val < x[1] for x in queue):
            queue.append((cur_idx, cur_val))
        else:
            count += 1
            if cur_idx == M:
                print(count)
                break