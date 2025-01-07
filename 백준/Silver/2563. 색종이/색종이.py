N = int(input())
arr = [[0] * 100 for _ in range(100)]
for _ in range(N):
    si, sj = map(int, input().split())
    for i in range(si, si + 10):
        for j in range(sj, sj + 10):
            arr[i][j] = 1
    cnt = 0
    for lst in arr:
        cnt += sum(lst)
print(cnt)
    
