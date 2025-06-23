from collections import defaultdict, deque

N, M = map(int, input().split())
graph = defaultdict(list)
indegree = [0] * (N + 1)

for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    indegree[b] += 1

queue = deque([i for i in range(1, N + 1) if indegree[i] == 0])
answer = []

while queue:
    num = queue.popleft()
    answer.append(num)
    for next_num in graph[num]:
        indegree[next_num] -= 1
        if indegree[next_num] == 0:
            queue.append(next_num)

print(*answer)