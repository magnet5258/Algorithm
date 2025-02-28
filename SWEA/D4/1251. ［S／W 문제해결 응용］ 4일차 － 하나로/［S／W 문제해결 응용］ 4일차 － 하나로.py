import heapq
 
def prim(N, x_lst, y_lst, E):
    pq = []
    visited = [False] * N
    min_cost = 0
 
    heapq.heappush(pq, (0, 0))
    count = 0
 
    while pq and count < N:
        cost, u = heapq.heappop(pq)
 
        if visited[u]: 
            continue

        visited[u] = True
        min_cost += cost
        count += 1
 
        for v in range(N):
            if not visited[v]:
                dist = (x_lst[v] - x_lst[u]) ** 2 + (y_lst[v] - y_lst[u]) ** 2
                heapq.heappush(pq, (E * dist, v))
 
    return round(min_cost)
 
T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    x_lst = list(map(int, input().split()))
    y_lst = list(map(int, input().split()))
    E = float(input())
 
    result = prim(N, x_lst, y_lst, E)
    print(f'#{test_case} {result}')