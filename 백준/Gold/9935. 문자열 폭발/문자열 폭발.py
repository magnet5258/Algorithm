word = input()
bomb = input()
stack = []
bomb_len = len(bomb)

for i in word:
    stack.append(i)
    if ''.join(stack[-bomb_len:]) == bomb:
        for _ in range(bomb_len):
            stack.pop()

if len(stack) == 0:
    print('FRULA')
else:
    print(''.join(stack))