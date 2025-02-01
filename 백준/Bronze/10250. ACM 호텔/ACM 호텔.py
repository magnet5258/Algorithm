T = int(input())
for _ in range(T):
    H, W, N = map(int, input().split())
    if N % H == 0:
        floor = H
        room = N // H
    else:
        floor = N % H
        room = N // H + 1
    if room >= 10:
        print(str(floor) + str(room))
    else:
        print(str(floor) + '0' + str(room))