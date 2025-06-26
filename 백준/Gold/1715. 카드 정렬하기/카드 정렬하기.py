import heapq

N = int(input())
cards = [int(input()) for _ in range(N)]
heapq.heapify(cards)
cnt_sum = 0

while len(cards) > 1:
    cnt1 = heapq.heappop(cards)
    cnt2 = heapq.heappop(cards)
    cnt_sum += cnt1 + cnt2
    heapq.heappush(cards, cnt1 + cnt2)

print(cnt_sum)