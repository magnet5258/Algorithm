def cut(N, arr):
    global w_cnt, b_cnt

    if sum(map(sum, arr)) == 0:
        w_cnt += 1
        return

    if sum(map(sum, arr)) == N ** 2:
        b_cnt += 1
        return

    half = N // 2
    cut(half, [row[:half] for row in arr[:half]])
    cut(half, [row[half:] for row in arr[:half]])
    cut(half, [row[:half] for row in arr[half:]])
    cut(half, [row[half:] for row in arr[half:]])


N = int(input())
papers = [list(map(int, input().split())) for _ in range(N)]
w_cnt = 0
b_cnt = 0
cut(N, papers)
print(f'{w_cnt}\n{b_cnt}')