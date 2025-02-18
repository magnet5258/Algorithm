import sys
from collections import deque

N = int(sys.stdin.readline().strip())
queue = deque()
commands = sys.stdin.readlines()

for command in commands:
    order_lst = command.split()
    if order_lst[0] == 'push':
        queue.append(order_lst[1])
    elif order_lst[0] == 'front':
        print(queue[0] if queue else -1)
    elif order_lst[0] == 'back':
        print(queue[-1] if queue else -1)
    elif order_lst[0] == 'pop':
        print(queue.popleft() if queue else -1)
    elif order_lst[0] == 'size':
        print(len(queue))
    elif order_lst[0] == 'empty':
        print(0 if queue else 1)