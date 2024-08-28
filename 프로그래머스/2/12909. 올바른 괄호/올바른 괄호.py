def solution(s):
    answer = []
    if s[0] == ')' or s[-1] == '(':
        return False
    else:
        for i in s:
            if i == '(':
                answer.append(i)
            else:
                if len(answer) >= 1:
                    answer.pop()
    if len(answer) == 0:
        return True
    else:
        return False