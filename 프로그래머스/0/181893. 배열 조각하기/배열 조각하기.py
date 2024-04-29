def solution(arr, query):
    for i in range(len(query)):
        x = query[i]
        if i % 2 == 0:
            arr = arr[:x+1]
        else:
            arr = arr[x:]
    return arr