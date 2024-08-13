def solution(a, b):
    answer = 0
    max_x = max(a, b)
    min_x = min(a, b)
    for i in range(min_x, max_x + 1):
        answer += i
    return answer