def solution(s):
    x, y = 0, 0
    
    while len(s) != 1:
        for i in s:
            if i == '0':
                y += 1
        s = bin(len(s.replace('0', '')))[2:]
        x += 1
    
    return [x, y]