def solution(a, b):
    x = int(str(a) + str(b))
    y = 2 * a * b
    if y > x:
        return y
    else:
        return x