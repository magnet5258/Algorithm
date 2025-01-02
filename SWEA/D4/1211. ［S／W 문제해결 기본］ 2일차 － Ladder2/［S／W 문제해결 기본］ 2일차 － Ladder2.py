T = 10
for t in range(1, T + 1):
    _ = int(input())
    arr = [[0] + list(map(int, input().split())) + [0] for _ in range(100)]
    min_cnt = 10000
    for j in range(1, 101):
        if arr[0][j] == 0:
            continue
        cj = j
        cnt = dr = ci = 0
        while ci < 99:
            cnt += 1
            if dr == 0:
                ci += 1
                if arr[ci][cj - 1] == 1:
                    dr = -1
                elif arr[ci][cj + 1] == 1:
                    dr = 1
            else:
                cj += dr
                if arr[ci][cj + dr] == 0:
                    dr = 0
        if min_cnt >= cnt:
            min_cnt = cnt
            ans = j - 1
    print(f'#{t} {ans}')
                    
        