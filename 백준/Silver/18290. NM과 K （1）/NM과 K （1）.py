dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def is_adjacent(x, y):
    for d in range(4):
        nx, ny = x + dx[d], y + dy[d]
        if 0 <= nx < N and 0 <= ny < M and visited[nx][ny]:
            return True
    return False

def find_num(depth, start_idx, total):
    global ans
    if depth == K:
        ans = max(ans, total)
        return

    for idx in range(start_idx, N * M):
        x, y = divmod(idx, M)
        if not visited[x][y] and not is_adjacent(x, y):
            visited[x][y] = True
            find_num(depth + 1, idx + 1, total + arr[x][y])
            visited[x][y] = False

N, M, K = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
visited = [[False] * M for _ in range(N)]
ans = float('-inf')
find_num(0, 0, 0)
print(ans)
