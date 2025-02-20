from collections import deque, defaultdict

def height_cnt(start, graph):
    queue = deque([start])
    visited = set([start])
    count = 0

    while queue:
        node = queue.popleft()
        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)
                count += 1

    return count

T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    M = int(input())

    greater = defaultdict(list)
    smaller = defaultdict(list)

    for _ in range(M):
        a, b = map(int, input().split())
        greater[a].append(b)
        smaller[b].append(a)

    ans = 0
    for i in range(1, N + 1):
        smaller_count = height_cnt(i, smaller)
        greater_count = height_cnt(i, greater)

        if smaller_count + greater_count == N - 1:
            ans += 1

    print(f'#{test_case} {ans}')