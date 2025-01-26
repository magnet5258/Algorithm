lst = [int(input()) for _ in range(10)]
for i in range(len(lst)):
    lst[i] = lst[i] % 42
print(len(set(lst)))