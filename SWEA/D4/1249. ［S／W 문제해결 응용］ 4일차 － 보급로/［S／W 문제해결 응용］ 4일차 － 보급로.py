from collections import deque
 
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
 
def fix_road():
    queue = deque([(0, 0)])
    dist[0][0] = data[0][0]
 
    while queue:
        x, y = queue.popleft()
        for k in range(4):
            nx, ny = x + dx[k], y + dy[k]
            if 0 <= nx < N and 0 <= ny < N:
                new_cost = dist[x][y] + data[nx][ny]
                if new_cost < dist[nx][ny]:
                    dist[nx][ny] = new_cost
                    queue.append((nx, ny))
    return dist[N - 1][N - 1]
 
T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    data = [list(map(int, input())) for _ in range(N)]
    dist = [[float('inf')] * N for _ in range(N)]
    min_cost = fix_road()
    print(f'#{test_case} {min_cost}')