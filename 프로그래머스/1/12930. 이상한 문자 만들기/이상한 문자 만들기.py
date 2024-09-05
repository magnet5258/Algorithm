def solution(s):
    s_list = list(s)
    idx = 0
    for i in range(len(s_list)):
        if s_list[i].isalpha():
            if idx % 2 == 0:
                s_list[i] = s_list[i].upper()
                idx += 1
            else:
                s_list[i] = s_list[i].lower()
                idx += 1
        else:
            idx = 0
    return ''.join(s_list)