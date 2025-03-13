from collections import defaultdict

T = int(input())
for _ in range(T):
    n = int(input())
    clothes = defaultdict(list)
    ans = 1
    for _ in range(n):
        a, b = input().split()
        clothes[b].append(a)
    for cloth in clothes:
        ans *= len(clothes[cloth]) + 1
    print(ans - 1)