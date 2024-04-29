def solution(num_list):
    x = 0
    y = 0
    for i in range(len(num_list)):
        if i % 2 == 0:
            x += num_list[i]
        else:
            y += num_list[i]
    if x > y :
        return x
    else:
        return y