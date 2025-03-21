while True:
    sentence = input()
    if sentence == '.':
        break
    stack = []
    ans = 'yes'
    for i in range(len(sentence)):
        if sentence[i] == '.':
            if stack:
                ans = 'no'
            print(ans)
            break
        elif sentence[i] in '([':
            stack.append(sentence[i])
        elif sentence[i] == ')':
            if stack and stack[-1] == '(':
                stack.pop()
            else:
                ans = 'no'
        elif sentence[i] == ']':
            if stack and stack[-1] == '[':
                stack.pop()
            else:
                ans = 'no'