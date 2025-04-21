import sys

MAX = 1000000
is_prime = [True] * (MAX + 1)
is_prime[0] = is_prime[1] = False
for i in range(2, int(MAX ** 0.5) + 1):
    if is_prime[i]:
        for j in range(i * i, MAX + 1, i):
            is_prime[j] = False

data = sys.stdin.read().split()
for num in data:
    n = int(num)
    if n == 0:
        break
    found = False
    for i in range(3, n // 2 + 1):
        if is_prime[i] and is_prime[n - i]:
            print(f'{n} = {i} + {n - i}')
            found = True
            break
    if not found:
        print("Goldbach's conjecture is wrong.")
        