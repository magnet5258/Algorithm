import heapq

N = int(input())
grid = [list(map(int, input().split())) for _ in range(N)]
lst = grid[-1]
new_lst = []
pq = []
for idx, num in enumerate(lst):
    heapq.heappush(pq, num)
    new_lst.append((num, idx))

new_lst.sort(key=lambda x: x[0], reverse=True)
idx_lst = []
for num, idx in new_lst:
    idx_lst.append(idx)

if N == 1:
    print(grid[0][0])
else:
    answer = float('-inf')
    for i in range(N - 2, -1, -1):
        n = heapq.heappop(pq)
        check = True
        for j in idx_lst:
            if grid[i][j] > n:
                check = False
                heapq.heappush(pq, grid[i][j])

        if check:
            answer = n
            break
        else:
            while len(pq) > N:
                heapq.heappop(pq)

    if answer != float('-inf'):
        print(answer)
    else:
        print(heapq.heappop(pq))