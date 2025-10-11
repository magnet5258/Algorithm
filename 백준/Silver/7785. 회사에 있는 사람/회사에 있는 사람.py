n = int(input())
enter_lst = set()
for _ in range(n):
    name, status = input().split()
    if name in enter_lst and status == 'leave':
        enter_lst.discard(name)
    elif name not in enter_lst and status == 'enter':
        enter_lst.add(name)

for name in sorted(enter_lst, reverse=True):
    print(name)