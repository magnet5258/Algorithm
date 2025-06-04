from collections import deque

N = int(input())
grid = [list(input().strip()) for _ in range(N)]

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def divide(x, y, visited, check):
    queue = deque([(x, y)])
    visited[x][y] = True
    c_color = grid[x][y]
    while queue:
        x, y = queue.popleft()
        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]
            if 0 <= nx < N and 0 <= ny < N:
                if not visited[nx][ny]:
                    n_color = grid[nx][ny]
                    if check:
                        if (c_color in 'RG' and n_color in 'RG') or c_color == n_color:
                            visited[nx][ny] = True
                            queue.append((nx, ny))
                    else:
                        if c_color == n_color:
                            visited[nx][ny] = True
                            queue.append((nx, ny))


visited_normal = [[False] * N for _ in range(N)]
cnt_normal = 0
for i in range(N):
    for j in range(N):
        if not visited_normal[i][j]:
            divide(i, j, visited_normal, False)
            cnt_normal += 1

visited_weak = [[False] * N for _ in range(N)]
cnt_weak = 0
for i in range(N):
    for j in range(N):
        if not visited_weak[i][j]:
            divide(i, j, visited_weak, True)
            cnt_weak += 1

print(cnt_normal, cnt_weak)