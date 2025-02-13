from collections import deque

T = 10
for test_case in range(1, T + 1):
    V, E = map(int, input().split())
    lst = list(map(int, input().split()))
    edges = list(zip(lst[::2], lst[1::2]))
    nodes = set(range(1, V + 1))
    graph = {node: [] for node in nodes}
    in_degree = {node: 0 for node in nodes}

    for i, j in edges:
        graph[i].append(j)
        in_degree[j] += 1

    queue = deque([node for node in nodes if in_degree[node] == 0])
    ans = []

    while queue:
        node = queue.popleft()
        ans.append(node)

        for n in graph[node]:
            in_degree[n] -= 1
            if in_degree[n] == 0:
                queue.append(n)

    print(f'#{test_case}', *ans)