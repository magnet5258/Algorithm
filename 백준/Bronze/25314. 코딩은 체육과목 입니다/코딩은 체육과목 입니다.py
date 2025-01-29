N = int(input())
lst = []
num = N // 4
lst.extend(['long'] * num)
lst.append('int')
print(' '.join(lst))