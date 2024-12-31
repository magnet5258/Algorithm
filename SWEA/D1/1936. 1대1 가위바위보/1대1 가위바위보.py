A, B = map(int, input().split())

if (A, B) == (3, 1) or (A, B) == (1, 3):
    print('A' if A < B else 'B')
else:
    print('A' if A > B else 'B')