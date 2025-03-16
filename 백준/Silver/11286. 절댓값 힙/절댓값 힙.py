import heapq

N = int(input())
queue = []
for i in range(N):
    num = int(input())
    if num == 0:
        if queue:
            print(heapq.heappop(queue)[1])
        else:
            print(0)
    else:
        heapq.heappush(queue, (abs(num), num))