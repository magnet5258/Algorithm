from itertools import combinations

def is_valid(seq):
    for a, b, c in combinations(seq, 3):
        if a ^ b ^ c == 0:
            return False
    return True

def solve(n):
    result = []
    all_nums = list(range(1, n + 1))
    for bits in range(1, 1 << n):
        subset = [all_nums[i] for i in range(n) if (bits >> i) & 1]
        if is_valid(subset) and len(subset) > len(result):
            result = subset
    return result

T = int(input())
for _ in range(T):
    N = int(input())
    ans = solve(N)
    print(len(ans))
    print(*ans)