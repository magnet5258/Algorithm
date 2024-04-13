def solution(my_string, m, c):
    answer = []
    result = []
    x = int(len(my_string) / m)
    for i in range(x):
        answer.append(my_string[m*i:m*(i+1)])
    for y in answer:
        result.append(y[c-1])        
    return ''.join(result)