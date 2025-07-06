from itertools import combinations
from copy import deepcopy

N, M, D = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

archer_positions = list(combinations(range(M), 3))
max_kill = 0

for archer_cols in archer_positions:
    temp_map = deepcopy(arr)
    total_kill = 0

    for _ in range(N):
        targets = set()
        for col in archer_cols:
            target = None
            min_dist = D + 1

            for r in range(N):
                for c in range(M):
                    if temp_map[r][c] == 1:
                        dist = abs(N - r) + abs(col - c)
                        if dist <= D:
                            if dist < min_dist or (dist == min_dist and (target is None or c < target[1])):
                                target = (r, c)
                                min_dist = dist

            if target:
                targets.add(target)

        for r,c in targets:
            if temp_map[r][c] == 1:
                temp_map[r][c] = 0
                total_kill += 1

        temp_map.pop()
        temp_map.insert(0, [0] * M)

    max_kill = max(max_kill, total_kill)

print(max_kill)