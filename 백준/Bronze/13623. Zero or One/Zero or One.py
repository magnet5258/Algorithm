A, B, C = map(int, input().split())
if A == B == C:
    print('*')
elif B == C and A != B:
    print('A')
elif A == C and A != B:
    print('B')
elif A == B and B != C:
    print('C')