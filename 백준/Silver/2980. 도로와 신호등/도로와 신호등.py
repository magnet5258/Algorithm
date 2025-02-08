N, L = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
time = 0
length = 0
for i in range(N):
    if length < arr[i][0]:
        time += arr[i][0] - length
        length = arr[i][0]
        if time % (arr[i][1] + arr[i][2]) < arr[i][1]:
            time += arr[i][1] - (time % (arr[i][1] + arr[i][2]))
time += L - length
print(time)