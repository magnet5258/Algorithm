def solution(a, b, n):
    answer = 0
    while n >= a:
        answer += (n // a) * b
        if n % a == 0:    
            n = (n // a) * b
        else:
            n = (n // a) * b + (n % a)
    return answer