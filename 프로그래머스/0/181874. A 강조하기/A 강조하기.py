def solution(myString):
    answer = list(myString)
    for i in range(len(answer)):
        if answer[i] == "a":
            answer[i] = answer[i].upper()
        elif answer[i] == "A":
            pass
        else:
            answer[i] = answer[i].lower()
    return ''.join(answer)