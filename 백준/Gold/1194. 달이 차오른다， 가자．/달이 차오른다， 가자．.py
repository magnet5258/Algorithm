from collections import deque

N, M = map(int, input().split())
maze = [list(input()) for _ in range(N)]
queue = deque()
visited = [[[False] * (1 << 6) for _ in range(M)] for _ in range(N)]
for i in range(N):
    for j in range(M):
        if maze[i][j] == '0':
            queue.append((i, j, 0, 0))
            visited[i][j][0] = True

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

while queue:
    x, y, state, dist = queue.popleft()
    for d in range(4):
        nx, ny = x + dx[d], y + dy[d]
        if not (0 <= nx < N and 0 <= ny < M):
            continue

        if maze[nx][ny] == '#':
            continue
        elif maze[nx][ny] == '1':
            print(dist + 1)
            exit()

        new_state = state
        if 'a' <= maze[nx][ny] <= 'f':
            new_state |= (1 << ord(maze[nx][ny]) - ord('a'))

        if 'A' <= maze[nx][ny] <= 'F':
            if not (state & (1 << ord(maze[nx][ny]) - ord('A'))):
                continue

        if not visited[nx][ny][new_state]:
            visited[nx][ny][new_state] = True
            queue.append((nx, ny, new_state, dist + 1))

print(-1)