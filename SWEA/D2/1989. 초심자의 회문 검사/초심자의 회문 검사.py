T = int(input())
for test_case in range(1, T + 1):
    x = input()
    ans = 1
    for i in range(len(x) // 2):
        if x[i] != x[-1 - i]:
            ans = 0
            break
    print(f'#{test_case} {ans}')