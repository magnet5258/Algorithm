def solution(n,a,b):
    answer = 0
    while a != b:
        if a % 2 == 1 and b % 2 == 1:
            a = int(a / 2 + 1)
            b = int(b / 2 + 1)
        elif a % 2 == 1 and b % 2 == 0:
            a = int(a / 2 + 1)
            b = int(b / 2)
        elif a % 2 == 0 and b % 2 == 1:
            a = int(a / 2)
            b = int(b / 2 + 1)
        else:
            a = int(a / 2)
            b = int(b / 2)
        answer += 1
    return answer