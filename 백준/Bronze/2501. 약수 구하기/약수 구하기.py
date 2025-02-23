N, K = map(int, input().split())
lst = []
cnt = 0
for i in range(1, N + 1):
    if N % i == 0:
        lst.append(i)
        cnt += 1
    if cnt == K:
        ans = i
        break
if cnt < K:
    ans = 0
print(ans)