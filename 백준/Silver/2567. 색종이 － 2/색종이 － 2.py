N = int(input())
arr = [[0] * 102 for _ in range(102)]
for _ in range(N):
    si, sj = map(int, input().split())
    for i in range(si, si + 10):
        for j in range(sj, sj + 10):
            arr[i][j] = 1
arr_zip = list(map(list, zip(*arr)))
cnt = 0
for lst in arr:
    for a in range(1, len(lst)):
        if lst[a - 1] != lst[a]:
            cnt += 1
for lst in arr_zip:
    for b in range(1, len(lst)):
        if lst[b - 1] != lst[b]:
            cnt += 1
print(cnt)

