from itertools import combinations

T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    ingredients = list(range(N))
    combs_1 = combinations(ingredients, N // 2)
    min_sum = float('inf')

    for comb_1 in combs_1:
        comb_2 = tuple(i for i in ingredients if i not in comb_1)
        sum_1 = sum(arr[i][j] for i in comb_1 for j in comb_1)
        sum_2 = sum(arr[i][j] for i in comb_2 for j in comb_2)
        min_sum = min(min_sum, abs(sum_1 - sum_2))

    print(f'#{test_case} {min_sum}')