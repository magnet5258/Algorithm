T = int(input())
for test_case in range(1, T + 1):
    N, K = map(int, input().split())
    arr1 = [list(map(int, input().split())) for _ in range(N)]
    arr2 = list(map(list, zip(*arr1)))
    word_cnt = 0
    
    for i in arr1:
        for j in range(N - K + 1):
            if sum(i[j:j+K]) == K:
                if (j == 0 or i[j-1] == 0) and (j+K == N or i[j+K] == 0):
                    word_cnt += 1
                
    for i in arr2:
        for j in range(N - K + 1):
            if sum(i[j:j+K]) == K:
                if (j == 0 or i[j-1] == 0) and (j+K == N or i[j+K] == 0):
                    word_cnt += 1
    
    print(f'#{test_case} {word_cnt}')