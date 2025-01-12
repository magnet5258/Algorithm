T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    lst = [[1] * (i + 1) for i in range(N)]
    for j in range(2, N):
        for k in range(1, j):
            lst[j][k] = lst[j - 1][k - 1] + lst[j - 1][k]
    
    print(f'#{test_case}')
    for x in lst:
        print(' '.join(map(str, x)))
        