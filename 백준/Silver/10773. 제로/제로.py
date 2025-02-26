K = int(input())
num_lst = [int(input()) for _ in range(K)]
new_lst = []
for num in num_lst:
    if num != 0:
        new_lst.append(num)
    else:
        new_lst.pop()
print(sum(new_lst))