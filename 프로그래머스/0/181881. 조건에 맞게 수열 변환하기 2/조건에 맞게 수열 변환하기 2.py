def solution(arr):
    answer = 0
    prev = arr
    while True:
        change = []
        for i in range(len(prev)):
            if prev[i] >= 50 and prev[i] % 2 == 0:
                change.append(int(prev[i] / 2))
            elif prev[i] < 50 and prev[i] % 2 == 1:
                change.append(prev[i] * 2 + 1)
            else:
                change.append(prev[i])
        
        if prev == change:
            break
        answer += 1
        prev = change
    return answer        