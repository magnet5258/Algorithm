def solution(n):
    answer = 0
    
    for i in range(1, n + 1):
        temp_n = n
        while temp_n > 0:
            temp_n -= i
            i += 1
        if temp_n == 0:
            answer += 1
    
    return answer
