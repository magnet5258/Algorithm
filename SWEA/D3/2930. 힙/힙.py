import heapq
 
T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    num_lst = []
    max_num_lst = []
    for lst in arr:
        if lst[0] == 1:
            heapq.heappush(num_lst, -lst[1])
        else:
            if not num_lst:
                max_num_lst.append(-1)
            else:
                max_num_lst.append(-heapq.heappop(num_lst))
 
    print(f"#{test_case} {' '.join(map(str, max_num_lst))}")