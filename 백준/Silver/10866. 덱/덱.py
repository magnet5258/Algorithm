from collections import deque

N = int(input())
queue = deque()
for _ in range(N):
    order = input().split()
    if order[0] == 'push_front':
        queue.appendleft(int(order[1]))
    elif order[0] == 'push_back':
        queue.append(int(order[1]))
    elif order[0] == 'pop_front':
        print(queue.popleft() if queue else -1)
    elif order[0] == 'pop_back':
        print(queue.pop() if queue else -1)
    elif order[0] == 'size':
        print(len(queue))
    elif order[0] == 'empty':
        print(0 if queue else 1)
    elif order[0] == 'front':
        print(queue[0] if queue else -1)
    elif order[0] == 'back':
        print(queue[-1] if queue else -1)