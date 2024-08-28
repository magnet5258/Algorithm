def solution(arr1, arr2):
    rows = len(arr1)
    cols = len(arr1[0])
    answer = [[0 for a in range(cols)] for b in range(rows)]
    
    for i in range(rows):
        for j in range(cols):
            answer[i][j] = arr1[i][j] + arr2[i][j]
    return answer