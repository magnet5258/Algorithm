def solution(sizes):
    size_max_list = []
    size_min_list = []
    for a, b in sizes:
        size_max_list.append(max(a, b))
        size_min_list.append(min(a, b))
    return max(size_max_list) * max(size_min_list)