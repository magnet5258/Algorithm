def insert(heap, value):
    heap.append(value)
    idx = len(heap) - 1
    while idx > 1 and heap[idx] < heap[idx // 2]:
        heap[idx], heap[idx // 2] = heap[idx // 2], heap[idx]
        idx //= 2


T = int(input())
for t in range(T):
    N = int(input())
    nums = list(map(int, input().split()))
    heap = [0]

    for num in nums:
        insert(heap, num)
    t_idx = len(heap) - 1
    answer = 0

    while t_idx > 1:
        t_idx //= 2
        answer += heap[t_idx]

    print(f'#{t + 1} {answer}')