from collections import deque
 
dx = [-1, -1, -1, 0, 0, 1, 1, 1]
dy = [-1, 0, 1, -1, 1, -1, 0, 1]
 
def build_board(grid, n):
    board = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if grid[i][j] == '*':
                board[i][j] = -1
            else:
                count = 0
                for d in range(8):
                    ni = i + dx[d]
                    nj = j + dy[d]
                    if 0 <= ni < n and 0 <= nj < n and grid[ni][nj] == '*':
                        count += 1
                board[i][j] = count
    return board
 
 
def find_bomb(x, y, board, visited, n):
    queue = deque()
    queue.append((x, y))
    visited[x][y] = True
 
    while queue:
        cx, cy = queue.popleft()
        if board[cx][cy] == 0:
            for d in range(8):
                nx = cx + dx[d]
                ny = cy + dy[d]
                if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny]:
                    if board[nx][ny] != -1:
                        visited[nx][ny] = True
                        queue.append((nx, ny))
 
 
T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    arr = [list(input().strip()) for _ in range(N)]
    bomb_board = build_board(arr, N)
    visited = [[False] * N for _ in range(N)]
    cnt = 0
 
    for i in range(N):
        for j in range(N):
            if bomb_board[i][j] == 0 and not visited[i][j]:
                find_bomb(i, j, bomb_board, visited, N)
                cnt += 1
 
    for i in range(N):
        for j in range(N):
            if bomb_board[i][j] != -1 and not visited[i][j]:
                cnt += 1
 
    print(f'#{test_case} {cnt}')