T = 10
for test_case in range(1, T + 1):
    N = int(input())
    lst = list(map(int, input().split()))
    i = 1
    while True:
        num = lst.pop(0)
        num -= i
        if num <= 0:
            lst.append(0)
            break
        else:
            lst.append(num)
        i += 1
        if i > 5:
            i = 1
    print(f"#{N} {' '.join(map(str, lst))}")