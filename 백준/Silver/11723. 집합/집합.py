import sys

M = int(sys.stdin.readline().strip())
S = set()

for _ in range(M):
    cal = sys.stdin.readline().split()
    
    if cal[0] == 'add':
        S.add(int(cal[1]))
    elif cal[0] == 'remove':
        S.discard(int(cal[1]))
    elif cal[0] == 'check':
        print(1 if int(cal[1]) in S else 0)
    elif cal[0] == 'toggle':
        x = int(cal[1])
        if x in S:
            S.remove(x)
        else:
            S.add(x)
    elif cal[0] == 'all':
        S = set(range(1, 21))
    elif cal[0] == 'empty':
        S.clear()
