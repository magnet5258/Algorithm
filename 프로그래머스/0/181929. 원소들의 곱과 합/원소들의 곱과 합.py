def solution(num_list):
    mul = 1
    sum = 0
    for i in num_list:
        mul *= i
        sum += i
    if mul > (sum**2):
        return 0
    else:
        return 1