T = int(input())
for i in range(T):
    quiz = input()
    cnt = 0
    ans_lst = []
    for x in quiz:
        if x == 'O':
            cnt += 1
            ans_lst.append(cnt)
        else:
            cnt = 0
    print(sum(ans_lst))