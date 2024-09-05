def solution(n):
    answer = 0
    t_str = ''
    
    while n > 0:
        t_str = str(n % 3) + t_str
        n //= 3
    
    t_str_r = t_str[::-1]
    for i in range(1, len(t_str_r) + 1):
        answer += int(t_str_r[-i]) * (3 ** (i - 1))
    
    return answer