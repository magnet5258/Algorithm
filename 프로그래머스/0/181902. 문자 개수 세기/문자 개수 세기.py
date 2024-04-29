def solution(my_string):
    answer = []
    for i in range(52):
        answer.append(0)
    for s in my_string:
        if s.isupper():
            k = 65
        else:
            k = 71
        answer[ord(s) - k] += 1
    return answer