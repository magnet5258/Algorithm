N, K = map(int, input().split())
result = []
i = 1
cnt = 0
while len(result) < N:
    if i != N:
        i %= N
    if i not in result:
        cnt += 1
    if cnt == K:
        result.append(i)
        cnt = 0
    i += 1
print(f"<{', '.join(map(str, result))}>")