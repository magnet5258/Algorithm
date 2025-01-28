arr = [list(map(int, input().split())) for _ in range(9)]
max_value = max(max(row) for row in arr)
row_index = next(i for i, row in enumerate(arr) if max_value in row)
column_index = next(j for j, value in enumerate(arr[row_index]) if value == max_value)
print(max_value)
print(f'{row_index + 1} {column_index + 1}')