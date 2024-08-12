def solution(n):
    s = str(n)
    answer = []
    for i in range(len(s)):
        answer.append(int(s[-(i + 1)]))
    return answer