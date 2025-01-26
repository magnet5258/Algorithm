lst = [i for i in range(1, 31)]
for j in range(28):
    x = int(input())
    lst.remove(x)
print(f'{min(lst)}\n{max(lst)}')