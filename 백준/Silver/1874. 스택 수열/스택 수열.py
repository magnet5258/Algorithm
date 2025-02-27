n = int(input())
num_lst = [int(input()) for _ in range(n)]
stack = []
result = []
ans = 'YES'
num = 1

for i in range(len(num_lst)):
    if num_lst[i] not in stack:
        while num <= num_lst[i]:
            stack.append(num)
            result.append('+')
            num += 1
        stack.pop()
        result.append('-')
    elif num_lst[i] == stack[-1]:
        stack.pop()
        result.append('-')
    else:
        ans = 'NO'
        break

if ans == 'NO':
    print(ans)
else:
    for i in result:
        print(i)