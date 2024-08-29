import math

def solution(n, m):
    answer = []
    answer.append(math.gcd(n, m))
    answer.append(abs(n * m) // math.gcd(n, m))
    return answer