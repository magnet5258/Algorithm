def solution(n, m, section):
    answer = 1
    if len(section) > 1:
        check = section[0]
        for i in range(1, len(section)):
            if section[i] - check + 1 > m:
                answer += 1
                check = section[i]
    return answer