def solution(n):
    num_1 = bin(n).count('1')
    answer = n + 1
    
    while True:
        num_2 = bin(answer).count('1')
        if num_1 == num_2:
            return answer
        else:
            answer += 1
    