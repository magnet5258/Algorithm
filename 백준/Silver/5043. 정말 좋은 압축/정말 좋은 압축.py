N, b = map(int, input().split())
if (1 << (b + 1)) - 1 >= N:
    print('yes')
else:
    print('no')