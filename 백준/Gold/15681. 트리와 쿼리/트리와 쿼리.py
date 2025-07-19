import sys
sys.setrecursionlimit(10**5 + 50)

from collections import defaultdict

N, R, Q = map(int, input().split())
graph = defaultdict(list)
for _ in range(N - 1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

subtree = [0] * (N + 1)

def tree(node, parent):
    subtree[node] = 1
    for neighbor in graph[node]:
        if neighbor != parent:
            tree(neighbor, node)
            subtree[node] += subtree[neighbor]

tree(R, -1)

for _ in range(Q):
    num = int(input())
    print(subtree[num])