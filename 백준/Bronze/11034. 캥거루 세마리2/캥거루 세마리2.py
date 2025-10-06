while True:
    try:
        A, B, C = map(int, input().split())
        cnt = 0
        while C - B > 1 or B - A > 1:
            if B - A >= C - B:
                C = A + 1
                A, B, C = A, C, B
                cnt += 1
            else:
                A = C - 1
                A, B, C = B, A, C
                cnt += 1
        print(cnt)
    except EOFError:
        break