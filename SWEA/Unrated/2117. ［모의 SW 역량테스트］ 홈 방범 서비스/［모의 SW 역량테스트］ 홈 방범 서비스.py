def get_diamond_sum(prefix, i, j, d, N):
    total = 0
    for r in range(i - d, i + d + 1):
        if 0 <= r < N:
            span = d - abs(i - r)
            c1 = max(j - span, 0)
            c2 = min(j + span, N - 1)
            total += prefix[r][c2] - (prefix[r][c1 - 1] if c1 > 0 else 0)
    return total
 
 
T = int(input())
for test_case in range(1, T + 1):
    N, M = map(int, input().split())
    house = [list(map(int, input().split())) for _ in range(N)]
    prefix = []
    for row in house:
        cur = []
        s = 0
        for val in row:
            s += val
            cur.append(s)
        prefix.append(cur)
 
    max_cnt = 0
    for K in range(2 * N - 1, 0, -1):
        cost = K ** 2 + (K - 1) ** 2
        d = K - 1
        for i in range(N):
            for j in range(N):
                house_cnt = get_diamond_sum(prefix, i, j, d, N)
                if house_cnt * M >= cost:
                    max_cnt = max(max_cnt, house_cnt)
    print(f'#{test_case} {max_cnt}')