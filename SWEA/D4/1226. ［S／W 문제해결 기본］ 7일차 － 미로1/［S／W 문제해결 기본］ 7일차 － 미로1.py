from collections import deque
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
def maze(x, y):
    global result
    queue = deque([(x, y)])
    data[x][y] = 1
 
    while queue:
        x, y = queue.popleft()
        for k in range(4):
            nx, ny = x + dx[k], y + dy[k]
            if 0 > nx or nx >= 16 or 0 > ny or ny >= 16:
                continue
            if data[nx][ny] == 3:
                result = 1
                break
            if data[nx][ny] == 1:
                continue
            queue.append((nx, ny))
            data[nx][ny] = 1
 
T = 10
for test_case in range(1, T + 1):
    N = int(input())
    data = [list(map(int, input())) for _ in range(16)]
    result = 0
    maze(1, 1)
    print(f'#{test_case} {result}')