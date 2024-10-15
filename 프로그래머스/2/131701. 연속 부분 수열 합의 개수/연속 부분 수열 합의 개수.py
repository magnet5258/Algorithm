def solution(elements):
    sum_list = []
    n = len(elements)
    extended_elements = elements * 2
    for i in range(1, n + 1):
        for j in range(n):
            sum_list.append(sum(extended_elements[j:j + i]))
    return len(set(sum_list))