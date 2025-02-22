from collections import defaultdict

def order(v):
    visited[v] = True
    for neighbor in graph[v]:
        if not visited[neighbor]:
            order(neighbor)
    result.append(v)

T = 10
for test_case in range(1, T + 1):
    v_cnt, e_cnt = map(int, input().split())
    edges = list(map(int, input().split()))
    graph = defaultdict(list)
    for i in range(e_cnt):
        graph[edges[2 * i]].append(edges[2 * i + 1])
    visited = [False] * (v_cnt + 1)
    result = []
    for v in range(1, v_cnt + 1):
        if not visited[v]:
            order(v)
    ans = result[::-1]
    print(f"#{test_case} {' '.join(map(str, ans))}")