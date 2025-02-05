def inorder_list(tree, index):
    if index < len(tree) and tree[index] is not None:
        inorder_list(tree, 2 * index)
        ans.append(tree[index])
        inorder_list(tree, 2 * index + 1)
    return ans
 
T = 10
for test_case in range(1, T + 1):
    N = int(input())
    bin_tree = [0] * (N + 1)
    ans = []
    for _ in range(N):
        lst = list(input().split())
        bin_tree[int(lst[0])] = lst[1]
 
    print(f"#{test_case} {''.join(inorder_list(bin_tree, 1))}")