def solution(myString):
    answer = []
    x = myString.split("x")
    for i in x:
        answer.append(len(i))
    return answer