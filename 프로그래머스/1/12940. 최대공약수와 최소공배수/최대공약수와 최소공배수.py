def solution(n, m):
    answer = []
    c, d = max(n, m), min(n, m)
    while d != 0:
        c, d = d, c % d
    answer.append(abs(c))
    answer.append(n * m // abs(c))
    return answer