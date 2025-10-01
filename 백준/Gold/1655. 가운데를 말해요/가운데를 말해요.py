import sys, heapq
input = sys.stdin.readline

N = int(input())
lq, rq = [], []
res = []

for _ in range(N):
    num = int(input())
    heapq.heappush(lq, -num)

    if rq and -lq[0] > rq[0]:
        heapq.heappush(rq, -heapq.heappop(lq))
        heapq.heappush(lq, -heapq.heappop(rq))

    if len(lq) > len(rq) + 1:
        heapq.heappush(rq, -heapq.heappop(lq))
    elif len(rq) > len(lq):
        heapq.heappush(lq, -heapq.heappop(rq))

    res.append(str(-lq[0]))

print("\n".join(res))