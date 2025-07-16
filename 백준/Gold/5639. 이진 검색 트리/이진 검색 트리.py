import sys
sys.setrecursionlimit(15000)

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def insert(root, value):
    if root is None:
        return Node(value)
    if value < root.value:
        root.left = insert(root.left, value)
    else:
        root.right = insert(root.right, value)
    return root

def postorder(node):
    if node is None:
        return
    postorder(node.left)
    postorder(node.right)
    print(node.value)

preorder = []
while True:
    try:
        preorder.append(int(sys.stdin.readline()))
    except:
        break

root = None
for num in preorder:
    root = insert(root, num)

postorder(root)
