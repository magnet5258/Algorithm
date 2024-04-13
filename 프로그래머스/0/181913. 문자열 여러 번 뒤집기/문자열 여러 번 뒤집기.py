def solution(my_string, queries):
    answer = list(my_string)
    for query in queries:
        s = query[0]
        e = query[1]
        if (e - s) % 2 == 1:
            for i in range(s, (s+e)//2+1):
                answer[i], answer[s+e-i] = answer[s+e-i], answer[i]
        else:
            for i in range(s, int((s+e)/2)):
                answer[i], answer[s+e-i] = answer[s+e-i], answer[i]
    return ''.join(answer)
                