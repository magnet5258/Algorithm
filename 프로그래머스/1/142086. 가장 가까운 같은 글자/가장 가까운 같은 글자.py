def solution(s):
    answer = []
    stack = []
    for i in s:
        if i not in stack:
            answer.append(-1)
        else:
            answer.append(list(reversed(stack)).index(i) + 1)
        stack.append(i)
    return answer