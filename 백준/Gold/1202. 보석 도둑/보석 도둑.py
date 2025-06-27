import heapq

N, K = map(int, input().split())
jewelries = [tuple(map(int, input().split())) for _ in range(N)]
bags = [int(input()) for _ in range(K)]

jewelries.sort()
bags.sort()

answer = 0
jewel_idx = 0
price_heap = []

for bag in bags:
    while jewel_idx < N and jewelries[jewel_idx][0] <= bag:
        weight, price = jewelries[jewel_idx]
        heapq.heappush(price_heap, -price)
        jewel_idx += 1

    if price_heap:
        answer += -heapq.heappop(price_heap)

print(answer)