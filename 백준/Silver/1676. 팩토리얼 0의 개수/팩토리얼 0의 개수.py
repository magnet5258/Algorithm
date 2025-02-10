def fact(N):
    if N <= 1:
        return 1
    else:
        return N * fact(N - 1)

N = int(input())
reversed_N = str(fact(N))[::-1]
ans = 0
for i in reversed_N:
    if i == "0":
        ans += 1
    else:
        break
print(ans)