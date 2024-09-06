import itertools

def solution(number):
    answer = 0
    combinations = list(itertools.combinations(number, 3))
    
    for combo in combinations:
        if sum(combo) == 0:
            answer += 1
    
    return answer