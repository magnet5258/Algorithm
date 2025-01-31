T = int(input())
code_dic = {'0001101': 0, '0011001': 1, '0010011': 2, '0111101': 3, '0100011': 4, '0110001': 5, '0101111': 6,
            '0111011': 7, '0110111': 8, '0001011': 9}
for test_case in range(1, T + 1):
    N, M = map(int, input().split())
    arr = [list(map(int, input())) for _ in range(N)]
    found = False
    for i in range(N):
        for j in range(M - 1, -1, -1):
            if arr[i][j] == 1:
                code_i, code_j = i, j
                found = True
                break
        if found:
            break
    code = ''.join(map(str, arr[code_i][code_j - 55:code_j + 1]))
    num_lst = []
    odd_num_lst = []
    even_num_lst = []
    for k in range(0, 56, 7):
        num = code[k:k + 7]
        num_lst.append(code_dic[num])
    for idx, num in enumerate(num_lst):
        if idx % 2 == 0:
            odd_num_lst.append(num)
        else:
            even_num_lst.append(num)
    if (sum(odd_num_lst) * 3 + sum(even_num_lst)) % 10 == 0:
        ans = sum(odd_num_lst) + sum(even_num_lst)
    else:
        ans = 0
    print(f'#{test_case} {ans}')