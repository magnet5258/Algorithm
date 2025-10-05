from collections import deque

gears = [deque(input().strip()) for _ in range(4)]

K = int(input())
for _ in range(K):
    gear, direction = map(int, input().split())
    gear -= 1

    rotate_dir = [0] * 4
    rotate_dir[gear] = direction

    for i in range(gear - 1, -1, -1):
        if gears[i][2] != gears[i + 1][6]:
            rotate_dir[i] = -rotate_dir[i + 1]
        else:
            break

    for i in range(gear + 1, 4):
        if gears[i - 1][2] != gears[i][6]:
            rotate_dir[i] = -rotate_dir[i - 1]
        else:
            break

    for i in range(4):
        gears[i].rotate(rotate_dir[i])

score = 0
for i in range(4):
    if gears[i][0] == '1':
        score += 2 ** i

print(score)