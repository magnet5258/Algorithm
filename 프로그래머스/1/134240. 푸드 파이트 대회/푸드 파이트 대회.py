def solution(food):
    answer = ''
    for i in range(len(food)):
        if i >= 1:
            answer += (str(i) * (food[i] // 2))
    reversed_answer = answer[::-1]
    answer += '0'
    answer += reversed_answer
    return answer