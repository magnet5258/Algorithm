T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    lst = [list(map(int, input().split())) for _ in range(N)]
    speed = 0
    ans = 0
    for i in range(N):
        if lst[i][0] == 0:
            ans += speed
        elif lst[i][0] == 1:
            speed += lst[i][1]
            ans += speed
        else:
            if lst[i][1] > speed:
                speed = 0
            else:
                speed -= lst[i][1]
                ans += speed
    print(f'#{test_case} {ans}')
                
