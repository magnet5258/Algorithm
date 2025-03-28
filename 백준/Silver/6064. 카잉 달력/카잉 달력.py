import math

T = int(input())
for _ in range(T):
    M, N, x, y = map(int, input().split())
    lcm = M * N // math.gcd(M, N)
    k = x
    while k <= lcm:
        if (k - 1) % N + 1 == y:
            print(k)
            break
        k += M
    else:
        print(-1)