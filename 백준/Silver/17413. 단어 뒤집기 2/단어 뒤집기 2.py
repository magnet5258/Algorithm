S = input()
stack = []
ans = []
word = ''
for i in range(len(S)):
    if S[i] == '<':
        if word:
            ans.append(word[::-1])
            word = ''
        stack.append(S[i])
        word += S[i]
    elif S[i] == '>':
        stack.pop()
        word += S[i]
        ans.append(word)
        word = ''
    elif stack:
        word += S[i]
    elif S[i] != ' ':
        word += S[i]
    else:
        if word:
            ans.append(word[::-1])
            word = ''
        ans.append(' ')

if word:
    ans.append(word[::-1])

print(''.join(ans))