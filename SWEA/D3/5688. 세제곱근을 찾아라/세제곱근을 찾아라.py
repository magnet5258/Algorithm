T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    cube_root = round(N ** (1 / 3))
    if cube_root ** 3 == N:
        ans = cube_root
    else:
        ans = -1
    print(f'#{test_case} {ans}')