def plus_num(i, j, start_num):
    if len(start_num) == 7:
        result.add(start_num)
        return
 
    if i - 1 >= 0:
        plus_num(i - 1, j, start_num + arr[i - 1][j])
    if i + 1 <= 3:
        plus_num(i + 1, j, start_num + arr[i + 1][j])
    if j - 1 >= 0:
        plus_num(i, j - 1, start_num + arr[i][j - 1])
    if j + 1 <= 3:
        plus_num(i, j + 1, start_num + arr[i][j + 1])
 
T = int(input())
for test_case in range(1, T + 1):
    arr = [list(input().split()) for _ in range(4)]
    result = set()
    for i in range(4):
        for j in range(4):
            plus_num(i, j, arr[i][j])
             
    print(f'#{test_case} {len(result)}')