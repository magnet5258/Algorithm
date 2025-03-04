import sys
import heapq

heap = []
N = int(sys.stdin.readline())
for _ in range(N):
    x = int(sys.stdin.readline())
    if x > 0:
        heapq.heappush(heap, -1 * x)
    elif x == 0:
        print(-1 * heapq.heappop(heap) if heap else 0)