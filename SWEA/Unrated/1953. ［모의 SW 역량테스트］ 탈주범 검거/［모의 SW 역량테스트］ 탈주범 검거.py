from collections import deque

directions = {
    1: [(0, -1), (0, 1), (-1, 0), (1, 0)],
    2: [(-1, 0), (1, 0)],
    3: [(0, -1), (0, 1)],
    4: [(-1, 0), (0, 1)],
    5: [(1, 0), (0, 1)],
    6: [(1, 0), (0, -1)],
    7: [(-1, 0), (0, -1)]
}

reverse_check = {
    (-1, 0): [1, 2, 5, 6],
    (1, 0): [1, 2, 4, 7],
    (0, -1): [1, 3, 4, 5],
    (0, 1): [1, 3, 6, 7]
}

def catch(x, y):
    global cnt
    
    queue = deque([(x, y)])
    visited = set()
    visited.add((x, y))
    cnt = 1
    time = 1
    
    while time < L:
        size = len(queue)
        for _ in range(size):
            x, y = queue.popleft()
            current_type = arr[x][y]
            for dx, dy in directions[current_type]:
                nx, ny = x + dx, y + dy
                if 0 <= nx < N and 0 <= ny < M and (nx, ny) not in visited:
                    next_type = arr[nx][ny]
                    if next_type in reverse_check[(dx, dy)]:
                        queue.append((nx, ny))
                        visited.add((nx, ny))
                        cnt += 1
                        
        time += 1

T = int(input())
for test_case in range(1, T + 1):
    N, M, R, C, L = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    cnt = 0
    catch(R, C)
    print(f'#{test_case} {cnt}')
