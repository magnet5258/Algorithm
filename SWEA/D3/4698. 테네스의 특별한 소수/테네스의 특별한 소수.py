T = int(input())
cases = []
max_B = 0
for _ in range(T):
    D, A, B = map(int, input().split())
    cases.append((D, A, B))
    max_B = max(max_B, B)

is_prime = [True] * (max_B + 1)
is_prime[0] = is_prime[1] = False
for i in range(2, int(max_B ** 0.5) + 1):
    if is_prime[i]:
        for j in range(i * i, max_B + 1, i):
            is_prime[j] = False
            
for idx, (D, A, B) in enumerate(cases, 1):
    ans = 0
    for i in range(A, B + 1):
        if is_prime[i] and str(D) in str(i):
            ans += 1
    print(f'#{idx} {ans}')