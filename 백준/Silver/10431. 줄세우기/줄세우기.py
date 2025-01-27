P = int(input())
for test in range(1, P + 1):
    lst = list(map(int, input().split()))[1:]
    cnt = 0
    for i in range(len(lst)):
        for j in range(i):
            if lst[i] < lst[j]:
                cnt += 1
    print(f'{test} {cnt}')