def solution(myString):
    answer = []
    x = myString.split("x")
    for i in x:
        if i != "":
            answer.append(i)
    answer.sort()
    return answer