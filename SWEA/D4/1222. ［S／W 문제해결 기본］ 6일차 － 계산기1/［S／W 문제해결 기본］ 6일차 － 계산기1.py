T = 10
for test_case in range(1, T + 1):
    N = int(input())
    cal = input()
    ans = 0
    for i in cal:
        if i != '+':
            ans += int(i)
    print(f'#{test_case} {ans}')