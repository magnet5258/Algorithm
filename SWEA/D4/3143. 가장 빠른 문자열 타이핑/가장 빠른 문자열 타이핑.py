T = int(input())
for test_case in range(1, T + 1):
    A, B = input().split()
    cnt = len(A) - (A.count(B) * (len(B) - 1))
    print(f'#{test_case} {cnt}')