def solution(arr):
    answer = []
    for i in arr:
        for x in range(i):
            answer.append(i)
    return answer