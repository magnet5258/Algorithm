def solution(arr1, arr2):
    n, m, p = len(arr1), len(arr1[0]), len(arr2[0])
    answer = [[0] * p for _ in range(n)]
    for i in range(n):
        for j in range(p):
            for k in range(m):
                answer[i][j] += arr1[i][k] * arr2[k][j]
    return answer