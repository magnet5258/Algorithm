def solution(arr):
    answer = []
    for i in range(len(arr)):
        if arr[i] == 2:
            answer.append(i)
    if len(answer) == 0:
        return [-1]
    else:
        return arr[answer[0]:answer[-1]+1]