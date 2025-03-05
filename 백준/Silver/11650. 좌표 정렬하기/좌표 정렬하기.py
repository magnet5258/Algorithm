import sys

N = int(sys.stdin.readline())
lst = [tuple(map(int, line.split())) for line in sys.stdin.read().splitlines()]
sorted_lst = sorted(lst, key=lambda x: (x[0], x[1]))
for x, y in sorted_lst:
    print(x, y)