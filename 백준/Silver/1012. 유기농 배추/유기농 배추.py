from collections import deque

T = int(input())
for _ in range(T):
    M, N, K = map(int, input().split())
    ground = [[0] * M for _ in range(N)]
    for _ in range(K):
        X, Y = map(int, input().split())
        ground[Y][X] = 1

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    visited = [[False] * M for _ in range(N)]
    cnt = 0

    queue = deque()
    for i in range(N):
        for j in range(M):
            if ground[i][j] == 1 and not visited[i][j]:
                queue.append((i, j))
                visited[i][j] = True
                cnt += 1
                while queue:
                    x, y = queue.popleft()
                    for d in range(4):
                        nx, ny = x + dx[d], y + dy[d]
                        if 0 <= nx < N and 0 <= ny < M:
                            if ground[nx][ny] == 1 and not visited[nx][ny]:
                                queue.append((nx, ny))
                                visited[nx][ny] = True

    print(cnt)