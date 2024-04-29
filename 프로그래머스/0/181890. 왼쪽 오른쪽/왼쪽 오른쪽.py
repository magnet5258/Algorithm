def solution(str_list):
    answer = []
    for i in str_list:
        x = str_list.index(i)
        if i == "l":
            answer = str_list[:x]
            break
        elif i == "r":
            answer = str_list[x+1:]
            break
        else:
            pass
    return answer