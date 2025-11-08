def solution(progresses, speeds):
    n = len(progresses)
    answer = []
    lst = [0] * n
    for i in range(n):
        if (100 - progresses[i]) % speeds[i] == 0:
            lst[i] = (100 - progresses[i]) // speeds[i]
        else:
            lst[i] = ((100 - progresses[i]) // speeds[i]) + 1
    state = lst[0]
    cnt = 0
    for i in range(n):
        if lst[i] > state:
            state = lst[i]
            answer.append(cnt)
            cnt = 1
        else:
            cnt += 1
        if i == n - 1:
            answer.append(cnt)
    return answer