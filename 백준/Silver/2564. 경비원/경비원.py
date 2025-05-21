width, height = map(int, input().split())
n = int(input())
cashier = []
for _ in range(n):
    d, l = map(int, input().split())
    cashier.append((d, l))
sd, sl = map(int, input().split())

l_sum = 0
for d, l in cashier:
    if sd == d:
        l_sum += abs(l - sl)
    else:
        if sd == 1:
            if d == 2:
                l_sum += min(sl + l, (width * 2 - l - sl)) + height
            elif d == 3:
                l_sum += sl + l
            else:
                l_sum += (width - sl) + l
        elif sd == 2:
            if d == 1:
                l_sum += min(sl + l, (width * 2 - l - sl)) + height
            elif d == 3:
                l_sum += sl + (height - l)
            else:
                l_sum += (width - sl) + (height - l)
        elif sd == 3:
            if d == 1:
                l_sum += sl + l
            elif d == 2:
                l_sum += (height - sl) + l
            else:
                l_sum += min(sl + l, (height * 2 - l - sl)) + width
        else:
            if d == 1:
                l_sum += sl + (width - l)
            elif d == 2:
                l_sum += (height - sl) + (width - l)
            else:
                l_sum += min(sl + l, (height * 2 - l - sl)) + width

print(l_sum)