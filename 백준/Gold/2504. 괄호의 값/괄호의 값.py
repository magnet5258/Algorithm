pars = input()
stack = []
temp = 1
ans = 0

for i in range(len(pars)):
    if pars[i] == '(':
        stack.append('(')
        temp *= 2
    elif pars[i] == '[':
        stack.append('[')
        temp *= 3
    elif pars[i] == ')':
        if not stack or stack[-1] != '(':
            ans = 0
            break
        if i > 0 and pars[i - 1] == '(':
            ans += temp
        stack.pop()
        temp //= 2
    elif pars[i] == ']':
        if not stack or stack[-1] != '[':
            ans = 0
            break
        if i > 0 and pars[i - 1] == '[':
            ans += temp
        stack.pop()
        temp //= 3

if stack:
    ans = 0

print(ans)