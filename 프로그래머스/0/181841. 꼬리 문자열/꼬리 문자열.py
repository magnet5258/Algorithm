def solution(str_list, ex):
    for i in str_list[:]:
        if ex in i:
            str_list.remove(i)
    return ''.join(str_list)