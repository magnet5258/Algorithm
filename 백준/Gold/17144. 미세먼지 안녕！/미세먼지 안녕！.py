from collections import deque

R, C, T = map(int, input().split())
air = [list(map(int, input().split())) for _ in range(R)]

fresh = []
for i in range(R):
    for j in range(C):
        if air[i][j] == -1:
            fresh.append((i, j))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def air_clean():
    top, bottom = fresh

    for i in range(top[0]-1, 0, -1):
        air[i][0] = air[i-1][0]
    for i in range(C-1):
        air[0][i] = air[0][i+1]
    for i in range(0, top[0]):
        air[i][C-1] = air[i+1][C-1]
    for i in range(C-1, 1, -1):
        air[top[0]][i] = air[top[0]][i-1]
    air[top[0]][1] = 0

    for i in range(bottom[0]+1, R-1):
        air[i][0] = air[i+1][0]
    for i in range(C-1):
        air[R-1][i] = air[R-1][i+1]
    for i in range(R-1, bottom[0], -1):
        air[i][C-1] = air[i-1][C-1]
    for i in range(C-1, 1, -1):
        air[bottom[0]][i] = air[bottom[0]][i-1]
    air[bottom[0]][1] = 0


for _ in range(T):
    dust = deque()
    for i in range(R):
        for j in range(C):
            if air[i][j] > 0:
                dust.append((i, j, air[i][j]))

    while dust:
        x, y, num = dust.popleft()
        minus = 0
        for d in range(4):
            nx, ny = x + dx[d], y + dy[d]
            if 0 <= nx < R and 0 <= ny < C:
                if air[nx][ny] != -1:
                    air[nx][ny] += num // 5
                    minus += num // 5
        air[x][y] -= minus

    air_clean()

total = 0
for i in range(R):
    for j in range(C):
        if air[i][j] > 0:
            total += air[i][j]
print(total)