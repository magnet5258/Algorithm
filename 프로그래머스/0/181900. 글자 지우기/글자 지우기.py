def solution(my_string, indices):
    answer = list(my_string)
    indices.sort(reverse = True)
    for i in indices:
        answer.pop(i)
    return ''.join(answer)