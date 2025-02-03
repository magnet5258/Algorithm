T = int(input())
for test_case in range(1, T + 1):
    N, M = map(int, input().split())
    bin_M = bin(M)[2:].zfill(N)
    len_bin = len(bin_M)
    ans = 'ON'
    for i in range(len_bin - N, len_bin):
        if bin_M[i] == '0':
            ans = 'OFF'
            break
    print(f'#{test_case} {ans}')