equation = input().split('-')
num_lst = []
for num in equation:
    if '+' in num:
        num = sum(map(int, num.split('+')))
    else:
        num = int(num)
    num_lst.append(num)

cal = num_lst[0]
for i in range(1, len(num_lst)):
    cal -= num_lst[i]

print(cal)