C, R = map(int, input().split())
K = int(input())

if K > C * R:
    print(0)
else:
    arr = [[0] * C for _ in range(R)]
    di = [1, 0, -1, 0]
    dj = [0, 1, 0, -1]
    ci = cj = dr = 0
    for n in range(1, K):
        arr[ci][cj] = n
        ni, nj = ci + di[dr], cj + dj[dr]
        if 0<= ni < R and 0 <= nj < C and arr[ni][nj] == 0:
            ci, cj = ni, nj
        else:
            dr = (dr + 1) % 4
            ci, cj = ci + di[dr], cj + dj[dr]
    print(f'{cj + 1} {ci + 1}')