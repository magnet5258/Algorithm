def find(node, depth):
    visited[node] = True
    depths[node] = depth

    for child in tree[node]:
        if not visited[child]:
            parent[child] = node
            find(child, depth + 1)

    subtree_size[node] = 1
    for child in tree[node]:
        subtree_size[node] += subtree_size[child]

def ancestor(a, b):
    while depths[a] != depths[b]:
        if depths[a] > depths[b]:
            a = parent[a]
        else:
            b = parent[b]
    while a != b:
        a = parent[a]
        b = parent[b]
    return a

T = int(input())
for test_case in range(1, T +1):
    N, K, *nodes = map(int, input().split())
    edges = list(map(int, input().split()))
    tree = [[] for _ in range(N + 1)]
    for i in range(K):
        tree[edges[2 * i]].append(edges[2 * i + 1])
    parent = [0] * (N + 1)
    depths = [0] * (N + 1)
    visited = [False] * (N + 1)
    subtree_size = [0] * (N + 1)

    find(1, 0)
    result = ancestor(nodes[0], nodes[1])
    print(f'#{test_case} {result} {subtree_size[result]}')
    