N = int(input())
for i in range(2 * N - 1):
    if i < N:
        print(' ' * (N - 1 - i) + '*' * (2 * i + 1))
    else:
        print(' ' * (i - N + 1) + '*' * (2 * (2 * N - 2 - i) + 1))