arr = [list(input()) for _ in range(5)]
max_len = max([len(row) for row in arr])
lst = []
for j in range(max_len):
    for i in range(5):
        if j < len(arr[i]):
            lst.append(arr[i][j])
print(''.join(lst))