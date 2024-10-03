def solution(arr):
    answer = max(arr)
    while True:
        if all(answer % num == 0 for num in arr):
            return answer
        answer += max(arr)
        