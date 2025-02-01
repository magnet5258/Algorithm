num_lst = list(map(int, input().split()))
sum_num = 0
for num in num_lst:
    sum_num += num ** 2
print(sum_num % 10)