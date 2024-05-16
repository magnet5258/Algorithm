def solution(arr):
    n = len(arr)
    answer = 0
    for i in range(n):
        for j in range(n):
            if arr[i][j] == arr[j][i]:
                answer += 1
    if answer == n * n:
        return 1
    else:
        return 0