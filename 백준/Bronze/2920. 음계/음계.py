num_lst = list(map(int, input().split()))
if num_lst == [1, 2, 3, 4, 5, 6, 7, 8]:
    print('ascending')
elif num_lst == [8, 7, 6, 5, 4, 3, 2, 1]:
    print('descending')
else:
    print('mixed')