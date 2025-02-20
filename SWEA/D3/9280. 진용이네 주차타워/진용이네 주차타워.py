import heapq
from collections import deque

T = int(input())
for test_case in range(1, T + 1):
    n, m = map(int, input().split())
    price_lst = list(int(input()) for _ in range(n))
    priority_lst = list(range(n))
    heapq.heapify(priority_lst)
    car_lst = list(int(input()) for _ in range(m))
    ans = 0
    park_status = [-1] * n
    waiting_car = deque()
    for _ in range(2 * m):
        park = int(input())
        if park > 0:
            car = park - 1
            if priority_lst:
                parking = heapq.heappop(priority_lst)
                park_status[parking] = car
                ans += car_lst[car] * price_lst[parking]
            else:
                waiting_car.append(car)
        else:
            car = abs(park) - 1
            for i in range(n):
                if park_status[i] == car:
                    park_status[i] = -1
                    if waiting_car:
                        new_car = waiting_car.popleft()
                        park_status[i] = new_car
                        ans += car_lst[new_car] * price_lst[i]
                    else:
                        heapq.heappush(priority_lst, i)
                    break

    print(f'#{test_case} {ans}')