import heapq
from collections import defaultdict

def longest_increasing_path():
    distances = {num: 1 for num in nums}
    queue = [(1, num) for num in nums]
    heapq.heapify(queue)

    while queue:
        dist, node = heapq.heappop(queue)
        for neighbor in graph[node]:
            new_dist = dist + 1
            if new_dist > distances[neighbor]:
                distances[neighbor] = new_dist
                heapq.heappush(queue, (new_dist, neighbor))

    return max(distances.values())


T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    nums = list(map(int, input().split()))
    graph = defaultdict(list)

    for i in range(N):
        for j in range(i + 1, N):
            if nums[i] < nums[j]:
                graph[nums[i]].append(nums[j])

    print(f'#{test_case} {longest_increasing_path()}')