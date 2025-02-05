T = 10
for test_case in range(1, T + 1):
    N = int(input())
    bin_tree = [0] * (N + 1)
    arr = []
    for _ in range(N):
        lst = list(input().split())
        arr.append(lst)
    arr.reverse()
    for lst in arr:
        if lst[1] == '+':
            bin_tree[int(lst[0])] = bin_tree[int(lst[2])] + bin_tree[int(lst[3])]
        elif lst[1] == '-':
            bin_tree[int(lst[0])] = bin_tree[int(lst[2])] - bin_tree[int(lst[3])]
        elif lst[1] == '*':
            bin_tree[int(lst[0])] = bin_tree[int(lst[2])] * bin_tree[int(lst[3])]
        elif lst[1] == '/':
            bin_tree[int(lst[0])] = bin_tree[int(lst[2])] / bin_tree[int(lst[3])]
        else:
            bin_tree[int(lst[0])] = int(lst[1])
 
    print(f'#{test_case} {int(bin_tree[1])}')