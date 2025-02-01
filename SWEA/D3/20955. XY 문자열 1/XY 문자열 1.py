T = int(input())
for test_case in range(1, T + 1):
    S = input()
    E = input()
    while len(E) > len(S):
        if E[-1] == 'X':
            E = E[:-1]
        elif E[-1] == 'Y':
            E = E[:-1][::-1]
    if S == E:
        print(f'#{test_case} Yes')
    else:
        print(f'#{test_case} No')
    