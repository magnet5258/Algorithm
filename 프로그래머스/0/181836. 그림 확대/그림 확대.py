def solution(picture, k):
    answer = []
    for i in picture:
        x = list(i)
        y = map(lambda a: a*k, x)
        z = ''.join(y)
        for i in range(k):
            answer.append(z)
    return answer