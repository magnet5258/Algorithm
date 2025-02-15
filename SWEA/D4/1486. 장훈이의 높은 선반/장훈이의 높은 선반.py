from itertools import combinations

T = int(input())
for test_case in range(1, T + 1):
    N, B = map(int, input().split())
    lst = list(map(int, input().split()))
    result = []
    for i in range(N + 1):
        for comb in combinations(lst, i):
            if sum(comb) >= B:
                result.append(sum(comb))
    print(f'#{test_case} {min(result) - B}')