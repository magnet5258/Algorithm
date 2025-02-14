def check(expression):
    stack = []
    for char in expression:
        if char == '(':
            stack.append(char)
        elif char == ')':
            if not stack or stack[-1] != '(':
                return 'NO'
            stack.pop()
    if not stack:
        return 'YES'
    return 'NO'

T = int(input())
for _ in range(T):
    parenthesis = input()
    print(check(parenthesis))