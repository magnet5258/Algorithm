T = int(input())
for test_case in range(1, T + 1):
    S = input()
    K = int(input())
    lst = list(map(int, input().split()))
    shift = sum(lst) % len(S)
    S = S[shift:] + S[:shift]
    print(S)
