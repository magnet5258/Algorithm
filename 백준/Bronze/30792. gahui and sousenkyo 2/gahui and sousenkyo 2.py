import heapq

n = int(input())
m = int(input())
lst = list(map(int, input().split()))
characters = [-x for x in lst]
heapq.heapify(characters)

rank = 1
for _ in range(len(characters)):
    num = heapq.heappop(characters)
    if m > -num:
        break
    else:
        rank += 1

print(rank)