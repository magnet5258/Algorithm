from collections import deque

N, K = map(int, input().split())

if N == K:
    print(0)
    exit()

time_dict = {}
queue = deque([N])
time_dict[N] = 0

while queue:
    num = queue.popleft()
    nxt_lst = [num - 1, num + 1, 2 * num]
    for nxt in nxt_lst:
        if nxt == K:
            print(time_dict[num] + 1)
            exit()
        if 0 <= nxt <= 100000 and nxt not in time_dict:
            time_dict[nxt] = time_dict[num] + 1
            queue.append(nxt)