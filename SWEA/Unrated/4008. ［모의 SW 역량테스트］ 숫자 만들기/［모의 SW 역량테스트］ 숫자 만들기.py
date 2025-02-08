def dfs(idx, num):
    global max_result, min_result
 
    if idx == N - 1:
        max_result = max(max_result, num)
        min_result = min(min_result, num)
        return
 
    for i in range(4):
        if cal[i] > 0:
            cal[i] -= 1
            next_num = num_lst[idx + 1]
 
            if i == 0:
                dfs(idx + 1, num + next_num)
            elif i == 1:
                dfs(idx + 1, num - next_num)
            elif i == 2:
                dfs(idx + 1, num * next_num)
            else:
                dfs(idx + 1, int(num / next_num))
 
            cal[i] += 1
 
T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    cal = list(map(int, input().split()))
    calculators = ['+'] * cal[0] + ['-'] * cal[1] + ['*'] * cal[2] + ['/'] * cal[3]
    num_lst = list(map(int, input().split()))
    max_result = float('-inf')
    min_result = float('inf')
    dfs(0, num_lst[0])
    print(f'#{test_case} {max_result - min_result}')