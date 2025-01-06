T = 10
for test_case in range(1, T + 1):
    N = int(input())
    arr1 = [list(map(int, input().split())) for _ in range(N)]
    arr2 = list(map(list, zip(*arr1)))
    pair_cnt = 0
    for i in arr2:
        found = False
        for j in range(N):
            if i[j] == 1:
                found = True
            elif i[j] == 2 and found == True:
                pair_cnt += 1
                found = False
    print(f'#{test_case} {pair_cnt}')