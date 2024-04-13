def solution(my_string, is_suffix):
    answer = []
    for i in range(len(my_string)):
        answer.append(my_string[i:])
    for x in answer:
        if is_suffix == x:
            return 1
    return 0