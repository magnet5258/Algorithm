def solution(arr, queries):
    result = []
    for query in queries:
        temp = []
        for i in range(query[0], query[1]+1):
            if arr[i] > query[2]:
                temp.append(arr[i])
        result.append(-1 if len(temp) == 0 else min(temp))
    return result