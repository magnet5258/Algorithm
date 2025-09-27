from collections import deque

def solution(priorities, location):
    answer = 0
    queue = deque()
    for i, num in enumerate(priorities):
        queue.append((i, num))
    cnt = 0
    while queue:
        max_rank = max(queue, key=lambda x: x[1])
        i, num = queue.popleft()
        if num == max_rank[1]:
            cnt += 1
            if i  == location:
                answer = cnt
                break
            else:
                continue
        else:
            queue.append((i, num))
    return answer