T = int(input())
for case in range(T):
    ballons = input()
    a_cnt = ballons.count('a')
    b_cnt = ballons.count('b')
    print(min(a_cnt, b_cnt))