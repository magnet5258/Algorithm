T = int(input())
a = list(map(int, input().split()))
a_sort = sorted(a)
print(a_sort[len(a_sort) // 2])