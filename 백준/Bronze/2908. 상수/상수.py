A, B = map(int, input().split())
reversed_A, reversed_B = str(A)[::-1], str(B)[::-1]
print(max(int(reversed_A), int(reversed_B)))
