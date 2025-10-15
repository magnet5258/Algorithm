N, M, B = map(int, input().split())
ground = [list(map(int, input().split())) for _ in range(N)]

block_set = set()
blocks = []
for i in range(N):
    for j in range(M):
        block_set.add(ground[i][j])
        blocks.append(ground[i][j])

block_lst = sorted(block_set)
if len(block_lst) == 1:
    print(0, block_lst[0])
else:
    min_time = float('inf')
    height = 0
    for i in range(257):
        block_plus = block_minus = 0
        for block in blocks:
            if block >= i:
                block_minus += 2 * (block - i)
            else:
                block_plus += i - block
        if block_plus <= B + (block_minus // 2):
            if min_time >= block_plus + block_minus:
                min_time = block_plus + block_minus
                height = i
        else:
            continue
    print(min_time, height)