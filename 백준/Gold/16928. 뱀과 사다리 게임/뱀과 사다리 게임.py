from collections import deque, defaultdict

N, M = map(int, input().split())
move = defaultdict(list)
for _ in range(N):
    a, b = map(int, input().split())
    move[a] = b
for _ in range(M):
    a, b = map(int, input().split())
    move[a] = b

visited = [False] * 101
queue = deque([(1, 0)])
visited[1] = True

while queue:
    pos, cnt = queue.popleft()
    if pos == 100:
        print(cnt)
        break
    for dice in range(1, 7):
        next_pos = pos + dice
        if next_pos > 100:
            continue
        if next_pos in move:
            next_pos = move[next_pos]
        if not visited[next_pos]:
            visited[next_pos] = True
            queue.append((next_pos, cnt + 1))