def solution(myString):
    answer = list(myString)
    for i in range(len(answer)):
        if answer[i] < "l":
            answer[i] = "l"
    return ''.join(answer)