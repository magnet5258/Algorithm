def hanoi(n, source, target, auxiliary):
    if n > 0:
        hanoi(n - 1, source, auxiliary, target)
        print(source, target)
        hanoi(n - 1, auxiliary, target, source)

N = int(input())
print(2 ** N - 1)
if N <= 20:
    hanoi(N, 1, 3, 2)