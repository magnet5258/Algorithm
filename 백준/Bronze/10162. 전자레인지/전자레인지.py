T = int(input())
if T % 10 != 0:
    print(-1)
    exit()
else:
    A = T // 300
    T -= A * 300
    B = T // 60
    T -= B * 60
    C = T // 10
    T -= C * 10
    print(A, B, C)