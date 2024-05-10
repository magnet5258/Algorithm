def solution(strArr):
    answer = [len(i) for i in strArr]
    length = []
    for i in set(answer):
        length.append(answer.count(i))
    return max(length)