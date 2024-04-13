def solution(my_string, index_list):
    answer = []
    x = list(my_string)
    for i in index_list:
        answer.append(x[i])
    return ''.join(answer)