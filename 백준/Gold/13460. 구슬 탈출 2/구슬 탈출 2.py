from collections import deque

N, M = map(int, input().split())
board = [list(input().strip()) for _ in range(N)]

for i in range(N):
    for j in range(M):
        if board[i][j] == 'R':
            Rx, Ry = i, j
        elif board[i][j] == 'B':
            Bx, By = i, j

visited = [[[[False] * M for _ in range(N)] for _ in range(M)] for _ in range(N)]

queue = deque()
queue.append((Rx, Ry, Bx, By, 0))
visited[Rx][Ry][Bx][By] = True

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

while queue:
    Rx, Ry, Bx, By, depth = queue.popleft()
    if depth >= 10:
        break
    for d in range(4):
        nRx, nRy = Rx, Ry
        nBx, nBy = Bx, By
        r_cnt = b_cnt = 0

        while True:
            if board[nRx + dx[d]][nRy + dy[d]] == '#':
                break
            nRx += dx[d]
            nRy += dy[d]
            r_cnt += 1
            if board[nRx][nRy] == 'O':
                break

        while True:
            if board[nBx + dx[d]][nBy + dy[d]] == '#':
                break
            nBx += dx[d]
            nBy += dy[d]
            b_cnt += 1
            if board[nBx][nBy] == 'O':
                break

        if board[nBx][nBy] == 'O':
            continue
        if board[nRx][nRy] == 'O':
            print(depth + 1)
            exit()

        if nRx == nBx and nRy == nBy:
            if r_cnt > b_cnt:
                nRx -= dx[d]
                nRy -= dy[d]
            else:
                nBx -= dx[d]
                nBy -= dy[d]

        if not visited[nRx][nRy][nBx][nBy]:
            visited[nRx][nRy][nBx][nBy] = True
            queue.append((nRx, nRy, nBx, nBy, depth + 1))

print(-1)