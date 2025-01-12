T = int(input())
score_dic = {0 : 'A+', 1 : 'A0', 2 : 'A-', 3 : 'B+', 4 : 'B0', 5 : 'B-', 6 : 'C+', 7 : 'C0', 8 : 'C-', 9 : 'D0'}
for test_case in range(1, T + 1):
    N, K = map(int, input().split())
    num = int(N / 10)
    lst = [list(map(int, input().split())) for _ in range(N)]
    score_lst = []
    for i in lst:
        score_lst.append(i[0] * 0.35 + i[1] * 0.45 + i[2] * 0.2)
    score = score_lst[K - 1]
    sorted_score = sorted(score_lst, reverse = True)
    score_index = sorted_score.index(score)
    ans = score_dic[score_index // num]
    print(f'#{test_case} {ans}')
        
