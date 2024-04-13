def solution(a, d, included):
    answer = 0
    for i in range(len(included)):
        r = a + (d * i)
        if i == 0 and included[i] == True:
            answer += a            
        elif i > 0 and included[i] == True:
            answer += r
    return answer