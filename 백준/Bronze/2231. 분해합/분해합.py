N = int(input())
str_N = str(N)
min_gen = max(0, N - len(str_N) * 9)
for num in range(min_gen, N):
    ans = sum(map(int, str(num)))
    if ans + num == N:
        print(num)
        break
else:
    print(0)