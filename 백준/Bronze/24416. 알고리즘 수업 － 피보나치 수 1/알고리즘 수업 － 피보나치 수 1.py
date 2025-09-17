n = int(input())
cnt_1 = 0
cnt_2 = 0

def fib(n):
    global cnt_1
    if n == 1 or n == 2:
        cnt_1 += 1
        return cnt_1
    else:
        return fib(n - 1) + fib(n - 2)

def fibonacci(n):
    global cnt_2
    dp = [0] * (n + 1)
    for i in range(3, n + 1):
        cnt_2 += 1
        dp[i] = dp[i - 1] + dp[i - 2]
    return dp[n]

fib(n)
fibonacci(n)
print(cnt_1, cnt_2)