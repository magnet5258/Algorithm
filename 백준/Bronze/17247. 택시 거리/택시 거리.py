N, M = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(N)]
taxi = []

start_end = False
for i in range(N):
    for j in range(M):
        if grid[i][j] == 1:
            taxi.append((i, j))
            if len(taxi) == 2:
                start_end = True
                break
    if start_end:
        break

D = abs(taxi[1][0] - taxi[0][0]) + abs(taxi[1][1] - taxi[0][1])
print(D)