def solution(s):
    x = 0
    y = 0
    answer = []
    
    while len(s) != 1:
        for i in s:
            if i == '0':
                y += 1
        s = bin(len(s.replace('0', '')))[2:]
        x += 1
    
    answer.append(x)
    answer.append(y)
    
    return answer