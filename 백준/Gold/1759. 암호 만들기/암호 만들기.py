from itertools import combinations

L, C = map(int, input().split())
a_list = sorted(list(input().split()))
possible_list = list(combinations(a_list, L))
vowels = {'a', 'e', 'i', 'o', 'u'}

for password in possible_list:
    v_cnt = 0
    c_cnt = 0
    for i in password:
        if i in vowels:
            v_cnt += 1
        else:
            c_cnt += 1
    if v_cnt >= 1 and c_cnt >= 2:
        print(''.join(password))