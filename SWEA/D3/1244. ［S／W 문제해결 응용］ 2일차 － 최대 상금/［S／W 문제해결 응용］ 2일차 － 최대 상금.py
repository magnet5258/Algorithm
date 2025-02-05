from itertools import combinations

def dfs(cnt):
    global max_result
    num_str = ''.join(num_lst)

    if (num_str, cnt) in visited:
        return
    visited.add((num_str, cnt))

    if cnt == check:
        max_result = max(max_result, int(num_str))
        return

    for a, b in change_lst:
        num_lst[a], num_lst[b] = num_lst[b], num_lst[a]
        dfs(cnt + 1)
        num_lst[a], num_lst[b] = num_lst[b], num_lst[a]

T = int(input())
for test_case in range(1, T + 1):
    num, change = input().split()
    num_lst = list(num)
    check = int(change)
    lst = [i for i in range(len(num_lst))]
    change_lst = list(combinations(lst, 2))
    max_result = 0
    visited = set()
    dfs(0)

    print(f'#{test_case} {max_result}')