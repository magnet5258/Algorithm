import heapq

N = int(input())
time = []
for _ in range(N):
    start, end = map(int, input().split())
    time.append((start, end))

time.sort()

pq = []
for s, e in time:
    if pq and pq[0] <= s:
        heapq.heappop(pq)
    heapq.heappush(pq, e)

print(len(pq))