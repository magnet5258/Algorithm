import sys
from collections import deque

input = sys.stdin.readline
N = int(input())
queue = deque()
for _ in range(N):
    order = input().split()
    if order[0] == 'push':
        queue.append(int(order[1]))
    elif order[0] == 'pop':
        print(queue.popleft() if queue else -1)
    elif order[0] == 'size':
        print(len(queue))
    elif order[0] == 'empty':
        print(0 if queue else 1)
    elif order[0] == 'front':
        print(queue[0] if queue else -1)
    elif order[0] == 'back':
        print(queue[-1] if queue else -1)