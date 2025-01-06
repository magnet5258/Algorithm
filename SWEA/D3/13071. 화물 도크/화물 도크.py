T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    sorted_arr = sorted(arr, key = lambda x: x[1])
    max_cnt = 0
    end_time = 0
    for i in sorted_arr:
        if i[0] >= end_time:
            max_cnt += 1
            end_time = i[1]
    print(f'#{test_case} {max_cnt}')
            
    