N, K = map(int, input().split())
num = input()

stack = []
cnt = K

for digit in num:
    while stack and cnt > 0 and stack[-1] < digit:
        stack.pop()
        cnt -= 1
    stack.append(digit)

while cnt > 0:
    stack.pop()
    cnt -= 1

print(''.join(stack))