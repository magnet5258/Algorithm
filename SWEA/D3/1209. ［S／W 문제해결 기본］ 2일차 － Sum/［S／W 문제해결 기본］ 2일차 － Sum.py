T = 10
for t in range(1, T+1):
    a = int(input())
    n = 100
    arr = [list(map(int, input().split())) for b in range(n)]
    ans = s3 = s4 = 0
    for i in range(n):
        s1 = s2 = 0
        for j in range(n):
            s1 += arr[i][j]
            s2 += arr[j][i]
        ans = max(ans, s1, s2)
        s3 += arr[i][i]
        s4 += arr[i][n-1-i]
    ans = max(ans, s3, s4)
    print(f'#{t} {ans}')