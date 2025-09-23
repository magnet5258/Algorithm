N, M = map(int, input().split())
r, c, d = map(int, input().split())
room = [list(map(int, input().split())) for _ in range(N)]

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

cnt = 0
while True:
    if room[r][c] == 0:
        room[r][c] = 2
        cnt += 1

    check = False
    for _ in range(4):
        d = (d + 3) % 4
        nx, ny = r + dx[d], c + dy[d]
        if 0 <= nx < N and 0 <= ny < M and room[nx][ny] == 0:
            r, c = nx, ny
            check = True
            break

    if check:
        continue
    else:
        back = (d + 2) % 4
        r, c = r + dx[back], c + dy[back]
        if room[r][c] == 1:
            break

print(cnt)