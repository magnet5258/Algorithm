N = int(input())
is_prime = [True] * (N + 1)
is_prime[0] = is_prime[1] = False
for i in range(2, int(N ** 0.5) + 1):
    if is_prime[i]:
        for j in range(i * i, N + 1, i):
            is_prime[j] = False

primes = [i for i, ok in enumerate(is_prime) if ok]

left = 0
right = 0
cur = 0
ans = 0
L = len(primes)

while True:
    if cur >= N:
        if cur == N:
            ans += 1
        if left < L:
            cur -= primes[left]
            left += 1
        else:
            break
    else:
        if right == L:
            break
        cur += primes[right]
        right += 1

print(ans)