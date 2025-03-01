N = int(input())
lst = []
for _ in range(N):
    x, y = map(int, input().split())
    lst.append((x, y))
sorted_lst = sorted(lst, key=lambda x: (x[1], x[0]))
for x, y in sorted_lst:
    print(x, y)