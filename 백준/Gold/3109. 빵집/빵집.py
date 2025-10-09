import sys
sys.setrecursionlimit(10000)

R, C = map(int, input().split())
bakery = [list(input().strip()) for _ in range(R)]

cnt = 0
dx = [-1, 0, 1]

visited = [[False] * C for _ in range(R)]

def check_pipe(x, y):
    if y == C - 1:
        return True

    for d in range(3):
        nx, ny = x + dx[d], y + 1
        if 0 <= nx < R and 0 <= ny < C:
            if bakery[nx][ny] != 'x' and not visited[nx][ny]:
                visited[nx][ny] = True
                if check_pipe(nx, ny):
                    return True
    
    return False

for i in range(R):
    visited[i][0] = True
    if check_pipe(i, 0):
        cnt += 1

print(cnt)