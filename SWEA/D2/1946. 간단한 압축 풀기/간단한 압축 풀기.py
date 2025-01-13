T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    lst = [list(map(str, input().split())) for _ in range(N)]
    new_lst = []
    for i in lst:
        new_lst.append(i[0] * int(i[1]))
    ans = ''.join(new_lst)
    print(f'#{test_case}')
    for i in range(0, len(ans), 10):
        print(ans[i:i + 10])
