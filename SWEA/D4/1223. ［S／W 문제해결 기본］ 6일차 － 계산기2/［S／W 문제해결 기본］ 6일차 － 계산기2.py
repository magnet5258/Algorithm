T = 10
for test_case in range(1, T + 1):
    N = int(input())
    cal = input()
    num = []
    mul = []
    
    for i in cal:
        if i.isdigit():
            num.append(int(i))
        elif i == '*':
            mul.append(i)
            continue
        if num and mul:
            a = num.pop()
            b = num.pop()
            num.append(a * b)
            mul.pop()
        
    print(f'#{test_case} {sum(num)}')