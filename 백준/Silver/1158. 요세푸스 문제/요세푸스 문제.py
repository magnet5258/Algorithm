from collections import deque

def josephus(n, k):
    queue = deque(range(1, n + 1))
    result = []
    while queue:
        queue.rotate(-(k - 1))
        result.append(queue.popleft())

    return result


N, K = map(int, input().split())
ans = josephus(N, K)
print(f"<{(', ').join(map(str, ans))}>")