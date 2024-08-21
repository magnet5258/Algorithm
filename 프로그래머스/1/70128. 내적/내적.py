def solution(a, b):
    answer = []
    for i, j in zip(a, b):
        answer.append(i * j)
    return sum(answer)