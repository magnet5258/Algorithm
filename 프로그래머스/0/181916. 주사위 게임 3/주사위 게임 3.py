def solution(a, b, c, d):
    x = [a, b, c, d]
    y = list(set(x))
    if len(y) == 1:
        answer = 1111 * y[0]
    elif len(y) == 2:
        for i in y:
            if x.count(i) == 2:
                answer = (y[0] + y[1]) * abs(y[0] - y[1])
            elif x.count(i) == 3:
                t = [w for w in y if w != i]
                answer = (10 * i + t[0]) ** 2
    elif len(y) == 3:
        for i in y:
            if x.count(i) == 2:
                t = [w for w in y if w != i]
                answer = t[0] * t[1]
    else:
        answer = min(y)
    return answer