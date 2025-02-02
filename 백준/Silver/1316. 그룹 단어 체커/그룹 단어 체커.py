N = int(input())
cnt = 0
for _ in range(N):
    word = input()
    seen = set()
    prev = ''
    is_group = True
    for i in word:
        if i in seen and i != prev:
            is_group = False
            break
        else:
            seen.add(i)
            prev = i
    if is_group:
        cnt += 1
print(cnt)