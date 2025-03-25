from collections import deque

N = int(input())
K = int(input())
arr = [[0] * N for _ in range(N)]
for _ in range(K):
    x, y = map(int, input().split())
    arr[x - 1][y - 1] = 1

L = int(input())
directions = deque()
for _ in range(L):
    X, C = input().split()
    directions.append([X, C])

dx = deque([0, 1, 0, -1])
dy = deque([1, 0, -1, 0])

snake = deque()
snake.append((0, 0))
arr[0][0] = 2

ans = 0
while True:
    ans += 1
    head_x, head_y = snake[-1]
    nx = head_x + dx[0]
    ny = head_y + dy[0]

    if nx >= N or nx < 0 or ny >= N or ny < 0 or arr[nx][ny] == 2:
        break
    elif arr[nx][ny] == 0:
        tail_x, tail_y = snake.popleft()
        arr[tail_x][tail_y] = 0

    arr[nx][ny] = 2
    snake.append((nx, ny))

    if directions and ans == int(directions[0][0]):
        if directions[0][1] == 'L':
            dx.rotate(1)
            dy.rotate(1)
        else:
            dx.rotate(-1)
            dy.rotate(-1)
        directions.popleft()

print(ans)