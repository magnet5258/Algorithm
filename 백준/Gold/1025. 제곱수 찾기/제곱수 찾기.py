def is_square(n):
    root = int(n ** 0.5)
    return root * root == n


N, M = map(int, input().split())
board = [input() for _ in range(N)]
answer = -1

for i in range(N):
    for j in range(M):
        for dx in range(-N, N):
            for dy in range(-M, M):
                if dx == 0 and dy == 0:
                    continue
                x, y = i, j
                num = ''
                while 0 <= x < N and 0 <= y < M:
                    num += board[x][y]
                    val = int(num)
                    if is_square(val):
                        answer = max(answer, val)
                    x += dx
                    y += dy

print(answer)