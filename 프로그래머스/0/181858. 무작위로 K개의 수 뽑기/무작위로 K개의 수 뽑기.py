def solution(arr, k):
    answer = []
    arr_set = list(dict.fromkeys(arr))
    if len(arr_set) >= k:
        for i in range(k):
            answer.append(arr_set[i])
    else:
        answer.extend(arr_set)
        for i in range(k - len(arr_set)):
            answer.append(-1)
    return answer