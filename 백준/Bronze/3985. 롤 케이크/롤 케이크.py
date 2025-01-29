L = int(input())
N = int(input())
lst = [0] * L
max_num = 0
max_cnt = 0
for i in range(1, N + 1):
    P, K = map(int, input().split())
    if K - P > max_num:
        max_num = K - P
        max_i = i
    for j in range(P - 1, K):
        if lst[j] == 0:
            lst[j] = i
    if lst.count(i) > max_cnt:
        max_cnt = lst.count(i)
        max_cnt_i = i
print(f'{max_i}\n{max_cnt_i}')