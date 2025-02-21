import math

def comb(N, K):
    return math.factorial(N) // (math.factorial(K) * math.factorial(N - K))

N, K = map(int, input().split())
print(comb(N, K))