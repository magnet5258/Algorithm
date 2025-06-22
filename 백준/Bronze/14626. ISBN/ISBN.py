ISBN = input()
missing_index = ISBN.index('*')
ISBN_sum = 0

for num in range(10):
    total = 0
    for i in range(13):
        if i == missing_index:
            digit = num
        else:
            digit = int(ISBN[i])
        if i % 2 == 0:
            total += digit
        else:
            total += digit * 3
    if total % 10 == 0:
        print(num)
        break