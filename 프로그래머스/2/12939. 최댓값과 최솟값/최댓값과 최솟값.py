def solution(s):
    answer = []
    x = s.split(" ")
    for i in range(len(x)):
        x[i] = int(x[i])
    answer.append(min(x))
    answer.append(max(x))
    for i in range(len(answer)):
        answer[i] = str(answer[i])
    return " ".join(answer)