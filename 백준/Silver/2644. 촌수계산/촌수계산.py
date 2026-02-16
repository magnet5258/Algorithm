from collections import deque, defaultdict

n = int(input())
a, b = map(int, input().split())
m = int(input())

relatives = defaultdict(list)
for _ in range(m):
    x, y = map(int, input().split())
    relatives[x].append(y)
    relatives[y].append(x)

visited = [False] * (n + 1)
queue = deque()
queue.append((a, 0))
cnt = 1
answer = -1
while queue:
    person, dist = queue.popleft()
    if person == b:
        answer = dist
        break
    for next_person in relatives[person]:
        if not visited[next_person]:
            visited[next_person] = True
            queue.append((next_person, dist + 1))

print(answer)