from collections import defaultdict, deque

N, M = map(int, input().split())
graph = defaultdict(list)
indegree = [0] * (N + 1)

for _ in range(M):
    singer_lst = list(map(int, input().split()))[1:]
    for i in range(len(singer_lst) - 1):
        a = singer_lst[i]
        b = singer_lst[i + 1]
        graph[a].append(b)
        indegree[b] += 1

queue = deque()
for i in range(1, N + 1):
    if indegree[i] == 0:
        queue.append(i)

result = []
while queue:
    cur_singer = queue.popleft()
    result.append(cur_singer)
    for next_singer in graph[cur_singer]:
        indegree[next_singer] -= 1
        if indegree[next_singer] == 0:
            queue.append(next_singer)

if len(result) == N:
    for x in result:
        print(x)
else:
    print(0)