from collections import defaultdict, deque

N, M = map(int, input().split())
graph = defaultdict(list)
for _ in range(M):
    A, B = map(int, input().split())
    graph[A].append(B)
    graph[B].append(A)

min_total = float('inf')
answer = 0

for i in range(1, N + 1):
    visited = [-1] * (N + 1)
    queue = deque()
    queue.append(i)
    visited[i] = 0

    while queue:
        num = queue.popleft()
        for neighbor in graph[num]:
            if visited[neighbor] == -1:
                visited[neighbor] = visited[num] + 1
                queue.append(neighbor)

    total_sum = sum(visited[1:])
    if min_total > total_sum:
        min_total = total_sum
        answer = i

print(answer)