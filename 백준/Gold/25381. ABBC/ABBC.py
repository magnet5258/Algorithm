S = input()[::-1]
a, b, c = 0, 0, 0
cnt = 0

for ch in S:
    if ch == 'A':
        if b > 0:
            b -= 1
            cnt += 1
        else:
            a += 1
    elif ch == 'B':
        if c > 0:
            c -= 1
            cnt += 1
        else:
            b += 1
    else:
        c += 1

print(cnt)