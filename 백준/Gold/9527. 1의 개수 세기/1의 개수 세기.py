def ones(n):
    total = 0
    k = 0

    while (1 << k) <= n:
        step = 1 << (k + 1)
        half = 1 << k
        full = (n + 1) // step * half
        rest = (n + 1) % step
        total += full + max(0, rest - half)
        k += 1

    return total


A, B = map(int, input().split())
print(ones(B) - ones(A - 1))