def solution(numbers):
    answer = 0
    for i in [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]:
        if i not in numbers:
            answer += i
    return answer