S = input()
stack = []

for i in range(len(S)):
    if S[i] == ')':
        temp_len = 0
        while stack and stack[-1] != '(':
            temp_len += stack.pop()
        stack.pop()
        K = stack.pop()
        stack.append(temp_len * K)
    elif S[i] == '(':
        stack.append(S[i])
    else:
        if i + 1 < len(S) and S[i + 1] == '(':
            stack.append(int(S[i]))
        else:
            stack.append(1)

print(sum(stack))