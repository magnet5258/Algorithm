def build(node, start, end):
    if start == end:
        tree_min[node] = arr[start]
        tree_max[node] = arr[start]
    else:
        mid = (start + end) // 2
        build(node * 2, start, mid)
        build(node * 2 + 1, mid + 1, end)
        tree_min[node] = min(tree_min[node * 2], tree_min[node * 2 + 1])
        tree_max[node] = max(tree_max[node * 2], tree_max[node * 2 + 1])

def query_min(node, start, end, l, r):
    if r < start or end < l:
        return float('inf')

    if l <= start and end <= r:
        return tree_min[node]

    mid = (start + end) // 2
    left = query_min(node*2, start, mid, l, r)
    right = query_min(node*2+1, mid+1, end, l, r)
    return min(left, right)

def query_max(node, start, end, l, r):
    if r < start or end < l:
        return float('-inf')
    if l <= start and end <= r:
        return tree_max[node]
    mid = (start + end) // 2
    left = query_max(node*2, start, mid, l, r)
    right = query_max(node*2+1, mid+1, end, l, r)
    return max(left, right)

N, M = map(int, input().split())
arr = [0] + [int(input()) for _ in range(N)]

tree_min = [0] * (4 * N)
tree_max = [0] * (4 * N)

build(1, 1, N)

for _ in range(M):
    a, b = map(int, input().split())
    mn = query_min(1, 1, N, a, b)
    mx = query_max(1, 1, N, a, b)
    print(mn, mx)