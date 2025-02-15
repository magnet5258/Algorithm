def fibonacci_cnt(n):
    if n == 0:
        return (1, 0)
    elif n == 1:
        return (0, 1)

    prev1 = (1, 0)
    prev2 = (0, 1)

    for _ in range(2, n + 1):
        zero = prev1[0] + prev2[0]
        one = prev1[1] + prev2[1]
        prev1, prev2 = prev2, (zero, one)

    return prev2

T = int(input())
for _ in range(T):
    N = int(input())
    cnt_zero, cnt_one = fibonacci_cnt(N)
    print(cnt_zero, cnt_one)