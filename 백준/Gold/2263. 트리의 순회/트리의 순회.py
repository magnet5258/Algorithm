import sys

sys.setrecursionlimit(10**5 + 100)

n = int(input())
inorder = list(map(int, input().split()))
postorder = list(map(int, input().split()))

pos = {inorder[i]: i for i in range(n)}


def preorder(in_start, in_end, post_start, post_end):
    if in_start > in_end or post_start > post_end:
        return

    root = postorder[post_end]
    print(root, end=' ')

    root_idx = pos[root]
    left_size = root_idx - in_start

    preorder(in_start, root_idx - 1, post_start, post_start + left_size - 1)
    preorder(root_idx + 1, in_end, post_start + left_size, post_end - 1)


preorder(0, n - 1, 0, n - 1)