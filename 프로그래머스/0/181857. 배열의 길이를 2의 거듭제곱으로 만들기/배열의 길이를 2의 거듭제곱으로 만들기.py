def solution(arr):
    x = len(arr)
    y = 1
    
    while x > y:
        y *= 2
    
    return arr + [0] * (y - x)