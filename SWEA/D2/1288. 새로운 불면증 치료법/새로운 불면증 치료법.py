T = int(input())
num_set = set('0123456789')
for test_case in range(1, T + 1):
    a = input()
    initial_a = int(a)
    count_set = set(a)
    ans = 1
    while count_set != num_set:
        ans += 1
        a = str(initial_a * ans)
        count_set.update(a)
    print(f'#{test_case} {a}')
        
            
        
        