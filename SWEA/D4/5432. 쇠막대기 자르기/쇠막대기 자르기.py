T = int(input())
for test_case in range(1, T + 1):
    x = input()
    stack = []
    cnt = 0
    for i in range(len(x)):
        if x[i] == '(':
            stack.append('(')
        else:
            stack.pop()
            if x[i - 1] == '(':
            	cnt += len(stack)
            else:
                cnt += 1
    print(f'#{test_case} {cnt}')