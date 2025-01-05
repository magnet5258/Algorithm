T = int(input())
for t in range(1, T + 1):
    arr = [list(map(int, input().split())) for _ in range(9)]
    ans = 1
    for i in range(9):
        check_lst = []
        for j in range(9):           
            if arr[i][j] in range(1, 10) and arr[i][j] not in check_lst:
                check_lst.append(arr[i][j])
            else:
                ans = 0
                break
    for j in range(9):
        check_lst = []
        for i in range(9):            
            if arr[i][j] in range(1, 10) and arr[i][j] not in check_lst:
                check_lst.append(arr[i][j])
            else:
                ans = 0
                break
    for box_i in range(0, 9, 3):
        for box_j in range(0, 9, 3):
            check_lst = []
            for i in range(3):
                for j in range(3):
                    num = arr[box_i + i][box_j + j]
                    if num in range(1, 10) and num not in check_lst:
                        check_lst.append(num)
                    else:
                        ans = 0
                        break
    
    print(f'#{t} {ans}')