from collections import defaultdict

def delete_subtree(node):
    for child in tree[node]:
        delete_subtree(child)
    tree[node] = []
    parents[node] = -2

N = int(input())
parents = list(map(int, input().split()))
erase_node = int(input())

tree = defaultdict(list)
root = -1
for i in range(N):
    if parents[i] == -1:
        root = i
    else:
        tree[parents[i]].append(i)

if erase_node == root:
    print(0)
else:
    parent = parents[erase_node]

    delete_subtree(erase_node)

    leaf_count = 0
    for i in range(N):
        if parents[i] != -2 and i not in tree:
            leaf_count += 1
        elif parents[i] == -2 and len(tree[parent]) == 1:
            leaf_count += 1

    print(leaf_count)