from itertools import combinations

N, M = map(int, input().split())
city = [list(map(int, input().split())) for _ in range(N)]
chicken = []
dist_lst = []

for i in range(N):
    for j in range(N):
        if city[i][j] == 2:
            chicken.append((i, j))

selected_chicken = list(combinations(chicken, M))
for selected in selected_chicken:
    dist_sum = 0
    for i in range(N):
        for j in range(N):
            if city[i][j] == 1:
                dist = []
                for x, y in selected:
                    dist.append(abs(i - x) + abs(j - y))
                dist_sum += min(dist)
    dist_lst.append(dist_sum)

print(min(dist_lst))