def solution(n):
    answer = [n]
    while True:
        if answer[-1] == 1:
            break
        elif answer[-1] % 2 == 0:
            answer.append(int(answer[-1] / 2))
        else:
            answer.append(3 * answer[-1] + 1)
    return answer