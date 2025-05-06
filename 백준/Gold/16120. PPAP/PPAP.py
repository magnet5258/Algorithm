word = input()
stack = []
for i in range(len(word)):
    if len(stack) < 3:
        stack.append(word[i])
    elif word[i] == 'P':
        if stack[-1] == 'A' and stack[-2] == 'P' and stack[-3] == 'P':
            stack.pop()
            stack.pop()
        else:
            stack.append(word[i])
    else:
        stack.append(word[i])

if len(stack) == 1 and stack[0] == 'P':
    print('PPAP')
else:
    print('NP')