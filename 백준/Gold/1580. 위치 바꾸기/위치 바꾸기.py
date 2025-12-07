from collections import deque

N, M = map(int, input().split())
grid = [list(input()) for _ in range(N)]
Ax = Ay = Bx = By = -1

for i in range(N):
    for j in range(M):
        if grid[i][j] == 'A':
            Ax, Ay = i, j
        elif grid[i][j] == 'B':
            Bx, By = i, j

moves = [(1, 1), (1, 0), (1, -1), (0, 1), (0, 0), (0, -1), (-1, 1), (-1, 0), (-1, -1)]

queue = deque()
visited = [[[[False] * M for _ in range(N)] for _ in range(M)] for _ in range(N)]
queue.append((Ax, Ay, Bx, By, 0))
visited[Ax][Ay][Bx][By] = True
answer = -1

while queue:
    ax, ay, bx, by, d = queue.popleft()
    if (ax, ay) == (Bx, By) and (bx, by) == (Ax, Ay):
        answer = d
        break

    for dax, day in moves:
        nax, nay = ax + dax, ay + day
        if 0 <= nax < N and 0 <= nay < M:
            if grid[nax][nay] != 'X':
                for dbx, dby in moves:
                    nbx, nby = bx + dbx, by + dby
                    if 0 <= nbx < N and 0 <= nby < M:
                        if grid[nbx][nby] != 'X':
                            if (nax, nay) == (bx, by) and (nbx, nby) == (ax, ay):
                                continue
                            if dax == 0 and day == 0 and dbx == 0 and dby == 0:
                                continue
                            if nax == nbx and nay == nby:
                                continue
                            if not visited[nax][nay][nbx][nby]:
                                queue.append((nax, nay, nbx, nby, d + 1))
                                visited[nax][nay][nbx][nby] = True

print(answer)