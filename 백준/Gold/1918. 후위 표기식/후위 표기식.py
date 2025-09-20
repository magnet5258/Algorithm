cal = list(input())
stack = []
answer = []
for i in range(len(cal)):
    if cal[i] == '(':
        stack.append(cal[i])
    elif cal[i] == ')':
        while stack[-1] != '(':
            answer.append(stack.pop())
        stack.pop()
    elif cal[i] in ('*', '/'):
        if stack:
            while stack and stack[-1] in ('*', '/'):
                answer.append(stack.pop())
        stack.append(cal[i])
    elif cal[i] in ('+', '-'):
        if stack:
            while stack and stack[-1] in ('*', '/', '+', '-'):
                answer.append(stack.pop())
        stack.append(cal[i])
    else:
        answer.append(cal[i])

while len(stack) > 0:
    answer.append(stack.pop())

print(''.join(answer))