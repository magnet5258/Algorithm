import sys

N = int(sys.stdin.readline().strip())
stack = []
commands = sys.stdin.readlines()

for command in commands:
    order_lst = command.split()
    if order_lst[0] == 'push':
        stack.append(int(order_lst[1]))
    elif order_lst[0] == 'pop':
        print(stack.pop() if stack else -1)
    elif order_lst[0] == 'size':
        print(len(stack))
    elif order_lst[0] == 'empty':
        print(1 if not stack else 0)
    elif order_lst[0] == 'top':
        print(stack[-1] if stack else -1)