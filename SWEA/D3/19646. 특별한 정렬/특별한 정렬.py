from collections import deque

T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    sorted_lst = sorted(list(map(int, input().split())))
    queue = deque(sorted_lst)
    new_lst = []
    while queue:
        new_lst.append(queue.pop())
        new_lst.append(queue.popleft())
    print(f"#{test_case} {' '.join(map(str, new_lst[:10]))}")
