def solution(s):
    answer = 0
    for x in range(len(s)):
        par = s[x:] + s[:x]
        valid = True
        stack = []
        for i in par:
            if i in '([{':
                stack.append(i)
            elif stack and i == ')' and stack[-1] == '(':
                stack.pop()
            elif stack and i == ']' and stack[-1] == '[':
                stack.pop()
            elif stack and i == '}' and stack[-1] == '{':
                stack.pop()
            else:
                valid = False
                break
        if valid and not stack:
            answer += 1
    return answer