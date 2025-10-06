def solution(answers):
    answer = []
    cnt_1 = cnt_2 = cnt_3 = 0
    
    for i in range(len(answers)):
        if answers[i] == i % 5 + 1:
            cnt_1 += 1
            
        if i % 2 == 0 and answers[i] == 2:
            cnt_2 += 1
        elif i % 8 == 1 and answers[i] == 1:
            cnt_2 += 1
        elif i % 8 == 3 and answers[i] == 3:
            cnt_2 += 1
        elif i % 8 == 5 and answers[i] == 4:
            cnt_2 += 1
        elif i % 8 == 7 and answers[i] == 5:
            cnt_2 += 1
            
        if i % 10 in (0, 1) and answers[i] == 3:
            cnt_3 += 1
        elif i % 10 in (2, 3) and answers[i] == 1:
            cnt_3 += 1
        elif i % 10 in (4, 5) and answers[i] == 2:
            cnt_3 += 1
        elif i % 10 in (6, 7) and answers[i] == 4:
            cnt_3 += 1
        elif i % 10 in (8, 9) and answers[i] == 5:
            cnt_3 += 1
        
    result = max(cnt_1, cnt_2, cnt_3)
    
    if cnt_1 == result:
        answer.append(1)
    if cnt_2 == result:
        answer.append(2)
    if cnt_3 == result:
        answer.append(3)
    
    return answer