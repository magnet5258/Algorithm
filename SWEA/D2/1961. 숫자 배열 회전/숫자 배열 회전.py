T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    
    rotate_90 = [[arr[N - 1 - j][i] for j in range(N)]for i in range(N)]
    rotate_180 = [[rotate_90[N - 1 - j][i] for j in range(N)]for i in range(N)]
    rotate_270 = [[rotate_180[N - 1 - j][i] for j in range(N)]for i in range(N)]
    
    print(f'#{test_case}')
    for i in range(N):
        print(''.join(map(str, rotate_90[i])), ''.join(map(str, rotate_180[i])), ''.join(map(str, rotate_270[i])))