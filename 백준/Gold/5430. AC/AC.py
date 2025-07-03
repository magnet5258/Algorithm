from collections import deque

T = int(input())
for _ in range(T):
    p = input()
    n = int(input())
    arr = input()

    if n == 0:
        x_lst = deque()
    else:
        x_lst = deque(map(int, arr[1:-1].split(',')))

    reverse = False

    for cmd in p:
        if cmd == 'R':
            reverse = not reverse
        elif cmd == 'D':
            if not x_lst:
                print('error')
                break
            if reverse:
                x_lst.pop()
            else:
                x_lst.popleft()
    else:
        if reverse:
            x_lst.reverse()
        print('[' + ','.join(map(str, x_lst)) + ']')