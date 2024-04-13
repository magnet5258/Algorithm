def solution(x1, x2, x3, x4):
    x_list = [x1, x2, x3, x4]
    answer = all([any(x_list[0:2]), any(x_list[2:])])
    return answer