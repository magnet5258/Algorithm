def solution(number):
    answer = 0
    from itertools import combinations
    
    for i in combinations(number, 3):
        if sum(i) == 0:
            answer += 1
    
    return answer