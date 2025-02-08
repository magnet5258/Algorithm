def find_max_score(idx, score_sum, cal_sum):
    global max_score
 
    if cal_sum > L:
        return
 
    max_score = max(max_score, score_sum)
 
    for i in range(idx, N):
        find_max_score(i + 1, score_sum + food_lst[i][0], cal_sum + food_lst[i][1])
 
T = int(input())
for test_case in range(1, T + 1):
    N, L = map(int, input().split())
    food_lst = [list(map(int, input().split())) for _ in range(N)]
    max_score = 0
    find_max_score(0, 0, 0)
    print(f'#{test_case} {max_score}')