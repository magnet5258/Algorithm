T = int(input())
for test_case in range(1, T + 1):
    num = list(map(int, input().split()))
    sum_n = 0
    for i in num:
        if i % 2 == 1:
            sum_n += i
    print('#' + str(test_case), sum_n)
