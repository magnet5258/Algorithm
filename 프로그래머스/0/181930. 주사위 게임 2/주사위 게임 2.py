import math

def solution(a, b, c):
    if a == b and b == c and a == c:
        answer = (3*a)*(3*(math.pow(a,2)))*(3*(math.pow(a,3)))
        return answer
    elif a != b and b != c and a!= c:
        answer = a+b+c
        return answer
    else:
        answer = (a+b+c)*(math.pow(a,2)+math.pow(b,2)+math.pow(c,2))
        return answer
        