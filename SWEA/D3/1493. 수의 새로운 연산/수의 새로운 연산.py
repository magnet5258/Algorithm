dic = {}
r_dic = {}
x, y = 1, 1

for n in range(1, 50000):
    dic[n] = (x, y)
    r_dic[(x, y)] = n
    x, y = x - 1, y + 1
    if x < 1:
        x, y = y, 1

T = int(input())
for test_case in range(1, T + 1):
    p, q = map(int, input().split())
    new_x, new_y = dic[p][0] + dic[q][0], dic[p][1] + dic[q][1]
    new_n = r_dic[(new_x, new_y)]
    print(f'#{test_case} {new_n}')
    