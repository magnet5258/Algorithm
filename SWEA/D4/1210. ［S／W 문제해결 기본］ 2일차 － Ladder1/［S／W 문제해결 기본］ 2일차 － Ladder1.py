T = 10
for t in range(1, T + 1):
    _ = int(input())
    arr = [[0] + list(map(int, input().split())) + [0] for _ in range(100)]
    ci = 99
    for j in range(1, 101):
        if arr[ci][j] == 2:
            cj = j
            break
    while ci > 0:
        arr[ci][cj] = 0
        if arr[ci][cj - 1] == 1:
            cj -= 1
        elif arr[ci][cj + 1] == 1:
            cj += 1
        else:
            ci -= 1
    print(f'#{t} {cj - 1}')
            
        
    
    
    
