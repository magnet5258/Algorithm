def solution(my_string, is_prefix):
    for n in range(len(my_string), 1, -1):
        if my_string[:n].startswith(is_prefix):
            return 1
        else:
            return 0