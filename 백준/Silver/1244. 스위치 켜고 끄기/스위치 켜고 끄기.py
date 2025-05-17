def switch_num(i):
    if i == 0:
        return 1
    elif i == 1:
        return 0


N = int(input())
switch = [2] + list(map(int, input().split()))
st_num = int(input())
st_lst = []
for _ in range(st_num):
    x, y = map(int, input().split())
    st_lst.append((x, y))
for x, y in st_lst:
    if x == 1:
        i = y
        while i < len(switch):
            switch[i] = switch_num(switch[i])
            i += y
    else:
        switch[y] = switch_num(switch[y])
        ly = y - 1
        ry = y + 1
        while ly >= 1 and ry < len(switch):
            if switch[ly] == switch[ry]:
                switch[ly] = switch_num(switch[ly])
                switch[ry] = switch_num(switch[ry])
                ly -= 1
                ry += 1
            else:
                break

for i in range(1, N + 1):
    print(switch[i], end=' ')
    if i % 20 == 0:
        print()