T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    trees = list(map(int, input().split()))
    max_tree = max(trees)

    S_even = 0
    S_odd = 0
    total_diff = 0
    for tree in trees:
        d = max_tree - tree
        total_diff += d
        S_even += d // 2
        S_odd += d % 2

    D = S_even + S_odd
    while True:
        odd_available = (D + 1) // 2
        even_available = D // 2

        if odd_available + 2 * even_available < total_diff:
            D += 1
            continue

        if even_available < S_even:
            needed_odd = S_odd + 2 * (S_even - even_available)
        else:
            needed_odd = S_odd

        if odd_available >= needed_odd:
            break
        D += 1

    print(f'#{test_case} {D}')