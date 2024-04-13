def solution(arr, queries):
    for query in queries:
        for i in range(query[0], query[1] + 1):
            try:
                if i % query[2] == 0:
                    arr[i] += 1
            except:
                arr[i] += 0
    return arr