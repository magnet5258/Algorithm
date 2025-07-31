from collections import defaultdict, deque

N = int(input())
pair = int(input())
computers = defaultdict(list)
for _ in range(pair):
    a, b = map(int, input().split())
    computers[a].append(b)
    computers[b].append(a)

visited = [False] * (N + 1)

queue = deque()
queue.append(1)
visited[1] = True
cnt = 0
while queue:
    x = queue.popleft()
    for n in computers[x]:
        if not visited[n]:
            cnt += 1
            visited[n] = True
            queue.append(n)

print(cnt)