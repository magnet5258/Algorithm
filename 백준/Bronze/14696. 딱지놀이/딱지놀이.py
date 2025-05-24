from collections import Counter

N = int(input())
for _ in range(N):
    A = sorted(list(map(int, input().split()))[1:])
    B = sorted(list(map(int, input().split()))[1:])
    cnt_A = Counter(A)
    cnt_B = Counter(B)

    for shape in [4, 3, 2, 1]:
        if cnt_A[shape] > cnt_B[shape]:
            print('A')
            break
        elif cnt_A[shape] < cnt_B[shape]:
            print('B')
            break
    else:
        print('D')