from collections import deque

N, L, R = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(N)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

migration = True
answer = 0
while migration:
    visited = [[False] * N for _ in range(N)]
    cnt = 0
    for i in range(N):
        for j in range(N):
            if not visited[i][j]:
                queue = deque([(i, j)])
                land = [(A[i][j], i, j)]
                visited[i][j] = True
                while queue:
                    x, y = queue.popleft()
                    for d in range(4):
                        nx, ny = x + dx[d], y + dy[d]
                        if 0 <= nx < N and 0 <= ny < N:
                            if not visited[nx][ny] and L <= abs(A[x][y] - A[nx][ny]) <= R:
                                land.append((A[nx][ny], nx, ny))
                                visited[nx][ny] = True
                                queue.append((nx, ny))

                if len(land) >= 2:
                    cnt += 1
                    total = 0
                    for a, b, c in land:
                        total += a
                    for a, b, c in land:
                        A[b][c] = total // len(land)

    if cnt == 0:
        migration = False
    else:
        answer += 1

print(answer)