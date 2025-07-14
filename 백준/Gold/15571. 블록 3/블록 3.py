N, M = map(int, input().split())
MOD = 1999

dp = [0] * (M + 1)
pref = [0] * (M + 1)

dp[0] = 1
pref[0] = 1
if M >= 1:
    dp[1] = 1
    pref[1] = 2

for i in range(2, min(N, M) + 1):
    if i < N:
        dp[i] = pref[i-1] % MOD
    else:
        dp[i] = (pref[i-1] * 2 - 1) % MOD
    pref[i] = (pref[i-1] + dp[i]) % MOD

if M > N:
    H = pref[N-1]
    for j in range(N + 1, M + 1):
        window = (pref[j-1] - pref[j-N]) % MOD
        dp[j] = (window + dp[j-N] * H) % MOD
        pref[j] = (pref[j-1] + dp[j]) % MOD

print(dp[M] % MOD)